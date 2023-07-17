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

import proto  # type: ignore

from google.cloud.netapp_v1beta1.types import common
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.netapp.v1beta1',
    manifest={
        'Protocols',
        'AccessType',
        'SMBSettings',
        'SecurityStyle',
        'ListVolumesRequest',
        'ListVolumesResponse',
        'GetVolumeRequest',
        'CreateVolumeRequest',
        'UpdateVolumeRequest',
        'DeleteVolumeRequest',
        'RevertVolumeRequest',
        'Volume',
        'ExportPolicy',
        'SimpleExportPolicyRule',
        'SnapshotPolicy',
        'HourlySchedule',
        'DailySchedule',
        'WeeklySchedule',
        'MonthlySchedule',
        'MountOption',
        'RestoreParameters',
    },
)


class Protocols(proto.Enum):
    r"""Protocols
    The protocols

    Values:
        PROTOCOLS_UNSPECIFIED (0):
            Unspecified protocol
        NFSV3 (1):
            NFS V3 protocol
        NFSV4 (2):
            NFS V4 protocol
        SMB (3):
            SMB protocol
    """
    PROTOCOLS_UNSPECIFIED = 0
    NFSV3 = 1
    NFSV4 = 2
    SMB = 3


class AccessType(proto.Enum):
    r"""AccessType
    The access types

    Values:
        ACCESS_TYPE_UNSPECIFIED (0):
            Unspecified Access Type
        READ_ONLY (1):
            Read Only
        READ_WRITE (2):
            Read Write
        READ_NONE (3):
            None
    """
    ACCESS_TYPE_UNSPECIFIED = 0
    READ_ONLY = 1
    READ_WRITE = 2
    READ_NONE = 3


class SMBSettings(proto.Enum):
    r"""SMBSettings
    Modifies the behaviour of a SMB volume.

    Values:
        SMB_SETTINGS_UNSPECIFIED (0):
            Unspecified default option
        ENCRYPT_DATA (1):
            SMB setting encrypt data
        BROWSABLE (2):
            SMB setting browsable
        CHANGE_NOTIFY (3):
            SMB setting notify change
        NON_BROWSABLE (4):
            SMB setting not to notify change
        OPLOCKS (5):
            SMB setting oplocks
        SHOW_SNAPSHOT (6):
            SMB setting to show snapshots
        SHOW_PREVIOUS_VERSIONS (7):
            SMB setting to show previous versions
        ACCESS_BASED_ENUMERATION (8):
            SMB setting to access volume based on
            enumerartion
        CONTINUOUSLY_AVAILABLE (9):
            Continuously available enumeration
    """
    SMB_SETTINGS_UNSPECIFIED = 0
    ENCRYPT_DATA = 1
    BROWSABLE = 2
    CHANGE_NOTIFY = 3
    NON_BROWSABLE = 4
    OPLOCKS = 5
    SHOW_SNAPSHOT = 6
    SHOW_PREVIOUS_VERSIONS = 7
    ACCESS_BASED_ENUMERATION = 8
    CONTINUOUSLY_AVAILABLE = 9


class SecurityStyle(proto.Enum):
    r"""The security style of the volume, can be either UNIX or NTFS.

    Values:
        SECURITY_STYLE_UNSPECIFIED (0):
            SecurityStyle is unspecified
        NTFS (1):
            SecurityStyle uses NTFS
        UNIX (2):
            SecurityStyle uses NTFS
    """
    SECURITY_STYLE_UNSPECIFIED = 0
    NTFS = 1
    UNIX = 2


