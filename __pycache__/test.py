# Юлия Шиянова, 14-я когорта — Финальный проект. Инженер по тестированию плюс
import stand_requests


def test_get_order_info_by_track():
    new_order = stand_requests.create_order()
    track = new_order.json()["track"]
    order_info = stand_requests.get_order_info_by_track(track)
    assert order_info.status_code == 200

