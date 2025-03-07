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
import os

# try/except added for compatibility with python < 3.8
try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    import mock

from collections.abc import Iterable
import json
import math

from google.api_core import (
    future,
    gapic_v1,
    grpc_helpers,
    grpc_helpers_async,
    operation,
    operations_v1,
    path_template,
)
from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import operation_async  # type: ignore
import google.auth
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.location import locations_pb2
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import options_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import json_format
from google.protobuf import timestamp_pb2  # type: ignore
from google.type import expr_pb2  # type: ignore
import grpc
from grpc.experimental import aio
from proto.marshal.rules import wrappers
from proto.marshal.rules.dates import DurationRule, TimestampRule
import pytest
from requests import PreparedRequest, Request, Response
from requests.sessions import Session

from google.cloud.security.privateca_v1.services.certificate_authority_service import (
    CertificateAuthorityServiceAsyncClient,
    CertificateAuthorityServiceClient,
    pagers,
    transports,
)
from google.cloud.security.privateca_v1.types import resources, service


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert CertificateAuthorityServiceClient._get_default_mtls_endpoint(None) is None
    assert (
        CertificateAuthorityServiceClient._get_default_mtls_endpoint(api_endpoint)
        == api_mtls_endpoint
    )
    assert (
        CertificateAuthorityServiceClient._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        CertificateAuthorityServiceClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        CertificateAuthorityServiceClient._get_default_mtls_endpoint(
            sandbox_mtls_endpoint
        )
        == sandbox_mtls_endpoint
    )
    assert (
        CertificateAuthorityServiceClient._get_default_mtls_endpoint(non_googleapi)
        == non_googleapi
    )


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (CertificateAuthorityServiceClient, "grpc"),
        (CertificateAuthorityServiceAsyncClient, "grpc_asyncio"),
        (CertificateAuthorityServiceClient, "rest"),
    ],
)
def test_certificate_authority_service_client_from_service_account_info(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "privateca.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://privateca.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.CertificateAuthorityServiceGrpcTransport, "grpc"),
        (transports.CertificateAuthorityServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.CertificateAuthorityServiceRestTransport, "rest"),
    ],
)
def test_certificate_authority_service_client_service_account_always_use_jwt(
    transport_class, transport_name
):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (CertificateAuthorityServiceClient, "grpc"),
        (CertificateAuthorityServiceAsyncClient, "grpc_asyncio"),
        (CertificateAuthorityServiceClient, "rest"),
    ],
)
def test_certificate_authority_service_client_from_service_account_file(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "privateca.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://privateca.googleapis.com"
        )


def test_certificate_authority_service_client_get_transport_class():
    transport = CertificateAuthorityServiceClient.get_transport_class()
    available_transports = [
        transports.CertificateAuthorityServiceGrpcTransport,
        transports.CertificateAuthorityServiceRestTransport,
    ]
    assert transport in available_transports

    transport = CertificateAuthorityServiceClient.get_transport_class("grpc")
    assert transport == transports.CertificateAuthorityServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceGrpcTransport,
            "grpc",
        ),
        (
            CertificateAuthorityServiceAsyncClient,
            transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    CertificateAuthorityServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(CertificateAuthorityServiceClient),
)
@mock.patch.object(
    CertificateAuthorityServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(CertificateAuthorityServiceAsyncClient),
)
def test_certificate_authority_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(
        CertificateAuthorityServiceClient, "get_transport_class"
    ) as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(
        CertificateAuthorityServiceClient, "get_transport_class"
    ) as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class(transport=transport_name)

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class(transport=transport_name)

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(
        api_audience="https://language.googleapis.com"
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com",
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            CertificateAuthorityServiceAsyncClient,
            transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            CertificateAuthorityServiceAsyncClient,
            transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceRestTransport,
            "rest",
            "true",
        ),
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    CertificateAuthorityServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(CertificateAuthorityServiceClient),
)
@mock.patch.object(
    CertificateAuthorityServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(CertificateAuthorityServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_certificate_authority_service_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                        api_audience=None,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                    api_audience=None,
                )


@pytest.mark.parametrize(
    "client_class",
    [CertificateAuthorityServiceClient, CertificateAuthorityServiceAsyncClient],
)
@mock.patch.object(
    CertificateAuthorityServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(CertificateAuthorityServiceClient),
)
@mock.patch.object(
    CertificateAuthorityServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(CertificateAuthorityServiceAsyncClient),
)
def test_certificate_authority_service_client_get_mtls_endpoint_and_cert_source(
    client_class,
):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=False,
        ):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=True,
        ):
            with mock.patch(
                "google.auth.transport.mtls.default_client_cert_source",
                return_value=mock_client_cert_source,
            ):
                (
                    api_endpoint,
                    cert_source,
                ) = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceGrpcTransport,
            "grpc",
        ),
        (
            CertificateAuthorityServiceAsyncClient,
            transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceRestTransport,
            "rest",
        ),
    ],
)
def test_certificate_authority_service_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            CertificateAuthorityServiceAsyncClient,
            transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_certificate_authority_service_client_client_options_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


def test_certificate_authority_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.security.privateca_v1.services.certificate_authority_service.transports.CertificateAuthorityServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = CertificateAuthorityServiceClient(
            client_options={"api_endpoint": "squid.clam.whelk"}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            CertificateAuthorityServiceAsyncClient,
            transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_certificate_authority_service_client_create_channel_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "privateca.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=None,
            default_host="privateca.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.CreateCertificateRequest,
        dict,
    ],
)
def test_create_certificate(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate(
            name="name_value",
            issuer_certificate_authority="issuer_certificate_authority_value",
            certificate_template="certificate_template_value",
            subject_mode=resources.SubjectRequestMode.DEFAULT,
            pem_certificate="pem_certificate_value",
            pem_certificate_chain=["pem_certificate_chain_value"],
            pem_csr="pem_csr_value",
        )
        response = client.create_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


def test_create_certificate_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate), "__call__"
    ) as call:
        client.create_certificate()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateRequest()


@pytest.mark.asyncio
async def test_create_certificate_async(
    transport: str = "grpc_asyncio", request_type=service.CreateCertificateRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate(
                name="name_value",
                issuer_certificate_authority="issuer_certificate_authority_value",
                certificate_template="certificate_template_value",
                subject_mode=resources.SubjectRequestMode.DEFAULT,
                pem_certificate="pem_certificate_value",
                pem_certificate_chain=["pem_certificate_chain_value"],
            )
        )
        response = await client.create_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


@pytest.mark.asyncio
async def test_create_certificate_async_from_dict():
    await test_create_certificate_async(request_type=dict)


def test_create_certificate_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateCertificateRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate), "__call__"
    ) as call:
        call.return_value = resources.Certificate()
        client.create_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_certificate_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateCertificateRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate()
        )
        await client.create_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_create_certificate_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_certificate(
            parent="parent_value",
            certificate=resources.Certificate(name="name_value"),
            certificate_id="certificate_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].certificate
        mock_val = resources.Certificate(name="name_value")
        assert arg == mock_val
        arg = args[0].certificate_id
        mock_val = "certificate_id_value"
        assert arg == mock_val


def test_create_certificate_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_certificate(
            service.CreateCertificateRequest(),
            parent="parent_value",
            certificate=resources.Certificate(name="name_value"),
            certificate_id="certificate_id_value",
        )


@pytest.mark.asyncio
async def test_create_certificate_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_certificate(
            parent="parent_value",
            certificate=resources.Certificate(name="name_value"),
            certificate_id="certificate_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].certificate
        mock_val = resources.Certificate(name="name_value")
        assert arg == mock_val
        arg = args[0].certificate_id
        mock_val = "certificate_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_certificate_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_certificate(
            service.CreateCertificateRequest(),
            parent="parent_value",
            certificate=resources.Certificate(name="name_value"),
            certificate_id="certificate_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCertificateRequest,
        dict,
    ],
)
def test_get_certificate(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_certificate), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate(
            name="name_value",
            issuer_certificate_authority="issuer_certificate_authority_value",
            certificate_template="certificate_template_value",
            subject_mode=resources.SubjectRequestMode.DEFAULT,
            pem_certificate="pem_certificate_value",
            pem_certificate_chain=["pem_certificate_chain_value"],
            pem_csr="pem_csr_value",
        )
        response = client.get_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


def test_get_certificate_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_certificate), "__call__") as call:
        client.get_certificate()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateRequest()


@pytest.mark.asyncio
async def test_get_certificate_async(
    transport: str = "grpc_asyncio", request_type=service.GetCertificateRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_certificate), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate(
                name="name_value",
                issuer_certificate_authority="issuer_certificate_authority_value",
                certificate_template="certificate_template_value",
                subject_mode=resources.SubjectRequestMode.DEFAULT,
                pem_certificate="pem_certificate_value",
                pem_certificate_chain=["pem_certificate_chain_value"],
            )
        )
        response = await client.get_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


@pytest.mark.asyncio
async def test_get_certificate_async_from_dict():
    await test_get_certificate_async(request_type=dict)


def test_get_certificate_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCertificateRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_certificate), "__call__") as call:
        call.return_value = resources.Certificate()
        client.get_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_certificate_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCertificateRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_certificate), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate()
        )
        await client.get_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_certificate_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_certificate), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_certificate(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_certificate_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_certificate(
            service.GetCertificateRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_certificate_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_certificate), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_certificate(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_certificate_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_certificate(
            service.GetCertificateRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCertificatesRequest,
        dict,
    ],
)
def test_list_certificates(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificatesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )
        response = client.list_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificatesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificatesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_certificates_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        client.list_certificates()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificatesRequest()


@pytest.mark.asyncio
async def test_list_certificates_async(
    transport: str = "grpc_asyncio", request_type=service.ListCertificatesRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificatesResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        response = await client.list_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificatesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificatesAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.asyncio
async def test_list_certificates_async_from_dict():
    await test_list_certificates_async(request_type=dict)


def test_list_certificates_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCertificatesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        call.return_value = service.ListCertificatesResponse()
        client.list_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_certificates_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCertificatesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificatesResponse()
        )
        await client.list_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_certificates_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificatesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_certificates(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_certificates_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_certificates(
            service.ListCertificatesRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_certificates_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificatesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificatesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_certificates(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_certificates_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_certificates(
            service.ListCertificatesRequest(),
            parent="parent_value",
        )


def test_list_certificates_pager(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                    resources.Certificate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificatesResponse(
                certificates=[],
                next_page_token="def",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_certificates(request={})

        assert pager._metadata == metadata

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.Certificate) for i in results)


def test_list_certificates_pages(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                    resources.Certificate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificatesResponse(
                certificates=[],
                next_page_token="def",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_certificates(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_certificates_async_pager():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                    resources.Certificate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificatesResponse(
                certificates=[],
                next_page_token="def",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_certificates(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.Certificate) for i in responses)


@pytest.mark.asyncio
async def test_list_certificates_async_pages():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificates),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                    resources.Certificate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificatesResponse(
                certificates=[],
                next_page_token="def",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        # Workaround issue in python 3.9 related to code coverage by adding `# pragma: no branch`
        # See https://github.com/googleapis/gapic-generator-python/pull/1174#issuecomment-1025132372
        async for page_ in (  # pragma: no branch
            await client.list_certificates(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.RevokeCertificateRequest,
        dict,
    ],
)
def test_revoke_certificate(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.revoke_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate(
            name="name_value",
            issuer_certificate_authority="issuer_certificate_authority_value",
            certificate_template="certificate_template_value",
            subject_mode=resources.SubjectRequestMode.DEFAULT,
            pem_certificate="pem_certificate_value",
            pem_certificate_chain=["pem_certificate_chain_value"],
            pem_csr="pem_csr_value",
        )
        response = client.revoke_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.RevokeCertificateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


def test_revoke_certificate_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.revoke_certificate), "__call__"
    ) as call:
        client.revoke_certificate()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.RevokeCertificateRequest()


@pytest.mark.asyncio
async def test_revoke_certificate_async(
    transport: str = "grpc_asyncio", request_type=service.RevokeCertificateRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.revoke_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate(
                name="name_value",
                issuer_certificate_authority="issuer_certificate_authority_value",
                certificate_template="certificate_template_value",
                subject_mode=resources.SubjectRequestMode.DEFAULT,
                pem_certificate="pem_certificate_value",
                pem_certificate_chain=["pem_certificate_chain_value"],
            )
        )
        response = await client.revoke_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.RevokeCertificateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


@pytest.mark.asyncio
async def test_revoke_certificate_async_from_dict():
    await test_revoke_certificate_async(request_type=dict)


def test_revoke_certificate_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.RevokeCertificateRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.revoke_certificate), "__call__"
    ) as call:
        call.return_value = resources.Certificate()
        client.revoke_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_revoke_certificate_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.RevokeCertificateRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.revoke_certificate), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate()
        )
        await client.revoke_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_revoke_certificate_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.revoke_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.revoke_certificate(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_revoke_certificate_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.revoke_certificate(
            service.RevokeCertificateRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_revoke_certificate_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.revoke_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.revoke_certificate(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_revoke_certificate_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.revoke_certificate(
            service.RevokeCertificateRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCertificateRequest,
        dict,
    ],
)
def test_update_certificate(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate(
            name="name_value",
            issuer_certificate_authority="issuer_certificate_authority_value",
            certificate_template="certificate_template_value",
            subject_mode=resources.SubjectRequestMode.DEFAULT,
            pem_certificate="pem_certificate_value",
            pem_certificate_chain=["pem_certificate_chain_value"],
            pem_csr="pem_csr_value",
        )
        response = client.update_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


def test_update_certificate_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate), "__call__"
    ) as call:
        client.update_certificate()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateRequest()


@pytest.mark.asyncio
async def test_update_certificate_async(
    transport: str = "grpc_asyncio", request_type=service.UpdateCertificateRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate(
                name="name_value",
                issuer_certificate_authority="issuer_certificate_authority_value",
                certificate_template="certificate_template_value",
                subject_mode=resources.SubjectRequestMode.DEFAULT,
                pem_certificate="pem_certificate_value",
                pem_certificate_chain=["pem_certificate_chain_value"],
            )
        )
        response = await client.update_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


@pytest.mark.asyncio
async def test_update_certificate_async_from_dict():
    await test_update_certificate_async(request_type=dict)


def test_update_certificate_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCertificateRequest()

    request.certificate.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate), "__call__"
    ) as call:
        call.return_value = resources.Certificate()
        client.update_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "certificate.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_certificate_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCertificateRequest()

    request.certificate.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate()
        )
        await client.update_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "certificate.name=name_value",
    ) in kw["metadata"]


def test_update_certificate_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_certificate(
            certificate=resources.Certificate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].certificate
        mock_val = resources.Certificate(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_certificate_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_certificate(
            service.UpdateCertificateRequest(),
            certificate=resources.Certificate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_certificate_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Certificate()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Certificate()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_certificate(
            certificate=resources.Certificate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].certificate
        mock_val = resources.Certificate(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_certificate_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_certificate(
            service.UpdateCertificateRequest(),
            certificate=resources.Certificate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ActivateCertificateAuthorityRequest,
        dict,
    ],
)
def test_activate_certificate_authority(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.activate_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.activate_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ActivateCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_activate_certificate_authority_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.activate_certificate_authority), "__call__"
    ) as call:
        client.activate_certificate_authority()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ActivateCertificateAuthorityRequest()


@pytest.mark.asyncio
async def test_activate_certificate_authority_async(
    transport: str = "grpc_asyncio",
    request_type=service.ActivateCertificateAuthorityRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.activate_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.activate_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ActivateCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_activate_certificate_authority_async_from_dict():
    await test_activate_certificate_authority_async(request_type=dict)


def test_activate_certificate_authority_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ActivateCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.activate_certificate_authority), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.activate_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_activate_certificate_authority_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ActivateCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.activate_certificate_authority), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.activate_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_activate_certificate_authority_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.activate_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.activate_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_activate_certificate_authority_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.activate_certificate_authority(
            service.ActivateCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_activate_certificate_authority_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.activate_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.activate_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_activate_certificate_authority_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.activate_certificate_authority(
            service.ActivateCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.CreateCertificateAuthorityRequest,
        dict,
    ],
)
def test_create_certificate_authority(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_certificate_authority_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_authority), "__call__"
    ) as call:
        client.create_certificate_authority()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateAuthorityRequest()


@pytest.mark.asyncio
async def test_create_certificate_authority_async(
    transport: str = "grpc_asyncio",
    request_type=service.CreateCertificateAuthorityRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_create_certificate_authority_async_from_dict():
    await test_create_certificate_authority_async(request_type=dict)


def test_create_certificate_authority_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateCertificateAuthorityRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_authority), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_certificate_authority_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateCertificateAuthorityRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_authority), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_create_certificate_authority_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_certificate_authority(
            parent="parent_value",
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            certificate_authority_id="certificate_authority_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].certificate_authority
        mock_val = resources.CertificateAuthority(name="name_value")
        assert arg == mock_val
        arg = args[0].certificate_authority_id
        mock_val = "certificate_authority_id_value"
        assert arg == mock_val


def test_create_certificate_authority_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_certificate_authority(
            service.CreateCertificateAuthorityRequest(),
            parent="parent_value",
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            certificate_authority_id="certificate_authority_id_value",
        )


@pytest.mark.asyncio
async def test_create_certificate_authority_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_certificate_authority(
            parent="parent_value",
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            certificate_authority_id="certificate_authority_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].certificate_authority
        mock_val = resources.CertificateAuthority(name="name_value")
        assert arg == mock_val
        arg = args[0].certificate_authority_id
        mock_val = "certificate_authority_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_certificate_authority_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_certificate_authority(
            service.CreateCertificateAuthorityRequest(),
            parent="parent_value",
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            certificate_authority_id="certificate_authority_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.DisableCertificateAuthorityRequest,
        dict,
    ],
)
def test_disable_certificate_authority(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.disable_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.disable_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DisableCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_disable_certificate_authority_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.disable_certificate_authority), "__call__"
    ) as call:
        client.disable_certificate_authority()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DisableCertificateAuthorityRequest()


@pytest.mark.asyncio
async def test_disable_certificate_authority_async(
    transport: str = "grpc_asyncio",
    request_type=service.DisableCertificateAuthorityRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.disable_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.disable_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DisableCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_disable_certificate_authority_async_from_dict():
    await test_disable_certificate_authority_async(request_type=dict)


def test_disable_certificate_authority_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DisableCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.disable_certificate_authority), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.disable_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_disable_certificate_authority_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DisableCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.disable_certificate_authority), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.disable_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_disable_certificate_authority_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.disable_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.disable_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_disable_certificate_authority_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.disable_certificate_authority(
            service.DisableCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_disable_certificate_authority_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.disable_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.disable_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_disable_certificate_authority_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.disable_certificate_authority(
            service.DisableCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.EnableCertificateAuthorityRequest,
        dict,
    ],
)
def test_enable_certificate_authority(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.enable_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.enable_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.EnableCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_enable_certificate_authority_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.enable_certificate_authority), "__call__"
    ) as call:
        client.enable_certificate_authority()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.EnableCertificateAuthorityRequest()


@pytest.mark.asyncio
async def test_enable_certificate_authority_async(
    transport: str = "grpc_asyncio",
    request_type=service.EnableCertificateAuthorityRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.enable_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.enable_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.EnableCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_enable_certificate_authority_async_from_dict():
    await test_enable_certificate_authority_async(request_type=dict)


def test_enable_certificate_authority_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.EnableCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.enable_certificate_authority), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.enable_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_enable_certificate_authority_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.EnableCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.enable_certificate_authority), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.enable_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_enable_certificate_authority_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.enable_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.enable_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_enable_certificate_authority_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.enable_certificate_authority(
            service.EnableCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_enable_certificate_authority_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.enable_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.enable_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_enable_certificate_authority_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.enable_certificate_authority(
            service.EnableCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.FetchCertificateAuthorityCsrRequest,
        dict,
    ],
)
def test_fetch_certificate_authority_csr(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_certificate_authority_csr), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.FetchCertificateAuthorityCsrResponse(
            pem_csr="pem_csr_value",
        )
        response = client.fetch_certificate_authority_csr(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.FetchCertificateAuthorityCsrRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.FetchCertificateAuthorityCsrResponse)
    assert response.pem_csr == "pem_csr_value"


def test_fetch_certificate_authority_csr_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_certificate_authority_csr), "__call__"
    ) as call:
        client.fetch_certificate_authority_csr()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.FetchCertificateAuthorityCsrRequest()