class ListVolumesRequest(proto.Message):
    r"""ListVolumesRequest
    Message for requesting list of Volumes

    Attributes:
        parent (str):
            Required. Parent value for ListVolumesRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, the server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListVolumesResponse(proto.Message):
    r"""ListVolumesResponse
    Message for response to listing Volumes

    Attributes:
        volumes (MutableSequence[google.cloud.netapp_v1beta1.types.Volume]):
            The list of Volume
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    volumes: MutableSequence['Volume'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Volume',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetVolumeRequest(proto.Message):
    r"""GetVolumeRequest
    Message for getting a Volume

    Attributes:
        name (str):
            Required. Name of the volume
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateVolumeRequest(proto.Message):
    r"""CreateVolumeRequest
    Message for creating a Volume

    Attributes:
        parent (str):
            Required. Value for parent.
        volume_id (str):
            Required. Id of the requesting volume If auto-generating Id
            server-side, remove this field and Id from the
            method_signature of Create RPC
        volume (google.cloud.netapp_v1beta1.types.Volume):
            Required. The volume being created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    volume_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    volume: 'Volume' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Volume',
    )


class UpdateVolumeRequest(proto.Message):
    r"""UpdateVolumeRequest
    Message for updating a Volume

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Volume resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        volume (google.cloud.netapp_v1beta1.types.Volume):
            Required. The volume being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    volume: 'Volume' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Volume',
    )


class DeleteVolumeRequest(proto.Message):
    r"""DeleteVolumeRequest
    Message for deleting a Volume

    Attributes:
        name (str):
            Required. Name of the volume
        force (bool):
            If this field is set as true, CCFE will not
            block the volume resource deletion even if it
            has any snapshots resource. (Otherwise, the
            request will only work if the volume has no
            snapshots.)
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class RevertVolumeRequest(proto.Message):
    r"""RevertVolumeRequest reverts the given volume to the
    specified snapshot.

    Attributes:
        name (str):
            Required. The resource name of the volume, in the format of
            projects/{project_id}/locations/{location}/volumes/{volume_id}.
        snapshot_id (str):
            Required. The snapshot resource ID, in the format
            'my-snapshot', where the specified ID is the {snapshot_id}
            of the fully qualified name like
            projects/{project_id}/locations/{location_id}/volumes/{volume_id}/snapshots/{snapshot_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snapshot_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Volume(proto.Message):
    r"""Volume
    Volume provides a filesystem that you can mount.

    Attributes:
        name (str):
            Output only. Name of the volume
        state (google.cloud.netapp_v1beta1.types.Volume.State):
            Output only. State of the volume
        state_details (str):
            Output only. State details of the volume
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the volume
        share_name (str):
            Required. Share name of the volume
        psa_range (str):
            Output only. Name of the Private Service
            Access allocated range. This is optional. If not
            provided, any available range will be chosen.
        storage_pool (str):
            Required. StoragePool name of the volume
        network (str):
            Output only. VPC Network name.
            Format:
            projects/{project}/global/networks/{network}
        service_level (google.cloud.netapp_v1beta1.types.ServiceLevel):
            Output only. Service level of the volume
        capacity_gib (int):
            Required. Capacity in GIB of the volume
        export_policy (google.cloud.netapp_v1beta1.types.ExportPolicy):
            Optional. Export policy of the volume
        protocols (MutableSequence[google.cloud.netapp_v1beta1.types.Protocols]):
            Required. Protocols required for the volume
        smb_settings (MutableSequence[google.cloud.netapp_v1beta1.types.SMBSettings]):
            Optional. SMB share settings for the volume.
        mount_options (MutableSequence[google.cloud.netapp_v1beta1.types.MountOption]):
            Output only. Mount options of this volume
        unix_permissions (str):
            Optional. Default unix style permission (e.g.
            777) the mount point will be created with.
            Applicable for NFS protocol types only.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        description (str):
            Optional. Description of the volume
        snapshot_policy (google.cloud.netapp_v1beta1.types.SnapshotPolicy):
            Optional. SnapshotPolicy for a volume.
        snap_reserve (float):
            Optional. Snap_reserve specifies percentage of volume
            storage reserved for snapshot storage. Default is 0 percent.
        snapshot_directory (bool):
            Optional. Snapshot_directory if enabled (true) the volume
            will contain a read-only .snapshot directory which provides
            access to each of the volume's snapshots.
        used_gib (int):
            Output only. Used capacity in GIB of the
            volume. This is computed periodically and it
            does not represent the realtime usage.
        security_style (google.cloud.netapp_v1beta1.types.SecurityStyle):
            Optional. Security Style of the Volume
        kerberos_enabled (bool):
            Optional. Flag indicating if the volume is a
            kerberos volume or not, export policy rules
            control kerberos security modes (krb5, krb5i,
            krb5p).
        ldap_enabled (bool):
            Output only. Flag indicating if the volume is
            NFS LDAP enabled or not.
        active_directory (str):
            Output only. Specifies the ActiveDirectory
            name of a SMB volume.
        restore_parameters (google.cloud.netapp_v1beta1.types.RestoreParameters):
            Optional. Specifies the source of the volume
            to be created from.
        kms_config (str):
            Output only. Specifies the KMS config to be
            used for volume encryption.
        encryption_type (google.cloud.netapp_v1beta1.types.EncryptionType):
            Output only. Specified the current volume
            encryption key source.
        has_replication (bool):
            Output only. Indicates whether the volume is
            part of a replication relationship.
    """
    class State(proto.Enum):
        r"""The volume states

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified Volume State
            READY (1):
                Volume State is Ready
            CREATING (2):
                Volume State is Creating
            DELETING (3):
                Volume State is Deleting
            UPDATING (4):
                Volume State is Updating
            RESTORING (5):
                Volume State is Restoring
            DISABLED (6):
                Volume State is Disabled
            ERROR (7):
                Volume State is Error
        """
        STATE_UNSPECIFIED = 0
        READY = 1
        CREATING = 2
        DELETING = 3
        UPDATING = 4
        RESTORING = 5
        DISABLED = 6
        ERROR = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    share_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    psa_range: str = proto.Field(
        proto.STRING,
        number=6,
    )
    storage_pool: str = proto.Field(
        proto.STRING,
        number=7,
    )
    network: str = proto.Field(
        proto.STRING,
        number=8,
    )
    service_level: common.ServiceLevel = proto.Field(
        proto.ENUM,
        number=9,
        enum=common.ServiceLevel,
    )
    capacity_gib: int = proto.Field(
        proto.INT64,
        number=10,
    )
    export_policy: 'ExportPolicy' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='ExportPolicy',
    )
    protocols: MutableSequence['Protocols'] = proto.RepeatedField(
        proto.ENUM,
        number=12,
        enum='Protocols',
    )
    smb_settings: MutableSequence['SMBSettings'] = proto.RepeatedField(
        proto.ENUM,
        number=13,
        enum='SMBSettings',
    )
    mount_options: MutableSequence['MountOption'] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message='MountOption',
    )
    unix_permissions: str = proto.Field(
        proto.STRING,
        number=15,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    description: str = proto.Field(
        proto.STRING,
        number=17,
    )
    snapshot_policy: 'SnapshotPolicy' = proto.Field(
        proto.MESSAGE,
        number=18,
        message='SnapshotPolicy',
    )
    snap_reserve: float = proto.Field(
        proto.DOUBLE,
        number=19,
    )
    snapshot_directory: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    used_gib: int = proto.Field(
        proto.INT64,
        number=21,
    )
    security_style: 'SecurityStyle' = proto.Field(
        proto.ENUM,
        number=22,
        enum='SecurityStyle',
    )
    kerberos_enabled: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    ldap_enabled: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    active_directory: str = proto.Field(
        proto.STRING,
        number=25,
    )
    restore_parameters: 'RestoreParameters' = proto.Field(
        proto.MESSAGE,
        number=26,
        message='RestoreParameters',
    )
    kms_config: str = proto.Field(
        proto.STRING,
        number=27,
    )
    encryption_type: common.EncryptionType = proto.Field(
        proto.ENUM,
        number=28,
        enum=common.EncryptionType,
    )
    has_replication: bool = proto.Field(
        proto.BOOL,
        number=29,
    )


class ExportPolicy(proto.Message):
    r"""ExportPolicy
    Defined the export policy for the volume.

    Attributes:
        rules (MutableSequence[google.cloud.netapp_v1beta1.types.SimpleExportPolicyRule]):
            Required. List of export policy rules
    """

    rules: MutableSequence['SimpleExportPolicyRule'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='SimpleExportPolicyRule',
    )


class SimpleExportPolicyRule(proto.Message):
    r"""SimpleExportPolicyRule
    An export policy rule describing various export options.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        allowed_clients (str):
            Comma separated list of allowed clients IP
            addresses

            This field is a member of `oneof`_ ``_allowed_clients``.
        has_root_access (str):
            Whether Unix root access will be granted.

            This field is a member of `oneof`_ ``_has_root_access``.
        access_type (google.cloud.netapp_v1beta1.types.AccessType):
            Access type (ReadWrite, ReadOnly, None)

            This field is a member of `oneof`_ ``_access_type``.
        nfsv3 (bool):
            NFS V3 protocol.

            This field is a member of `oneof`_ ``_nfsv3``.
        nfsv4 (bool):
            NFS V4 protocol.

            This field is a member of `oneof`_ ``_nfsv4``.
        kerberos_5_read_only (bool):
            If enabled (true) the rule defines a read
            only access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'authentication' kerberos
            security mode.

            This field is a member of `oneof`_ ``_kerberos_5_read_only``.
        kerberos_5_read_write (bool):
            If enabled (true) the rule defines read and
            write access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'authentication' kerberos
            security mode. The 'kerberos5ReadOnly' value be
            ignored if this is enabled.

            This field is a member of `oneof`_ ``_kerberos_5_read_write``.
        kerberos_5i_read_only (bool):
            If enabled (true) the rule defines a read
            only access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'integrity' kerberos
            security mode.

            This field is a member of `oneof`_ ``_kerberos_5i_read_only``.
        kerberos_5i_read_write (bool):
            If enabled (true) the rule defines read and
            write access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'integrity' kerberos
            security mode. The 'kerberos5iReadOnly' value be
            ignored if this is enabled.

            This field is a member of `oneof`_ ``_kerberos_5i_read_write``.
        kerberos_5p_read_only (bool):
            If enabled (true) the rule defines a read
            only access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'privacy' kerberos
            security mode.

            This field is a member of `oneof`_ ``_kerberos_5p_read_only``.
        kerberos_5p_read_write (bool):
            If enabled (true) the rule defines read and
            write access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'privacy' kerberos
            security mode. The 'kerberos5pReadOnly' value be
            ignored if this is enabled.

            This field is a member of `oneof`_ ``_kerberos_5p_read_write``.
    """

    allowed_clients: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    has_root_access: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    access_type: 'AccessType' = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum='AccessType',
    )
    nfsv3: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    nfsv4: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    kerberos_5_read_only: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    kerberos_5_read_write: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    kerberos_5i_read_only: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    kerberos_5i_read_write: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    kerberos_5p_read_only: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    kerberos_5p_read_write: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )


class SnapshotPolicy(proto.Message):
    r"""Snapshot Policy for a volume.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enabled (bool):
            If enabled, make snapshots automatically
            according to the schedules. Default is false.

            This field is a member of `oneof`_ ``_enabled``.
        hourly_schedule (google.cloud.netapp_v1beta1.types.HourlySchedule):
            Hourly schedule policy.

            This field is a member of `oneof`_ ``_hourly_schedule``.
        daily_schedule (google.cloud.netapp_v1beta1.types.DailySchedule):
            Daily schedule policy.

            This field is a member of `oneof`_ ``_daily_schedule``.
        weekly_schedule (google.cloud.netapp_v1beta1.types.WeeklySchedule):
            Weekly schedule policy.

            This field is a member of `oneof`_ ``_weekly_schedule``.
        monthly_schedule (google.cloud.netapp_v1beta1.types.MonthlySchedule):
            Monthly schedule policy.

            This field is a member of `oneof`_ ``_monthly_schedule``.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    hourly_schedule: 'HourlySchedule' = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message='HourlySchedule',
    )
    daily_schedule: 'DailySchedule' = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message='DailySchedule',
    )
    weekly_schedule: 'WeeklySchedule' = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message='WeeklySchedule',
    )
    monthly_schedule: 'MonthlySchedule' = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message='MonthlySchedule',
    )


