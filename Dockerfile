FROM python:3.9-slim-buster
WORKDIR /app
ADD . .
RUN apt-get update
RUN pip3 install -r requirements.txt



# run as non-root user
RUN adduser --disabled-password myuser
USER myuser

# run gunicorn with 3 threads listening on port 5000.
EXPOSE 5000
CMD gunicorn --threads=3 --bind 0.0.0.0:5000 wsgi:app
