# search43

[![Build Status](https://drone.element-43.com/api/badges/EVE-Tools/search43/status.svg)](https://drone.element-43.com/EVE-Tools/search43)

Search43 is a simple and fast market search service for Element43 based on PyPy, gunicorn and falcon. All market types are loaded from CREST at startup and are available for query at `GET api/search/v1/market-type`. The query is passed to the service via the `query` URL parameter. The service then performs a simple case-insensitive substring search over all type's names and returns up to 25 matching type descriptions in CREST's format in its JSON response.

## Installation
Either use the prebuilt Docker images and pass the appropriate env vars (see below), or:
* Get Python/PyPy (and make a fresh virtualenv if you like)
* Clone this repo
* Install dependencies with `pip install -r requirements.txt`
* Run with e.g. `gunicorn main:application -b :8000 --workers 2 --worker-class meinheld.gmeinheld.MeinheldWorker`

## Deployment Info
Builds are handled by Drone.

Environment Variable | Example | Description
--- | --- | ---
PORT | 8000 | Port the server will listen on
NUM_WORKERS | 2 | Number of gunicorn workers used for processing requests

## Example response

`GET api/search/v1/market-type/?query=plex`
```json
[{
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/1333/",
        "id": 1333,
        "id_str": "1333"
    },
    "type": {
        "id_str": "2287",
        "href": "https://crest-tq.eveonline.com/inventory/types/2287/",
        "id": 2287,
        "name": "Complex Organisms",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/2287_64.png"
        }
    },
    "id": 2287,
    "id_str": "2287"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/1907/",
        "id": 1907,
        "id_str": "1907"
    },
    "type": {
        "id_str": "11462",
        "href": "https://crest-tq.eveonline.com/inventory/types/11462/",
        "id": 11462,
        "name": "R.Db - Core Complexion",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/11462_64.png"
        }
    },
    "id": 11462,
    "id_str": "11462"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/490/",
        "id": 490,
        "id_str": "490"
    },
    "type": {
        "id_str": "16869",
        "href": "https://crest-tq.eveonline.com/inventory/types/16869/",
        "id": 16869,
        "name": "Complex Reactor Array",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/16869_64.png"
        }
    },
    "id": 16869,
    "id_str": "16869"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/1919/",
        "id": 1919,
        "id_str": "1919"
    },
    "type": {
        "id_str": "11877",
        "href": "https://crest-tq.eveonline.com/inventory/types/11877/",
        "id": 11877,
        "name": "R.Db - Core Complexion Blueprint",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/11877_64.png"
        }
    },
    "id": 11877,
    "id_str": "11877"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/1923/",
        "id": 1923,
        "id_str": "1923"
    },
    "type": {
        "id_str": "29668",
        "href": "https://crest-tq.eveonline.com/inventory/types/29668/",
        "id": 29668,
        "name": "30 Day Pilot's License Extension (PLEX)",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/29668_64.png"
        }
    },
    "id": 29668,
    "id_str": "29668"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/1351/",
        "id": 1351,
        "id_str": "1351"
    },
    "type": {
        "id_str": "2791",
        "href": "https://crest-tq.eveonline.com/inventory/types/2791/",
        "id": 2791,
        "name": "Complex Reactor Array Blueprint",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/2791_64.png"
        }
    },
    "id": 2791,
    "id_str": "2791"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/1901/",
        "id": 1901,
        "id_str": "1901"
    },
    "type": {
        "id_str": "23155",
        "href": "https://crest-tq.eveonline.com/inventory/types/23155/",
        "id": 23155,
        "name": "Serpentis Complex Target Guider",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/23155_64.png"
        }
    },
    "id": 23155,
    "id_str": "23155"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/645/",
        "id": 645,
        "id_str": "645"
    },
    "type": {
        "id_str": "21484",
        "href": "https://crest-tq.eveonline.com/inventory/types/21484/",
        "id": 21484,
        "name": "'Full Duplex' Ballistic Control System",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/21484_64.png"
        }
    },
    "id": 21484,
    "id_str": "21484"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/2205/",
        "id": 2205,
        "id_str": "2205"
    },
    "type": {
        "id_str": "37232",
        "href": "https://crest-tq.eveonline.com/inventory/types/37232/",
        "id": 37232,
        "name": "Standup M-Set Structure Target Multiplexing I",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/37232_64.png"
        }
    },
    "id": 37232,
    "id_str": "37232"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/2205/",
        "id": 2205,
        "id_str": "2205"
    },
    "type": {
        "id_str": "37233",
        "href": "https://crest-tq.eveonline.com/inventory/types/37233/",
        "id": 37233,
        "name": "Standup M-Set Structure Target Multiplexing II",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/37233_64.png"
        }
    },
    "id": 37233,
    "id_str": "37233"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/1611/",
        "id": 1611,
        "id_str": "1611"
    },
    "type": {
        "id_str": "30036",
        "href": "https://crest-tq.eveonline.com/inventory/types/30036/",
        "id": 30036,
        "name": "Legion Electronics - Energy Parasitic Complex",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/30036_64.png"
        }
    },
    "id": 30036,
    "id_str": "30036"
}, {
    "marketGroup": {
        "href": "https://crest-tq.eveonline.com/market/groups/2159/",
        "id": 2159,
        "id_str": "2159"
    },
    "type": {
        "id_str": "37394",
        "href": "https://crest-tq.eveonline.com/inventory/types/37394/",
        "id": 37394,
        "name": "Standup M-Set Structure Target Multiplexing I Blueprint",
        "icon": {
            "href": "http://imageserver.eveonline.com/Type/37394_64.png"
        }
    },
    "id": 37394,
    "id_str": "37394"
}]
```
