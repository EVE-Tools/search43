# search43

[![Build Status](https://drone.element-43.com/api/badges/EVE-Tools/search43/status.svg)](https://drone.element-43.com/EVE-Tools/search43)

Search43 is a simple and fast market search service for Element43 based on PyPy, gunicorn and falcon. It can easily serve multiple thousand requests per second even on an older multi-core machine. All market types are loaded from CREST at startup and are available for query at `GET api/search/v1/market-type`. The query is passed to the service via the `query` URL parameter. The service then performs a simple case-insensitive substring search over all type's names and returns up to 25 matching type descriptions in CREST's format in its JSON response.

## Deployment of the Container
The service exposes its interface on port `8000`. The number of gunicorn workers can be adjusted by setting the environment variable `NUM_WORKERS` to the desired value.
