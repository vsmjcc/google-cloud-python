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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1beta",
    manifest={
        "Form",
        "OutdatedLibrary",
        "ViolatingResource",
        "VulnerableParameters",
        "VulnerableHeaders",
        "Xss",
    },
)


class Form(proto.Message):
    r"""! Information about a vulnerability with an HTML.

    Attributes:
        action_uri (str):
            ! The URI where to send the form when it's
            submitted.
        fields (MutableSequence[str]):
            ! The names of form fields related to the
            vulnerability.
    """

    action_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class OutdatedLibrary(proto.Message):
    r"""Information reported for an outdated library.

    Attributes:
        library_name (str):
            The name of the outdated library.
        version (str):
            The version number.
        learn_more_urls (MutableSequence[str]):
            URLs to learn more information about the
            vulnerabilities in the library.
    """

    library_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    learn_more_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ViolatingResource(proto.Message):
    r"""Information regarding any resource causing the vulnerability
    such as JavaScript sources, image, audio files, etc.

    Attributes:
        content_type (str):
            The MIME type of this resource.
        resource_url (str):
            URL of this violating resource.
    """

    content_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_url: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VulnerableParameters(proto.Message):
    r"""Information about vulnerable request parameters.

    Attributes:
        parameter_names (MutableSequence[str]):
            The vulnerable parameter names.
    """

    parameter_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class VulnerableHeaders(proto.Message):
    r"""Information about vulnerable or missing HTTP Headers.

    Attributes:
        headers (MutableSequence[google.cloud.websecurityscanner_v1beta.types.VulnerableHeaders.Header]):
            List of vulnerable headers.
        missing_headers (MutableSequence[google.cloud.websecurityscanner_v1beta.types.VulnerableHeaders.Header]):
            List of missing headers.
    """

    class Header(proto.Message):
        r"""Describes a HTTP Header.

        Attributes:
            name (str):
                Header name.
            value (str):
                Header value.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )

    headers: MutableSequence[Header] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Header,
    )
    missing_headers: MutableSequence[Header] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Header,
    )


class Xss(proto.Message):
    r"""Information reported for an XSS.

    Attributes:
        stack_traces (MutableSequence[str]):
            Stack traces leading to the point where the
            XSS occurred.
        error_message (str):
            An error message generated by a javascript
            breakage.
    """

    stack_traces: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