class HourlySchedule(proto.Message):
    r"""Make a snapshot every hour e.g. at 04:00, 05:00, 06:00.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snapshots_to_keep (float):
            The maximum number of Snapshots to keep for
            the hourly schedule

            This field is a member of `oneof`_ ``_snapshots_to_keep``.
        minute (float):
            Set the minute of the hour to start the
            snapshot (0-59), defaults to the top of the hour
            (0).

            This field is a member of `oneof`_ ``_minute``.
    """

    snapshots_to_keep: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class DailySchedule(proto.Message):
    r"""Make a snapshot every day e.g. at 04:00, 05:20, 23:50

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snapshots_to_keep (float):
            The maximum number of Snapshots to keep for
            the hourly schedule

            This field is a member of `oneof`_ ``_snapshots_to_keep``.
        minute (float):
            Set the minute of the hour to start the
            snapshot (0-59), defaults to the top of the hour
            (0).

            This field is a member of `oneof`_ ``_minute``.
        hour (float):
            Set the hour to start the snapshot (0-23),
            defaults to midnight (0).

            This field is a member of `oneof`_ ``_hour``.
    """

    snapshots_to_keep: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    hour: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )


class WeeklySchedule(proto.Message):
    r"""Make a snapshot every week e.g. at Monday 04:00, Wednesday
    05:20, Sunday
    23:50


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snapshots_to_keep (float):
            The maximum number of Snapshots to keep for
            the hourly schedule

            This field is a member of `oneof`_ ``_snapshots_to_keep``.
        minute (float):
            Set the minute of the hour to start the
            snapshot (0-59), defaults to the top of the hour
            (0).

            This field is a member of `oneof`_ ``_minute``.
        hour (float):
            Set the hour to start the snapshot (0-23),
            defaults to midnight (0).

            This field is a member of `oneof`_ ``_hour``.
        day (str):
            Set the day or days of the week to make a
            snapshot. Accepts a comma separated days of the
            week. Defaults to 'Sunday'.

            This field is a member of `oneof`_ ``_day``.
    """

    snapshots_to_keep: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    hour: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    day: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class MonthlySchedule(proto.Message):
    r"""Make a snapshot once a month e.g. at 2nd 04:00, 7th 05:20,
    24th 23:50


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snapshots_to_keep (float):
            The maximum number of Snapshots to keep for
            the hourly schedule

            This field is a member of `oneof`_ ``_snapshots_to_keep``.
        minute (float):
            Set the minute of the hour to start the
            snapshot (0-59), defaults to the top of the hour
            (0).

            This field is a member of `oneof`_ ``_minute``.
        hour (float):
            Set the hour to start the snapshot (0-23),
            defaults to midnight (0).

            This field is a member of `oneof`_ ``_hour``.
        days_of_month (str):
            Set the day or days of the month to make a
            snapshot (1-31). Accepts a comma separated
            number of days. Defaults to '1'.

            This field is a member of `oneof`_ ``_days_of_month``.
    """

    snapshots_to_keep: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    hour: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    days_of_month: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class MountOption(proto.Message):
    r"""MountOption
    View only mount options for a volume.

    Attributes:
        export (str):
            Export string
        export_full (str):
            Full export string
        protocol (google.cloud.netapp_v1beta1.types.Protocols):
            Protocol to mount with.
        instructions (str):
            Instructions for mounting
    """

    export: str = proto.Field(
        proto.STRING,
        number=1,
    )
    export_full: str = proto.Field(
        proto.STRING,
        number=2,
    )
    protocol: 'Protocols' = proto.Field(
        proto.ENUM,
        number=3,
        enum='Protocols',
    )
    instructions: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RestoreParameters(proto.Message):
    r"""The RestoreParameters if volume is created from a snapshot or
    backup.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_snapshot (str):
            Full name of the snapshot resource.
            Format:

            projects/{project}/locations/{location}/volumes/{volume}/snapshots/{snapshot}

            This field is a member of `oneof`_ ``source``.
    """

    source_snapshot: str = proto.Field(
        proto.STRING,
        number=1,
        oneof='source',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
