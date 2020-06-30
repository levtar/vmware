import pytest
import prometheus_client
from helpers.url_collector import UrlCollector

# For implementation of unittest we have to mock behaviour of the real web services.
# Due to time limitation I've did not reached the implementation of the UrlCollector unit tests
# Bellow tests are skeletons for implementation of the real unit tests.

@pytest.mark.skip(reason="Test pending implementation")
def test_metrics_created(self):
    url_collector = UrlCollector(['https://httpstat.us/200'])
    url_collector.collect()
    prometheus_client.REGISTRY.get_sample_value('sample_external_url_up', labels=['https://httpstat.us/200'])
    assert prometheus_client.REGISTRY.get_target_info() == 1


@pytest.mark.skip(reason="Test pending implementation")
def test_test_multiple_metrics_created(self):
    # url_collector = UrlCollector(['https://httpstat.us/200', 'https://httpstat.us/503'])
    # url_collector.collect()
    assert False


@pytest.mark.skip(reason="Test pending implementation")
def test_test_urls_with_trailing_slash(self):
    # url_collector = UrlCollector(['https://httpstat.us/200/'])
    # url_collector.collect()
    assert False


@pytest.mark.skip(reason="Test pending implementation")
def test_empty_list_url_collector(self):
    # url_collector = UrlCollector([])
    # url_collector.collect()
    assert False


@pytest.mark.skip(reason="Test pending implementation")
def test_empty_url_collector(self):
    # url_collector = UrlCollector()
    # url_collector.collect()
    assert False


@pytest.mark.skip(reason="Test pending implementation")
def test_invalid_url_collector(self):
    # url_collector = UrlCollector(['INVALID_URL'])
    # url_collector.collect()
    assert False
