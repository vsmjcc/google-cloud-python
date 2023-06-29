# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from collections import OrderedDict
import functools
import re
from typing import (
    AsyncIterable,
    Awaitable,
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.maps.routing_v2 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.protobuf import duration_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore

from google.maps.routing_v2.types import (
    fallback_info,
    geocoding_results,
    route,
    routes_service,
)

from .client import RoutesClient
from .transports.base import DEFAULT_CLIENT_INFO, RoutesTransport
from .transports.grpc_asyncio import RoutesGrpcAsyncIOTransport


class RoutesAsyncClient:
    """The Routes API."""

    _client: RoutesClient

    DEFAULT_ENDPOINT = RoutesClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = RoutesClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(RoutesClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(
        RoutesClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(RoutesClient.common_folder_path)
    parse_common_folder_path = staticmethod(RoutesClient.parse_common_folder_path)
    common_organization_path = staticmethod(RoutesClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        RoutesClient.parse_common_organization_path
    )
    common_project_path = staticmethod(RoutesClient.common_project_path)
    parse_common_project_path = staticmethod(RoutesClient.parse_common_project_path)
    common_location_path = staticmethod(RoutesClient.common_location_path)
    parse_common_location_path = staticmethod(RoutesClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RoutesAsyncClient: The constructed client.
        """
        return RoutesClient.from_service_account_info.__func__(RoutesAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RoutesAsyncClient: The constructed client.
        """
        return RoutesClient.from_service_account_file.__func__(RoutesAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return RoutesClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> RoutesTransport:
        """Returns the transport used by the client instance.

        Returns:
            RoutesTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(RoutesClient).get_transport_class, type(RoutesClient)
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, RoutesTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the routes client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.RoutesTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = RoutesClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def compute_routes(
        self,
        request: Optional[Union[routes_service.ComputeRoutesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> routes_service.ComputeRoutesResponse:
        r"""Returns the primary route along with optional alternate routes,
        given a set of terminal and intermediate waypoints.

        **NOTE:** This method requires that you specify a response field
        mask in the input. You can provide the response field mask by
        using URL parameter ``$fields`` or ``fields``, or by using an
        HTTP/gRPC header ``X-Goog-FieldMask`` (see the `available URL
        parameters and
        headers <https://cloud.google.com/apis/docs/system-parameters>`__.
        The value is a comma separated list of field paths. See detailed
        documentation about `how to construct the field
        paths <https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/field_mask.proto>`__.

        For example, in this method:

        -  Field mask of all available fields (for manual inspection):
           ``X-Goog-FieldMask: *``
        -  Field mask of Route-level duration, distance, and polyline
           (an example production setup):
           ``X-Goog-FieldMask: routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline``

        Google discourage the use of the wildcard (``*``) response field
        mask, or specifying the field mask at the top level
        (``routes``), because:

        -  Selecting only the fields that you need helps our server save
           computation cycles, allowing us to return the result to you
           with a lower latency.
        -  Selecting only the fields that you need in your production
           job ensures stable latency performance. We might add more
           response fields in the future, and those new fields might
           require extra computation time. If you select all fields, or
           if you select all fields at the top level, then you might
           experience performance degradation because any new field we
           add will be automatically included in the response.
        -  Selecting only the fields that you need results in a smaller
           response size, and thus higher network throughput.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import routing_v2

            async def sample_compute_routes():
                # Create a client
                client = routing_v2.RoutesAsyncClient()

                # Initialize request argument(s)
                request = routing_v2.ComputeRoutesRequest(
                )

                # Make the request
                response = await client.compute_routes(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.routing_v2.types.ComputeRoutesRequest, dict]]):
                The request object. ComputeRoutes request message.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.maps.routing_v2.types.ComputeRoutesResponse:
                ComputeRoutes the response message.
        """
        # Create or coerce a protobuf request object.
        request = routes_service.ComputeRoutesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.compute_routes,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def compute_route_matrix(
        self,
        request: Optional[Union[routes_service.ComputeRouteMatrixRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> Awaitable[AsyncIterable[routes_service.RouteMatrixElement]]:
        r"""Takes in a list of origins and destinations and returns a stream
        containing route information for each combination of origin and
        destination.

        **NOTE:** This method requires that you specify a response field
        mask in the input. You can provide the response field mask by
        using the URL parameter ``$fields`` or ``fields``, or by using
        the HTTP/gRPC header ``X-Goog-FieldMask`` (see the `available
        URL parameters and
        headers <https://cloud.google.com/apis/docs/system-parameters>`__.
        The value is a comma separated list of field paths. See this
        detailed documentation about `how to construct the field
        paths <https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/field_mask.proto>`__.

        For example, in this method:

        -  Field mask of all available fields (for manual inspection):
           ``X-Goog-FieldMask: *``
        -  Field mask of route durations, distances, element status,
           condition, and element indices (an example production setup):
           ``X-Goog-FieldMask: originIndex,destinationIndex,status,condition,distanceMeters,duration``

        It is critical that you include ``status`` in your field mask as
        otherwise all messages will appear to be OK. Google discourages
        the use of the wildcard (``*``) response field mask, because:

        -  Selecting only the fields that you need helps our server save
           computation cycles, allowing us to return the result to you
           with a lower latency.
        -  Selecting only the fields that you need in your production
           job ensures stable latency performance. We might add more
           response fields in the future, and those new fields might
           require extra computation time. If you select all fields, or
           if you select all fields at the top level, then you might
           experience performance degradation because any new field we
           add will be automatically included in the response.
        -  Selecting only the fields that you need results in a smaller
           response size, and thus higher network throughput.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import routing_v2

            async def sample_compute_route_matrix():
                # Create a client
                client = routing_v2.RoutesAsyncClient()

                # Initialize request argument(s)
                request = routing_v2.ComputeRouteMatrixRequest(
                )

                # Make the request
                stream = await client.compute_route_matrix(request=request)

                # Handle the response
                async for response in stream:
                    print(response)

        Args:
            request (Optional[Union[google.maps.routing_v2.types.ComputeRouteMatrixRequest, dict]]):
                The request object. ComputeRouteMatrix request message
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            AsyncIterable[google.maps.routing_v2.types.RouteMatrixElement]:
                Contains route information computed
                for an origin/destination pair in the
                ComputeRouteMatrix API. This proto can
                be streamed to the client.

        """
        # Create or coerce a protobuf request object.
        request = routes_service.ComputeRouteMatrixRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.compute_route_matrix,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("RoutesAsyncClient",)
