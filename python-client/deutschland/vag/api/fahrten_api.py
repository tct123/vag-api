"""
    VAG API

    OpenAPI-Dokumentation der API zu start.vag - dem Verkehrs-Aktiengesellschaft (VAG) Abfahrsmonitor mit Echtzeitprognose. Die API gibt Zugriff auf alle Haltestellen, Fahrten und Abfahrten im Gebiet des Verkehrsbund Großraum Nürnberg (VGN). Eine Schnittstellenbeschreibung durch die VAG findet sich auf https://opendata.vag.de/dataset/api-echtzeitauskunft unter Creative CommonsAttribution 4.0 Int veröffentlicht.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.vag.api_client import ApiClient
from deutschland.vag.api_client import Endpoint as _Endpoint
from deutschland.vag.model.fahrten_api_response import FahrtenAPIResponse
from deutschland.vag.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class FahrtenApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.fahrten_get_endpoint = _Endpoint(
            settings={
                "response_type": (FahrtenAPIResponse,),
                "auth": [],
                "endpoint_path": "/api/v1/fahrten/{betriebszweig}",
                "operation_id": "fahrten_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "betriebszweig",
                    "timespan",
                ],
                "required": [
                    "betriebszweig",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "betriebszweig": (str,),
                    "timespan": (int,),
                },
                "attribute_map": {
                    "betriebszweig": "betriebszweig",
                    "timespan": "timespan",
                },
                "location_map": {
                    "betriebszweig": "path",
                    "timespan": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": [
                    "application/json",
                    "text/json",
                    "application/xml",
                    "text/xml",
                ],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.fahrten_get_fahrt1_endpoint = _Endpoint(
            settings={
                "response_type": (FahrtenAPIResponse,),
                "auth": [],
                "endpoint_path": "/api/v1/fahrten/{betriebszweig}/{fahrtnummer}",
                "operation_id": "fahrten_get_fahrt1",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "betriebszweig",
                    "fahrtnummer",
                ],
                "required": [
                    "betriebszweig",
                    "fahrtnummer",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "betriebszweig": (str,),
                    "fahrtnummer": (int,),
                },
                "attribute_map": {
                    "betriebszweig": "betriebszweig",
                    "fahrtnummer": "fahrtnummer",
                },
                "location_map": {
                    "betriebszweig": "path",
                    "fahrtnummer": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": [
                    "application/json",
                    "text/json",
                    "application/xml",
                    "text/xml",
                ],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.fahrten_get_fahrt2_endpoint = _Endpoint(
            settings={
                "response_type": (FahrtenAPIResponse,),
                "auth": [],
                "endpoint_path": "/api/v1/fahrten/{betriebszweig}/{betriebstag}/{fahrtnummer}",
                "operation_id": "fahrten_get_fahrt2",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "betriebszweig",
                    "betriebstag",
                    "fahrtnummer",
                ],
                "required": [
                    "betriebszweig",
                    "betriebstag",
                    "fahrtnummer",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "betriebszweig": (str,),
                    "betriebstag": (datetime,),
                    "fahrtnummer": (int,),
                },
                "attribute_map": {
                    "betriebszweig": "betriebszweig",
                    "betriebstag": "betriebstag",
                    "fahrtnummer": "fahrtnummer",
                },
                "location_map": {
                    "betriebszweig": "path",
                    "betriebstag": "path",
                    "fahrtnummer": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": [
                    "application/json",
                    "text/json",
                    "application/xml",
                    "text/xml",
                ],
                "content_type": [],
            },
            api_client=api_client,
        )

    def fahrten_get(self, betriebszweig, **kwargs):
        """Liefert alle laufenden und startenden Fahrten zu dem angegebenen Betriebszweig innerhalb des angegebenen Zeitfenster.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fahrten_get(betriebszweig, async_req=True)
        >>> result = thread.get()

        Args:
            betriebszweig (str): Betriebszweig der VAG: Bus|Tram|UBahn

        Keyword Args:
            timespan (int): Zeitfenster für die Abfrage in Minuten (Default 60 Minuten). [optional]
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
            FahrtenAPIResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["betriebszweig"] = betriebszweig
        return self.fahrten_get_endpoint.call_with_http_info(**kwargs)

    def fahrten_get_fahrt1(self, betriebszweig, fahrtnummer, **kwargs):
        """Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem aktuellen Betriebstag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fahrten_get_fahrt1(betriebszweig, fahrtnummer, async_req=True)
        >>> result = thread.get()

        Args:
            betriebszweig (str): Betriebszweig der VAG: Bus|Tram|UBahn
            fahrtnummer (int): Fahrtnummer für die Anfrage

        Keyword Args:
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
            FahrtenAPIResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["betriebszweig"] = betriebszweig
        kwargs["fahrtnummer"] = fahrtnummer
        return self.fahrten_get_fahrt1_endpoint.call_with_http_info(**kwargs)

    def fahrten_get_fahrt2(self, betriebszweig, betriebstag, fahrtnummer, **kwargs):
        """Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem angegebenen Betriebstag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fahrten_get_fahrt2(betriebszweig, betriebstag, fahrtnummer, async_req=True)
        >>> result = thread.get()

        Args:
            betriebszweig (str): Betriebszweig der VAG: Bus|Tram|UBahn
            betriebstag (datetime): Betriebstagsdatum für die Anfrag
            fahrtnummer (int): Fahrtnummer für die Anfrage

        Keyword Args:
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
            FahrtenAPIResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["betriebszweig"] = betriebszweig
        kwargs["betriebstag"] = betriebstag
        kwargs["fahrtnummer"] = fahrtnummer
        return self.fahrten_get_fahrt2_endpoint.call_with_http_info(**kwargs)
