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
from typing import Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, grpc_helpers, operations_v1
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
import grpc  # type: ignore

from google.cloud.orchestration.airflow.service_v1.types import environments

from .base import DEFAULT_CLIENT_INFO, EnvironmentsTransport


class EnvironmentsGrpcTransport(EnvironmentsTransport):
    """gRPC backend transport for Environments.

    Managed Apache Airflow Environments.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "composer.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[grpc.Channel] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
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
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "composer.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def create_environment(
        self,
    ) -> Callable[[environments.CreateEnvironmentRequest], operations_pb2.Operation]:
        r"""Return a callable for the create environment method over gRPC.

        Create a new environment.

        Returns:
            Callable[[~.CreateEnvironmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_environment" not in self._stubs:
            self._stubs["create_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/CreateEnvironment",
                request_serializer=environments.CreateEnvironmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_environment"]

    @property
    def get_environment(
        self,
    ) -> Callable[[environments.GetEnvironmentRequest], environments.Environment]:
        r"""Return a callable for the get environment method over gRPC.

        Get an existing environment.

        Returns:
            Callable[[~.GetEnvironmentRequest],
                    ~.Environment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_environment" not in self._stubs:
            self._stubs["get_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/GetEnvironment",
                request_serializer=environments.GetEnvironmentRequest.serialize,
                response_deserializer=environments.Environment.deserialize,
            )
        return self._stubs["get_environment"]

    @property
    def list_environments(
        self,
    ) -> Callable[
        [environments.ListEnvironmentsRequest], environments.ListEnvironmentsResponse
    ]:
        r"""Return a callable for the list environments method over gRPC.

        List environments.

        Returns:
            Callable[[~.ListEnvironmentsRequest],
                    ~.ListEnvironmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_environments" not in self._stubs:
            self._stubs["list_environments"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/ListEnvironments",
                request_serializer=environments.ListEnvironmentsRequest.serialize,
                response_deserializer=environments.ListEnvironmentsResponse.deserialize,
            )
        return self._stubs["list_environments"]

    @property
    def update_environment(
        self,
    ) -> Callable[[environments.UpdateEnvironmentRequest], operations_pb2.Operation]:
        r"""Return a callable for the update environment method over gRPC.

        Update an environment.

        Returns:
            Callable[[~.UpdateEnvironmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_environment" not in self._stubs:
            self._stubs["update_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/UpdateEnvironment",
                request_serializer=environments.UpdateEnvironmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_environment"]

    @property
    def delete_environment(
        self,
    ) -> Callable[[environments.DeleteEnvironmentRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete environment method over gRPC.

        Delete an environment.

        Returns:
            Callable[[~.DeleteEnvironmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_environment" not in self._stubs:
            self._stubs["delete_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/DeleteEnvironment",
                request_serializer=environments.DeleteEnvironmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_environment"]

    @property
    def execute_airflow_command(
        self,
    ) -> Callable[
        [environments.ExecuteAirflowCommandRequest],
        environments.ExecuteAirflowCommandResponse,
    ]:
        r"""Return a callable for the execute airflow command method over gRPC.

        Executes Airflow CLI command.

        Returns:
            Callable[[~.ExecuteAirflowCommandRequest],
                    ~.ExecuteAirflowCommandResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "execute_airflow_command" not in self._stubs:
            self._stubs["execute_airflow_command"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/ExecuteAirflowCommand",
                request_serializer=environments.ExecuteAirflowCommandRequest.serialize,
                response_deserializer=environments.ExecuteAirflowCommandResponse.deserialize,
            )
        return self._stubs["execute_airflow_command"]

    @property
    def stop_airflow_command(
        self,
    ) -> Callable[
        [environments.StopAirflowCommandRequest],
        environments.StopAirflowCommandResponse,
    ]:
        r"""Return a callable for the stop airflow command method over gRPC.

        Stops Airflow CLI command execution.

        Returns:
            Callable[[~.StopAirflowCommandRequest],
                    ~.StopAirflowCommandResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_airflow_command" not in self._stubs:
            self._stubs["stop_airflow_command"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/StopAirflowCommand",
                request_serializer=environments.StopAirflowCommandRequest.serialize,
                response_deserializer=environments.StopAirflowCommandResponse.deserialize,
            )
        return self._stubs["stop_airflow_command"]

    @property
    def poll_airflow_command(
        self,
    ) -> Callable[
        [environments.PollAirflowCommandRequest],
        environments.PollAirflowCommandResponse,
    ]:
        r"""Return a callable for the poll airflow command method over gRPC.

        Polls Airflow CLI command execution and fetches logs.

        Returns:
            Callable[[~.PollAirflowCommandRequest],
                    ~.PollAirflowCommandResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "poll_airflow_command" not in self._stubs:
            self._stubs["poll_airflow_command"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/PollAirflowCommand",
                request_serializer=environments.PollAirflowCommandRequest.serialize,
                response_deserializer=environments.PollAirflowCommandResponse.deserialize,
            )
        return self._stubs["poll_airflow_command"]

    @property
    def save_snapshot(
        self,
    ) -> Callable[[environments.SaveSnapshotRequest], operations_pb2.Operation]:
        r"""Return a callable for the save snapshot method over gRPC.

        Creates a snapshots of a Cloud Composer environment.
        As a result of this operation, snapshot of environment's
        state is stored in a location specified in the
        SaveSnapshotRequest.

        Returns:
            Callable[[~.SaveSnapshotRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "save_snapshot" not in self._stubs:
            self._stubs["save_snapshot"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/SaveSnapshot",
                request_serializer=environments.SaveSnapshotRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["save_snapshot"]

    @property
    def load_snapshot(
        self,
    ) -> Callable[[environments.LoadSnapshotRequest], operations_pb2.Operation]:
        r"""Return a callable for the load snapshot method over gRPC.

        Loads a snapshot of a Cloud Composer environment.
        As a result of this operation, a snapshot of
        environment's specified in LoadSnapshotRequest is loaded
        into the environment.

        Returns:
            Callable[[~.LoadSnapshotRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "load_snapshot" not in self._stubs:
            self._stubs["load_snapshot"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/LoadSnapshot",
                request_serializer=environments.LoadSnapshotRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["load_snapshot"]

    @property
    def database_failover(
        self,
    ) -> Callable[[environments.DatabaseFailoverRequest], operations_pb2.Operation]:
        r"""Return a callable for the database failover method over gRPC.

        Triggers database failover (only for highly resilient
        environments).

        Returns:
            Callable[[~.DatabaseFailoverRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "database_failover" not in self._stubs:
            self._stubs["database_failover"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/DatabaseFailover",
                request_serializer=environments.DatabaseFailoverRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["database_failover"]

    @property
    def fetch_database_properties(
        self,
    ) -> Callable[
        [environments.FetchDatabasePropertiesRequest],
        environments.FetchDatabasePropertiesResponse,
    ]:
        r"""Return a callable for the fetch database properties method over gRPC.

        Fetches database properties.

        Returns:
            Callable[[~.FetchDatabasePropertiesRequest],
                    ~.FetchDatabasePropertiesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_database_properties" not in self._stubs:
            self._stubs["fetch_database_properties"] = self.grpc_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1.Environments/FetchDatabaseProperties",
                request_serializer=environments.FetchDatabasePropertiesRequest.serialize,
                response_deserializer=environments.FetchDatabasePropertiesResponse.deserialize,
            )
        return self._stubs["fetch_database_properties"]

    def close(self):
        self.grpc_channel.close()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse
    ]:
        r"""Return a callable for the list_operations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("EnvironmentsGrpcTransport",)
