# search43

[![Build Status](https://drone.element-43.com/api/badges/EVE-Tools/search43/status.svg)](https://drone.element-43.com/EVE-Tools/search43)

Search43 is a simple and fast market search service for Element43 based on PyPy, gunicorn and falcon. All market types are loaded from CREST at startup and are available for query at `GET api/search/v1/market-type`. The query is passed to the service via the `query` URL parameter. The service then performs a simple case-insensitive substring search over all type's names and returns up to 25 matching type descriptions in CREST's format in its JSON response.

## Installation
Either use the prebuilt Docker images and pass the appropriate env vars (see below), or:
* Get PyPy (and make a fresh virtualenv)
* Clone this repo
* Install dependencies with `pip install -r requirements.txt`
* Run with e.g. `gunicorn main:application -b :8000 --workers 2 --worker-class meinheld.gmeinheld.MeinheldWorker`

## Deployment Info
Builds are handled by Drone.

Environment Variable | Example | Description
--- | --- | ---
PORT | 8000 | Port the server will listen on
NUM_WORKERS | 2 | Number of gunicorn workers used for processing requests
