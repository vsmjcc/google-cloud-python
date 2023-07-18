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
from google.cloud.migrationcenter import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.migrationcenter_v1.services.migration_center.async_client import (
    MigrationCenterAsyncClient,
)
from google.cloud.migrationcenter_v1.services.migration_center.client import (
    MigrationCenterClient,
)
from google.cloud.migrationcenter_v1.types.migrationcenter import (
    AddAssetsToGroupRequest,
    AggregateAssetsValuesRequest,
    AggregateAssetsValuesResponse,
    Aggregation,
    AggregationResult,
    Asset,
    AssetFrame,
    AssetList,
    AssetPerformanceData,
    AssetView,
    AwsEc2PlatformDetails,
    AzureVmPlatformDetails,
    BatchDeleteAssetsRequest,
    BatchUpdateAssetsRequest,
    BatchUpdateAssetsResponse,
    BiosDetails,
    CommitmentPlan,
    ComputeEngineMigrationTarget,
    ComputeEnginePreferences,
    ComputeEngineShapeDescriptor,
    CpuUsageSample,
    CreateGroupRequest,
    CreateImportDataFileRequest,
    CreateImportJobRequest,
    CreatePreferenceSetRequest,
    CreateReportConfigRequest,
    CreateReportRequest,
    CreateSourceRequest,
    DailyResourceUsageAggregation,
    DeleteAssetRequest,
    DeleteGroupRequest,
    DeleteImportDataFileRequest,
    DeleteImportJobRequest,
    DeletePreferenceSetRequest,
    DeleteReportConfigRequest,
    DeleteReportRequest,
    DeleteSourceRequest,
    DiskEntry,
    DiskEntryList,
    DiskPartition,
    DiskPartitionList,
    DiskUsageSample,
    ErrorFrame,
    ErrorFrameView,
    ExecutionReport,
    FileValidationReport,
    FitDescriptor,
    Frames,
    FrameViolationEntry,
    FstabEntry,
    FstabEntryList,
    GenericPlatformDetails,
    GetAssetRequest,
    GetErrorFrameRequest,
    GetGroupRequest,
    GetImportDataFileRequest,
    GetImportJobRequest,
    GetPreferenceSetRequest,
    GetReportConfigRequest,
    GetReportRequest,
    GetSettingsRequest,
    GetSourceRequest,
    Group,
    GuestConfigDetails,
    GuestInstalledApplication,
    GuestInstalledApplicationList,
    GuestOsDetails,
    GuestRuntimeDetails,
    HostsEntry,
    HostsEntryList,
    ImportDataFile,
    ImportError,
    ImportJob,
    ImportJobFormat,
    ImportJobView,
    ImportRowError,
    Insight,
    InsightList,
    LicenseType,
    ListAssetsRequest,
    ListAssetsResponse,
    ListErrorFramesRequest,
    ListErrorFramesResponse,
    ListGroupsRequest,
    ListGroupsResponse,
    ListImportDataFilesRequest,
    ListImportDataFilesResponse,
    ListImportJobsRequest,
    ListImportJobsResponse,
    ListPreferenceSetsRequest,
    ListPreferenceSetsResponse,
    ListReportConfigsRequest,
    ListReportConfigsResponse,
    ListReportsRequest,
    ListReportsResponse,
    ListSourcesRequest,
    ListSourcesResponse,
    MachineArchitectureDetails,
    MachineDetails,
    MachineDiskDetails,
    MachineNetworkDetails,
    MachinePreferences,
    MachineSeries,
    MemoryUsageSample,
    MigrationInsight,
    NetworkAdapterDetails,
    NetworkAdapterList,
    NetworkAddress,
    NetworkAddressList,
    NetworkConnection,
    NetworkConnectionList,
    NetworkUsageSample,
    NfsExport,
    NfsExportList,
    OpenFileDetails,
    OpenFileList,
    OperatingSystemFamily,
    OperationMetadata,
    PerformanceSample,
    PersistentDiskType,
    PhysicalPlatformDetails,
    PlatformDetails,
    PreferenceSet,
    RegionPreferences,
    RemoveAssetsFromGroupRequest,
    Report,
    ReportAssetFramesRequest,
    ReportAssetFramesResponse,
    ReportConfig,
    ReportSummary,
    ReportView,
    RunImportJobRequest,
    RunningProcess,
    RunningProcessList,
    RunningService,
    RunningServiceList,
    RuntimeNetworkInfo,
    Settings,
    SizingOptimizationStrategy,
    Source,
    UpdateAssetRequest,
    UpdateGroupRequest,
    UpdateImportJobRequest,
    UpdatePreferenceSetRequest,
    UpdateSettingsRequest,
    UpdateSourceRequest,
    UploadFileInfo,
    ValidateImportJobRequest,
    ValidationReport,
    VirtualMachinePreferences,
    VmwareDiskConfig,
    VmwarePlatformDetails,
)

