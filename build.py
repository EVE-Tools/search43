import requests
import json
import os

from whoosh import index
from whoosh.fields import Schema, NGRAMWORDS


def refresh_types():

    # Load items into dict and create name list
    # Names are stored in lower case
    types = {}

    # Create a directory for Whoosh index
    os.mkdir('types.idx')

    # Initialize index
    ix = index.create_in('types.idx', Schema(name=NGRAMWORDS(stored=True)))

    writer = ix.writer()

    # Get all items, put them to index and json storage
    items = get_all_items("https://crest-tq.eveonline.com/market/types/")
    for item in items:
        name = item["type"]["name"].lower()
        types[name] = item
        writer.add_document(name=name)

    writer.commit()

    with open('types.json', 'w') as f:
        json.dump(types, f)


def get_all_items(url):
    """
    :param url: Starting url
    :return: All items from all pages
    """
    result = requests.get(url).json()
    items = result["items"]

    if "pageCount" in result.keys():
        for page_number in range(2, result["pageCount"] + 1):
            items.extend(requests.get(url + ("?page=%d" % page_number)).json()["items"])

    return items


if __name__ == "__main__":
    print("Refreshing types from CREST...")
    refresh_types()
    print("Done!")
