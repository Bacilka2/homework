import unittest
from unittest.mock import patch, Mock

from src.external_api import convert


class TestConvert(unittest.TestCase):
    def test_rub_amount_return(self):
        tx = {
            "operationAmount": {
                "amount": "1000",
                "currency": {"code": "RUB"}
            }
        }
        self.assertEqual(convert(tx), "1000")

    @patch("requests.request")
    def test_usd_conversion_mock(self, mock_request):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"result": 7400.0}
        mock_request.return_value = mock_resp

        tx = {
            "operationAmount": {
                "amount": "1000",
                "currency": {"code": "USD"}
            }
        }

        result = convert(tx)


        mock_request.assert_called_once()
        called_args, called_kwargs = mock_request.call_args
        assert('https://api.apilayer.com/exchangerates_data/convert', called_args[0])

        self.assertEqual(result, 7400.0)

    @patch("requests.request")
    def test_eur_conversion_mock(self, mock_request):

        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"result": 8200.0}
        mock_request.return_value = mock_resp

        tx = {
            "operationAmount": {
                "amount": "1000",
                "currency": {"code": "EUR"}
            }
        }

        result = convert(tx)

        mock_request.assert_called_once()
        self.assertEqual(result, 8200.0)


if __name__ == "__main__":
    unittest.main()