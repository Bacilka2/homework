import json
import unittest

from unittest.mock import patch, mock_open


from src.utils  import path_json


class TestPathJson(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id":1,"amount":100}]')
    @patch("json.load")
    def test_path_json_success(self, mock_json_load, mock_file):
        # mock_json_load нужен, чтобы контролировать возвращаемое значение json.load
        mock_json_load.return_value = [{"id": 1, "amount": 100}]

        path = "dummy_path.json"
        result = path_json(path)

        mock_file.assert_called_once_with(path, encoding="utf-8")
        mock_json_load.assert_called_once()
        self.assertEqual(result, [{"id": 1, "amount": 100}])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_path_json_file_not_found(self, mock_open):
        path = "missing.json"
        result = path_json(path)

        mock_open.assert_called_once_with(path, encoding="utf-8")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()