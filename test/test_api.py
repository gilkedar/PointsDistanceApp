import unittest
import os
import utils.config as config
import requests


def publish_csv_file_request(ip, port, uri, files):
    url = f"http://{ip}:{port}{uri}"
    headers = {'Content-type': 'text/csv'}
    ans = requests.post(url, headers=headers, files=files)
    return ans

class TestPointsDistanceApp(unittest.TestCase):
    def test_get_addresses_api(self):
        test_file = os.path.join(os.getcwd(), "points_test_file_1.csv")
        with open(test_file, 'rb') as fin:
            files = {'file': fin}
            result = publish_csv_file_request(config.HTTP_SERVER_IP, config.HTTP_SERVER_PORT, config.URI_POST_ADDRESSES, files)
        result_id = result.text
        assert type(result_id) is str
        assert len(result_id) == 24
        self.assertNotEqual(result_id, "")

    def test_get_response_api(self):
        pass


if __name__ == '__main__':
    unittest.main()