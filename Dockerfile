FROM python:3

WORKDIR /usr/src/spotify-ranker
COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/bin/sh", "-c", "flask db upgrade && exec flask run --host 0.0.0.0"]
