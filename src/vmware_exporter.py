from flask import Flask, Response, redirect, url_for
from helpers.url_collector import UrlCollector
import prometheus_client
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')


# The assignment requested measurement of two URLs
# In the real world the URLs should not be hardcoded in the script but provided as external configuration
# Due to time constrain, I've decided to leave the URLs hardcoded.
# TODO: Get rid of hard coded url definition
url_collector = UrlCollector(['https://httpstat.us/200', 'https://httpstat.us/503'])

app = Flask(__name__)


@app.errorhandler(500)
def handle_500(error):
    return str(error), 500


@app.route('/')
def main():
    return redirect(url_for('metrics'))


@app.route('/metrics')
def metrics():
    url_collector.collect()
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run()
