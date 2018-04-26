import requests

class IFTTT:
    def __init__(self, key, event_name):
        assert isinstance(key, str), 'key should be str'
        assert isinstance(event_name, str), 'event_name should be str'
        self.key = key
        self.event_name = event_name

    def notify(self, value1='', value2='', value3=''):
        report = {}
        assert isinstance(value1, str), 'value1 should be str'
        assert isinstance(value2, str), 'value2 should be str'
        assert isinstance(value3, str), 'value3 should be str'
        report["value1"] = value1
        report["value2"] = value2
        report["value3"] = value3
        requests.post("https://maker.ifttt.com/trigger/{}/with/key/{}".format(self.event_name, self.key), data=report)