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
from collections import OrderedDict
import functools
import re
from typing import (
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

from google.cloud.shell_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.longrunning import operations_pb2

from google.cloud.shell_v1.types import cloudshell

from .client import CloudShellServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, CloudShellServiceTransport
from .transports.grpc_asyncio import CloudShellServiceGrpcAsyncIOTransport


class CloudShellServiceAsyncClient:
    """API for interacting with Google Cloud Shell. Each user of
    Cloud Shell has at least one environment, which has the ID
    "default". Environment consists of a Docker image defining what
    is installed on the environment and a home directory containing
    the user's data that will remain across sessions. Clients use
    this API to start and fetch information about their environment,
    which can then be used to connect to that environment via a
    separate SSH client.
    """

    _client: CloudShellServiceClient

    DEFAULT_ENDPOINT = CloudShellServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CloudShellServiceClient.DEFAULT_MTLS_ENDPOINT

    environment_path = staticmethod(CloudShellServiceClient.environment_path)
    parse_environment_path = staticmethod(
        CloudShellServiceClient.parse_environment_path
    )
    common_billing_account_path = staticmethod(
        CloudShellServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CloudShellServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(CloudShellServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        CloudShellServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        CloudShellServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        CloudShellServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(CloudShellServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        CloudShellServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(CloudShellServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        CloudShellServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudShellServiceAsyncClient: The constructed client.
        """
        return CloudShellServiceClient.from_service_account_info.__func__(CloudShellServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            CloudShellServiceAsyncClient: The constructed client.
        """
        return CloudShellServiceClient.from_service_account_file.__func__(CloudShellServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return CloudShellServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> CloudShellServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudShellServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(CloudShellServiceClient).get_transport_class, type(CloudShellServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, CloudShellServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud shell service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.CloudShellServiceTransport]): The
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
        self._client = CloudShellServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def get_environment(
        self,
        request: Optional[Union[cloudshell.GetEnvironmentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cloudshell.Environment:
        r"""Gets an environment. Returns NOT_FOUND if the environment does
        not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import shell_v1

            async def sample_get_environment():
                # Create a client
                client = shell_v1.CloudShellServiceAsyncClient()

                # Initialize request argument(s)
                request = shell_v1.GetEnvironmentRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_environment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.shell_v1.types.GetEnvironmentRequest, dict]]):
                The request object. Request message for
                [GetEnvironment][google.cloud.shell.v1.CloudShellService.GetEnvironment].
            name (:class:`str`):
                Required. Name of the requested resource, for example
                ``users/me/environments/default`` or
                ``users/someone@example.com/environments/default``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.shell_v1.types.Environment:
                A Cloud Shell environment, which is
                defined as the combination of a Docker
                image specifying what is installed on
                the environment and a home directory
                containing the user's data that will
                remain across sessions. Each user has at
                least an environment with the ID
                "default".

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloudshell.GetEnvironmentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_environment,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                    core_exceptions.Unknown,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
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

    async def start_environment(
        self,
        request: Optional[Union[cloudshell.StartEnvironmentRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Starts an existing environment, allowing clients to
        connect to it. The returned operation will contain an
        instance of StartEnvironmentMetadata in its metadata
        field. Users can wait for the environment to start by
        polling this operation via GetOperation. Once the
        environment has finished starting and is ready to accept
        connections, the operation will contain a
        StartEnvironmentResponse in its response field.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import shell_v1

            async def sample_start_environment():
                # Create a client
                client = shell_v1.CloudShellServiceAsyncClient()

                # Initialize request argument(s)
                request = shell_v1.StartEnvironmentRequest(
                )

                # Make the request
                operation = client.start_environment(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.shell_v1.types.StartEnvironmentRequest, dict]]):
                The request object. Request message for
                [StartEnvironment][google.cloud.shell.v1.CloudShellService.StartEnvironment].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.shell_v1.types.StartEnvironmentResponse` Message included in the response field of operations returned from
                   [StartEnvironment][google.cloud.shell.v1.CloudShellService.StartEnvironment]
                   once the operation is complete.

        """
        # Create or coerce a protobuf request object.
        request = cloudshell.StartEnvironmentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.start_environment,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudshell.StartEnvironmentResponse,
            metadata_type=cloudshell.StartEnvironmentMetadata,
        )

        # Done; return the response.
        return response

    async def authorize_environment(
        self,
        request: Optional[Union[cloudshell.AuthorizeEnvironmentRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Sends OAuth credentials to a running environment on
        behalf of a user. When this completes, the environment
        will be authorized to run various Google Cloud command
        line tools without requiring the user to manually
        authenticate.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import shell_v1

            async def sample_authorize_environment():
                # Create a client
                client = shell_v1.CloudShellServiceAsyncClient()

                # Initialize request argument(s)
                request = shell_v1.AuthorizeEnvironmentRequest(
                )

                # Make the request
                operation = client.authorize_environment(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.shell_v1.types.AuthorizeEnvironmentRequest, dict]]):
                The request object. Request message for
                [AuthorizeEnvironment][google.cloud.shell.v1.CloudShellService.AuthorizeEnvironment].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.shell_v1.types.AuthorizeEnvironmentResponse` Response message for
                   [AuthorizeEnvironment][google.cloud.shell.v1.CloudShellService.AuthorizeEnvironment].

        """
        # Create or coerce a protobuf request object.
        request = cloudshell.AuthorizeEnvironmentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.authorize_environment,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudshell.AuthorizeEnvironmentResponse,
            metadata_type=cloudshell.AuthorizeEnvironmentMetadata,
        )

        # Done; return the response.
        return response

    async def add_public_key(
        self,
        request: Optional[Union[cloudshell.AddPublicKeyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Adds a public SSH key to an environment, allowing clients with
        the corresponding private key to connect to that environment via
        SSH. If a key with the same content already exists, this will
        error with ALREADY_EXISTS.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import shell_v1

            async def sample_add_public_key():
                # Create a client
                client = shell_v1.CloudShellServiceAsyncClient()

                # Initialize request argument(s)
                request = shell_v1.AddPublicKeyRequest(
                )

                # Make the request
                operation = client.add_public_key(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.shell_v1.types.AddPublicKeyRequest, dict]]):
                The request object. Request message for
                [AddPublicKey][google.cloud.shell.v1.CloudShellService.AddPublicKey].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.shell_v1.types.AddPublicKeyResponse` Response message for
                   [AddPublicKey][google.cloud.shell.v1.CloudShellService.AddPublicKey].

        """
        # Create or coerce a protobuf request object.
        request = cloudshell.AddPublicKeyRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.add_public_key,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudshell.AddPublicKeyResponse,
            metadata_type=cloudshell.AddPublicKeyMetadata,
        )

        # Done; return the response.
        return response

    async def remove_public_key(
        self,
        request: Optional[Union[cloudshell.RemovePublicKeyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Removes a public SSH key from an environment. Clients will no
        longer be able to connect to the environment using the
        corresponding private key. If a key with the same content is not
        present, this will error with NOT_FOUND.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import shell_v1

            async def sample_remove_public_key():
                # Create a client
                client = shell_v1.CloudShellServiceAsyncClient()

                # Initialize request argument(s)
                request = shell_v1.RemovePublicKeyRequest(
                )

                # Make the request
                operation = client.remove_public_key(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.shell_v1.types.RemovePublicKeyRequest, dict]]):
                The request object. Request message for
                [RemovePublicKey][google.cloud.shell.v1.CloudShellService.RemovePublicKey].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.shell_v1.types.RemovePublicKeyResponse` Response message for
                   [RemovePublicKey][google.cloud.shell.v1.CloudShellService.RemovePublicKey].

        """
        # Create or coerce a protobuf request object.
        request = cloudshell.RemovePublicKeyRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.remove_public_key,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudshell.RemovePublicKeyResponse,
            metadata_type=cloudshell.RemovePublicKeyMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "CloudShellServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("CloudShellServiceAsyncClient",)
