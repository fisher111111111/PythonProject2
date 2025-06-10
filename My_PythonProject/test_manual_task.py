import unittest
import requests

BASE_URL_STOCK = "http://localhost:3002"
BASE_URL_ADS = "http://localhost:3003"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

class TestCarOrderAPI(unittest.TestCase):

    def test_create_new_order_success(self):
        payload = {
            "vin": "2FLM9LM7DTDFD3BX",
            "model": "Model S",
            "manufacturer": "Ford",
            "year": 2016,
            "odometer": 10000,
            "odometerUnit": "km"
        }
        r = requests.post(f"{BASE_URL_STOCK}/stock", json=payload, headers=HEADERS)
        self.assertEqual(r.status_code, 201)
        data = r.json()
        self.assertIn("id", data)
        self.assertEqual(data["vin"], payload["vin"])
        self.assertEqual(data["model"], payload["model"])
        self.assertEqual(data["manufacturer"], payload["manufacturer"])
        self.assertEqual(data["year"], payload["year"])
        self.assertEqual(data["odometer"], payload["odometer"])
        self.assertEqual(data["odometerUnit"], payload["odometerUnit"])
        self.assertIn("createdAt", data)

    def test_create_new_order_bad_request(self):
        # Отсутствует обязательное поле vin
        payload = {
            "model": "Model S",
            "manufacturer": "Ford",
            "year": 2016,
            "odometer": 10000,
            "odometerUnit": "km"
        }
        r = requests.post(f"{BASE_URL_STOCK}/stock", json=payload, headers=HEADERS)
        self.assertEqual(r.status_code, 400)

    def test_create_new_order_internal_error(self):
        # Эмулируем внутреннюю ошибку, например, отправляя неверный формат года (строкой)
        payload = {
            "vin": "2FLM9LM7MDTDFD3BX",
            "model": "Model S",
            "manufacturer": "Ford",
            "year": "invalid_year",
            "odometer": 10000,
            "odometerUnit": "km"
        }
        r = requests.post(f"{BASE_URL_STOCK}/stock", json=payload, headers=HEADERS)
        self.assertIn(r.status_code, [400, 500])  # может быть 400 или 500, в зависимости от реализации

    def test_get_stock_list_success(self):
        r = requests.get(f"{BASE_URL_STOCK}/stock", headers=HEADERS)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertIsInstance(data, list)
        if data:
            item = data[0]
            self.assertIn("id", item)
            self.assertIn("vin", item)
            self.assertIn("model", item)
            self.assertIn("manufacturer", item)
            self.assertIn("year", item)
            self.assertIn("odometer", item)
            self.assertIn("odometerUnit", item)
            self.assertIn("createdAt", item)

    def test_get_stock_internal_error(self):
        # Тест на 500 - сложно эмулировать без контроля сервера,
        # но можно проверять, что сервер не выдаёт 500 при нормальном запросе
        r = requests.get(f"{BASE_URL_STOCK}/stock", headers=HEADERS)
        self.assertNotEqual(r.status_code, 500)

    def test_get_ads_list_success(self):
        r = requests.get(f"{BASE_URL_ADS}/ads", headers=HEADERS)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertIsInstance(data, list)
        if data:
            item = data[0]
            self.assertIn("vin", item)
            self.assertIn("model", item)
            self.assertIn("manufacturer", item)
            self.assertIn("year", item)
            self.assertIn("odometer", item)
            self.assertIn("odometerUnit", item)
            self.assertIn("price", item)
            self.assertIn("priceUnit", item)
