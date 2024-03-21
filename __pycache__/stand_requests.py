import configuration
import requests
import data


def create_order():
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order_body)


def get_order_info_by_track(track):
    return requests.get(url=configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track))
