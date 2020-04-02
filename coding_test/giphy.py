from django.conf import settings
import random

test_static_gifs = [
    {
        "title": "Banana",
        "url": "https://www.gifapi.com/banana.gif"
    },
    {
        "title": "Apple",
        "url": "https://www.gifapi.com/apple.gif"
    },
    {
        "title": "Pear",
        "url": "https://www.gifapi.com/pear.gif"
    },
    {
        "title": "Orange",
        "url": "https://www.gifapi.com/orange.gif"
    },
]


class Giphy:
    """
    This class is responsible for making different requests to the giphy api to retrieve gifs
    """

    def __init__(self):
        """
        Further config params would be passed into the constructor but this seems sufficent for now
        """
        self.api_key = settings.GIPHY_API_KEY
        self.base_url = 'api.giphy.com/v1'
        super().__init__()

    def get_gif_random(self):
        url = self.base_url + 'random/'
        headers = self._make_request_headers()
        payload = {
            "options": "parameters"
        }
        response = self._make_post_request(url, headers, payload)
        return random.choice(test_static_gifs)

    def get_gif_search(self, search_term):
        url = self.base_url + 'search/'
        headers = self._make_request_headers()
        payload = {
            "search": search_term
        }
        response = self._make_post_request(url, headers, payload)
        return self._placeholder_search_response(search_term)

    def _placeholder_search_response(self, search_term):
        """
        A placeholder method to emulate a search response from giphy
        :param search_term:
        :return:
        """
        for gif in test_static_gifs:
            if gif['title'] == search_term:
                return gif
        raise LookupError(
            'No gif found with the specified title: {}'.format(search_term))

    def _make_request_headers(self):
        """
        A function to create the required headers for calling a giphy endpoint
        :return:
        """
        return {
            'api-key': self.api_key
        }

    def _make_post_request(self, url, headers, payload):
        """
        A generic function which would call a given endpoint with the given headers and payload
        :param url:
        :param payload:
        :return:
        """
        return None
