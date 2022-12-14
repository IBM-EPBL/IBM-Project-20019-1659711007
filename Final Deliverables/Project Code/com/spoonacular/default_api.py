"""
    spoonacular API

    The spoonacular Nutrition, Recipe, and Food API allows you to access over thousands of recipes, thousands of ingredients, 800,000 food products, over 100,000 menu items, and restaurants. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Contact: mail@spoonacular.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.analyze_recipe_request import AnalyzeRecipeRequest
from openapi_client.model.analyze_recipe_request1 import AnalyzeRecipeRequest1
from openapi_client.model.search_restaurants200_response import SearchRestaurants200Response


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.analyze_recipe_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'apiKeyScheme'
                ],
                'endpoint_path': '/recipes/analyze',
                'operation_id': 'analyze_recipe',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'analyze_recipe_request',
                    'language',
                    'include_nutrition',
                    'include_taste',
                ],
                'required': [
                    'analyze_recipe_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'analyze_recipe_request':
                        (AnalyzeRecipeRequest,),
                    'language':
                        (str,),
                    'include_nutrition':
                        (bool,),
                    'include_taste':
                        (bool,),
                },
                'attribute_map': {
                    'language': 'language',
                    'include_nutrition': 'includeNutrition',
                    'include_taste': 'includeTaste',
                },
                'location_map': {
                    'analyze_recipe_request': 'body',
                    'language': 'query',
                    'include_nutrition': 'query',
                    'include_taste': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    '',
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_recipe_card_get_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'apiKeyScheme'
                ],
                'endpoint_path': '/recipes/{id}/card',
                'operation_id': 'create_recipe_card_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'mask',
                    'background_image',
                    'background_color',
                    'font_color',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (float,),
                    'mask':
                        (str,),
                    'background_image':
                        (str,),
                    'background_color':
                        (str,),
                    'font_color':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'mask': 'mask',
                    'background_image': 'backgroundImage',
                    'background_color': 'backgroundColor',
                    'font_color': 'fontColor',
                },
                'location_map': {
                    'id': 'path',
                    'mask': 'query',
                    'background_image': 'query',
                    'background_color': 'query',
                    'font_color': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.search_restaurants_endpoint = _Endpoint(
            settings={
                'response_type': (SearchRestaurants200Response,),
                'auth': [
                    'apiKeyScheme'
                ],
                'endpoint_path': '/food/restaurants/search',
                'operation_id': 'search_restaurants',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'query',
                    'lat',
                    'lng',
                    'distance',
                    'budget',
                    'cuisine',
                    'min_rating',
                    'is_open',
                    'sort',
                    'page',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'query':
                        (str,),
                    'lat':
                        (float,),
                    'lng':
                        (float,),
                    'distance':
                        (float,),
                    'budget':
                        (float,),
                    'cuisine':
                        (str,),
                    'min_rating':
                        (float,),
                    'is_open':
                        (bool,),
                    'sort':
                        (str,),
                    'page':
                        (float,),
                },
                'attribute_map': {
                    'query': 'query',
                    'lat': 'lat',
                    'lng': 'lng',
                    'distance': 'distance',
                    'budget': 'budget',
                    'cuisine': 'cuisine',
                    'min_rating': 'min-rating',
                    'is_open': 'is-open',
                    'sort': 'sort',
                    'page': 'page',
                },
                'location_map': {
                    'query': 'query',
                    'lat': 'query',
                    'lng': 'query',
                    'distance': 'query',
                    'budget': 'query',
                    'cuisine': 'query',
                    'min_rating': 'query',
                    'is_open': 'query',
                    'sort': 'query',
                    'page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def analyze_recipe(
        self,
        analyze_recipe_request,
        **kwargs
    ):
        """Analyze Recipe  # noqa: E501

        This endpoint allows you to send raw recipe information, such as title, servings, and ingredients, to then see what we compute (badges, diets, nutrition, and more). This is useful if you have your own recipe data and want to enrich it with our semantic analysis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.analyze_recipe(analyze_recipe_request, async_req=True)
        >>> result = thread.get()

        Args:
            analyze_recipe_request (AnalyzeRecipeRequest): Example request body.

        Keyword Args:
            language (str): The input language, either \"en\" or \"de\".. [optional]
            include_nutrition (bool): Whether nutrition data should be added to correctly parsed ingredients.. [optional]
            include_taste (bool): Whether taste data should be added to correctly parsed ingredients.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['analyze_recipe_request'] = \
            analyze_recipe_request
        return self.analyze_recipe_endpoint.call_with_http_info(**kwargs)

    def create_recipe_card_get(
        self,
        id,
        **kwargs
    ):
        """Create Recipe Card  # noqa: E501

        Generate a recipe card for a recipe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_recipe_card_get(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (float): The recipe id.

        Keyword Args:
            mask (str): The mask to put over the recipe image (\"ellipseMask\", \"diamondMask\", \"starMask\", \"heartMask\", \"potMask\", \"fishMask\").. [optional]
            background_image (str): The background image (\"none\",\"background1\", or \"background2\").. [optional]
            background_color (str): The background color for the recipe card as a hex-string.. [optional]
            font_color (str): The font color for the recipe card as a hex-string.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['id'] = \
            id
        return self.create_recipe_card_get_endpoint.call_with_http_info(**kwargs)

    def search_restaurants(
        self,
        **kwargs
    ):
        """Search Restaurants  # noqa: E501

        Search through thousands of restaurants (in North America) by location, cuisine, budget, and more.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_restaurants(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            query (str): The search query.. [optional]
            lat (float): The latitude of the user's location.. [optional]
            lng (float): The longitude of the user's location.\".. [optional]
            distance (float): The distance around the location in miles.. [optional]
            budget (float): The user's budget for a meal in USD.. [optional]
            cuisine (str): The cuisine of the restaurant.. [optional]
            min_rating (float): The minimum rating of the restaurant between 0 and 5.. [optional]
            is_open (bool): Whether the restaurant must be open at the time of search.. [optional]
            sort (str): How to sort the results, one of the following 'cheapest', 'fastest', 'rating', 'distance' or the default 'relevance'.. [optional]
            page (float): The page number of results.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SearchRestaurants200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.search_restaurants_endpoint.call_with_http_info(**kwargs)