__all__ = (
    "MigrationCenterClient",
    "MigrationCenterAsyncClient",
    "AddAssetsToGroupRequest",
    "AggregateAssetsValuesRequest",
    "AggregateAssetsValuesResponse",
    "Aggregation",
    "AggregationResult",
    "Asset",
    "AssetFrame",
    "AssetList",
    "AssetPerformanceData",
    "AwsEc2PlatformDetails",
    "AzureVmPlatformDetails",
    "BatchDeleteAssetsRequest",
    "BatchUpdateAssetsRequest",
    "BatchUpdateAssetsResponse",
    "BiosDetails",
    "ComputeEngineMigrationTarget",
    "ComputeEnginePreferences",
    "ComputeEngineShapeDescriptor",
    "CpuUsageSample",
    "CreateGroupRequest",
    "CreateImportDataFileRequest",
    "CreateImportJobRequest",
    "CreatePreferenceSetRequest",
    "CreateReportConfigRequest",
    "CreateReportRequest",
    "CreateSourceRequest",
    "DailyResourceUsageAggregation",
    "DeleteAssetRequest",
    "DeleteGroupRequest",
    "DeleteImportDataFileRequest",
    "DeleteImportJobRequest",
    "DeletePreferenceSetRequest",
    "DeleteReportConfigRequest",
    "DeleteReportRequest",
    "DeleteSourceRequest",
    "DiskEntry",
    "DiskEntryList",
    "DiskPartition",
    "DiskPartitionList",
    "DiskUsageSample",
    "ErrorFrame",
    "ExecutionReport",
    "FileValidationReport",
    "FitDescriptor",
    "Frames",
    "FrameViolationEntry",
    "FstabEntry",
    "FstabEntryList",
    "GenericPlatformDetails",
    "GetAssetRequest",
    "GetErrorFrameRequest",
    "GetGroupRequest",
    "GetImportDataFileRequest",
    "GetImportJobRequest",
    "GetPreferenceSetRequest",
    "GetReportConfigRequest",
    "GetReportRequest",
    "GetSettingsRequest",
    "GetSourceRequest",
    "Group",
    "GuestConfigDetails",
    "GuestInstalledApplication",
    "GuestInstalledApplicationList",
    "GuestOsDetails",
    "GuestRuntimeDetails",
    "HostsEntry",
    "HostsEntryList",
    "ImportDataFile",
    "ImportError",
    "ImportJob",
    "ImportRowError",
    "Insight",
    "InsightList",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListErrorFramesRequest",
    "ListErrorFramesResponse",
    "ListGroupsRequest",
    "ListGroupsResponse",
    "ListImportDataFilesRequest",
    "ListImportDataFilesResponse",
    "ListImportJobsRequest",
    "ListImportJobsResponse",
    "ListPreferenceSetsRequest",
    "ListPreferenceSetsResponse",
    "ListReportConfigsRequest",
    "ListReportConfigsResponse",
    "ListReportsRequest",
    "ListReportsResponse",
    "ListSourcesRequest",
    "ListSourcesResponse",
    "MachineArchitectureDetails",
    "MachineDetails",
    "MachineDiskDetails",
    "MachineNetworkDetails",
    "MachinePreferences",
    "MachineSeries",
    "MemoryUsageSample",
    "MigrationInsight",
    "NetworkAdapterDetails",
    "NetworkAdapterList",
    "NetworkAddress",
    "NetworkAddressList",
    "NetworkConnection",
    "NetworkConnectionList",
    "NetworkUsageSample",
    "NfsExport",
    "NfsExportList",
    "OpenFileDetails",
    "OpenFileList",
    "OperationMetadata",
    "PerformanceSample",
    "PhysicalPlatformDetails",
    "PlatformDetails",
    "PreferenceSet",
    "RegionPreferences",
    "RemoveAssetsFromGroupRequest",
    "Report",
    "ReportAssetFramesRequest",
    "ReportAssetFramesResponse",
    "ReportConfig",
    "ReportSummary",
    "RunImportJobRequest",
    "RunningProcess",
    "RunningProcessList",
    "RunningService",
    "RunningServiceList",
    "RuntimeNetworkInfo",
    "Settings",
    "Source",
    "UpdateAssetRequest",
    "UpdateGroupRequest",
    "UpdateImportJobRequest",
    "UpdatePreferenceSetRequest",
    "UpdateSettingsRequest",
    "UpdateSourceRequest",
    "UploadFileInfo",
    "ValidateImportJobRequest",
    "ValidationReport",
    "VirtualMachinePreferences",
    "VmwareDiskConfig",
    "VmwarePlatformDetails",
    "AssetView",
    "CommitmentPlan",
    "ErrorFrameView",
    "ImportJobFormat",
    "ImportJobView",
    "LicenseType",
    "OperatingSystemFamily",
    "PersistentDiskType",
    "ReportView",
    "SizingOptimizationStrategy",
)