@pytest.mark.asyncio
async def test_fetch_certificate_authority_csr_async(
    transport: str = "grpc_asyncio",
    request_type=service.FetchCertificateAuthorityCsrRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_certificate_authority_csr), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.FetchCertificateAuthorityCsrResponse(
                pem_csr="pem_csr_value",
            )
        )
        response = await client.fetch_certificate_authority_csr(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.FetchCertificateAuthorityCsrRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.FetchCertificateAuthorityCsrResponse)
    assert response.pem_csr == "pem_csr_value"


@pytest.mark.asyncio
async def test_fetch_certificate_authority_csr_async_from_dict():
    await test_fetch_certificate_authority_csr_async(request_type=dict)


def test_fetch_certificate_authority_csr_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.FetchCertificateAuthorityCsrRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_certificate_authority_csr), "__call__"
    ) as call:
        call.return_value = service.FetchCertificateAuthorityCsrResponse()
        client.fetch_certificate_authority_csr(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_fetch_certificate_authority_csr_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.FetchCertificateAuthorityCsrRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_certificate_authority_csr), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.FetchCertificateAuthorityCsrResponse()
        )
        await client.fetch_certificate_authority_csr(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_fetch_certificate_authority_csr_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_certificate_authority_csr), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.FetchCertificateAuthorityCsrResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.fetch_certificate_authority_csr(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_fetch_certificate_authority_csr_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.fetch_certificate_authority_csr(
            service.FetchCertificateAuthorityCsrRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_fetch_certificate_authority_csr_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_certificate_authority_csr), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.FetchCertificateAuthorityCsrResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.FetchCertificateAuthorityCsrResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.fetch_certificate_authority_csr(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_fetch_certificate_authority_csr_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.fetch_certificate_authority_csr(
            service.FetchCertificateAuthorityCsrRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCertificateAuthorityRequest,
        dict,
    ],
)
def test_get_certificate_authority(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateAuthority(
            name="name_value",
            type_=resources.CertificateAuthority.Type.SELF_SIGNED,
            tier=resources.CaPool.Tier.ENTERPRISE,
            state=resources.CertificateAuthority.State.ENABLED,
            pem_ca_certificates=["pem_ca_certificates_value"],
            gcs_bucket="gcs_bucket_value",
        )
        response = client.get_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateAuthority)
    assert response.name == "name_value"
    assert response.type_ == resources.CertificateAuthority.Type.SELF_SIGNED
    assert response.tier == resources.CaPool.Tier.ENTERPRISE
    assert response.state == resources.CertificateAuthority.State.ENABLED
    assert response.pem_ca_certificates == ["pem_ca_certificates_value"]
    assert response.gcs_bucket == "gcs_bucket_value"


def test_get_certificate_authority_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_authority), "__call__"
    ) as call:
        client.get_certificate_authority()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateAuthorityRequest()


@pytest.mark.asyncio
async def test_get_certificate_authority_async(
    transport: str = "grpc_asyncio", request_type=service.GetCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateAuthority(
                name="name_value",
                type_=resources.CertificateAuthority.Type.SELF_SIGNED,
                tier=resources.CaPool.Tier.ENTERPRISE,
                state=resources.CertificateAuthority.State.ENABLED,
                pem_ca_certificates=["pem_ca_certificates_value"],
                gcs_bucket="gcs_bucket_value",
            )
        )
        response = await client.get_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateAuthority)
    assert response.name == "name_value"
    assert response.type_ == resources.CertificateAuthority.Type.SELF_SIGNED
    assert response.tier == resources.CaPool.Tier.ENTERPRISE
    assert response.state == resources.CertificateAuthority.State.ENABLED
    assert response.pem_ca_certificates == ["pem_ca_certificates_value"]
    assert response.gcs_bucket == "gcs_bucket_value"


@pytest.mark.asyncio
async def test_get_certificate_authority_async_from_dict():
    await test_get_certificate_authority_async(request_type=dict)


def test_get_certificate_authority_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_authority), "__call__"
    ) as call:
        call.return_value = resources.CertificateAuthority()
        client.get_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_certificate_authority_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_authority), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateAuthority()
        )
        await client.get_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_certificate_authority_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateAuthority()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_certificate_authority_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_certificate_authority(
            service.GetCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_certificate_authority_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateAuthority()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateAuthority()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_certificate_authority_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_certificate_authority(
            service.GetCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCertificateAuthoritiesRequest,
        dict,
    ],
)
def test_list_certificate_authorities(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateAuthoritiesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )
        response = client.list_certificate_authorities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateAuthoritiesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateAuthoritiesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_certificate_authorities_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        client.list_certificate_authorities()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateAuthoritiesRequest()


@pytest.mark.asyncio
async def test_list_certificate_authorities_async(
    transport: str = "grpc_asyncio",
    request_type=service.ListCertificateAuthoritiesRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateAuthoritiesResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        response = await client.list_certificate_authorities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateAuthoritiesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateAuthoritiesAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.asyncio
async def test_list_certificate_authorities_async_from_dict():
    await test_list_certificate_authorities_async(request_type=dict)


def test_list_certificate_authorities_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCertificateAuthoritiesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        call.return_value = service.ListCertificateAuthoritiesResponse()
        client.list_certificate_authorities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_certificate_authorities_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCertificateAuthoritiesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateAuthoritiesResponse()
        )
        await client.list_certificate_authorities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_certificate_authorities_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateAuthoritiesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_certificate_authorities(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_certificate_authorities_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_certificate_authorities(
            service.ListCertificateAuthoritiesRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_certificate_authorities_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateAuthoritiesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateAuthoritiesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_certificate_authorities(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_certificate_authorities_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_certificate_authorities(
            service.ListCertificateAuthoritiesRequest(),
            parent="parent_value",
        )


def test_list_certificate_authorities_pager(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[],
                next_page_token="def",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_certificate_authorities(request={})

        assert pager._metadata == metadata

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.CertificateAuthority) for i in results)


def test_list_certificate_authorities_pages(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[],
                next_page_token="def",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_certificate_authorities(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_certificate_authorities_async_pager():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[],
                next_page_token="def",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_certificate_authorities(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.CertificateAuthority) for i in responses)


@pytest.mark.asyncio
async def test_list_certificate_authorities_async_pages():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_authorities),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[],
                next_page_token="def",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        # Workaround issue in python 3.9 related to code coverage by adding `# pragma: no branch`
        # See https://github.com/googleapis/gapic-generator-python/pull/1174#issuecomment-1025132372
        async for page_ in (  # pragma: no branch
            await client.list_certificate_authorities(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.UndeleteCertificateAuthorityRequest,
        dict,
    ],
)
def test_undelete_certificate_authority(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.undelete_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.undelete_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UndeleteCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_undelete_certificate_authority_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.undelete_certificate_authority), "__call__"
    ) as call:
        client.undelete_certificate_authority()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UndeleteCertificateAuthorityRequest()


@pytest.mark.asyncio
async def test_undelete_certificate_authority_async(
    transport: str = "grpc_asyncio",
    request_type=service.UndeleteCertificateAuthorityRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.undelete_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.undelete_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UndeleteCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_undelete_certificate_authority_async_from_dict():
    await test_undelete_certificate_authority_async(request_type=dict)


def test_undelete_certificate_authority_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UndeleteCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.undelete_certificate_authority), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.undelete_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_undelete_certificate_authority_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UndeleteCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.undelete_certificate_authority), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.undelete_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_undelete_certificate_authority_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.undelete_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.undelete_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_undelete_certificate_authority_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.undelete_certificate_authority(
            service.UndeleteCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_undelete_certificate_authority_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.undelete_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.undelete_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_undelete_certificate_authority_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.undelete_certificate_authority(
            service.UndeleteCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.DeleteCertificateAuthorityRequest,
        dict,
    ],
)
def test_delete_certificate_authority(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.delete_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_certificate_authority_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_authority), "__call__"
    ) as call:
        client.delete_certificate_authority()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCertificateAuthorityRequest()


@pytest.mark.asyncio
async def test_delete_certificate_authority_async(
    transport: str = "grpc_asyncio",
    request_type=service.DeleteCertificateAuthorityRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.delete_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_delete_certificate_authority_async_from_dict():
    await test_delete_certificate_authority_async(request_type=dict)


def test_delete_certificate_authority_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_authority), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_certificate_authority_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteCertificateAuthorityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_authority), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.delete_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_delete_certificate_authority_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_certificate_authority_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_certificate_authority(
            service.DeleteCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_certificate_authority_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_certificate_authority(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_certificate_authority_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_certificate_authority(
            service.DeleteCertificateAuthorityRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCertificateAuthorityRequest,
        dict,
    ],
)
def test_update_certificate_authority(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_certificate_authority_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_authority), "__call__"
    ) as call:
        client.update_certificate_authority()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateAuthorityRequest()


@pytest.mark.asyncio
async def test_update_certificate_authority_async(
    transport: str = "grpc_asyncio",
    request_type=service.UpdateCertificateAuthorityRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateAuthorityRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_update_certificate_authority_async_from_dict():
    await test_update_certificate_authority_async(request_type=dict)


def test_update_certificate_authority_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCertificateAuthorityRequest()

    request.certificate_authority.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_authority), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "certificate_authority.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_certificate_authority_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCertificateAuthorityRequest()

    request.certificate_authority.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_authority), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_certificate_authority(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "certificate_authority.name=name_value",
    ) in kw["metadata"]


def test_update_certificate_authority_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_certificate_authority(
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].certificate_authority
        mock_val = resources.CertificateAuthority(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_certificate_authority_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_certificate_authority(
            service.UpdateCertificateAuthorityRequest(),
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_certificate_authority_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_authority), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_certificate_authority(
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].certificate_authority
        mock_val = resources.CertificateAuthority(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_certificate_authority_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_certificate_authority(
            service.UpdateCertificateAuthorityRequest(),
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.CreateCaPoolRequest,
        dict,
    ],
)
def test_create_ca_pool(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCaPoolRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_ca_pool_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ca_pool), "__call__") as call:
        client.create_ca_pool()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCaPoolRequest()


@pytest.mark.asyncio
async def test_create_ca_pool_async(
    transport: str = "grpc_asyncio", request_type=service.CreateCaPoolRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCaPoolRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_create_ca_pool_async_from_dict():
    await test_create_ca_pool_async(request_type=dict)


def test_create_ca_pool_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateCaPoolRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ca_pool), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_ca_pool_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateCaPoolRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ca_pool), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_create_ca_pool_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_ca_pool(
            parent="parent_value",
            ca_pool=resources.CaPool(name="name_value"),
            ca_pool_id="ca_pool_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].ca_pool
        mock_val = resources.CaPool(name="name_value")
        assert arg == mock_val
        arg = args[0].ca_pool_id
        mock_val = "ca_pool_id_value"
        assert arg == mock_val


def test_create_ca_pool_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_ca_pool(
            service.CreateCaPoolRequest(),
            parent="parent_value",
            ca_pool=resources.CaPool(name="name_value"),
            ca_pool_id="ca_pool_id_value",
        )


@pytest.mark.asyncio
async def test_create_ca_pool_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_ca_pool(
            parent="parent_value",
            ca_pool=resources.CaPool(name="name_value"),
            ca_pool_id="ca_pool_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].ca_pool
        mock_val = resources.CaPool(name="name_value")
        assert arg == mock_val
        arg = args[0].ca_pool_id
        mock_val = "ca_pool_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_ca_pool_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_ca_pool(
            service.CreateCaPoolRequest(),
            parent="parent_value",
            ca_pool=resources.CaPool(name="name_value"),
            ca_pool_id="ca_pool_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCaPoolRequest,
        dict,
    ],
)
def test_update_ca_pool(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCaPoolRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_ca_pool_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_ca_pool), "__call__") as call:
        client.update_ca_pool()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCaPoolRequest()


@pytest.mark.asyncio
async def test_update_ca_pool_async(
    transport: str = "grpc_asyncio", request_type=service.UpdateCaPoolRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCaPoolRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_update_ca_pool_async_from_dict():
    await test_update_ca_pool_async(request_type=dict)


def test_update_ca_pool_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCaPoolRequest()

    request.ca_pool.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_ca_pool), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "ca_pool.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_ca_pool_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCaPoolRequest()

    request.ca_pool.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_ca_pool), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "ca_pool.name=name_value",
    ) in kw["metadata"]


def test_update_ca_pool_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_ca_pool(
            ca_pool=resources.CaPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].ca_pool
        mock_val = resources.CaPool(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_ca_pool_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_ca_pool(
            service.UpdateCaPoolRequest(),
            ca_pool=resources.CaPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_ca_pool_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_ca_pool(
            ca_pool=resources.CaPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].ca_pool
        mock_val = resources.CaPool(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_ca_pool_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_ca_pool(
            service.UpdateCaPoolRequest(),
            ca_pool=resources.CaPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCaPoolRequest,
        dict,
    ],
)
def test_get_ca_pool(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CaPool(
            name="name_value",
            tier=resources.CaPool.Tier.ENTERPRISE,
        )
        response = client.get_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCaPoolRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CaPool)
    assert response.name == "name_value"
    assert response.tier == resources.CaPool.Tier.ENTERPRISE


def test_get_ca_pool_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_ca_pool), "__call__") as call:
        client.get_ca_pool()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCaPoolRequest()


@pytest.mark.asyncio
async def test_get_ca_pool_async(
    transport: str = "grpc_asyncio", request_type=service.GetCaPoolRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CaPool(
                name="name_value",
                tier=resources.CaPool.Tier.ENTERPRISE,
            )
        )
        response = await client.get_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCaPoolRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CaPool)
    assert response.name == "name_value"
    assert response.tier == resources.CaPool.Tier.ENTERPRISE


@pytest.mark.asyncio
async def test_get_ca_pool_async_from_dict():
    await test_get_ca_pool_async(request_type=dict)


def test_get_ca_pool_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCaPoolRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_ca_pool), "__call__") as call:
        call.return_value = resources.CaPool()
        client.get_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_ca_pool_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCaPoolRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_ca_pool), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.CaPool())
        await client.get_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_ca_pool_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CaPool()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_ca_pool(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_ca_pool_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_ca_pool(
            service.GetCaPoolRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_ca_pool_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CaPool()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.CaPool())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_ca_pool(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_ca_pool_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_ca_pool(
            service.GetCaPoolRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCaPoolsRequest,
        dict,
    ],
)
def test_list_ca_pools(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCaPoolsResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )
        response = client.list_ca_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCaPoolsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCaPoolsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_ca_pools_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        client.list_ca_pools()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCaPoolsRequest()


@pytest.mark.asyncio
async def test_list_ca_pools_async(
    transport: str = "grpc_asyncio", request_type=service.ListCaPoolsRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCaPoolsResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        response = await client.list_ca_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCaPoolsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCaPoolsAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.asyncio
async def test_list_ca_pools_async_from_dict():
    await test_list_ca_pools_async(request_type=dict)


def test_list_ca_pools_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCaPoolsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        call.return_value = service.ListCaPoolsResponse()
        client.list_ca_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_ca_pools_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCaPoolsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCaPoolsResponse()
        )
        await client.list_ca_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_ca_pools_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCaPoolsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_ca_pools(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_ca_pools_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_ca_pools(
            service.ListCaPoolsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_ca_pools_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCaPoolsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCaPoolsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_ca_pools(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_ca_pools_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_ca_pools(
            service.ListCaPoolsRequest(),
            parent="parent_value",
        )


def test_list_ca_pools_pager(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                    resources.CaPool(),
                ],
                next_page_token="abc",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[],
                next_page_token="def",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                ],
                next_page_token="ghi",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_ca_pools(request={})

        assert pager._metadata == metadata

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.CaPool) for i in results)


def test_list_ca_pools_pages(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_ca_pools), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                    resources.CaPool(),
                ],
                next_page_token="abc",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[],
                next_page_token="def",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                ],
                next_page_token="ghi",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_ca_pools(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_ca_pools_async_pager():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_ca_pools), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                    resources.CaPool(),
                ],
                next_page_token="abc",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[],
                next_page_token="def",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                ],
                next_page_token="ghi",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_ca_pools(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.CaPool) for i in responses)


@pytest.mark.asyncio
async def test_list_ca_pools_async_pages():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_ca_pools), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                    resources.CaPool(),
                ],
                next_page_token="abc",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[],
                next_page_token="def",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                ],
                next_page_token="ghi",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        # Workaround issue in python 3.9 related to code coverage by adding `# pragma: no branch`
        # See https://github.com/googleapis/gapic-generator-python/pull/1174#issuecomment-1025132372
        async for page_ in (  # pragma: no branch
            await client.list_ca_pools(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.DeleteCaPoolRequest,
        dict,
    ],
)
def test_delete_ca_pool(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.delete_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCaPoolRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_ca_pool_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_ca_pool), "__call__") as call:
        client.delete_ca_pool()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCaPoolRequest()


@pytest.mark.asyncio
async def test_delete_ca_pool_async(
    transport: str = "grpc_asyncio", request_type=service.DeleteCaPoolRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.delete_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCaPoolRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_delete_ca_pool_async_from_dict():
    await test_delete_ca_pool_async(request_type=dict)


def test_delete_ca_pool_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteCaPoolRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_ca_pool), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_ca_pool_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteCaPoolRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_ca_pool), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.delete_ca_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_delete_ca_pool_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_ca_pool(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_ca_pool_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_ca_pool(
            service.DeleteCaPoolRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_ca_pool_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_ca_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_ca_pool(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_ca_pool_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_ca_pool(
            service.DeleteCaPoolRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.FetchCaCertsRequest,
        dict,
    ],
)
def test_fetch_ca_certs(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_ca_certs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.FetchCaCertsResponse()
        response = client.fetch_ca_certs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.FetchCaCertsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.FetchCaCertsResponse)


def test_fetch_ca_certs_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_ca_certs), "__call__") as call:
        client.fetch_ca_certs()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.FetchCaCertsRequest()


@pytest.mark.asyncio
async def test_fetch_ca_certs_async(
    transport: str = "grpc_asyncio", request_type=service.FetchCaCertsRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_ca_certs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.FetchCaCertsResponse()
        )
        response = await client.fetch_ca_certs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.FetchCaCertsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.FetchCaCertsResponse)


@pytest.mark.asyncio
async def test_fetch_ca_certs_async_from_dict():
    await test_fetch_ca_certs_async(request_type=dict)


def test_fetch_ca_certs_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.FetchCaCertsRequest()

    request.ca_pool = "ca_pool_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_ca_certs), "__call__") as call:
        call.return_value = service.FetchCaCertsResponse()
        client.fetch_ca_certs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "ca_pool=ca_pool_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_fetch_ca_certs_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.FetchCaCertsRequest()

    request.ca_pool = "ca_pool_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_ca_certs), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.FetchCaCertsResponse()
        )
        await client.fetch_ca_certs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "ca_pool=ca_pool_value",
    ) in kw["metadata"]


def test_fetch_ca_certs_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_ca_certs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.FetchCaCertsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.fetch_ca_certs(
            ca_pool="ca_pool_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].ca_pool
        mock_val = "ca_pool_value"
        assert arg == mock_val


def test_fetch_ca_certs_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.fetch_ca_certs(
            service.FetchCaCertsRequest(),
            ca_pool="ca_pool_value",
        )


@pytest.mark.asyncio
async def test_fetch_ca_certs_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_ca_certs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.FetchCaCertsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.FetchCaCertsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.fetch_ca_certs(
            ca_pool="ca_pool_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].ca_pool
        mock_val = "ca_pool_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_fetch_ca_certs_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.fetch_ca_certs(
            service.FetchCaCertsRequest(),
            ca_pool="ca_pool_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCertificateRevocationListRequest,
        dict,
    ],
)
def test_get_certificate_revocation_list(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_revocation_list), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateRevocationList(
            name="name_value",
            sequence_number=1601,
            pem_crl="pem_crl_value",
            access_url="access_url_value",
            state=resources.CertificateRevocationList.State.ACTIVE,
            revision_id="revision_id_value",
        )
        response = client.get_certificate_revocation_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateRevocationListRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateRevocationList)
    assert response.name == "name_value"
    assert response.sequence_number == 1601
    assert response.pem_crl == "pem_crl_value"
    assert response.access_url == "access_url_value"
    assert response.state == resources.CertificateRevocationList.State.ACTIVE
    assert response.revision_id == "revision_id_value"


def test_get_certificate_revocation_list_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_revocation_list), "__call__"
    ) as call:
        client.get_certificate_revocation_list()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateRevocationListRequest()


