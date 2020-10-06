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
        desired_reuslt = { "points" : [{"name":"A",
                                        "lat" : 50.448069,
                                        "lon" : 30.5194453},
                                       {"name": "B",
                                        "lat": 50.448616,
                                        "lon": 30.5116673},
                                       {"name": "C",
                                        "lat": 50.913788,
                                        "lon": 34.7828343}],
                            "links": [{"name" : "AB", "distance" : 350.6 },
                                      {"name" : "BC", "distance" : 125.8},
                                      {"name" : "AC", "distance" : 1024.9}],
                            "result_id" : "b47d4112-31c2-4f02-a98d-10c3d6b001be"
                           }
        fin = open(test_file, 'rb')
        files = {'file': fin}
        result = publish_csv_file_request(config.HTTP_SERVER_IP, config.HTTP_SERVER_PORT, config.URI_POST_ADDRESSES, files)
        self.assertEqual(result, desired_reuslt)

    # def test_get_respoonse_api(self):
    #     pass


if __name__ == '__main__':
    unittest.main()