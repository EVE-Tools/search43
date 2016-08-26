import falcon
import requests
import json


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
        self.name_list = []

        for item in items:
            name = item["type"]["name"].lower()
            self.types[name] = item
            self.name_list.append(name)

        print("Done!")

    def on_get(self, request, response):
        """
        :param request: Request
        :param response: Response
        :return: Search result in JSON format
        """

        # Convert query to lower case unicode string
        query = unicode(request.get_param('query', True), "utf-8").lower()

        # Find matches and retrieve results by name from dict
        matches = [name for name in self.name_list if query in name][:25]
        results = [self.types[match] for match in matches]

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
