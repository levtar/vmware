import requests
from prometheus_client import Gauge
import logging

logger = logging.getLogger(__name__)

class UrlCollector:
    def __init__(self, urls):
        self.urls = [x.rstrip("/") for x in urls]
        self.sample_external_url_up = Gauge('sample_external_url_up',
                                                  'Sample external url response status OK',
                                                  ['url']
                                                  )
        # According to Prometheus guide, seconds should be used as base time measurement unit instead of milliseconds
        # https://prometheus.io/docs/practices/naming/
        self.sample_external_url_response_ms_gauge = Gauge('sample_external_url_response_ms',
                                                           'Sample external url response time(ms)',
                                                           ['url']
                                                           )

    def collect(self):
        for url in self.urls:
            try:
                response = requests.get(url=url)
                self.sample_external_url_up.labels(url).set(response.ok)
                self.sample_external_url_response_ms_gauge.labels(url).set(response.elapsed.microseconds / 1000)
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                # http error
                logger.warning("HTTP Error: %s", e)
            except requests.exceptions.ConnectionError as e:
                # connection error
                logger.warning("Connection Error: %s", e)
            except requests.exceptions.Timeout as e:
                # connection timeout
                logger.warning("Timeout Error: %s", e)
            except requests.exceptions.RequestException as e:
                # catastrophic error.
                logger.warning('Something went wrong: %s', e)