@pytest.mark.asyncio
async def test_get_certificate_revocation_list_async(
    transport: str = "grpc_asyncio",
    request_type=service.GetCertificateRevocationListRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_revocation_list), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateRevocationList(
                name="name_value",
                sequence_number=1601,
                pem_crl="pem_crl_value",
                access_url="access_url_value",
                state=resources.CertificateRevocationList.State.ACTIVE,
                revision_id="revision_id_value",
            )
        )
        response = await client.get_certificate_revocation_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateRevocationListRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateRevocationList)
    assert response.name == "name_value"
    assert response.sequence_number == 1601
    assert response.pem_crl == "pem_crl_value"
    assert response.access_url == "access_url_value"
    assert response.state == resources.CertificateRevocationList.State.ACTIVE
    assert response.revision_id == "revision_id_value"


@pytest.mark.asyncio
async def test_get_certificate_revocation_list_async_from_dict():
    await test_get_certificate_revocation_list_async(request_type=dict)


def test_get_certificate_revocation_list_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCertificateRevocationListRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_revocation_list), "__call__"
    ) as call:
        call.return_value = resources.CertificateRevocationList()
        client.get_certificate_revocation_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_certificate_revocation_list_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCertificateRevocationListRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_revocation_list), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateRevocationList()
        )
        await client.get_certificate_revocation_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_certificate_revocation_list_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_revocation_list), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateRevocationList()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_certificate_revocation_list(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_certificate_revocation_list_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_certificate_revocation_list(
            service.GetCertificateRevocationListRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_certificate_revocation_list_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_revocation_list), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateRevocationList()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateRevocationList()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_certificate_revocation_list(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_certificate_revocation_list_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_certificate_revocation_list(
            service.GetCertificateRevocationListRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCertificateRevocationListsRequest,
        dict,
    ],
)
def test_list_certificate_revocation_lists(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateRevocationListsResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )
        response = client.list_certificate_revocation_lists(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateRevocationListsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateRevocationListsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_certificate_revocation_lists_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        client.list_certificate_revocation_lists()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateRevocationListsRequest()


@pytest.mark.asyncio
async def test_list_certificate_revocation_lists_async(
    transport: str = "grpc_asyncio",
    request_type=service.ListCertificateRevocationListsRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateRevocationListsResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        response = await client.list_certificate_revocation_lists(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateRevocationListsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateRevocationListsAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.asyncio
async def test_list_certificate_revocation_lists_async_from_dict():
    await test_list_certificate_revocation_lists_async(request_type=dict)


def test_list_certificate_revocation_lists_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCertificateRevocationListsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        call.return_value = service.ListCertificateRevocationListsResponse()
        client.list_certificate_revocation_lists(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_certificate_revocation_lists_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCertificateRevocationListsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateRevocationListsResponse()
        )
        await client.list_certificate_revocation_lists(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_certificate_revocation_lists_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateRevocationListsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_certificate_revocation_lists(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_certificate_revocation_lists_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_certificate_revocation_lists(
            service.ListCertificateRevocationListsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_certificate_revocation_lists_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateRevocationListsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateRevocationListsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_certificate_revocation_lists(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_certificate_revocation_lists_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_certificate_revocation_lists(
            service.ListCertificateRevocationListsRequest(),
            parent="parent_value",
        )


def test_list_certificate_revocation_lists_pager(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[],
                next_page_token="def",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_certificate_revocation_lists(request={})

        assert pager._metadata == metadata

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.CertificateRevocationList) for i in results)


def test_list_certificate_revocation_lists_pages(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[],
                next_page_token="def",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_certificate_revocation_lists(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_certificate_revocation_lists_async_pager():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[],
                next_page_token="def",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_certificate_revocation_lists(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, resources.CertificateRevocationList) for i in responses
        )


@pytest.mark.asyncio
async def test_list_certificate_revocation_lists_async_pages():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_revocation_lists),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[],
                next_page_token="def",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        # Workaround issue in python 3.9 related to code coverage by adding `# pragma: no branch`
        # See https://github.com/googleapis/gapic-generator-python/pull/1174#issuecomment-1025132372
        async for page_ in (  # pragma: no branch
            await client.list_certificate_revocation_lists(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCertificateRevocationListRequest,
        dict,
    ],
)
def test_update_certificate_revocation_list(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_revocation_list), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_certificate_revocation_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateRevocationListRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_certificate_revocation_list_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_revocation_list), "__call__"
    ) as call:
        client.update_certificate_revocation_list()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateRevocationListRequest()


@pytest.mark.asyncio
async def test_update_certificate_revocation_list_async(
    transport: str = "grpc_asyncio",
    request_type=service.UpdateCertificateRevocationListRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_revocation_list), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_certificate_revocation_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateRevocationListRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_update_certificate_revocation_list_async_from_dict():
    await test_update_certificate_revocation_list_async(request_type=dict)


def test_update_certificate_revocation_list_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCertificateRevocationListRequest()

    request.certificate_revocation_list.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_revocation_list), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_certificate_revocation_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "certificate_revocation_list.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_certificate_revocation_list_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCertificateRevocationListRequest()

    request.certificate_revocation_list.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_revocation_list), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_certificate_revocation_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "certificate_revocation_list.name=name_value",
    ) in kw["metadata"]


def test_update_certificate_revocation_list_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_revocation_list), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_certificate_revocation_list(
            certificate_revocation_list=resources.CertificateRevocationList(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].certificate_revocation_list
        mock_val = resources.CertificateRevocationList(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_certificate_revocation_list_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_certificate_revocation_list(
            service.UpdateCertificateRevocationListRequest(),
            certificate_revocation_list=resources.CertificateRevocationList(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_certificate_revocation_list_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_revocation_list), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_certificate_revocation_list(
            certificate_revocation_list=resources.CertificateRevocationList(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].certificate_revocation_list
        mock_val = resources.CertificateRevocationList(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_certificate_revocation_list_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_certificate_revocation_list(
            service.UpdateCertificateRevocationListRequest(),
            certificate_revocation_list=resources.CertificateRevocationList(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.CreateCertificateTemplateRequest,
        dict,
    ],
)
def test_create_certificate_template(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateTemplateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_certificate_template_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_template), "__call__"
    ) as call:
        client.create_certificate_template()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateTemplateRequest()


@pytest.mark.asyncio
async def test_create_certificate_template_async(
    transport: str = "grpc_asyncio",
    request_type=service.CreateCertificateTemplateRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.CreateCertificateTemplateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_create_certificate_template_async_from_dict():
    await test_create_certificate_template_async(request_type=dict)


def test_create_certificate_template_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateCertificateTemplateRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_template), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_certificate_template_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateCertificateTemplateRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_template), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_create_certificate_template_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_certificate_template(
            parent="parent_value",
            certificate_template=resources.CertificateTemplate(name="name_value"),
            certificate_template_id="certificate_template_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].certificate_template
        mock_val = resources.CertificateTemplate(name="name_value")
        assert arg == mock_val
        arg = args[0].certificate_template_id
        mock_val = "certificate_template_id_value"
        assert arg == mock_val


def test_create_certificate_template_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_certificate_template(
            service.CreateCertificateTemplateRequest(),
            parent="parent_value",
            certificate_template=resources.CertificateTemplate(name="name_value"),
            certificate_template_id="certificate_template_id_value",
        )


@pytest.mark.asyncio
async def test_create_certificate_template_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_certificate_template(
            parent="parent_value",
            certificate_template=resources.CertificateTemplate(name="name_value"),
            certificate_template_id="certificate_template_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].certificate_template
        mock_val = resources.CertificateTemplate(name="name_value")
        assert arg == mock_val
        arg = args[0].certificate_template_id
        mock_val = "certificate_template_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_certificate_template_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_certificate_template(
            service.CreateCertificateTemplateRequest(),
            parent="parent_value",
            certificate_template=resources.CertificateTemplate(name="name_value"),
            certificate_template_id="certificate_template_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.DeleteCertificateTemplateRequest,
        dict,
    ],
)
def test_delete_certificate_template(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.delete_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCertificateTemplateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_certificate_template_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_template), "__call__"
    ) as call:
        client.delete_certificate_template()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCertificateTemplateRequest()


@pytest.mark.asyncio
async def test_delete_certificate_template_async(
    transport: str = "grpc_asyncio",
    request_type=service.DeleteCertificateTemplateRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.delete_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.DeleteCertificateTemplateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_delete_certificate_template_async_from_dict():
    await test_delete_certificate_template_async(request_type=dict)


def test_delete_certificate_template_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteCertificateTemplateRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_template), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_certificate_template_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteCertificateTemplateRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_template), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.delete_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_delete_certificate_template_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_certificate_template(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_certificate_template_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_certificate_template(
            service.DeleteCertificateTemplateRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_certificate_template_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_certificate_template(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_certificate_template_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_certificate_template(
            service.DeleteCertificateTemplateRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCertificateTemplateRequest,
        dict,
    ],
)
def test_get_certificate_template(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateTemplate(
            name="name_value",
            description="description_value",
        )
        response = client.get_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateTemplateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateTemplate)
    assert response.name == "name_value"
    assert response.description == "description_value"


def test_get_certificate_template_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_template), "__call__"
    ) as call:
        client.get_certificate_template()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateTemplateRequest()


@pytest.mark.asyncio
async def test_get_certificate_template_async(
    transport: str = "grpc_asyncio", request_type=service.GetCertificateTemplateRequest
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateTemplate(
                name="name_value",
                description="description_value",
            )
        )
        response = await client.get_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.GetCertificateTemplateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateTemplate)
    assert response.name == "name_value"
    assert response.description == "description_value"


@pytest.mark.asyncio
async def test_get_certificate_template_async_from_dict():
    await test_get_certificate_template_async(request_type=dict)


def test_get_certificate_template_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCertificateTemplateRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_template), "__call__"
    ) as call:
        call.return_value = resources.CertificateTemplate()
        client.get_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_certificate_template_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetCertificateTemplateRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_template), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateTemplate()
        )
        await client.get_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_certificate_template_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateTemplate()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_certificate_template(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_certificate_template_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_certificate_template(
            service.GetCertificateTemplateRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_certificate_template_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.CertificateTemplate()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.CertificateTemplate()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_certificate_template(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_certificate_template_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_certificate_template(
            service.GetCertificateTemplateRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCertificateTemplatesRequest,
        dict,
    ],
)
def test_list_certificate_templates(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateTemplatesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )
        response = client.list_certificate_templates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateTemplatesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateTemplatesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_certificate_templates_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        client.list_certificate_templates()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateTemplatesRequest()


@pytest.mark.asyncio
async def test_list_certificate_templates_async(
    transport: str = "grpc_asyncio",
    request_type=service.ListCertificateTemplatesRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateTemplatesResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        response = await client.list_certificate_templates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.ListCertificateTemplatesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateTemplatesAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.asyncio
async def test_list_certificate_templates_async_from_dict():
    await test_list_certificate_templates_async(request_type=dict)


def test_list_certificate_templates_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCertificateTemplatesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        call.return_value = service.ListCertificateTemplatesResponse()
        client.list_certificate_templates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_certificate_templates_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListCertificateTemplatesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateTemplatesResponse()
        )
        await client.list_certificate_templates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_certificate_templates_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateTemplatesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_certificate_templates(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_certificate_templates_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_certificate_templates(
            service.ListCertificateTemplatesRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_certificate_templates_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListCertificateTemplatesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListCertificateTemplatesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_certificate_templates(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_certificate_templates_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_certificate_templates(
            service.ListCertificateTemplatesRequest(),
            parent="parent_value",
        )


def test_list_certificate_templates_pager(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[],
                next_page_token="def",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_certificate_templates(request={})

        assert pager._metadata == metadata

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.CertificateTemplate) for i in results)


def test_list_certificate_templates_pages(transport_name: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[],
                next_page_token="def",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_certificate_templates(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_certificate_templates_async_pager():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[],
                next_page_token="def",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_certificate_templates(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.CertificateTemplate) for i in responses)


@pytest.mark.asyncio
async def test_list_certificate_templates_async_pages():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_certificate_templates),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[],
                next_page_token="def",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        # Workaround issue in python 3.9 related to code coverage by adding `# pragma: no branch`
        # See https://github.com/googleapis/gapic-generator-python/pull/1174#issuecomment-1025132372
        async for page_ in (  # pragma: no branch
            await client.list_certificate_templates(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCertificateTemplateRequest,
        dict,
    ],
)
def test_update_certificate_template(request_type, transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateTemplateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_certificate_template_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_template), "__call__"
    ) as call:
        client.update_certificate_template()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateTemplateRequest()


@pytest.mark.asyncio
async def test_update_certificate_template_async(
    transport: str = "grpc_asyncio",
    request_type=service.UpdateCertificateTemplateRequest,
):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service.UpdateCertificateTemplateRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_update_certificate_template_async_from_dict():
    await test_update_certificate_template_async(request_type=dict)


def test_update_certificate_template_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCertificateTemplateRequest()

    request.certificate_template.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_template), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "certificate_template.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_certificate_template_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateCertificateTemplateRequest()

    request.certificate_template.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_template), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_certificate_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "certificate_template.name=name_value",
    ) in kw["metadata"]


