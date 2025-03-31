import sender_stand_request
import data
import requests

# Андрей Половинкин, 28-я когорта — Финальный проект. Инженер по тестированию плюс


# Тест 1. Проверка номера трека заказа
def test_create_orders():
    orders_track = sender_stand_request.get_orders_track()
    # Проверяется, что код ответа равен 200
    assert orders_track.status_code == 200
