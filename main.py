import falcon
import requests
import json

from whoosh.fields import Schema, NGRAMWORDS
from whoosh.filedb.filestore import RamStorage
from whoosh.qparser import QueryParser


# workaround https://bitbucket.org/mchaput/whoosh/issues/450/ramstorage-wants-tmp
class ReallyRamStorage(RamStorage):
    def temp_storage(self, name=None):
        return ReallyRamStorage().create()


class SearchResource(object):

    def __init__(self):
        self.types = {}
        self.name_list = []

        self.refresh_types()

    def refresh_types(self):
        print("Refreshing types from CREST...")

        # Get all items
        items = get_all_items("https://crest-tq.eveonline.com/market/types/")

        # Load items into dict and create name list
        # Names are stored in lower case
        self.types = {}

        # Whoosh index to speedup queries
        self.ix = ReallyRamStorage().create_index(Schema(name=NGRAMWORDS(stored=True)))
        self.query_parser = QueryParser("name", self.ix.schema)

        writer = self.ix.writer()

        for item in items:
            name = item["type"]["name"].lower()
            self.types[name] = item
            writer.add_document(name=name)

        writer.commit()

        print("Done!")

    def on_get(self, request, response):
        """
        :param request: Request
        :param response: Response
        :return: Search result in JSON format
        """

        # Convert query to lower case unicode string
        query = unicode(request.get_param('query', True), "utf-8").lower()
        query = self.query_parser.parse(query)

        # Find matches and retrieve results by name from dict
        with self.ix.searcher() as searcher:
            matches = searcher.search(query, limit=25)
            results = [self.types[match["name"]] for match in matches]

        # Encode JSON and send response
        encoded_results = json.dumps(results)

        response.body = encoded_results
        response.status = falcon.HTTP_200
        response.content_type = "application/json"
        response.append_header("Access-Control-Allow-Origin", "*")


def get_all_items(url):
    """
    :param url: Starting url
    :return: All items from all pages
    """
    result = requests.get(url).json()
    items = result["items"]

    if "pageCount" in result.keys():
        for page_number in range(2, result["pageCount"]+1):
            items.extend(requests.get(url + ("?page=%d" % page_number)).json()["items"])

    return items

# Initialize application
application = falcon.API()

# Instantiate search
search = SearchResource()

# Wire up route
application.add_route('/api/search/v1/market-type/', search)
