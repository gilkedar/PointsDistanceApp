import unittest
import os
import utils.config as config
import requests


def publish_csv_file_request(ip, port, uri, files):
    url = f"http://{ip}:{port}{uri}"
    headers = {'Content-type': 'text/csv'}
    ans = requests.post(url, headers=headers, files=files)
    return ans

def publish_get_result_request(ip, port, uri, key):
    url = f"http://{ip}:{port}{uri}"
    headers = {'Content-type': 'plain/text'}
    ans = requests.get(url, headers=headers, data=key)
    return ans


class TestPointsDistanceApp(unittest.TestCase):

    returned_id = None

    def test_get_addresses_api(self):
        test_file = os.path.join(os.getcwd(), "points_test_file_1.csv")
        with open(test_file, 'rb') as fin:
            files = {'file': fin}
            result = publish_csv_file_request(config.HTTP_SERVER_IP, config.HTTP_SERVER_PORT, config.URI_POST_ADDRESSES, files)
        result_id = result.text
        assert type(result_id) is str
        assert len(result_id) == 24
        TestPointsDistanceApp.returned_id = result_id
        self.assertNotEqual(result_id, "")

    def test_get_response_api(self):
        self.assertIsNotNone(TestPointsDistanceApp.returned_id)
        desired_res = {"points": [{"name": "A",
                                      "lat": 50.448069,
                                      "lon": 30.5194453},
                                     {"name": "B",
                                      "lat": 50.448616,
                                      "lon": 30.5116673},
                                     {"name": "C",
                                      "lat": 50.913788,
                                      "lon": 34.7828343}],
                          "links": [{"name": "AB", "distance": 555.787232279111},
                                    {"name": "AC", "distance": 305703.7018959083},
                                    {"name": "BC", "distance": 306233.25843844604}]
                          }
        result = publish_get_result_request(config.HTTP_SERVER_IP,
                                            config.HTTP_SERVER_PORT,
                                            config.URI_GET_RESPONSE,
                                            TestPointsDistanceApp.returned_id)
        item = result.json()
        del item["_id"]
        self.assertEqual(item, desired_res)


if __name__ == '__main__':
    unittest.main()