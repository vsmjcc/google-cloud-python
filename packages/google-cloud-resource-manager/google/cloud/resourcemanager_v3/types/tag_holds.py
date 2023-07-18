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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.resourcemanager.v3",
    manifest={
        "TagHold",
        "CreateTagHoldRequest",
        "CreateTagHoldMetadata",
        "DeleteTagHoldRequest",
        "DeleteTagHoldMetadata",
        "ListTagHoldsRequest",
        "ListTagHoldsResponse",
    },
)


class TagHold(proto.Message):
    r"""A TagHold represents the use of a TagValue that is not captured by
    TagBindings. If a TagValue has any TagHolds, deletion will be
    blocked. This resource is intended to be created in the same cloud
    location as the ``holder``.

    Attributes:
        name (str):
            Output only. The resource name of a TagHold. This is a
            String of the form:
            ``tagValues/{tag-value-id}/tagHolds/{tag-hold-id}`` (e.g.
            ``tagValues/123/tagHolds/456``). This resource name is
            generated by the server.
        holder (str):
            Required. The name of the resource where the TagValue is
            being used. Must be less than 200 characters. E.g.
            ``//compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group``
        origin (str):
            Optional. An optional string representing the origin of this
            request. This field should include human-understandable
            information to distinguish origins from each other. Must be
            less than 200 characters. E.g. ``migs-35678234``
        help_link (str):
            Optional. A URL where an end user can learn more about
            removing this hold. E.g.
            ``https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this TagHold was
            created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    holder: str = proto.Field(
        proto.STRING,
        number=2,
    )
    origin: str = proto.Field(
        proto.STRING,
        number=3,
    )
    help_link: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class CreateTagHoldRequest(proto.Message):
    r"""The request message to create a TagHold.

    Attributes:
        parent (str):
            Required. The resource name of the TagHold's parent
            TagValue. Must be of the form: ``tagValues/{tag-value-id}``.
        tag_hold (google.cloud.resourcemanager_v3.types.TagHold):
            Required. The TagHold to be created.
        validate_only (bool):
            Optional. Set to true to perform the
            validations necessary for creating the resource,
            but not actually perform the action.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag_hold: "TagHold" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TagHold",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CreateTagHoldMetadata(proto.Message):
    r"""Runtime operation information for creating a TagHold.
    (-- The metadata is currently empty, but may include information
    in the future. --)

    """


class DeleteTagHoldRequest(proto.Message):
    r"""The request message to delete a TagHold.

    Attributes:
        name (str):
            Required. The resource name of the TagHold to delete. Must
            be of the form:
            ``tagValues/{tag-value-id}/tagHolds/{tag-hold-id}``.
        validate_only (bool):
            Optional. Set to true to perform the
            validations necessary for deleting the resource,
            but not actually perform the action.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class DeleteTagHoldMetadata(proto.Message):
    r"""Runtime operation information for deleting a TagHold.
    (-- The metadata is currently empty, but may include information
    in the future. --)

    """


class ListTagHoldsRequest(proto.Message):
    r"""The request message for listing the TagHolds under a
    TagValue.

    Attributes:
        parent (str):
            Required. The resource name of the parent TagValue. Must be
            of the form: ``tagValues/{tag-value-id}``.
        page_size (int):
            Optional. The maximum number of TagHolds to
            return in the response. The server allows a
            maximum of 300 TagHolds to return. If
            unspecified, the server will use 100 as the
            default.
        page_token (str):
            Optional. A pagination token returned from a previous call
            to ``ListTagHolds`` that indicates where this listing should
            continue from.
        filter (str):
            Optional. Criteria used to select a subset of TagHolds
            parented by the TagValue to return. This field follows the
            syntax defined by aip.dev/160; the ``holder`` and ``origin``
            fields are supported for filtering. Currently only ``AND``
            syntax is supported. Some example queries are:

            -  ``holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group``
            -  ``origin = 35678234``
            -  ``holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group AND origin = 35678234``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListTagHoldsResponse(proto.Message):
    r"""The ListTagHolds response.

    Attributes:
        tag_holds (MutableSequence[google.cloud.resourcemanager_v3.types.TagHold]):
            A possibly paginated list of TagHolds.
        next_page_token (str):
            Pagination token.

            If the result set is too large to fit in a single response,
            this token is returned. It encodes the position of the
            current result cursor. Feeding this value into a new list
            request with the ``page_token`` parameter gives the next
            page of the results.

            When ``next_page_token`` is not filled in, there is no next
            page and the list returned is the last page in the result
            set.

            Pagination tokens have a limited lifetime.
    """

    @property
    def raw_page(self):
        return self

    tag_holds: MutableSequence["TagHold"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TagHold",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