def test_update_certificate_template_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_certificate_template(
            certificate_template=resources.CertificateTemplate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].certificate_template
        mock_val = resources.CertificateTemplate(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_certificate_template_flattened_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_certificate_template(
            service.UpdateCertificateTemplateRequest(),
            certificate_template=resources.CertificateTemplate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_certificate_template_flattened_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_certificate_template), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_certificate_template(
            certificate_template=resources.CertificateTemplate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].certificate_template
        mock_val = resources.CertificateTemplate(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_certificate_template_flattened_error_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_certificate_template(
            service.UpdateCertificateTemplateRequest(),
            certificate_template=resources.CertificateTemplate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        service.CreateCertificateRequest,
        dict,
    ],
)
def test_create_certificate_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/caPools/sample3"}
    request_init["certificate"] = {
        "name": "name_value",
        "pem_csr": "pem_csr_value",
        "config": {
            "subject_config": {
                "subject": {
                    "common_name": "common_name_value",
                    "country_code": "country_code_value",
                    "organization": "organization_value",
                    "organizational_unit": "organizational_unit_value",
                    "locality": "locality_value",
                    "province": "province_value",
                    "street_address": "street_address_value",
                    "postal_code": "postal_code_value",
                },
                "subject_alt_name": {
                    "dns_names": ["dns_names_value1", "dns_names_value2"],
                    "uris": ["uris_value1", "uris_value2"],
                    "email_addresses": [
                        "email_addresses_value1",
                        "email_addresses_value2",
                    ],
                    "ip_addresses": ["ip_addresses_value1", "ip_addresses_value2"],
                    "custom_sans": [
                        {
                            "object_id": {"object_id_path": [1456, 1457]},
                            "critical": True,
                            "value": b"value_blob",
                        }
                    ],
                },
            },
            "x509_config": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": {},
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": {},
            },
            "public_key": {"key": b"key_blob", "format_": 1},
        },
        "issuer_certificate_authority": "issuer_certificate_authority_value",
        "lifetime": {"seconds": 751, "nanos": 543},
        "certificate_template": "certificate_template_value",
        "subject_mode": 1,
        "revocation_details": {
            "revocation_state": 1,
            "revocation_time": {"seconds": 751, "nanos": 543},
        },
        "pem_certificate": "pem_certificate_value",
        "certificate_description": {
            "subject_description": {
                "subject": {},
                "subject_alt_name": {},
                "hex_serial_number": "hex_serial_number_value",
                "lifetime": {},
                "not_before_time": {},
                "not_after_time": {},
            },
            "x509_description": {},
            "public_key": {},
            "subject_key_id": {"key_id": "key_id_value"},
            "authority_key_id": {},
            "crl_distribution_points": [
                "crl_distribution_points_value1",
                "crl_distribution_points_value2",
            ],
            "aia_issuing_certificate_urls": [
                "aia_issuing_certificate_urls_value1",
                "aia_issuing_certificate_urls_value2",
            ],
            "cert_fingerprint": {"sha256_hash": "sha256_hash_value"},
        },
        "pem_certificate_chain": [
            "pem_certificate_chain_value1",
            "pem_certificate_chain_value2",
        ],
        "create_time": {},
        "update_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Certificate(
            name="name_value",
            issuer_certificate_authority="issuer_certificate_authority_value",
            certificate_template="certificate_template_value",
            subject_mode=resources.SubjectRequestMode.DEFAULT,
            pem_certificate="pem_certificate_value",
            pem_certificate_chain=["pem_certificate_chain_value"],
            pem_csr="pem_csr_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.Certificate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.create_certificate(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


def test_create_certificate_rest_required_fields(
    request_type=service.CreateCertificateRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).create_certificate._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).create_certificate._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "certificate_id",
            "issuing_certificate_authority_id",
            "request_id",
            "validate_only",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.Certificate()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = resources.Certificate.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.create_certificate(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_create_certificate_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.create_certificate._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "certificateId",
                "issuingCertificateAuthorityId",
                "requestId",
                "validateOnly",
            )
        )
        & set(
            (
                "parent",
                "certificate",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_certificate_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_create_certificate"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_create_certificate"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.CreateCertificateRequest.pb(
            service.CreateCertificateRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = resources.Certificate.to_json(
            resources.Certificate()
        )

        request = service.CreateCertificateRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.Certificate()

        client.create_certificate(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_create_certificate_rest_bad_request(
    transport: str = "rest", request_type=service.CreateCertificateRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/caPools/sample3"}
    request_init["certificate"] = {
        "name": "name_value",
        "pem_csr": "pem_csr_value",
        "config": {
            "subject_config": {
                "subject": {
                    "common_name": "common_name_value",
                    "country_code": "country_code_value",
                    "organization": "organization_value",
                    "organizational_unit": "organizational_unit_value",
                    "locality": "locality_value",
                    "province": "province_value",
                    "street_address": "street_address_value",
                    "postal_code": "postal_code_value",
                },
                "subject_alt_name": {
                    "dns_names": ["dns_names_value1", "dns_names_value2"],
                    "uris": ["uris_value1", "uris_value2"],
                    "email_addresses": [
                        "email_addresses_value1",
                        "email_addresses_value2",
                    ],
                    "ip_addresses": ["ip_addresses_value1", "ip_addresses_value2"],
                    "custom_sans": [
                        {
                            "object_id": {"object_id_path": [1456, 1457]},
                            "critical": True,
                            "value": b"value_blob",
                        }
                    ],
                },
            },
            "x509_config": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": {},
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": {},
            },
            "public_key": {"key": b"key_blob", "format_": 1},
        },
        "issuer_certificate_authority": "issuer_certificate_authority_value",
        "lifetime": {"seconds": 751, "nanos": 543},
        "certificate_template": "certificate_template_value",
        "subject_mode": 1,
        "revocation_details": {
            "revocation_state": 1,
            "revocation_time": {"seconds": 751, "nanos": 543},
        },
        "pem_certificate": "pem_certificate_value",
        "certificate_description": {
            "subject_description": {
                "subject": {},
                "subject_alt_name": {},
                "hex_serial_number": "hex_serial_number_value",
                "lifetime": {},
                "not_before_time": {},
                "not_after_time": {},
            },
            "x509_description": {},
            "public_key": {},
            "subject_key_id": {"key_id": "key_id_value"},
            "authority_key_id": {},
            "crl_distribution_points": [
                "crl_distribution_points_value1",
                "crl_distribution_points_value2",
            ],
            "aia_issuing_certificate_urls": [
                "aia_issuing_certificate_urls_value1",
                "aia_issuing_certificate_urls_value2",
            ],
            "cert_fingerprint": {"sha256_hash": "sha256_hash_value"},
        },
        "pem_certificate_chain": [
            "pem_certificate_chain_value1",
            "pem_certificate_chain_value2",
        ],
        "create_time": {},
        "update_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.create_certificate(request)


def test_create_certificate_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Certificate()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/caPools/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            certificate=resources.Certificate(name="name_value"),
            certificate_id="certificate_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.Certificate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.create_certificate(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/caPools/*}/certificates"
            % client.transport._host,
            args[1],
        )


def test_create_certificate_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_certificate(
            service.CreateCertificateRequest(),
            parent="parent_value",
            certificate=resources.Certificate(name="name_value"),
            certificate_id="certificate_id_value",
        )


def test_create_certificate_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCertificateRequest,
        dict,
    ],
)
def test_get_certificate_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Certificate(
            name="name_value",
            issuer_certificate_authority="issuer_certificate_authority_value",
            certificate_template="certificate_template_value",
            subject_mode=resources.SubjectRequestMode.DEFAULT,
            pem_certificate="pem_certificate_value",
            pem_certificate_chain=["pem_certificate_chain_value"],
            pem_csr="pem_csr_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.Certificate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.get_certificate(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


def test_get_certificate_rest_required_fields(
    request_type=service.GetCertificateRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_certificate._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_certificate._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.Certificate()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = resources.Certificate.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.get_certificate(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_get_certificate_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.get_certificate._get_unset_required_fields({})
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_certificate_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_get_certificate"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_get_certificate"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.GetCertificateRequest.pb(service.GetCertificateRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = resources.Certificate.to_json(
            resources.Certificate()
        )

        request = service.GetCertificateRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.Certificate()

        client.get_certificate(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_get_certificate_rest_bad_request(
    transport: str = "rest", request_type=service.GetCertificateRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_certificate(request)


def test_get_certificate_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Certificate()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.Certificate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.get_certificate(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificates/*}"
            % client.transport._host,
            args[1],
        )


def test_get_certificate_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_certificate(
            service.GetCertificateRequest(),
            name="name_value",
        )


def test_get_certificate_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCertificatesRequest,
        dict,
    ],
)
def test_list_certificates_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCertificatesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCertificatesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.list_certificates(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificatesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_certificates_rest_required_fields(
    request_type=service.ListCertificatesRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_certificates._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_certificates._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "order_by",
            "page_size",
            "page_token",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = service.ListCertificatesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = service.ListCertificatesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.list_certificates(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_list_certificates_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.list_certificates._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "filter",
                "orderBy",
                "pageSize",
                "pageToken",
            )
        )
        & set(("parent",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_certificates_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_list_certificates"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_list_certificates"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.ListCertificatesRequest.pb(
            service.ListCertificatesRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = service.ListCertificatesResponse.to_json(
            service.ListCertificatesResponse()
        )

        request = service.ListCertificatesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = service.ListCertificatesResponse()

        client.list_certificates(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_list_certificates_rest_bad_request(
    transport: str = "rest", request_type=service.ListCertificatesRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_certificates(request)


def test_list_certificates_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCertificatesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/caPools/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCertificatesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.list_certificates(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/caPools/*}/certificates"
            % client.transport._host,
            args[1],
        )


def test_list_certificates_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_certificates(
            service.ListCertificatesRequest(),
            parent="parent_value",
        )


def test_list_certificates_rest_pager(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                    resources.Certificate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificatesResponse(
                certificates=[],
                next_page_token="def",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificatesResponse(
                certificates=[
                    resources.Certificate(),
                    resources.Certificate(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(service.ListCertificatesResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/caPools/sample3"
        }

        pager = client.list_certificates(request=sample_request)

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.Certificate) for i in results)

        pages = list(client.list_certificates(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.RevokeCertificateRequest,
        dict,
    ],
)
def test_revoke_certificate_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Certificate(
            name="name_value",
            issuer_certificate_authority="issuer_certificate_authority_value",
            certificate_template="certificate_template_value",
            subject_mode=resources.SubjectRequestMode.DEFAULT,
            pem_certificate="pem_certificate_value",
            pem_certificate_chain=["pem_certificate_chain_value"],
            pem_csr="pem_csr_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.Certificate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.revoke_certificate(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


def test_revoke_certificate_rest_required_fields(
    request_type=service.RevokeCertificateRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).revoke_certificate._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).revoke_certificate._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.Certificate()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = resources.Certificate.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.revoke_certificate(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_revoke_certificate_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.revoke_certificate._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(())
        & set(
            (
                "name",
                "reason",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_revoke_certificate_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_revoke_certificate"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_revoke_certificate"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.RevokeCertificateRequest.pb(
            service.RevokeCertificateRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = resources.Certificate.to_json(
            resources.Certificate()
        )

        request = service.RevokeCertificateRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.Certificate()

        client.revoke_certificate(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_revoke_certificate_rest_bad_request(
    transport: str = "rest", request_type=service.RevokeCertificateRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.revoke_certificate(request)


def test_revoke_certificate_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Certificate()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.Certificate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.revoke_certificate(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificates/*}:revoke"
            % client.transport._host,
            args[1],
        )


def test_revoke_certificate_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.revoke_certificate(
            service.RevokeCertificateRequest(),
            name="name_value",
        )


def test_revoke_certificate_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCertificateRequest,
        dict,
    ],
)
def test_update_certificate_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "certificate": {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
        }
    }
    request_init["certificate"] = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4",
        "pem_csr": "pem_csr_value",
        "config": {
            "subject_config": {
                "subject": {
                    "common_name": "common_name_value",
                    "country_code": "country_code_value",
                    "organization": "organization_value",
                    "organizational_unit": "organizational_unit_value",
                    "locality": "locality_value",
                    "province": "province_value",
                    "street_address": "street_address_value",
                    "postal_code": "postal_code_value",
                },
                "subject_alt_name": {
                    "dns_names": ["dns_names_value1", "dns_names_value2"],
                    "uris": ["uris_value1", "uris_value2"],
                    "email_addresses": [
                        "email_addresses_value1",
                        "email_addresses_value2",
                    ],
                    "ip_addresses": ["ip_addresses_value1", "ip_addresses_value2"],
                    "custom_sans": [
                        {
                            "object_id": {"object_id_path": [1456, 1457]},
                            "critical": True,
                            "value": b"value_blob",
                        }
                    ],
                },
            },
            "x509_config": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": {},
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": {},
            },
            "public_key": {"key": b"key_blob", "format_": 1},
        },
        "issuer_certificate_authority": "issuer_certificate_authority_value",
        "lifetime": {"seconds": 751, "nanos": 543},
        "certificate_template": "certificate_template_value",
        "subject_mode": 1,
        "revocation_details": {
            "revocation_state": 1,
            "revocation_time": {"seconds": 751, "nanos": 543},
        },
        "pem_certificate": "pem_certificate_value",
        "certificate_description": {
            "subject_description": {
                "subject": {},
                "subject_alt_name": {},
                "hex_serial_number": "hex_serial_number_value",
                "lifetime": {},
                "not_before_time": {},
                "not_after_time": {},
            },
            "x509_description": {},
            "public_key": {},
            "subject_key_id": {"key_id": "key_id_value"},
            "authority_key_id": {},
            "crl_distribution_points": [
                "crl_distribution_points_value1",
                "crl_distribution_points_value2",
            ],
            "aia_issuing_certificate_urls": [
                "aia_issuing_certificate_urls_value1",
                "aia_issuing_certificate_urls_value2",
            ],
            "cert_fingerprint": {"sha256_hash": "sha256_hash_value"},
        },
        "pem_certificate_chain": [
            "pem_certificate_chain_value1",
            "pem_certificate_chain_value2",
        ],
        "create_time": {},
        "update_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Certificate(
            name="name_value",
            issuer_certificate_authority="issuer_certificate_authority_value",
            certificate_template="certificate_template_value",
            subject_mode=resources.SubjectRequestMode.DEFAULT,
            pem_certificate="pem_certificate_value",
            pem_certificate_chain=["pem_certificate_chain_value"],
            pem_csr="pem_csr_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.Certificate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.update_certificate(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Certificate)
    assert response.name == "name_value"
    assert response.issuer_certificate_authority == "issuer_certificate_authority_value"
    assert response.certificate_template == "certificate_template_value"
    assert response.subject_mode == resources.SubjectRequestMode.DEFAULT
    assert response.pem_certificate == "pem_certificate_value"
    assert response.pem_certificate_chain == ["pem_certificate_chain_value"]


def test_update_certificate_rest_required_fields(
    request_type=service.UpdateCertificateRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_certificate._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_certificate._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "request_id",
            "update_mask",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.Certificate()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = resources.Certificate.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.update_certificate(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_update_certificate_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.update_certificate._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "requestId",
                "updateMask",
            )
        )
        & set(
            (
                "certificate",
                "updateMask",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_certificate_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_update_certificate"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_update_certificate"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.UpdateCertificateRequest.pb(
            service.UpdateCertificateRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = resources.Certificate.to_json(
            resources.Certificate()
        )

        request = service.UpdateCertificateRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.Certificate()

        client.update_certificate(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_update_certificate_rest_bad_request(
    transport: str = "rest", request_type=service.UpdateCertificateRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "certificate": {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
        }
    }
    request_init["certificate"] = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4",
        "pem_csr": "pem_csr_value",
        "config": {
            "subject_config": {
                "subject": {
                    "common_name": "common_name_value",
                    "country_code": "country_code_value",
                    "organization": "organization_value",
                    "organizational_unit": "organizational_unit_value",
                    "locality": "locality_value",
                    "province": "province_value",
                    "street_address": "street_address_value",
                    "postal_code": "postal_code_value",
                },
                "subject_alt_name": {
                    "dns_names": ["dns_names_value1", "dns_names_value2"],
                    "uris": ["uris_value1", "uris_value2"],
                    "email_addresses": [
                        "email_addresses_value1",
                        "email_addresses_value2",
                    ],
                    "ip_addresses": ["ip_addresses_value1", "ip_addresses_value2"],
                    "custom_sans": [
                        {
                            "object_id": {"object_id_path": [1456, 1457]},
                            "critical": True,
                            "value": b"value_blob",
                        }
                    ],
                },
            },
            "x509_config": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": {},
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": {},
            },
            "public_key": {"key": b"key_blob", "format_": 1},
        },
        "issuer_certificate_authority": "issuer_certificate_authority_value",
        "lifetime": {"seconds": 751, "nanos": 543},
        "certificate_template": "certificate_template_value",
        "subject_mode": 1,
        "revocation_details": {
            "revocation_state": 1,
            "revocation_time": {"seconds": 751, "nanos": 543},
        },
        "pem_certificate": "pem_certificate_value",
        "certificate_description": {
            "subject_description": {
                "subject": {},
                "subject_alt_name": {},
                "hex_serial_number": "hex_serial_number_value",
                "lifetime": {},
                "not_before_time": {},
                "not_after_time": {},
            },
            "x509_description": {},
            "public_key": {},
            "subject_key_id": {"key_id": "key_id_value"},
            "authority_key_id": {},
            "crl_distribution_points": [
                "crl_distribution_points_value1",
                "crl_distribution_points_value2",
            ],
            "aia_issuing_certificate_urls": [
                "aia_issuing_certificate_urls_value1",
                "aia_issuing_certificate_urls_value2",
            ],
            "cert_fingerprint": {"sha256_hash": "sha256_hash_value"},
        },
        "pem_certificate_chain": [
            "pem_certificate_chain_value1",
            "pem_certificate_chain_value2",
        ],
        "create_time": {},
        "update_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.update_certificate(request)


def test_update_certificate_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Certificate()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "certificate": {
                "name": "projects/sample1/locations/sample2/caPools/sample3/certificates/sample4"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            certificate=resources.Certificate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.Certificate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.update_certificate(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{certificate.name=projects/*/locations/*/caPools/*/certificates/*}"
            % client.transport._host,
            args[1],
        )


def test_update_certificate_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_certificate(
            service.UpdateCertificateRequest(),
            certificate=resources.Certificate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_update_certificate_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ActivateCertificateAuthorityRequest,
        dict,
    ],
)
def test_activate_certificate_authority_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.activate_certificate_authority(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_activate_certificate_authority_rest_required_fields(
    request_type=service.ActivateCertificateAuthorityRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request_init["pem_ca_certificate"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).activate_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"
    jsonified_request["pemCaCertificate"] = "pem_ca_certificate_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).activate_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"
    assert "pemCaCertificate" in jsonified_request
    assert jsonified_request["pemCaCertificate"] == "pem_ca_certificate_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.activate_certificate_authority(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_activate_certificate_authority_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.activate_certificate_authority._get_unset_required_fields(
        {}
    )
    assert set(unset_fields) == (
        set(())
        & set(
            (
                "name",
                "pemCaCertificate",
                "subordinateConfig",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_activate_certificate_authority_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_activate_certificate_authority",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_activate_certificate_authority",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.ActivateCertificateAuthorityRequest.pb(
            service.ActivateCertificateAuthorityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.ActivateCertificateAuthorityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.activate_certificate_authority(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_activate_certificate_authority_rest_bad_request(
    transport: str = "rest", request_type=service.ActivateCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.activate_certificate_authority(request)


def test_activate_certificate_authority_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.activate_certificate_authority(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificateAuthorities/*}:activate"
            % client.transport._host,
            args[1],
        )


def test_activate_certificate_authority_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.activate_certificate_authority(
            service.ActivateCertificateAuthorityRequest(),
            name="name_value",
        )


def test_activate_certificate_authority_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.CreateCertificateAuthorityRequest,
        dict,
    ],
)
def test_create_certificate_authority_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/caPools/sample3"}
    request_init["certificate_authority"] = {
        "name": "name_value",
        "type_": 1,
        "config": {
            "subject_config": {
                "subject": {
                    "common_name": "common_name_value",
                    "country_code": "country_code_value",
                    "organization": "organization_value",
                    "organizational_unit": "organizational_unit_value",
                    "locality": "locality_value",
                    "province": "province_value",
                    "street_address": "street_address_value",
                    "postal_code": "postal_code_value",
                },
                "subject_alt_name": {
                    "dns_names": ["dns_names_value1", "dns_names_value2"],
                    "uris": ["uris_value1", "uris_value2"],
                    "email_addresses": [
                        "email_addresses_value1",
                        "email_addresses_value2",
                    ],
                    "ip_addresses": ["ip_addresses_value1", "ip_addresses_value2"],
                    "custom_sans": [
                        {
                            "object_id": {"object_id_path": [1456, 1457]},
                            "critical": True,
                            "value": b"value_blob",
                        }
                    ],
                },
            },
            "x509_config": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": {},
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": {},
            },
            "public_key": {"key": b"key_blob", "format_": 1},
        },
        "lifetime": {"seconds": 751, "nanos": 543},
        "key_spec": {
            "cloud_kms_key_version": "cloud_kms_key_version_value",
            "algorithm": 1,
        },
        "subordinate_config": {
            "certificate_authority": "certificate_authority_value",
            "pem_issuer_chain": {
                "pem_certificates": [
                    "pem_certificates_value1",
                    "pem_certificates_value2",
                ]
            },
        },
        "tier": 1,
        "state": 1,
        "pem_ca_certificates": [
            "pem_ca_certificates_value1",
            "pem_ca_certificates_value2",
        ],
        "ca_certificate_descriptions": [
            {
                "subject_description": {
                    "subject": {},
                    "subject_alt_name": {},
                    "hex_serial_number": "hex_serial_number_value",
                    "lifetime": {},
                    "not_before_time": {"seconds": 751, "nanos": 543},
                    "not_after_time": {},
                },
                "x509_description": {},
                "public_key": {},
                "subject_key_id": {"key_id": "key_id_value"},
                "authority_key_id": {},
                "crl_distribution_points": [
                    "crl_distribution_points_value1",
                    "crl_distribution_points_value2",
                ],
                "aia_issuing_certificate_urls": [
                    "aia_issuing_certificate_urls_value1",
                    "aia_issuing_certificate_urls_value2",
                ],
                "cert_fingerprint": {"sha256_hash": "sha256_hash_value"},
            }
        ],
        "gcs_bucket": "gcs_bucket_value",
        "access_urls": {
            "ca_certificate_access_url": "ca_certificate_access_url_value",
            "crl_access_urls": ["crl_access_urls_value1", "crl_access_urls_value2"],
        },
        "create_time": {},
        "update_time": {},
        "delete_time": {},
        "expire_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.create_certificate_authority(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_create_certificate_authority_rest_required_fields(
    request_type=service.CreateCertificateAuthorityRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["certificate_authority_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped
    assert "certificateAuthorityId" not in jsonified_request

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).create_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "certificateAuthorityId" in jsonified_request
    assert (
        jsonified_request["certificateAuthorityId"]
        == request_init["certificate_authority_id"]
    )

    jsonified_request["parent"] = "parent_value"
    jsonified_request["certificateAuthorityId"] = "certificate_authority_id_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).create_certificate_authority._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "certificate_authority_id",
            "request_id",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "certificateAuthorityId" in jsonified_request
    assert (
        jsonified_request["certificateAuthorityId"] == "certificate_authority_id_value"
    )

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.create_certificate_authority(request)

            expected_params = [
                (
                    "certificateAuthorityId",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_create_certificate_authority_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.create_certificate_authority._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "certificateAuthorityId",
                "requestId",
            )
        )
        & set(
            (
                "parent",
                "certificateAuthorityId",
                "certificateAuthority",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_certificate_authority_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_create_certificate_authority",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_create_certificate_authority",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.CreateCertificateAuthorityRequest.pb(
            service.CreateCertificateAuthorityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.CreateCertificateAuthorityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.create_certificate_authority(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_create_certificate_authority_rest_bad_request(
    transport: str = "rest", request_type=service.CreateCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/caPools/sample3"}
    request_init["certificate_authority"] = {
        "name": "name_value",
        "type_": 1,
        "config": {
            "subject_config": {
                "subject": {
                    "common_name": "common_name_value",
                    "country_code": "country_code_value",
                    "organization": "organization_value",
                    "organizational_unit": "organizational_unit_value",
                    "locality": "locality_value",
                    "province": "province_value",
                    "street_address": "street_address_value",
                    "postal_code": "postal_code_value",
                },
                "subject_alt_name": {
                    "dns_names": ["dns_names_value1", "dns_names_value2"],
                    "uris": ["uris_value1", "uris_value2"],
                    "email_addresses": [
                        "email_addresses_value1",
                        "email_addresses_value2",
                    ],
                    "ip_addresses": ["ip_addresses_value1", "ip_addresses_value2"],
                    "custom_sans": [
                        {
                            "object_id": {"object_id_path": [1456, 1457]},
                            "critical": True,
                            "value": b"value_blob",
                        }
                    ],
                },
            },
            "x509_config": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": {},
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": {},
            },
            "public_key": {"key": b"key_blob", "format_": 1},
        },
        "lifetime": {"seconds": 751, "nanos": 543},
        "key_spec": {
            "cloud_kms_key_version": "cloud_kms_key_version_value",
            "algorithm": 1,
        },
        "subordinate_config": {
            "certificate_authority": "certificate_authority_value",
            "pem_issuer_chain": {
                "pem_certificates": [
                    "pem_certificates_value1",
                    "pem_certificates_value2",
                ]
            },
        },
        "tier": 1,
        "state": 1,
        "pem_ca_certificates": [
            "pem_ca_certificates_value1",
            "pem_ca_certificates_value2",
        ],
        "ca_certificate_descriptions": [
            {
                "subject_description": {
                    "subject": {},
                    "subject_alt_name": {},
                    "hex_serial_number": "hex_serial_number_value",
                    "lifetime": {},
                    "not_before_time": {"seconds": 751, "nanos": 543},
                    "not_after_time": {},
                },
                "x509_description": {},
                "public_key": {},
                "subject_key_id": {"key_id": "key_id_value"},
                "authority_key_id": {},
                "crl_distribution_points": [
                    "crl_distribution_points_value1",
                    "crl_distribution_points_value2",
                ],
                "aia_issuing_certificate_urls": [
                    "aia_issuing_certificate_urls_value1",
                    "aia_issuing_certificate_urls_value2",
                ],
                "cert_fingerprint": {"sha256_hash": "sha256_hash_value"},
            }
        ],
        "gcs_bucket": "gcs_bucket_value",
        "access_urls": {
            "ca_certificate_access_url": "ca_certificate_access_url_value",
            "crl_access_urls": ["crl_access_urls_value1", "crl_access_urls_value2"],
        },
        "create_time": {},
        "update_time": {},
        "delete_time": {},
        "expire_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.create_certificate_authority(request)


def test_create_certificate_authority_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/caPools/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            certificate_authority_id="certificate_authority_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.create_certificate_authority(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/caPools/*}/certificateAuthorities"
            % client.transport._host,
            args[1],
        )


def test_create_certificate_authority_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_certificate_authority(
            service.CreateCertificateAuthorityRequest(),
            parent="parent_value",
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            certificate_authority_id="certificate_authority_id_value",
        )


def test_create_certificate_authority_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.DisableCertificateAuthorityRequest,
        dict,
    ],
)
def test_disable_certificate_authority_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.disable_certificate_authority(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_disable_certificate_authority_rest_required_fields(
    request_type=service.DisableCertificateAuthorityRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).disable_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).disable_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.disable_certificate_authority(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_disable_certificate_authority_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.disable_certificate_authority._get_unset_required_fields(
        {}
    )
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_disable_certificate_authority_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_disable_certificate_authority",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_disable_certificate_authority",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.DisableCertificateAuthorityRequest.pb(
            service.DisableCertificateAuthorityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.DisableCertificateAuthorityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.disable_certificate_authority(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_disable_certificate_authority_rest_bad_request(
    transport: str = "rest", request_type=service.DisableCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.disable_certificate_authority(request)


def test_disable_certificate_authority_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.disable_certificate_authority(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificateAuthorities/*}:disable"
            % client.transport._host,
            args[1],
        )


def test_disable_certificate_authority_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.disable_certificate_authority(
            service.DisableCertificateAuthorityRequest(),
            name="name_value",
        )


def test_disable_certificate_authority_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.EnableCertificateAuthorityRequest,
        dict,
    ],
)
def test_enable_certificate_authority_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.enable_certificate_authority(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_enable_certificate_authority_rest_required_fields(
    request_type=service.EnableCertificateAuthorityRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).enable_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).enable_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.enable_certificate_authority(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_enable_certificate_authority_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.enable_certificate_authority._get_unset_required_fields({})
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_enable_certificate_authority_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_enable_certificate_authority",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_enable_certificate_authority",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.EnableCertificateAuthorityRequest.pb(
            service.EnableCertificateAuthorityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.EnableCertificateAuthorityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.enable_certificate_authority(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_enable_certificate_authority_rest_bad_request(
    transport: str = "rest", request_type=service.EnableCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.enable_certificate_authority(request)


def test_enable_certificate_authority_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.enable_certificate_authority(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificateAuthorities/*}:enable"
            % client.transport._host,
            args[1],
        )


def test_enable_certificate_authority_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.enable_certificate_authority(
            service.EnableCertificateAuthorityRequest(),
            name="name_value",
        )


def test_enable_certificate_authority_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.FetchCertificateAuthorityCsrRequest,
        dict,
    ],
)
def test_fetch_certificate_authority_csr_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.FetchCertificateAuthorityCsrResponse(
            pem_csr="pem_csr_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.FetchCertificateAuthorityCsrResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.fetch_certificate_authority_csr(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.FetchCertificateAuthorityCsrResponse)
    assert response.pem_csr == "pem_csr_value"


def test_fetch_certificate_authority_csr_rest_required_fields(
    request_type=service.FetchCertificateAuthorityCsrRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).fetch_certificate_authority_csr._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).fetch_certificate_authority_csr._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = service.FetchCertificateAuthorityCsrResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = service.FetchCertificateAuthorityCsrResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.fetch_certificate_authority_csr(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_fetch_certificate_authority_csr_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.fetch_certificate_authority_csr._get_unset_required_fields(
        {}
    )
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_certificate_authority_csr_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_fetch_certificate_authority_csr",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_fetch_certificate_authority_csr",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.FetchCertificateAuthorityCsrRequest.pb(
            service.FetchCertificateAuthorityCsrRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = (
            service.FetchCertificateAuthorityCsrResponse.to_json(
                service.FetchCertificateAuthorityCsrResponse()
            )
        )

        request = service.FetchCertificateAuthorityCsrRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = service.FetchCertificateAuthorityCsrResponse()

        client.fetch_certificate_authority_csr(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_fetch_certificate_authority_csr_rest_bad_request(
    transport: str = "rest", request_type=service.FetchCertificateAuthorityCsrRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.fetch_certificate_authority_csr(request)


def test_fetch_certificate_authority_csr_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.FetchCertificateAuthorityCsrResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.FetchCertificateAuthorityCsrResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.fetch_certificate_authority_csr(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificateAuthorities/*}:fetch"
            % client.transport._host,
            args[1],
        )


def test_fetch_certificate_authority_csr_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.fetch_certificate_authority_csr(
            service.FetchCertificateAuthorityCsrRequest(),
            name="name_value",
        )


def test_fetch_certificate_authority_csr_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCertificateAuthorityRequest,
        dict,
    ],
)
def test_get_certificate_authority_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.CertificateAuthority(
            name="name_value",
            type_=resources.CertificateAuthority.Type.SELF_SIGNED,
            tier=resources.CaPool.Tier.ENTERPRISE,
            state=resources.CertificateAuthority.State.ENABLED,
            pem_ca_certificates=["pem_ca_certificates_value"],
            gcs_bucket="gcs_bucket_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.CertificateAuthority.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.get_certificate_authority(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateAuthority)
    assert response.name == "name_value"
    assert response.type_ == resources.CertificateAuthority.Type.SELF_SIGNED
    assert response.tier == resources.CaPool.Tier.ENTERPRISE
    assert response.state == resources.CertificateAuthority.State.ENABLED
    assert response.pem_ca_certificates == ["pem_ca_certificates_value"]
    assert response.gcs_bucket == "gcs_bucket_value"


def test_get_certificate_authority_rest_required_fields(
    request_type=service.GetCertificateAuthorityRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.CertificateAuthority()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = resources.CertificateAuthority.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.get_certificate_authority(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_get_certificate_authority_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.get_certificate_authority._get_unset_required_fields({})
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_certificate_authority_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_get_certificate_authority",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_get_certificate_authority",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.GetCertificateAuthorityRequest.pb(
            service.GetCertificateAuthorityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = resources.CertificateAuthority.to_json(
            resources.CertificateAuthority()
        )

        request = service.GetCertificateAuthorityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.CertificateAuthority()

        client.get_certificate_authority(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_get_certificate_authority_rest_bad_request(
    transport: str = "rest", request_type=service.GetCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_certificate_authority(request)


def test_get_certificate_authority_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.CertificateAuthority()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.CertificateAuthority.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.get_certificate_authority(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificateAuthorities/*}"
            % client.transport._host,
            args[1],
        )


def test_get_certificate_authority_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_certificate_authority(
            service.GetCertificateAuthorityRequest(),
            name="name_value",
        )


def test_get_certificate_authority_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCertificateAuthoritiesRequest,
        dict,
    ],
)
def test_list_certificate_authorities_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCertificateAuthoritiesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCertificateAuthoritiesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.list_certificate_authorities(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateAuthoritiesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_certificate_authorities_rest_required_fields(
    request_type=service.ListCertificateAuthoritiesRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_certificate_authorities._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_certificate_authorities._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "order_by",
            "page_size",
            "page_token",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = service.ListCertificateAuthoritiesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = service.ListCertificateAuthoritiesResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.list_certificate_authorities(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_list_certificate_authorities_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.list_certificate_authorities._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "filter",
                "orderBy",
                "pageSize",
                "pageToken",
            )
        )
        & set(("parent",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_certificate_authorities_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_list_certificate_authorities",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_list_certificate_authorities",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.ListCertificateAuthoritiesRequest.pb(
            service.ListCertificateAuthoritiesRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = service.ListCertificateAuthoritiesResponse.to_json(
            service.ListCertificateAuthoritiesResponse()
        )

        request = service.ListCertificateAuthoritiesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = service.ListCertificateAuthoritiesResponse()

        client.list_certificate_authorities(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_list_certificate_authorities_rest_bad_request(
    transport: str = "rest", request_type=service.ListCertificateAuthoritiesRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_certificate_authorities(request)


def test_list_certificate_authorities_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCertificateAuthoritiesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/caPools/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCertificateAuthoritiesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.list_certificate_authorities(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/caPools/*}/certificateAuthorities"
            % client.transport._host,
            args[1],
        )


def test_list_certificate_authorities_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_certificate_authorities(
            service.ListCertificateAuthoritiesRequest(),
            parent="parent_value",
        )


def test_list_certificate_authorities_rest_pager(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[],
                next_page_token="def",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateAuthoritiesResponse(
                certificate_authorities=[
                    resources.CertificateAuthority(),
                    resources.CertificateAuthority(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            service.ListCertificateAuthoritiesResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/caPools/sample3"
        }

        pager = client.list_certificate_authorities(request=sample_request)

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.CertificateAuthority) for i in results)

        pages = list(client.list_certificate_authorities(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.UndeleteCertificateAuthorityRequest,
        dict,
    ],
)
def test_undelete_certificate_authority_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.undelete_certificate_authority(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_undelete_certificate_authority_rest_required_fields(
    request_type=service.UndeleteCertificateAuthorityRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).undelete_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).undelete_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.undelete_certificate_authority(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_undelete_certificate_authority_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.undelete_certificate_authority._get_unset_required_fields(
        {}
    )
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_undelete_certificate_authority_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_undelete_certificate_authority",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_undelete_certificate_authority",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.UndeleteCertificateAuthorityRequest.pb(
            service.UndeleteCertificateAuthorityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.UndeleteCertificateAuthorityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.undelete_certificate_authority(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_undelete_certificate_authority_rest_bad_request(
    transport: str = "rest", request_type=service.UndeleteCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.undelete_certificate_authority(request)


def test_undelete_certificate_authority_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.undelete_certificate_authority(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificateAuthorities/*}:undelete"
            % client.transport._host,
            args[1],
        )


def test_undelete_certificate_authority_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.undelete_certificate_authority(
            service.UndeleteCertificateAuthorityRequest(),
            name="name_value",
        )


def test_undelete_certificate_authority_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.DeleteCertificateAuthorityRequest,
        dict,
    ],
)
def test_delete_certificate_authority_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.delete_certificate_authority(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_delete_certificate_authority_rest_required_fields(
    request_type=service.DeleteCertificateAuthorityRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).delete_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).delete_certificate_authority._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "ignore_active_certificates",
            "ignore_dependent_resources",
            "request_id",
            "skip_grace_period",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.delete_certificate_authority(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_delete_certificate_authority_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.delete_certificate_authority._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "ignoreActiveCertificates",
                "ignoreDependentResources",
                "requestId",
                "skipGracePeriod",
            )
        )
        & set(("name",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_certificate_authority_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_delete_certificate_authority",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_delete_certificate_authority",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.DeleteCertificateAuthorityRequest.pb(
            service.DeleteCertificateAuthorityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.DeleteCertificateAuthorityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.delete_certificate_authority(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_delete_certificate_authority_rest_bad_request(
    transport: str = "rest", request_type=service.DeleteCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.delete_certificate_authority(request)


def test_delete_certificate_authority_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.delete_certificate_authority(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificateAuthorities/*}"
            % client.transport._host,
            args[1],
        )


def test_delete_certificate_authority_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_certificate_authority(
            service.DeleteCertificateAuthorityRequest(),
            name="name_value",
        )


def test_delete_certificate_authority_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCertificateAuthorityRequest,
        dict,
    ],
)
def test_update_certificate_authority_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "certificate_authority": {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }
    }
    request_init["certificate_authority"] = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4",
        "type_": 1,
        "config": {
            "subject_config": {
                "subject": {
                    "common_name": "common_name_value",
                    "country_code": "country_code_value",
                    "organization": "organization_value",
                    "organizational_unit": "organizational_unit_value",
                    "locality": "locality_value",
                    "province": "province_value",
                    "street_address": "street_address_value",
                    "postal_code": "postal_code_value",
                },
                "subject_alt_name": {
                    "dns_names": ["dns_names_value1", "dns_names_value2"],
                    "uris": ["uris_value1", "uris_value2"],
                    "email_addresses": [
                        "email_addresses_value1",
                        "email_addresses_value2",
                    ],
                    "ip_addresses": ["ip_addresses_value1", "ip_addresses_value2"],
                    "custom_sans": [
                        {
                            "object_id": {"object_id_path": [1456, 1457]},
                            "critical": True,
                            "value": b"value_blob",
                        }
                    ],
                },
            },
            "x509_config": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": {},
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": {},
            },
            "public_key": {"key": b"key_blob", "format_": 1},
        },
        "lifetime": {"seconds": 751, "nanos": 543},
        "key_spec": {
            "cloud_kms_key_version": "cloud_kms_key_version_value",
            "algorithm": 1,
        },
        "subordinate_config": {
            "certificate_authority": "certificate_authority_value",
            "pem_issuer_chain": {
                "pem_certificates": [
                    "pem_certificates_value1",
                    "pem_certificates_value2",
                ]
            },
        },
        "tier": 1,
        "state": 1,
        "pem_ca_certificates": [
            "pem_ca_certificates_value1",
            "pem_ca_certificates_value2",
        ],
        "ca_certificate_descriptions": [
            {
                "subject_description": {
                    "subject": {},
                    "subject_alt_name": {},
                    "hex_serial_number": "hex_serial_number_value",
                    "lifetime": {},
                    "not_before_time": {"seconds": 751, "nanos": 543},
                    "not_after_time": {},
                },
                "x509_description": {},
                "public_key": {},
                "subject_key_id": {"key_id": "key_id_value"},
                "authority_key_id": {},
                "crl_distribution_points": [
                    "crl_distribution_points_value1",
                    "crl_distribution_points_value2",
                ],
                "aia_issuing_certificate_urls": [
                    "aia_issuing_certificate_urls_value1",
                    "aia_issuing_certificate_urls_value2",
                ],
                "cert_fingerprint": {"sha256_hash": "sha256_hash_value"},
            }
        ],
        "gcs_bucket": "gcs_bucket_value",
        "access_urls": {
            "ca_certificate_access_url": "ca_certificate_access_url_value",
            "crl_access_urls": ["crl_access_urls_value1", "crl_access_urls_value2"],
        },
        "create_time": {},
        "update_time": {},
        "delete_time": {},
        "expire_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.update_certificate_authority(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_update_certificate_authority_rest_required_fields(
    request_type=service.UpdateCertificateAuthorityRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_certificate_authority._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_certificate_authority._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "request_id",
            "update_mask",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.update_certificate_authority(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_update_certificate_authority_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.update_certificate_authority._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "requestId",
                "updateMask",
            )
        )
        & set(
            (
                "certificateAuthority",
                "updateMask",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_certificate_authority_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_update_certificate_authority",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_update_certificate_authority",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.UpdateCertificateAuthorityRequest.pb(
            service.UpdateCertificateAuthorityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.UpdateCertificateAuthorityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.update_certificate_authority(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_update_certificate_authority_rest_bad_request(
    transport: str = "rest", request_type=service.UpdateCertificateAuthorityRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "certificate_authority": {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }
    }
    request_init["certificate_authority"] = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4",
        "type_": 1,
        "config": {
            "subject_config": {
                "subject": {
                    "common_name": "common_name_value",
                    "country_code": "country_code_value",
                    "organization": "organization_value",
                    "organizational_unit": "organizational_unit_value",
                    "locality": "locality_value",
                    "province": "province_value",
                    "street_address": "street_address_value",
                    "postal_code": "postal_code_value",
                },
                "subject_alt_name": {
                    "dns_names": ["dns_names_value1", "dns_names_value2"],
                    "uris": ["uris_value1", "uris_value2"],
                    "email_addresses": [
                        "email_addresses_value1",
                        "email_addresses_value2",
                    ],
                    "ip_addresses": ["ip_addresses_value1", "ip_addresses_value2"],
                    "custom_sans": [
                        {
                            "object_id": {"object_id_path": [1456, 1457]},
                            "critical": True,
                            "value": b"value_blob",
                        }
                    ],
                },
            },
            "x509_config": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": {},
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": {},
            },
            "public_key": {"key": b"key_blob", "format_": 1},
        },
        "lifetime": {"seconds": 751, "nanos": 543},
        "key_spec": {
            "cloud_kms_key_version": "cloud_kms_key_version_value",
            "algorithm": 1,
        },
        "subordinate_config": {
            "certificate_authority": "certificate_authority_value",
            "pem_issuer_chain": {
                "pem_certificates": [
                    "pem_certificates_value1",
                    "pem_certificates_value2",
                ]
            },
        },
        "tier": 1,
        "state": 1,
        "pem_ca_certificates": [
            "pem_ca_certificates_value1",
            "pem_ca_certificates_value2",
        ],
        "ca_certificate_descriptions": [
            {
                "subject_description": {
                    "subject": {},
                    "subject_alt_name": {},
                    "hex_serial_number": "hex_serial_number_value",
                    "lifetime": {},
                    "not_before_time": {"seconds": 751, "nanos": 543},
                    "not_after_time": {},
                },
                "x509_description": {},
                "public_key": {},
                "subject_key_id": {"key_id": "key_id_value"},
                "authority_key_id": {},
                "crl_distribution_points": [
                    "crl_distribution_points_value1",
                    "crl_distribution_points_value2",
                ],
                "aia_issuing_certificate_urls": [
                    "aia_issuing_certificate_urls_value1",
                    "aia_issuing_certificate_urls_value2",
                ],
                "cert_fingerprint": {"sha256_hash": "sha256_hash_value"},
            }
        ],
        "gcs_bucket": "gcs_bucket_value",
        "access_urls": {
            "ca_certificate_access_url": "ca_certificate_access_url_value",
            "crl_access_urls": ["crl_access_urls_value1", "crl_access_urls_value2"],
        },
        "create_time": {},
        "update_time": {},
        "delete_time": {},
        "expire_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.update_certificate_authority(request)


def test_update_certificate_authority_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "certificate_authority": {
                "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.update_certificate_authority(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{certificate_authority.name=projects/*/locations/*/caPools/*/certificateAuthorities/*}"
            % client.transport._host,
            args[1],
        )


def test_update_certificate_authority_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_certificate_authority(
            service.UpdateCertificateAuthorityRequest(),
            certificate_authority=resources.CertificateAuthority(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_update_certificate_authority_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.CreateCaPoolRequest,
        dict,
    ],
)
def test_create_ca_pool_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request_init["ca_pool"] = {
        "name": "name_value",
        "tier": 1,
        "issuance_policy": {
            "allowed_key_types": [
                {
                    "rsa": {"min_modulus_size": 1734, "max_modulus_size": 1736},
                    "elliptic_curve": {"signature_algorithm": 1},
                }
            ],
            "maximum_lifetime": {"seconds": 751, "nanos": 543},
            "allowed_issuance_modes": {
                "allow_csr_based_issuance": True,
                "allow_config_based_issuance": True,
            },
            "baseline_values": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": [{"object_id_path": [1456, 1457]}],
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": [
                    {"object_id": {}, "critical": True, "value": b"value_blob"}
                ],
            },
            "identity_constraints": {
                "cel_expression": {
                    "expression": "expression_value",
                    "title": "title_value",
                    "description": "description_value",
                    "location": "location_value",
                },
                "allow_subject_passthrough": True,
                "allow_subject_alt_names_passthrough": True,
            },
            "passthrough_extensions": {
                "known_extensions": [1],
                "additional_extensions": {},
            },
        },
        "publishing_options": {"publish_ca_cert": True, "publish_crl": True},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.create_ca_pool(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_create_ca_pool_rest_required_fields(request_type=service.CreateCaPoolRequest):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["ca_pool_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped
    assert "caPoolId" not in jsonified_request

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).create_ca_pool._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "caPoolId" in jsonified_request
    assert jsonified_request["caPoolId"] == request_init["ca_pool_id"]

    jsonified_request["parent"] = "parent_value"
    jsonified_request["caPoolId"] = "ca_pool_id_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).create_ca_pool._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "ca_pool_id",
            "request_id",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "caPoolId" in jsonified_request
    assert jsonified_request["caPoolId"] == "ca_pool_id_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.create_ca_pool(request)

            expected_params = [
                (
                    "caPoolId",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_create_ca_pool_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.create_ca_pool._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "caPoolId",
                "requestId",
            )
        )
        & set(
            (
                "parent",
                "caPoolId",
                "caPool",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_ca_pool_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_create_ca_pool"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_create_ca_pool"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.CreateCaPoolRequest.pb(service.CreateCaPoolRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.CreateCaPoolRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.create_ca_pool(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_create_ca_pool_rest_bad_request(
    transport: str = "rest", request_type=service.CreateCaPoolRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request_init["ca_pool"] = {
        "name": "name_value",
        "tier": 1,
        "issuance_policy": {
            "allowed_key_types": [
                {
                    "rsa": {"min_modulus_size": 1734, "max_modulus_size": 1736},
                    "elliptic_curve": {"signature_algorithm": 1},
                }
            ],
            "maximum_lifetime": {"seconds": 751, "nanos": 543},
            "allowed_issuance_modes": {
                "allow_csr_based_issuance": True,
                "allow_config_based_issuance": True,
            },
            "baseline_values": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": [{"object_id_path": [1456, 1457]}],
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": [
                    {"object_id": {}, "critical": True, "value": b"value_blob"}
                ],
            },
            "identity_constraints": {
                "cel_expression": {
                    "expression": "expression_value",
                    "title": "title_value",
                    "description": "description_value",
                    "location": "location_value",
                },
                "allow_subject_passthrough": True,
                "allow_subject_alt_names_passthrough": True,
            },
            "passthrough_extensions": {
                "known_extensions": [1],
                "additional_extensions": {},
            },
        },
        "publishing_options": {"publish_ca_cert": True, "publish_crl": True},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.create_ca_pool(request)


def test_create_ca_pool_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1/locations/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            ca_pool=resources.CaPool(name="name_value"),
            ca_pool_id="ca_pool_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.create_ca_pool(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*}/caPools" % client.transport._host,
            args[1],
        )


def test_create_ca_pool_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_ca_pool(
            service.CreateCaPoolRequest(),
            parent="parent_value",
            ca_pool=resources.CaPool(name="name_value"),
            ca_pool_id="ca_pool_id_value",
        )


def test_create_ca_pool_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCaPoolRequest,
        dict,
    ],
)
def test_update_ca_pool_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "ca_pool": {"name": "projects/sample1/locations/sample2/caPools/sample3"}
    }
    request_init["ca_pool"] = {
        "name": "projects/sample1/locations/sample2/caPools/sample3",
        "tier": 1,
        "issuance_policy": {
            "allowed_key_types": [
                {
                    "rsa": {"min_modulus_size": 1734, "max_modulus_size": 1736},
                    "elliptic_curve": {"signature_algorithm": 1},
                }
            ],
            "maximum_lifetime": {"seconds": 751, "nanos": 543},
            "allowed_issuance_modes": {
                "allow_csr_based_issuance": True,
                "allow_config_based_issuance": True,
            },
            "baseline_values": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": [{"object_id_path": [1456, 1457]}],
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": [
                    {"object_id": {}, "critical": True, "value": b"value_blob"}
                ],
            },
            "identity_constraints": {
                "cel_expression": {
                    "expression": "expression_value",
                    "title": "title_value",
                    "description": "description_value",
                    "location": "location_value",
                },
                "allow_subject_passthrough": True,
                "allow_subject_alt_names_passthrough": True,
            },
            "passthrough_extensions": {
                "known_extensions": [1],
                "additional_extensions": {},
            },
        },
        "publishing_options": {"publish_ca_cert": True, "publish_crl": True},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.update_ca_pool(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_update_ca_pool_rest_required_fields(request_type=service.UpdateCaPoolRequest):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_ca_pool._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_ca_pool._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "request_id",
            "update_mask",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.update_ca_pool(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_update_ca_pool_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.update_ca_pool._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "requestId",
                "updateMask",
            )
        )
        & set(
            (
                "caPool",
                "updateMask",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_ca_pool_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_update_ca_pool"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_update_ca_pool"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.UpdateCaPoolRequest.pb(service.UpdateCaPoolRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.UpdateCaPoolRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.update_ca_pool(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_update_ca_pool_rest_bad_request(
    transport: str = "rest", request_type=service.UpdateCaPoolRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "ca_pool": {"name": "projects/sample1/locations/sample2/caPools/sample3"}
    }
    request_init["ca_pool"] = {
        "name": "projects/sample1/locations/sample2/caPools/sample3",
        "tier": 1,
        "issuance_policy": {
            "allowed_key_types": [
                {
                    "rsa": {"min_modulus_size": 1734, "max_modulus_size": 1736},
                    "elliptic_curve": {"signature_algorithm": 1},
                }
            ],
            "maximum_lifetime": {"seconds": 751, "nanos": 543},
            "allowed_issuance_modes": {
                "allow_csr_based_issuance": True,
                "allow_config_based_issuance": True,
            },
            "baseline_values": {
                "key_usage": {
                    "base_key_usage": {
                        "digital_signature": True,
                        "content_commitment": True,
                        "key_encipherment": True,
                        "data_encipherment": True,
                        "key_agreement": True,
                        "cert_sign": True,
                        "crl_sign": True,
                        "encipher_only": True,
                        "decipher_only": True,
                    },
                    "extended_key_usage": {
                        "server_auth": True,
                        "client_auth": True,
                        "code_signing": True,
                        "email_protection": True,
                        "time_stamping": True,
                        "ocsp_signing": True,
                    },
                    "unknown_extended_key_usages": [{"object_id_path": [1456, 1457]}],
                },
                "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
                "policy_ids": {},
                "aia_ocsp_servers": [
                    "aia_ocsp_servers_value1",
                    "aia_ocsp_servers_value2",
                ],
                "name_constraints": {
                    "critical": True,
                    "permitted_dns_names": [
                        "permitted_dns_names_value1",
                        "permitted_dns_names_value2",
                    ],
                    "excluded_dns_names": [
                        "excluded_dns_names_value1",
                        "excluded_dns_names_value2",
                    ],
                    "permitted_ip_ranges": [
                        "permitted_ip_ranges_value1",
                        "permitted_ip_ranges_value2",
                    ],
                    "excluded_ip_ranges": [
                        "excluded_ip_ranges_value1",
                        "excluded_ip_ranges_value2",
                    ],
                    "permitted_email_addresses": [
                        "permitted_email_addresses_value1",
                        "permitted_email_addresses_value2",
                    ],
                    "excluded_email_addresses": [
                        "excluded_email_addresses_value1",
                        "excluded_email_addresses_value2",
                    ],
                    "permitted_uris": [
                        "permitted_uris_value1",
                        "permitted_uris_value2",
                    ],
                    "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
                },
                "additional_extensions": [
                    {"object_id": {}, "critical": True, "value": b"value_blob"}
                ],
            },
            "identity_constraints": {
                "cel_expression": {
                    "expression": "expression_value",
                    "title": "title_value",
                    "description": "description_value",
                    "location": "location_value",
                },
                "allow_subject_passthrough": True,
                "allow_subject_alt_names_passthrough": True,
            },
            "passthrough_extensions": {
                "known_extensions": [1],
                "additional_extensions": {},
            },
        },
        "publishing_options": {"publish_ca_cert": True, "publish_crl": True},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.update_ca_pool(request)


def test_update_ca_pool_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "ca_pool": {"name": "projects/sample1/locations/sample2/caPools/sample3"}
        }

        # get truthy value for each flattened field
        mock_args = dict(
            ca_pool=resources.CaPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.update_ca_pool(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{ca_pool.name=projects/*/locations/*/caPools/*}"
            % client.transport._host,
            args[1],
        )


def test_update_ca_pool_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_ca_pool(
            service.UpdateCaPoolRequest(),
            ca_pool=resources.CaPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_update_ca_pool_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCaPoolRequest,
        dict,
    ],
)
def test_get_ca_pool_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.CaPool(
            name="name_value",
            tier=resources.CaPool.Tier.ENTERPRISE,
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.CaPool.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.get_ca_pool(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CaPool)
    assert response.name == "name_value"
    assert response.tier == resources.CaPool.Tier.ENTERPRISE


def test_get_ca_pool_rest_required_fields(request_type=service.GetCaPoolRequest):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_ca_pool._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_ca_pool._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.CaPool()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = resources.CaPool.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.get_ca_pool(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_get_ca_pool_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.get_ca_pool._get_unset_required_fields({})
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_ca_pool_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_get_ca_pool"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_get_ca_pool"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.GetCaPoolRequest.pb(service.GetCaPoolRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = resources.CaPool.to_json(resources.CaPool())

        request = service.GetCaPoolRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.CaPool()

        client.get_ca_pool(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_get_ca_pool_rest_bad_request(
    transport: str = "rest", request_type=service.GetCaPoolRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_ca_pool(request)


def test_get_ca_pool_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.CaPool()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/locations/sample2/caPools/sample3"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.CaPool.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.get_ca_pool(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*}" % client.transport._host,
            args[1],
        )


def test_get_ca_pool_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_ca_pool(
            service.GetCaPoolRequest(),
            name="name_value",
        )


def test_get_ca_pool_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCaPoolsRequest,
        dict,
    ],
)
def test_list_ca_pools_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCaPoolsResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCaPoolsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.list_ca_pools(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCaPoolsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_ca_pools_rest_required_fields(request_type=service.ListCaPoolsRequest):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_ca_pools._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_ca_pools._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "order_by",
            "page_size",
            "page_token",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = service.ListCaPoolsResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = service.ListCaPoolsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.list_ca_pools(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_list_ca_pools_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.list_ca_pools._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "filter",
                "orderBy",
                "pageSize",
                "pageToken",
            )
        )
        & set(("parent",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_ca_pools_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_list_ca_pools"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_list_ca_pools"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.ListCaPoolsRequest.pb(service.ListCaPoolsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = service.ListCaPoolsResponse.to_json(
            service.ListCaPoolsResponse()
        )

        request = service.ListCaPoolsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = service.ListCaPoolsResponse()

        client.list_ca_pools(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_list_ca_pools_rest_bad_request(
    transport: str = "rest", request_type=service.ListCaPoolsRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_ca_pools(request)


def test_list_ca_pools_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCaPoolsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1/locations/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCaPoolsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.list_ca_pools(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*}/caPools" % client.transport._host,
            args[1],
        )


def test_list_ca_pools_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_ca_pools(
            service.ListCaPoolsRequest(),
            parent="parent_value",
        )


def test_list_ca_pools_rest_pager(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                    resources.CaPool(),
                ],
                next_page_token="abc",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[],
                next_page_token="def",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                ],
                next_page_token="ghi",
            ),
            service.ListCaPoolsResponse(
                ca_pools=[
                    resources.CaPool(),
                    resources.CaPool(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(service.ListCaPoolsResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1/locations/sample2"}

        pager = client.list_ca_pools(request=sample_request)

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.CaPool) for i in results)

        pages = list(client.list_ca_pools(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.DeleteCaPoolRequest,
        dict,
    ],
)
def test_delete_ca_pool_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.delete_ca_pool(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_delete_ca_pool_rest_required_fields(request_type=service.DeleteCaPoolRequest):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).delete_ca_pool._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).delete_ca_pool._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "ignore_dependent_resources",
            "request_id",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.delete_ca_pool(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_delete_ca_pool_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.delete_ca_pool._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "ignoreDependentResources",
                "requestId",
            )
        )
        & set(("name",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_ca_pool_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_delete_ca_pool"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_delete_ca_pool"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.DeleteCaPoolRequest.pb(service.DeleteCaPoolRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.DeleteCaPoolRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.delete_ca_pool(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_delete_ca_pool_rest_bad_request(
    transport: str = "rest", request_type=service.DeleteCaPoolRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.delete_ca_pool(request)


def test_delete_ca_pool_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/locations/sample2/caPools/sample3"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.delete_ca_pool(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*}" % client.transport._host,
            args[1],
        )


def test_delete_ca_pool_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_ca_pool(
            service.DeleteCaPoolRequest(),
            name="name_value",
        )


def test_delete_ca_pool_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.FetchCaCertsRequest,
        dict,
    ],
)
def test_fetch_ca_certs_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"ca_pool": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.FetchCaCertsResponse()

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.FetchCaCertsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.fetch_ca_certs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.FetchCaCertsResponse)


def test_fetch_ca_certs_rest_required_fields(request_type=service.FetchCaCertsRequest):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["ca_pool"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).fetch_ca_certs._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["caPool"] = "ca_pool_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).fetch_ca_certs._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "caPool" in jsonified_request
    assert jsonified_request["caPool"] == "ca_pool_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = service.FetchCaCertsResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = service.FetchCaCertsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.fetch_ca_certs(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_fetch_ca_certs_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.fetch_ca_certs._get_unset_required_fields({})
    assert set(unset_fields) == (set(()) & set(("caPool",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_ca_certs_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "post_fetch_ca_certs"
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor, "pre_fetch_ca_certs"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.FetchCaCertsRequest.pb(service.FetchCaCertsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = service.FetchCaCertsResponse.to_json(
            service.FetchCaCertsResponse()
        )

        request = service.FetchCaCertsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = service.FetchCaCertsResponse()

        client.fetch_ca_certs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_fetch_ca_certs_rest_bad_request(
    transport: str = "rest", request_type=service.FetchCaCertsRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"ca_pool": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.fetch_ca_certs(request)


def test_fetch_ca_certs_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.FetchCaCertsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "ca_pool": "projects/sample1/locations/sample2/caPools/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            ca_pool="ca_pool_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.FetchCaCertsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.fetch_ca_certs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{ca_pool=projects/*/locations/*/caPools/*}:fetchCaCerts"
            % client.transport._host,
            args[1],
        )


def test_fetch_ca_certs_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.fetch_ca_certs(
            service.FetchCaCertsRequest(),
            ca_pool="ca_pool_value",
        )


def test_fetch_ca_certs_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCertificateRevocationListRequest,
        dict,
    ],
)
def test_get_certificate_revocation_list_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4/certificateRevocationLists/sample5"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.CertificateRevocationList(
            name="name_value",
            sequence_number=1601,
            pem_crl="pem_crl_value",
            access_url="access_url_value",
            state=resources.CertificateRevocationList.State.ACTIVE,
            revision_id="revision_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.CertificateRevocationList.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.get_certificate_revocation_list(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateRevocationList)
    assert response.name == "name_value"
    assert response.sequence_number == 1601
    assert response.pem_crl == "pem_crl_value"
    assert response.access_url == "access_url_value"
    assert response.state == resources.CertificateRevocationList.State.ACTIVE
    assert response.revision_id == "revision_id_value"


def test_get_certificate_revocation_list_rest_required_fields(
    request_type=service.GetCertificateRevocationListRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_certificate_revocation_list._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_certificate_revocation_list._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.CertificateRevocationList()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = resources.CertificateRevocationList.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.get_certificate_revocation_list(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_get_certificate_revocation_list_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.get_certificate_revocation_list._get_unset_required_fields(
        {}
    )
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_certificate_revocation_list_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_get_certificate_revocation_list",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_get_certificate_revocation_list",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.GetCertificateRevocationListRequest.pb(
            service.GetCertificateRevocationListRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = resources.CertificateRevocationList.to_json(
            resources.CertificateRevocationList()
        )

        request = service.GetCertificateRevocationListRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.CertificateRevocationList()

        client.get_certificate_revocation_list(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_get_certificate_revocation_list_rest_bad_request(
    transport: str = "rest", request_type=service.GetCertificateRevocationListRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4/certificateRevocationLists/sample5"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_certificate_revocation_list(request)


def test_get_certificate_revocation_list_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.CertificateRevocationList()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4/certificateRevocationLists/sample5"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.CertificateRevocationList.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.get_certificate_revocation_list(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/caPools/*/certificateAuthorities/*/certificateRevocationLists/*}"
            % client.transport._host,
            args[1],
        )


def test_get_certificate_revocation_list_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_certificate_revocation_list(
            service.GetCertificateRevocationListRequest(),
            name="name_value",
        )


def test_get_certificate_revocation_list_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCertificateRevocationListsRequest,
        dict,
    ],
)
def test_list_certificate_revocation_lists_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "parent": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCertificateRevocationListsResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCertificateRevocationListsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.list_certificate_revocation_lists(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateRevocationListsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_certificate_revocation_lists_rest_required_fields(
    request_type=service.ListCertificateRevocationListsRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_certificate_revocation_lists._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_certificate_revocation_lists._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "order_by",
            "page_size",
            "page_token",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = service.ListCertificateRevocationListsResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = service.ListCertificateRevocationListsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.list_certificate_revocation_lists(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_list_certificate_revocation_lists_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = (
        transport.list_certificate_revocation_lists._get_unset_required_fields({})
    )
    assert set(unset_fields) == (
        set(
            (
                "filter",
                "orderBy",
                "pageSize",
                "pageToken",
            )
        )
        & set(("parent",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_certificate_revocation_lists_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_list_certificate_revocation_lists",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_list_certificate_revocation_lists",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.ListCertificateRevocationListsRequest.pb(
            service.ListCertificateRevocationListsRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = (
            service.ListCertificateRevocationListsResponse.to_json(
                service.ListCertificateRevocationListsResponse()
            )
        )

        request = service.ListCertificateRevocationListsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = service.ListCertificateRevocationListsResponse()

        client.list_certificate_revocation_lists(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_list_certificate_revocation_lists_rest_bad_request(
    transport: str = "rest", request_type=service.ListCertificateRevocationListsRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "parent": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_certificate_revocation_lists(request)


def test_list_certificate_revocation_lists_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCertificateRevocationListsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCertificateRevocationListsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.list_certificate_revocation_lists(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/caPools/*/certificateAuthorities/*}/certificateRevocationLists"
            % client.transport._host,
            args[1],
        )


def test_list_certificate_revocation_lists_rest_flattened_error(
    transport: str = "rest",
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_certificate_revocation_lists(
            service.ListCertificateRevocationListsRequest(),
            parent="parent_value",
        )


def test_list_certificate_revocation_lists_rest_pager(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[],
                next_page_token="def",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateRevocationListsResponse(
                certificate_revocation_lists=[
                    resources.CertificateRevocationList(),
                    resources.CertificateRevocationList(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            service.ListCertificateRevocationListsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4"
        }

        pager = client.list_certificate_revocation_lists(request=sample_request)

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.CertificateRevocationList) for i in results)

        pages = list(
            client.list_certificate_revocation_lists(request=sample_request).pages
        )
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCertificateRevocationListRequest,
        dict,
    ],
)
def test_update_certificate_revocation_list_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "certificate_revocation_list": {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4/certificateRevocationLists/sample5"
        }
    }
    request_init["certificate_revocation_list"] = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4/certificateRevocationLists/sample5",
        "sequence_number": 1601,
        "revoked_certificates": [
            {
                "certificate": "certificate_value",
                "hex_serial_number": "hex_serial_number_value",
                "revocation_reason": 1,
            }
        ],
        "pem_crl": "pem_crl_value",
        "access_url": "access_url_value",
        "state": 1,
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "revision_id": "revision_id_value",
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.update_certificate_revocation_list(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_update_certificate_revocation_list_rest_required_fields(
    request_type=service.UpdateCertificateRevocationListRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_certificate_revocation_list._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_certificate_revocation_list._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "request_id",
            "update_mask",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.update_certificate_revocation_list(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_update_certificate_revocation_list_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = (
        transport.update_certificate_revocation_list._get_unset_required_fields({})
    )
    assert set(unset_fields) == (
        set(
            (
                "requestId",
                "updateMask",
            )
        )
        & set(
            (
                "certificateRevocationList",
                "updateMask",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_certificate_revocation_list_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_update_certificate_revocation_list",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_update_certificate_revocation_list",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.UpdateCertificateRevocationListRequest.pb(
            service.UpdateCertificateRevocationListRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.UpdateCertificateRevocationListRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.update_certificate_revocation_list(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_update_certificate_revocation_list_rest_bad_request(
    transport: str = "rest", request_type=service.UpdateCertificateRevocationListRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "certificate_revocation_list": {
            "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4/certificateRevocationLists/sample5"
        }
    }
    request_init["certificate_revocation_list"] = {
        "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4/certificateRevocationLists/sample5",
        "sequence_number": 1601,
        "revoked_certificates": [
            {
                "certificate": "certificate_value",
                "hex_serial_number": "hex_serial_number_value",
                "revocation_reason": 1,
            }
        ],
        "pem_crl": "pem_crl_value",
        "access_url": "access_url_value",
        "state": 1,
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "revision_id": "revision_id_value",
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.update_certificate_revocation_list(request)


def test_update_certificate_revocation_list_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "certificate_revocation_list": {
                "name": "projects/sample1/locations/sample2/caPools/sample3/certificateAuthorities/sample4/certificateRevocationLists/sample5"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            certificate_revocation_list=resources.CertificateRevocationList(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.update_certificate_revocation_list(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{certificate_revocation_list.name=projects/*/locations/*/caPools/*/certificateAuthorities/*/certificateRevocationLists/*}"
            % client.transport._host,
            args[1],
        )


def test_update_certificate_revocation_list_rest_flattened_error(
    transport: str = "rest",
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_certificate_revocation_list(
            service.UpdateCertificateRevocationListRequest(),
            certificate_revocation_list=resources.CertificateRevocationList(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_update_certificate_revocation_list_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.CreateCertificateTemplateRequest,
        dict,
    ],
)
def test_create_certificate_template_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request_init["certificate_template"] = {
        "name": "name_value",
        "predefined_values": {
            "key_usage": {
                "base_key_usage": {
                    "digital_signature": True,
                    "content_commitment": True,
                    "key_encipherment": True,
                    "data_encipherment": True,
                    "key_agreement": True,
                    "cert_sign": True,
                    "crl_sign": True,
                    "encipher_only": True,
                    "decipher_only": True,
                },
                "extended_key_usage": {
                    "server_auth": True,
                    "client_auth": True,
                    "code_signing": True,
                    "email_protection": True,
                    "time_stamping": True,
                    "ocsp_signing": True,
                },
                "unknown_extended_key_usages": [{"object_id_path": [1456, 1457]}],
            },
            "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
            "policy_ids": {},
            "aia_ocsp_servers": ["aia_ocsp_servers_value1", "aia_ocsp_servers_value2"],
            "name_constraints": {
                "critical": True,
                "permitted_dns_names": [
                    "permitted_dns_names_value1",
                    "permitted_dns_names_value2",
                ],
                "excluded_dns_names": [
                    "excluded_dns_names_value1",
                    "excluded_dns_names_value2",
                ],
                "permitted_ip_ranges": [
                    "permitted_ip_ranges_value1",
                    "permitted_ip_ranges_value2",
                ],
                "excluded_ip_ranges": [
                    "excluded_ip_ranges_value1",
                    "excluded_ip_ranges_value2",
                ],
                "permitted_email_addresses": [
                    "permitted_email_addresses_value1",
                    "permitted_email_addresses_value2",
                ],
                "excluded_email_addresses": [
                    "excluded_email_addresses_value1",
                    "excluded_email_addresses_value2",
                ],
                "permitted_uris": ["permitted_uris_value1", "permitted_uris_value2"],
                "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
            },
            "additional_extensions": [
                {"object_id": {}, "critical": True, "value": b"value_blob"}
            ],
        },
        "identity_constraints": {
            "cel_expression": {
                "expression": "expression_value",
                "title": "title_value",
                "description": "description_value",
                "location": "location_value",
            },
            "allow_subject_passthrough": True,
            "allow_subject_alt_names_passthrough": True,
        },
        "passthrough_extensions": {
            "known_extensions": [1],
            "additional_extensions": {},
        },
        "description": "description_value",
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.create_certificate_template(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_create_certificate_template_rest_required_fields(
    request_type=service.CreateCertificateTemplateRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["certificate_template_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped
    assert "certificateTemplateId" not in jsonified_request

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).create_certificate_template._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "certificateTemplateId" in jsonified_request
    assert (
        jsonified_request["certificateTemplateId"]
        == request_init["certificate_template_id"]
    )

    jsonified_request["parent"] = "parent_value"
    jsonified_request["certificateTemplateId"] = "certificate_template_id_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).create_certificate_template._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "certificate_template_id",
            "request_id",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "certificateTemplateId" in jsonified_request
    assert jsonified_request["certificateTemplateId"] == "certificate_template_id_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.create_certificate_template(request)

            expected_params = [
                (
                    "certificateTemplateId",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_create_certificate_template_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.create_certificate_template._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "certificateTemplateId",
                "requestId",
            )
        )
        & set(
            (
                "parent",
                "certificateTemplateId",
                "certificateTemplate",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_certificate_template_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_create_certificate_template",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_create_certificate_template",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.CreateCertificateTemplateRequest.pb(
            service.CreateCertificateTemplateRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.CreateCertificateTemplateRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.create_certificate_template(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_create_certificate_template_rest_bad_request(
    transport: str = "rest", request_type=service.CreateCertificateTemplateRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request_init["certificate_template"] = {
        "name": "name_value",
        "predefined_values": {
            "key_usage": {
                "base_key_usage": {
                    "digital_signature": True,
                    "content_commitment": True,
                    "key_encipherment": True,
                    "data_encipherment": True,
                    "key_agreement": True,
                    "cert_sign": True,
                    "crl_sign": True,
                    "encipher_only": True,
                    "decipher_only": True,
                },
                "extended_key_usage": {
                    "server_auth": True,
                    "client_auth": True,
                    "code_signing": True,
                    "email_protection": True,
                    "time_stamping": True,
                    "ocsp_signing": True,
                },
                "unknown_extended_key_usages": [{"object_id_path": [1456, 1457]}],
            },
            "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
            "policy_ids": {},
            "aia_ocsp_servers": ["aia_ocsp_servers_value1", "aia_ocsp_servers_value2"],
            "name_constraints": {
                "critical": True,
                "permitted_dns_names": [
                    "permitted_dns_names_value1",
                    "permitted_dns_names_value2",
                ],
                "excluded_dns_names": [
                    "excluded_dns_names_value1",
                    "excluded_dns_names_value2",
                ],
                "permitted_ip_ranges": [
                    "permitted_ip_ranges_value1",
                    "permitted_ip_ranges_value2",
                ],
                "excluded_ip_ranges": [
                    "excluded_ip_ranges_value1",
                    "excluded_ip_ranges_value2",
                ],
                "permitted_email_addresses": [
                    "permitted_email_addresses_value1",
                    "permitted_email_addresses_value2",
                ],
                "excluded_email_addresses": [
                    "excluded_email_addresses_value1",
                    "excluded_email_addresses_value2",
                ],
                "permitted_uris": ["permitted_uris_value1", "permitted_uris_value2"],
                "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
            },
            "additional_extensions": [
                {"object_id": {}, "critical": True, "value": b"value_blob"}
            ],
        },
        "identity_constraints": {
            "cel_expression": {
                "expression": "expression_value",
                "title": "title_value",
                "description": "description_value",
                "location": "location_value",
            },
            "allow_subject_passthrough": True,
            "allow_subject_alt_names_passthrough": True,
        },
        "passthrough_extensions": {
            "known_extensions": [1],
            "additional_extensions": {},
        },
        "description": "description_value",
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.create_certificate_template(request)


def test_create_certificate_template_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1/locations/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            certificate_template=resources.CertificateTemplate(name="name_value"),
            certificate_template_id="certificate_template_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.create_certificate_template(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*}/certificateTemplates"
            % client.transport._host,
            args[1],
        )


def test_create_certificate_template_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_certificate_template(
            service.CreateCertificateTemplateRequest(),
            parent="parent_value",
            certificate_template=resources.CertificateTemplate(name="name_value"),
            certificate_template_id="certificate_template_id_value",
        )


def test_create_certificate_template_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.DeleteCertificateTemplateRequest,
        dict,
    ],
)
def test_delete_certificate_template_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.delete_certificate_template(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_delete_certificate_template_rest_required_fields(
    request_type=service.DeleteCertificateTemplateRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).delete_certificate_template._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).delete_certificate_template._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("request_id",))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.delete_certificate_template(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_delete_certificate_template_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.delete_certificate_template._get_unset_required_fields({})
    assert set(unset_fields) == (set(("requestId",)) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_certificate_template_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_delete_certificate_template",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_delete_certificate_template",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.DeleteCertificateTemplateRequest.pb(
            service.DeleteCertificateTemplateRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.DeleteCertificateTemplateRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.delete_certificate_template(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_delete_certificate_template_rest_bad_request(
    transport: str = "rest", request_type=service.DeleteCertificateTemplateRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.delete_certificate_template(request)


def test_delete_certificate_template_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.delete_certificate_template(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/certificateTemplates/*}"
            % client.transport._host,
            args[1],
        )


def test_delete_certificate_template_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_certificate_template(
            service.DeleteCertificateTemplateRequest(),
            name="name_value",
        )


def test_delete_certificate_template_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.GetCertificateTemplateRequest,
        dict,
    ],
)
def test_get_certificate_template_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.CertificateTemplate(
            name="name_value",
            description="description_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.CertificateTemplate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.get_certificate_template(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.CertificateTemplate)
    assert response.name == "name_value"
    assert response.description == "description_value"


def test_get_certificate_template_rest_required_fields(
    request_type=service.GetCertificateTemplateRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_certificate_template._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).get_certificate_template._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.CertificateTemplate()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = resources.CertificateTemplate.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.get_certificate_template(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_get_certificate_template_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.get_certificate_template._get_unset_required_fields({})
    assert set(unset_fields) == (set(()) & set(("name",)))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_certificate_template_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_get_certificate_template",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_get_certificate_template",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.GetCertificateTemplateRequest.pb(
            service.GetCertificateTemplateRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = resources.CertificateTemplate.to_json(
            resources.CertificateTemplate()
        )

        request = service.GetCertificateTemplateRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.CertificateTemplate()

        client.get_certificate_template(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_get_certificate_template_rest_bad_request(
    transport: str = "rest", request_type=service.GetCertificateTemplateRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_certificate_template(request)


def test_get_certificate_template_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.CertificateTemplate()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = resources.CertificateTemplate.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.get_certificate_template(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/certificateTemplates/*}"
            % client.transport._host,
            args[1],
        )


def test_get_certificate_template_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_certificate_template(
            service.GetCertificateTemplateRequest(),
            name="name_value",
        )


def test_get_certificate_template_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        service.ListCertificateTemplatesRequest,
        dict,
    ],
)
def test_list_certificate_templates_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCertificateTemplatesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCertificateTemplatesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.list_certificate_templates(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCertificateTemplatesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_certificate_templates_rest_required_fields(
    request_type=service.ListCertificateTemplatesRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_certificate_templates._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).list_certificate_templates._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "order_by",
            "page_size",
            "page_token",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = service.ListCertificateTemplatesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = service.ListCertificateTemplatesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.list_certificate_templates(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_list_certificate_templates_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.list_certificate_templates._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "filter",
                "orderBy",
                "pageSize",
                "pageToken",
            )
        )
        & set(("parent",))
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_certificate_templates_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_list_certificate_templates",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_list_certificate_templates",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.ListCertificateTemplatesRequest.pb(
            service.ListCertificateTemplatesRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = service.ListCertificateTemplatesResponse.to_json(
            service.ListCertificateTemplatesResponse()
        )

        request = service.ListCertificateTemplatesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = service.ListCertificateTemplatesResponse()

        client.list_certificate_templates(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_list_certificate_templates_rest_bad_request(
    transport: str = "rest", request_type=service.ListCertificateTemplatesRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_certificate_templates(request)


def test_list_certificate_templates_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = service.ListCertificateTemplatesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1/locations/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = service.ListCertificateTemplatesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.list_certificate_templates(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*}/certificateTemplates"
            % client.transport._host,
            args[1],
        )


def test_list_certificate_templates_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_certificate_templates(
            service.ListCertificateTemplatesRequest(),
            parent="parent_value",
        )


def test_list_certificate_templates_rest_pager(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
                next_page_token="abc",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[],
                next_page_token="def",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                ],
                next_page_token="ghi",
            ),
            service.ListCertificateTemplatesResponse(
                certificate_templates=[
                    resources.CertificateTemplate(),
                    resources.CertificateTemplate(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            service.ListCertificateTemplatesResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1/locations/sample2"}

        pager = client.list_certificate_templates(request=sample_request)

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.CertificateTemplate) for i in results)

        pages = list(client.list_certificate_templates(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        service.UpdateCertificateTemplateRequest,
        dict,
    ],
)
def test_update_certificate_template_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {
        "certificate_template": {
            "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
        }
    }
    request_init["certificate_template"] = {
        "name": "projects/sample1/locations/sample2/certificateTemplates/sample3",
        "predefined_values": {
            "key_usage": {
                "base_key_usage": {
                    "digital_signature": True,
                    "content_commitment": True,
                    "key_encipherment": True,
                    "data_encipherment": True,
                    "key_agreement": True,
                    "cert_sign": True,
                    "crl_sign": True,
                    "encipher_only": True,
                    "decipher_only": True,
                },
                "extended_key_usage": {
                    "server_auth": True,
                    "client_auth": True,
                    "code_signing": True,
                    "email_protection": True,
                    "time_stamping": True,
                    "ocsp_signing": True,
                },
                "unknown_extended_key_usages": [{"object_id_path": [1456, 1457]}],
            },
            "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
            "policy_ids": {},
            "aia_ocsp_servers": ["aia_ocsp_servers_value1", "aia_ocsp_servers_value2"],
            "name_constraints": {
                "critical": True,
                "permitted_dns_names": [
                    "permitted_dns_names_value1",
                    "permitted_dns_names_value2",
                ],
                "excluded_dns_names": [
                    "excluded_dns_names_value1",
                    "excluded_dns_names_value2",
                ],
                "permitted_ip_ranges": [
                    "permitted_ip_ranges_value1",
                    "permitted_ip_ranges_value2",
                ],
                "excluded_ip_ranges": [
                    "excluded_ip_ranges_value1",
                    "excluded_ip_ranges_value2",
                ],
                "permitted_email_addresses": [
                    "permitted_email_addresses_value1",
                    "permitted_email_addresses_value2",
                ],
                "excluded_email_addresses": [
                    "excluded_email_addresses_value1",
                    "excluded_email_addresses_value2",
                ],
                "permitted_uris": ["permitted_uris_value1", "permitted_uris_value2"],
                "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
            },
            "additional_extensions": [
                {"object_id": {}, "critical": True, "value": b"value_blob"}
            ],
        },
        "identity_constraints": {
            "cel_expression": {
                "expression": "expression_value",
                "title": "title_value",
                "description": "description_value",
                "location": "location_value",
            },
            "allow_subject_passthrough": True,
            "allow_subject_alt_names_passthrough": True,
        },
        "passthrough_extensions": {
            "known_extensions": [1],
            "additional_extensions": {},
        },
        "description": "description_value",
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.update_certificate_template(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


def test_update_certificate_template_rest_required_fields(
    request_type=service.UpdateCertificateTemplateRequest,
):
    transport_class = transports.CertificateAuthorityServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(
            pb_request,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        )
    )

    # verify fields with default values are dropped

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_certificate_template._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    unset_fields = transport_class(
        credentials=ga_credentials.AnonymousCredentials()
    ).update_certificate_template._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "request_id",
            "update_mask",
        )
    )
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone

    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value

            response = client.update_certificate_template(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert expected_params == actual_params


def test_update_certificate_template_rest_unset_required_fields():
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials
    )

    unset_fields = transport.update_certificate_template._get_unset_required_fields({})
    assert set(unset_fields) == (
        set(
            (
                "requestId",
                "updateMask",
            )
        )
        & set(
            (
                "certificateTemplate",
                "updateMask",
            )
        )
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_certificate_template_rest_interceptors(null_interceptor):
    transport = transports.CertificateAuthorityServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CertificateAuthorityServiceRestInterceptor(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "post_update_certificate_template",
    ) as post, mock.patch.object(
        transports.CertificateAuthorityServiceRestInterceptor,
        "pre_update_certificate_template",
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = service.UpdateCertificateTemplateRequest.pb(
            service.UpdateCertificateTemplateRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = service.UpdateCertificateTemplateRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.update_certificate_template(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_update_certificate_template_rest_bad_request(
    transport: str = "rest", request_type=service.UpdateCertificateTemplateRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {
        "certificate_template": {
            "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
        }
    }
    request_init["certificate_template"] = {
        "name": "projects/sample1/locations/sample2/certificateTemplates/sample3",
        "predefined_values": {
            "key_usage": {
                "base_key_usage": {
                    "digital_signature": True,
                    "content_commitment": True,
                    "key_encipherment": True,
                    "data_encipherment": True,
                    "key_agreement": True,
                    "cert_sign": True,
                    "crl_sign": True,
                    "encipher_only": True,
                    "decipher_only": True,
                },
                "extended_key_usage": {
                    "server_auth": True,
                    "client_auth": True,
                    "code_signing": True,
                    "email_protection": True,
                    "time_stamping": True,
                    "ocsp_signing": True,
                },
                "unknown_extended_key_usages": [{"object_id_path": [1456, 1457]}],
            },
            "ca_options": {"is_ca": True, "max_issuer_path_length": 2349},
            "policy_ids": {},
            "aia_ocsp_servers": ["aia_ocsp_servers_value1", "aia_ocsp_servers_value2"],
            "name_constraints": {
                "critical": True,
                "permitted_dns_names": [
                    "permitted_dns_names_value1",
                    "permitted_dns_names_value2",
                ],
                "excluded_dns_names": [
                    "excluded_dns_names_value1",
                    "excluded_dns_names_value2",
                ],
                "permitted_ip_ranges": [
                    "permitted_ip_ranges_value1",
                    "permitted_ip_ranges_value2",
                ],
                "excluded_ip_ranges": [
                    "excluded_ip_ranges_value1",
                    "excluded_ip_ranges_value2",
                ],
                "permitted_email_addresses": [
                    "permitted_email_addresses_value1",
                    "permitted_email_addresses_value2",
                ],
                "excluded_email_addresses": [
                    "excluded_email_addresses_value1",
                    "excluded_email_addresses_value2",
                ],
                "permitted_uris": ["permitted_uris_value1", "permitted_uris_value2"],
                "excluded_uris": ["excluded_uris_value1", "excluded_uris_value2"],
            },
            "additional_extensions": [
                {"object_id": {}, "critical": True, "value": b"value_blob"}
            ],
        },
        "identity_constraints": {
            "cel_expression": {
                "expression": "expression_value",
                "title": "title_value",
                "description": "description_value",
                "location": "location_value",
            },
            "allow_subject_passthrough": True,
            "allow_subject_alt_names_passthrough": True,
        },
        "passthrough_extensions": {
            "known_extensions": [1],
            "additional_extensions": {},
        },
        "description": "description_value",
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "labels": {},
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.update_certificate_template(request)


def test_update_certificate_template_rest_flattened():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "certificate_template": {
                "name": "projects/sample1/locations/sample2/certificateTemplates/sample3"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            certificate_template=resources.CertificateTemplate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        client.update_certificate_template(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{certificate_template.name=projects/*/locations/*/certificateTemplates/*}"
            % client.transport._host,
            args[1],
        )


def test_update_certificate_template_rest_flattened_error(transport: str = "rest"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_certificate_template(
            service.UpdateCertificateTemplateRequest(),
            certificate_template=resources.CertificateTemplate(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_update_certificate_template_rest_error():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.CertificateAuthorityServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = CertificateAuthorityServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.CertificateAuthorityServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = CertificateAuthorityServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.CertificateAuthorityServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = CertificateAuthorityServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = mock.Mock()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = CertificateAuthorityServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.CertificateAuthorityServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = CertificateAuthorityServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.CertificateAuthorityServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = CertificateAuthorityServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.CertificateAuthorityServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.CertificateAuthorityServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.CertificateAuthorityServiceGrpcTransport,
        transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
        transports.CertificateAuthorityServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "rest",
    ],
)
def test_transport_kind(transport_name):
    transport = CertificateAuthorityServiceClient.get_transport_class(transport_name)(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert transport.kind == transport_name


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.CertificateAuthorityServiceGrpcTransport,
    )


def test_certificate_authority_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.CertificateAuthorityServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_certificate_authority_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.security.privateca_v1.services.certificate_authority_service.transports.CertificateAuthorityServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.CertificateAuthorityServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "create_certificate",
        "get_certificate",
        "list_certificates",
        "revoke_certificate",
        "update_certificate",
        "activate_certificate_authority",
        "create_certificate_authority",
        "disable_certificate_authority",
        "enable_certificate_authority",
        "fetch_certificate_authority_csr",
        "get_certificate_authority",
        "list_certificate_authorities",
        "undelete_certificate_authority",
        "delete_certificate_authority",
        "update_certificate_authority",
        "create_ca_pool",
        "update_ca_pool",
        "get_ca_pool",
        "list_ca_pools",
        "delete_ca_pool",
        "fetch_ca_certs",
        "get_certificate_revocation_list",
        "list_certificate_revocation_lists",
        "update_certificate_revocation_list",
        "create_certificate_template",
        "delete_certificate_template",
        "get_certificate_template",
        "list_certificate_templates",
        "update_certificate_template",
        "set_iam_policy",
        "get_iam_policy",
        "test_iam_permissions",
        "get_location",
        "list_locations",
        "get_operation",
        "cancel_operation",
        "delete_operation",
        "list_operations",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client

    # Catch all for all remaining methods and properties
    remainder = [
        "kind",
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_certificate_authority_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch(
        "google.cloud.security.privateca_v1.services.certificate_authority_service.transports.CertificateAuthorityServiceTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.CertificateAuthorityServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_certificate_authority_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
        "google.cloud.security.privateca_v1.services.certificate_authority_service.transports.CertificateAuthorityServiceTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.CertificateAuthorityServiceTransport()
        adc.assert_called_once()


def test_certificate_authority_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        CertificateAuthorityServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.CertificateAuthorityServiceGrpcTransport,
        transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
    ],
)
def test_certificate_authority_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.CertificateAuthorityServiceGrpcTransport,
        transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
        transports.CertificateAuthorityServiceRestTransport,
    ],
)
def test_certificate_authority_service_transport_auth_gdch_credentials(transport_class):
    host = "https://language.com"
    api_audience_tests = [None, "https://language2.com"]
    api_audience_expect = [host, "https://language2.com"]
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, "default", autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(
                return_value=gdch_mock
            )
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(e)


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.CertificateAuthorityServiceGrpcTransport, grpc_helpers),
        (
            transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
            grpc_helpers_async,
        ),
    ],
)
def test_certificate_authority_service_transport_create_channel(
    transport_class, grpc_helpers
):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])

        create_channel.assert_called_with(
            "privateca.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=["1", "2"],
            default_host="privateca.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.CertificateAuthorityServiceGrpcTransport,
        transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
    ],
)
def test_certificate_authority_service_grpc_transport_client_cert_source_for_mtls(
    transport_class,
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds,
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback,
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert, private_key=expected_key
            )


def test_certificate_authority_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.CertificateAuthorityServiceRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


def test_certificate_authority_service_rest_lro_client():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.AbstractOperationsClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_certificate_authority_service_host_no_port(transport_name):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="privateca.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "privateca.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://privateca.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_certificate_authority_service_host_with_port(transport_name):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="privateca.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "privateca.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://privateca.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_certificate_authority_service_client_transport_session_collision(
    transport_name,
):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = CertificateAuthorityServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = CertificateAuthorityServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.create_certificate._session
    session2 = client2.transport.create_certificate._session
    assert session1 != session2
    session1 = client1.transport.get_certificate._session
    session2 = client2.transport.get_certificate._session
    assert session1 != session2
    session1 = client1.transport.list_certificates._session
    session2 = client2.transport.list_certificates._session
    assert session1 != session2
    session1 = client1.transport.revoke_certificate._session
    session2 = client2.transport.revoke_certificate._session
    assert session1 != session2
    session1 = client1.transport.update_certificate._session
    session2 = client2.transport.update_certificate._session
    assert session1 != session2
    session1 = client1.transport.activate_certificate_authority._session
    session2 = client2.transport.activate_certificate_authority._session
    assert session1 != session2
    session1 = client1.transport.create_certificate_authority._session
    session2 = client2.transport.create_certificate_authority._session
    assert session1 != session2
    session1 = client1.transport.disable_certificate_authority._session
    session2 = client2.transport.disable_certificate_authority._session
    assert session1 != session2
    session1 = client1.transport.enable_certificate_authority._session
    session2 = client2.transport.enable_certificate_authority._session
    assert session1 != session2
    session1 = client1.transport.fetch_certificate_authority_csr._session
    session2 = client2.transport.fetch_certificate_authority_csr._session
    assert session1 != session2
    session1 = client1.transport.get_certificate_authority._session
    session2 = client2.transport.get_certificate_authority._session
    assert session1 != session2
    session1 = client1.transport.list_certificate_authorities._session
    session2 = client2.transport.list_certificate_authorities._session
    assert session1 != session2
    session1 = client1.transport.undelete_certificate_authority._session
    session2 = client2.transport.undelete_certificate_authority._session
    assert session1 != session2
    session1 = client1.transport.delete_certificate_authority._session
    session2 = client2.transport.delete_certificate_authority._session
    assert session1 != session2
    session1 = client1.transport.update_certificate_authority._session
    session2 = client2.transport.update_certificate_authority._session
    assert session1 != session2
    session1 = client1.transport.create_ca_pool._session
    session2 = client2.transport.create_ca_pool._session
    assert session1 != session2
    session1 = client1.transport.update_ca_pool._session
    session2 = client2.transport.update_ca_pool._session
    assert session1 != session2
    session1 = client1.transport.get_ca_pool._session
    session2 = client2.transport.get_ca_pool._session
    assert session1 != session2
    session1 = client1.transport.list_ca_pools._session
    session2 = client2.transport.list_ca_pools._session
    assert session1 != session2
    session1 = client1.transport.delete_ca_pool._session
    session2 = client2.transport.delete_ca_pool._session
    assert session1 != session2
    session1 = client1.transport.fetch_ca_certs._session
    session2 = client2.transport.fetch_ca_certs._session
    assert session1 != session2
    session1 = client1.transport.get_certificate_revocation_list._session
    session2 = client2.transport.get_certificate_revocation_list._session
    assert session1 != session2
    session1 = client1.transport.list_certificate_revocation_lists._session
    session2 = client2.transport.list_certificate_revocation_lists._session
    assert session1 != session2
    session1 = client1.transport.update_certificate_revocation_list._session
    session2 = client2.transport.update_certificate_revocation_list._session
    assert session1 != session2
    session1 = client1.transport.create_certificate_template._session
    session2 = client2.transport.create_certificate_template._session
    assert session1 != session2
    session1 = client1.transport.delete_certificate_template._session
    session2 = client2.transport.delete_certificate_template._session
    assert session1 != session2
    session1 = client1.transport.get_certificate_template._session
    session2 = client2.transport.get_certificate_template._session
    assert session1 != session2
    session1 = client1.transport.list_certificate_templates._session
    session2 = client2.transport.list_certificate_templates._session
    assert session1 != session2
    session1 = client1.transport.update_certificate_template._session
    session2 = client2.transport.update_certificate_template._session
    assert session1 != session2


def test_certificate_authority_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.CertificateAuthorityServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_certificate_authority_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.CertificateAuthorityServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.CertificateAuthorityServiceGrpcTransport,
        transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
    ],
)
def test_certificate_authority_service_transport_channel_mtls_with_client_cert_source(
    transport_class,
):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, "default") as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.CertificateAuthorityServiceGrpcTransport,
        transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
    ],
)
def test_certificate_authority_service_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_certificate_authority_service_grpc_lro_client():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_certificate_authority_service_grpc_lro_async_client():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc_asyncio",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsAsyncClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_ca_pool_path():
    project = "squid"
    location = "clam"
    ca_pool = "whelk"
    expected = "projects/{project}/locations/{location}/caPools/{ca_pool}".format(
        project=project,
        location=location,
        ca_pool=ca_pool,
    )
    actual = CertificateAuthorityServiceClient.ca_pool_path(project, location, ca_pool)
    assert expected == actual


def test_parse_ca_pool_path():
    expected = {
        "project": "octopus",
        "location": "oyster",
        "ca_pool": "nudibranch",
    }
    path = CertificateAuthorityServiceClient.ca_pool_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_ca_pool_path(path)
    assert expected == actual


def test_certificate_path():
    project = "cuttlefish"
    location = "mussel"
    ca_pool = "winkle"
    certificate = "nautilus"
    expected = "projects/{project}/locations/{location}/caPools/{ca_pool}/certificates/{certificate}".format(
        project=project,
        location=location,
        ca_pool=ca_pool,
        certificate=certificate,
    )
    actual = CertificateAuthorityServiceClient.certificate_path(
        project, location, ca_pool, certificate
    )
    assert expected == actual


def test_parse_certificate_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
        "ca_pool": "squid",
        "certificate": "clam",
    }
    path = CertificateAuthorityServiceClient.certificate_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_certificate_path(path)
    assert expected == actual


def test_certificate_authority_path():
    project = "whelk"
    location = "octopus"
    ca_pool = "oyster"
    certificate_authority = "nudibranch"
    expected = "projects/{project}/locations/{location}/caPools/{ca_pool}/certificateAuthorities/{certificate_authority}".format(
        project=project,
        location=location,
        ca_pool=ca_pool,
        certificate_authority=certificate_authority,
    )
    actual = CertificateAuthorityServiceClient.certificate_authority_path(
        project, location, ca_pool, certificate_authority
    )
    assert expected == actual


def test_parse_certificate_authority_path():
    expected = {
        "project": "cuttlefish",
        "location": "mussel",
        "ca_pool": "winkle",
        "certificate_authority": "nautilus",
    }
    path = CertificateAuthorityServiceClient.certificate_authority_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_certificate_authority_path(path)
    assert expected == actual


def test_certificate_revocation_list_path():
    project = "scallop"
    location = "abalone"
    ca_pool = "squid"
    certificate_authority = "clam"
    certificate_revocation_list = "whelk"
    expected = "projects/{project}/locations/{location}/caPools/{ca_pool}/certificateAuthorities/{certificate_authority}/certificateRevocationLists/{certificate_revocation_list}".format(
        project=project,
        location=location,
        ca_pool=ca_pool,
        certificate_authority=certificate_authority,
        certificate_revocation_list=certificate_revocation_list,
    )
    actual = CertificateAuthorityServiceClient.certificate_revocation_list_path(
        project, location, ca_pool, certificate_authority, certificate_revocation_list
    )
    assert expected == actual


def test_parse_certificate_revocation_list_path():
    expected = {
        "project": "octopus",
        "location": "oyster",
        "ca_pool": "nudibranch",
        "certificate_authority": "cuttlefish",
        "certificate_revocation_list": "mussel",
    }
    path = CertificateAuthorityServiceClient.certificate_revocation_list_path(
        **expected
    )

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_certificate_revocation_list_path(
        path
    )
    assert expected == actual


def test_certificate_template_path():
    project = "winkle"
    location = "nautilus"
    certificate_template = "scallop"
    expected = "projects/{project}/locations/{location}/certificateTemplates/{certificate_template}".format(
        project=project,
        location=location,
        certificate_template=certificate_template,
    )
    actual = CertificateAuthorityServiceClient.certificate_template_path(
        project, location, certificate_template
    )
    assert expected == actual


def test_parse_certificate_template_path():
    expected = {
        "project": "abalone",
        "location": "squid",
        "certificate_template": "clam",
    }
    path = CertificateAuthorityServiceClient.certificate_template_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_certificate_template_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "whelk"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = CertificateAuthorityServiceClient.common_billing_account_path(
        billing_account
    )
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "octopus",
    }
    path = CertificateAuthorityServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "oyster"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = CertificateAuthorityServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nudibranch",
    }
    path = CertificateAuthorityServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "cuttlefish"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = CertificateAuthorityServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "mussel",
    }
    path = CertificateAuthorityServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "winkle"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = CertificateAuthorityServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nautilus",
    }
    path = CertificateAuthorityServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "scallop"
    location = "abalone"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = CertificateAuthorityServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "squid",
        "location": "clam",
    }
    path = CertificateAuthorityServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = CertificateAuthorityServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.CertificateAuthorityServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = CertificateAuthorityServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.CertificateAuthorityServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = CertificateAuthorityServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


@pytest.mark.asyncio
async def test_transport_close_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc_asyncio",
    )
    with mock.patch.object(
        type(getattr(client.transport, "grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_get_location_rest_bad_request(
    transport: str = "rest", request_type=locations_pb2.GetLocationRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/locations/sample2"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_location(request)


@pytest.mark.parametrize(
    "request_type",
    [
        locations_pb2.GetLocationRequest,
        dict,
    ],
)
def test_get_location_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"name": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = locations_pb2.Location()

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.get_location(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)


def test_list_locations_rest_bad_request(
    transport: str = "rest", request_type=locations_pb2.ListLocationsRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict({"name": "projects/sample1"}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_locations(request)


@pytest.mark.parametrize(
    "request_type",
    [
        locations_pb2.ListLocationsRequest,
        dict,
    ],
)
def test_list_locations_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"name": "projects/sample1"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = locations_pb2.ListLocationsResponse()

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.list_locations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)


def test_get_iam_policy_rest_bad_request(
    transport: str = "rest", request_type=iam_policy_pb2.GetIamPolicyRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict(
        {"resource": "projects/sample1/locations/sample2/caPools/sample3"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_iam_policy(request)


@pytest.mark.parametrize(
    "request_type",
    [
        iam_policy_pb2.GetIamPolicyRequest,
        dict,
    ],
)
def test_get_iam_policy_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"resource": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = policy_pb2.Policy()

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.get_iam_policy(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)


def test_set_iam_policy_rest_bad_request(
    transport: str = "rest", request_type=iam_policy_pb2.SetIamPolicyRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict(
        {"resource": "projects/sample1/locations/sample2/caPools/sample3"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.set_iam_policy(request)


@pytest.mark.parametrize(
    "request_type",
    [
        iam_policy_pb2.SetIamPolicyRequest,
        dict,
    ],
)
def test_set_iam_policy_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"resource": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = policy_pb2.Policy()

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.set_iam_policy(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)


def test_test_iam_permissions_rest_bad_request(
    transport: str = "rest", request_type=iam_policy_pb2.TestIamPermissionsRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict(
        {"resource": "projects/sample1/locations/sample2/caPools/sample3"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.test_iam_permissions(request)


@pytest.mark.parametrize(
    "request_type",
    [
        iam_policy_pb2.TestIamPermissionsRequest,
        dict,
    ],
)
def test_test_iam_permissions_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"resource": "projects/sample1/locations/sample2/caPools/sample3"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = iam_policy_pb2.TestIamPermissionsResponse()

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.test_iam_permissions(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)


def test_cancel_operation_rest_bad_request(
    transport: str = "rest", request_type=operations_pb2.CancelOperationRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/locations/sample2/operations/sample3"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.cancel_operation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.CancelOperationRequest,
        dict,
    ],
)
def test_cancel_operation_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"name": "projects/sample1/locations/sample2/operations/sample3"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = "{}"

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.cancel_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_operation_rest_bad_request(
    transport: str = "rest", request_type=operations_pb2.DeleteOperationRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/locations/sample2/operations/sample3"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.delete_operation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.DeleteOperationRequest,
        dict,
    ],
)
def test_delete_operation_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"name": "projects/sample1/locations/sample2/operations/sample3"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = "{}"

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.delete_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None


def test_get_operation_rest_bad_request(
    transport: str = "rest", request_type=operations_pb2.GetOperationRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/locations/sample2/operations/sample3"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_operation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.GetOperationRequest,
        dict,
    ],
)
def test_get_operation_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"name": "projects/sample1/locations/sample2/operations/sample3"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation()

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.get_operation(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)


def test_list_operations_rest_bad_request(
    transport: str = "rest", request_type=operations_pb2.ListOperationsRequest
):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/locations/sample2"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_operations(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.ListOperationsRequest,
        dict,
    ],
)
def test_list_operations_rest(request_type):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request_init = {"name": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.ListOperationsResponse()

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.list_operations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.ListOperationsResponse)


def test_delete_operation(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.DeleteOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_delete_operation_async(transport: str = "grpc"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.DeleteOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_operation_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.DeleteOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        call.return_value = None

        client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_operation_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.DeleteOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


def test_delete_operation_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        response = client.delete_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_delete_operation_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_cancel_operation(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.CancelOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_cancel_operation_async(transport: str = "grpc"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.CancelOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_cancel_operation_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.CancelOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        call.return_value = None

        client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_cancel_operation_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.CancelOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


def test_cancel_operation_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        response = client.cancel_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_cancel_operation_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.cancel_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_get_operation(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.GetOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation()
        response = client.get_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)


@pytest.mark.asyncio
async def test_get_operation_async(transport: str = "grpc"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.GetOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation()
        )
        response = await client.get_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)


def test_get_operation_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.GetOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        call.return_value = operations_pb2.Operation()

        client.get_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_operation_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.GetOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation()
        )
        await client.get_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


def test_get_operation_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation()

        response = client.get_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_get_operation_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation()
        )
        response = await client.get_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_list_operations(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.ListOperationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.ListOperationsResponse()
        response = client.list_operations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.ListOperationsResponse)


@pytest.mark.asyncio
async def test_list_operations_async(transport: str = "grpc"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.ListOperationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.ListOperationsResponse()
        )
        response = await client.list_operations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.ListOperationsResponse)


def test_list_operations_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.ListOperationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        call.return_value = operations_pb2.ListOperationsResponse()

        client.list_operations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_operations_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.ListOperationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.ListOperationsResponse()
        )
        await client.list_operations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


def test_list_operations_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.ListOperationsResponse()

        response = client.list_operations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_list_operations_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.ListOperationsResponse()
        )
        response = await client.list_operations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_list_locations(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.ListLocationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.ListLocationsResponse()
        response = client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)


@pytest.mark.asyncio
async def test_list_locations_async(transport: str = "grpc"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.ListLocationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        response = await client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)


def test_list_locations_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.ListLocationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        call.return_value = locations_pb2.ListLocationsResponse()

        client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_locations_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.ListLocationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        await client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


def test_list_locations_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.ListLocationsResponse()

        response = client.list_locations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_list_locations_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        response = await client.list_locations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_get_location(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.GetLocationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.Location()
        response = client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)


@pytest.mark.asyncio
async def test_get_location_async(transport: str = "grpc_asyncio"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.GetLocationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        response = await client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)


def test_get_location_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.GetLocationRequest()
    request.name = "locations/abc"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        call.return_value = locations_pb2.Location()

        client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations/abc",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_location_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.GetLocationRequest()
    request.name = "locations/abc"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        await client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations/abc",
    ) in kw["metadata"]


def test_get_location_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.Location()

        response = client.get_location(
            request={
                "name": "locations/abc",
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_get_location_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        response = await client.get_location(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_set_iam_policy(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.SetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy(
            version=774,
            etag=b"etag_blob",
        )
        response = client.set_iam_policy(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


@pytest.mark.asyncio
async def test_set_iam_policy_async(transport: str = "grpc_asyncio"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.SetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy(
                version=774,
                etag=b"etag_blob",
            )
        )
        response = await client.set_iam_policy(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


def test_set_iam_policy_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.SetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        call.return_value = policy_pb2.Policy()

        client.set_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "resource=resource/value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_set_iam_policy_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.SetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(policy_pb2.Policy())

        await client.set_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "resource=resource/value",
    ) in kw["metadata"]


def test_set_iam_policy_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        response = client.set_iam_policy(
            request={
                "resource": "resource_value",
                "policy": policy_pb2.Policy(version=774),
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_set_iam_policy_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(policy_pb2.Policy())

        response = await client.set_iam_policy(
            request={
                "resource": "resource_value",
                "policy": policy_pb2.Policy(version=774),
            }
        )
        call.assert_called()


def test_get_iam_policy(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.GetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy(
            version=774,
            etag=b"etag_blob",
        )

        response = client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


@pytest.mark.asyncio
async def test_get_iam_policy_async(transport: str = "grpc_asyncio"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.GetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy(
                version=774,
                etag=b"etag_blob",
            )
        )

        response = await client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


def test_get_iam_policy_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.GetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        call.return_value = policy_pb2.Policy()

        client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "resource=resource/value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_iam_policy_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.GetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(policy_pb2.Policy())

        await client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "resource=resource/value",
    ) in kw["metadata"]


def test_get_iam_policy_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        response = client.get_iam_policy(
            request={
                "resource": "resource_value",
                "options": options_pb2.GetPolicyOptions(requested_policy_version=2598),
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_get_iam_policy_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(policy_pb2.Policy())

        response = await client.get_iam_policy(
            request={
                "resource": "resource_value",
                "options": options_pb2.GetPolicyOptions(requested_policy_version=2598),
            }
        )
        call.assert_called()


def test_test_iam_permissions(transport: str = "grpc"):
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.TestIamPermissionsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse(
            permissions=["permissions_value"],
        )

        response = client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)

    assert response.permissions == ["permissions_value"]


@pytest.mark.asyncio
async def test_test_iam_permissions_async(transport: str = "grpc_asyncio"):
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.TestIamPermissionsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse(
                permissions=["permissions_value"],
            )
        )

        response = await client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)

    assert response.permissions == ["permissions_value"]


def test_test_iam_permissions_field_headers():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.TestIamPermissionsRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse()

        client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "resource=resource/value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_test_iam_permissions_field_headers_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.TestIamPermissionsRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse()
        )

        await client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "resource=resource/value",
    ) in kw["metadata"]


def test_test_iam_permissions_from_dict():
    client = CertificateAuthorityServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse()

        response = client.test_iam_permissions(
            request={
                "resource": "resource_value",
                "permissions": ["permissions_value"],
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_test_iam_permissions_from_dict_async():
    client = CertificateAuthorityServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse()
        )

        response = await client.test_iam_permissions(
            request={
                "resource": "resource_value",
                "permissions": ["permissions_value"],
            }
        )
        call.assert_called()


def test_transport_close():
    transports = {
        "rest": "_session",
        "grpc": "_grpc_channel",
    }

    for transport, close_name in transports.items():
        client = CertificateAuthorityServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        with mock.patch.object(
            type(getattr(client.transport, close_name)), "close"
        ) as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()


def test_client_ctx():
    transports = [
        "rest",
        "grpc",
    ]
    for transport in transports:
        client = CertificateAuthorityServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()


@pytest.mark.parametrize(
    "client_class,transport_class",
    [
        (
            CertificateAuthorityServiceClient,
            transports.CertificateAuthorityServiceGrpcTransport,
        ),
        (
            CertificateAuthorityServiceAsyncClient,
            transports.CertificateAuthorityServiceGrpcAsyncIOTransport,
        ),
    ],
)
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )
