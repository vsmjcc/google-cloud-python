# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import dataclasses
import json  # type: ignore
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, path_template, rest_helpers, rest_streaming
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2
from google.protobuf import json_format
import grpc  # type: ignore
from requests import __version__ as requests_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.protobuf import empty_pb2  # type: ignore

from google.cloud.talent_v4.types import company
from google.cloud.talent_v4.types import company as gct_company
from google.cloud.talent_v4.types import company_service

from .base import CompanyServiceTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class CompanyServiceRestInterceptor:
    """Interceptor for CompanyService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CompanyServiceRestTransport.

    .. code-block:: python
        class MyCustomCompanyServiceInterceptor(CompanyServiceRestInterceptor):
            def pre_create_company(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_company(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_company(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_company(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_company(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_companies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_companies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_company(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_company(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CompanyServiceRestTransport(interceptor=MyCustomCompanyServiceInterceptor())
        client = CompanyServiceClient(transport=transport)


    """

    def pre_create_company(
        self,
        request: company_service.CreateCompanyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[company_service.CreateCompanyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_company

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompanyService server.
        """
        return request, metadata

    def post_create_company(self, response: gct_company.Company) -> gct_company.Company:
        """Post-rpc interceptor for create_company

        Override in a subclass to manipulate the response
        after it is returned by the CompanyService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_company(
        self,
        request: company_service.DeleteCompanyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[company_service.DeleteCompanyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_company

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompanyService server.
        """
        return request, metadata

    def pre_get_company(
        self,
        request: company_service.GetCompanyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[company_service.GetCompanyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_company

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompanyService server.
        """
        return request, metadata

    def post_get_company(self, response: company.Company) -> company.Company:
        """Post-rpc interceptor for get_company

        Override in a subclass to manipulate the response
        after it is returned by the CompanyService server but before
        it is returned to user code.
        """
        return response

    def pre_list_companies(
        self,
        request: company_service.ListCompaniesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[company_service.ListCompaniesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_companies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompanyService server.
        """
        return request, metadata

    def post_list_companies(
        self, response: company_service.ListCompaniesResponse
    ) -> company_service.ListCompaniesResponse:
        """Post-rpc interceptor for list_companies

        Override in a subclass to manipulate the response
        after it is returned by the CompanyService server but before
        it is returned to user code.
        """
        return response

    def pre_update_company(
        self,
        request: company_service.UpdateCompanyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[company_service.UpdateCompanyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_company

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompanyService server.
        """
        return request, metadata

    def post_update_company(self, response: gct_company.Company) -> gct_company.Company:
        """Post-rpc interceptor for update_company

        Override in a subclass to manipulate the response
        after it is returned by the CompanyService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompanyService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CompanyService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CompanyServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CompanyServiceRestInterceptor


class CompanyServiceRestTransport(CompanyServiceTransport):
    """REST backend transport for CompanyService.

    A service that handles company management, including CRUD and
    enumeration.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(
        self,
        *,
        host: str = "jobs.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CompanyServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or CompanyServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateCompany(CompanyServiceRestStub):
        def __hash__(self):
            return hash("CreateCompany")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: company_service.CreateCompanyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gct_company.Company:
            r"""Call the create company method over HTTP.

            Args:
                request (~.company_service.CreateCompanyRequest):
                    The request object. The Request of the CreateCompany
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gct_company.Company:
                    A Company resource represents a
                company in the service. A company is the
                entity that owns job postings, that is,
                the hiring entity responsible for
                employing applicants for the job
                position.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v4/{parent=projects/*/tenants/*}/companies",
                    "body": "company",
                },
            ]
            request, metadata = self._interceptor.pre_create_company(request, metadata)
            pb_request = company_service.CreateCompanyRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gct_company.Company()
            pb_resp = gct_company.Company.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_company(resp)
            return resp

    class _DeleteCompany(CompanyServiceRestStub):
        def __hash__(self):
            return hash("DeleteCompany")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: company_service.DeleteCompanyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ):
            r"""Call the delete company method over HTTP.

            Args:
                request (~.company_service.DeleteCompanyRequest):
                    The request object. Request to delete a company.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v4/{name=projects/*/tenants/*/companies/*}",
                },
            ]
            request, metadata = self._interceptor.pre_delete_company(request, metadata)
            pb_request = company_service.DeleteCompanyRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _GetCompany(CompanyServiceRestStub):
        def __hash__(self):
            return hash("GetCompany")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: company_service.GetCompanyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> company.Company:
            r"""Call the get company method over HTTP.

            Args:
                request (~.company_service.GetCompanyRequest):
                    The request object. Request for getting a company by
                name.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.company.Company:
                    A Company resource represents a
                company in the service. A company is the
                entity that owns job postings, that is,
                the hiring entity responsible for
                employing applicants for the job
                position.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v4/{name=projects/*/tenants/*/companies/*}",
                },
            ]
            request, metadata = self._interceptor.pre_get_company(request, metadata)
            pb_request = company_service.GetCompanyRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = company.Company()
            pb_resp = company.Company.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_company(resp)
            return resp

    class _ListCompanies(CompanyServiceRestStub):
        def __hash__(self):
            return hash("ListCompanies")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: company_service.ListCompaniesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> company_service.ListCompaniesResponse:
            r"""Call the list companies method over HTTP.

            Args:
                request (~.company_service.ListCompaniesRequest):
                    The request object. List companies for which the client
                has ACL visibility.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.company_service.ListCompaniesResponse:
                    The List companies response object.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v4/{parent=projects/*/tenants/*}/companies",
                },
            ]
            request, metadata = self._interceptor.pre_list_companies(request, metadata)
            pb_request = company_service.ListCompaniesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = company_service.ListCompaniesResponse()
            pb_resp = company_service.ListCompaniesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_companies(resp)
            return resp

    class _UpdateCompany(CompanyServiceRestStub):
        def __hash__(self):
            return hash("UpdateCompany")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: company_service.UpdateCompanyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gct_company.Company:
            r"""Call the update company method over HTTP.

            Args:
                request (~.company_service.UpdateCompanyRequest):
                    The request object. Request for updating a specified
                company.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gct_company.Company:
                    A Company resource represents a
                company in the service. A company is the
                entity that owns job postings, that is,
                the hiring entity responsible for
                employing applicants for the job
                position.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v4/{company.name=projects/*/tenants/*/companies/*}",
                    "body": "company",
                },
            ]
            request, metadata = self._interceptor.pre_update_company(request, metadata)
            pb_request = company_service.UpdateCompanyRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gct_company.Company()
            pb_resp = gct_company.Company.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_company(resp)
            return resp

    @property
    def create_company(
        self,
    ) -> Callable[[company_service.CreateCompanyRequest], gct_company.Company]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCompany(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_company(
        self,
    ) -> Callable[[company_service.DeleteCompanyRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCompany(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_company(
        self,
    ) -> Callable[[company_service.GetCompanyRequest], company.Company]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCompany(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_companies(
        self,
    ) -> Callable[
        [company_service.ListCompaniesRequest], company_service.ListCompaniesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCompanies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_company(
        self,
    ) -> Callable[[company_service.UpdateCompanyRequest], gct_company.Company]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCompany(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(CompanyServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v4/{name=projects/*/operations/*}",
                },
            ]

            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.Operation()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_operation(resp)
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("CompanyServiceRestTransport",)
