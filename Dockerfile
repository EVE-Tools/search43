FROM pypy:2-slim

MAINTAINER zweizeichen@element-43.com

WORKDIR /search
COPY . .

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install -r requirements.txt && \
    pypy build.py && \
    apt-get remove --purge -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENV NUM_WORKERS=2

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "/usr/local/bin/gunicorn main:application -b :8000 --workers ${NUM_WORKERS} --worker-class meinheld.gmeinheld.MeinheldWorker"]
