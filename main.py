import falcon
import json

from whoosh import index
from whoosh.qparser import QueryParser


class SearchResource(object):

    def __init__(self):
        self.types = json.load(open('types.json'))
        self.ix = index.open_dir('types.idx')
        self.query_parser = QueryParser('name', self.ix.schema)

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


# Initialize application
application = falcon.API()

# Instantiate search
search = SearchResource()

# Wire up route
application.add_route('/api/search/v1/market-type/', search)
