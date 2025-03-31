import configuration
import requests
import data


# Создание клиентом нового заказа
def post_new_orders(orders_body):
    req = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=orders_body)
    return req
response = post_new_orders(data.orders_body)


# Сохранен track созданного заказа
track = response.json()["track"]


# Проверяется, что по треку заказа можно получить данные о заказе.
def get_orders_track():
    req = requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK + str(track))
    return req
response = get_orders_track()