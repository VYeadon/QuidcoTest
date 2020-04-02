from django.test import TestCase
from django.conf import settings

from coding_test.giphy import Giphy


class TestGiphy(TestCase):
    def setUp(self) -> None:
        self.giphy = Giphy()

    def test_get_gif_random(self):
        gif_array = []

        gif = self.giphy.get_gif_random()
        gif_array.append(gif)
        gif = self.giphy.get_gif_random()
        gif_array.append(gif)
        gif = self.giphy.get_gif_random()
        gif_array.append(gif)
        gif = self.giphy.get_gif_random()
        gif_array.append(gif)

        # Checks if all the titles are the same
        self.assertFalse(all(elem == gif_array[0] for elem in gif_array))

    def test_get_gif_search_with_result(self):
        gif = self.giphy.get_gif_search('Apple')
        self.assertEqual(gif, {
            "title": "Apple",
            "url": "https://www.gifapi.com/apple.gif"
        })

    def test_get_gif_search_with_no_result(self):
        self.assertRaises(LookupError, self.giphy.get_gif_search, 'cherry')

    def test__make_request_headers(self):
        headers = self.giphy._make_request_headers()
        self.assertEqual(headers, {
            'api-key': settings.GIPHY_API_KEY
        })
