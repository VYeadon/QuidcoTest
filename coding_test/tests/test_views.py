from django.test import TestCase
from unittest.mock import Mock, MagicMock
import json

from coding_test.views import GIFRandomView, GIFSearchView, GIFBaseView


class GIFViewTests(TestCase):

    def setUp(self) -> None:
        pass

    def test_random_gif_returns_result(self):
        request = Mock()
        response = GIFRandomView().get(request)

        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertIn('data', response_dict)
        self.assertIn('title', response_dict['data']['gif'])
        self.assertIn('url', response_dict['data']['gif'])

    def test_random_gif_returns_random_results(self):
        request = Mock()
        title_array = []

        response = GIFRandomView().get(request)
        response_dict = json.loads(response.content.decode('utf-8'))
        title = response_dict['data']['gif']['title']
        title_array.append(title)
        response = GIFRandomView().get(request)
        response_dict = json.loads(response.content.decode('utf-8'))
        title = response_dict['data']['gif']['title']
        title_array.append(title)
        response = GIFRandomView().get(request)
        response_dict = json.loads(response.content.decode('utf-8'))
        title = response_dict['data']['gif']['title']
        title_array.append(title)
        response = GIFRandomView().get(request)
        response_dict = json.loads(response.content.decode('utf-8'))
        title = response_dict['data']['gif']['title']
        title_array.append(title)

        # Checks if all the titles are the same
        self.assertFalse(all(elem == title_array[0] for elem in title_array))

    def test_search_gif_returns_result(self):
        request = MagicMock()
        request.query_params = {'title': 'Apple'}

        response = GIFSearchView().get(request)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertIn('data', response_dict)
        self.assertIn('title', response_dict['data']['gif'])
        self.assertIn('url', response_dict['data']['gif'])

    def test_search_gif_returns_error_with_no_search(self):
        request = MagicMock()

        response = GIFSearchView().get(request)
        self.assertEqual(response.status_code, 500)
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual('error', response_dict['status'])

    def test_get_search_title_returns_title(self):
        request = MagicMock()
        request.query_params = {'title': 'Apple'}

        title_value = GIFSearchView()._get_search_title(request)
        self.assertEqual(title_value, 'Apple')

    def test_get_search_title_throws_error_when_no_title(self):
        request = MagicMock()
        self.assertRaises(KeyError, GIFSearchView()._get_search_title, request)

    def test_construct_response(self):
        inner_data = {'inner_key': 'inner_value'}
        response = GIFBaseView().construct_response(inner_data)
        self.assertEqual(response, {
            "data": {
                "gif":
                    inner_data
            }
        })
