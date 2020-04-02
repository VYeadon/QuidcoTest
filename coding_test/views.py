from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey
from coding_test.giphy import Giphy
from django.http import JsonResponse


class GIFBaseView(APIView):
    """
    Base View for all gif searches
    Implements the requirement for an API key when calling the endpoint
    """
    permission_classes = [HasAPIKey]

    def get_giphy_connection(self):
        """
        This creates an instance of the giphy class.
        Used a method to call this as norally more config would be passed into the constructor.
        arguments could be passsed into get_giphy_connection method and then into giphy.
        :return:
        """
        return Giphy()

    def construct_response(self, gif_data: dict):
        """
        Constructs a json response which mimics the one given in the example
        This could also contain further metadata
        :param gif_data: dict response object
        :return:
        """
        return {
            "data": {
                "gif":
                    gif_data

            }
        }


class GIFRandomView(GIFBaseView):

    def get(self, request):
        """
        This view gets a random gif from giphy.
        A JSON payload is returned containing the title and url of gif.
        If no gif is retrieved it returns an error response.
        :param request:
        :return:
        """
        try:
            giphy = self.get_giphy_connection()
            result = giphy.get_gif_random()

            if result:
                json_response = self.construct_response(result)
                return JsonResponse(json_response)

            return JsonResponse({'status': 'error', 'message': 'No results returned'}, status=500)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


class GIFSearchView(GIFBaseView):

    def get(self, request):
        """
        This view gets a gif from giphy by its title given by the query parameter 'title' in the get request.
        A JSON payload is returned containing the title and url of gif.
        If no gif is retrieved it returns an error response.
        :param request:
        :return:
        """
        try:
            title = self._get_search_title(request)

            giphy = self.get_giphy_connection()
            result = giphy.get_gif_search(title)

            if result:
                json_response = self.construct_response(result)
                return JsonResponse(json_response)

            return JsonResponse({'status': 'error', 'message': 'No results returned'}, status=500)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    def _get_search_title(self, request):
        """
        Attempts to extra the query parameter 'title' from the get request
        Raises an error if no title is found
        :param request:
        :return:
        """
        query_params = request.query_params
        if 'title' not in query_params:
            raise KeyError(
                'Search query parameter "title" was not included in the url. Please try again with the query paramter title added.')
        return query_params['title']
