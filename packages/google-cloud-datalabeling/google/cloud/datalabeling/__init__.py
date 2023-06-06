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
from google.cloud.datalabeling import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.datalabeling_v1beta1.services.data_labeling_service.async_client import (
    DataLabelingServiceAsyncClient,
)
from google.cloud.datalabeling_v1beta1.services.data_labeling_service.client import (
    DataLabelingServiceClient,
)
from google.cloud.datalabeling_v1beta1.types.annotation import (
    Annotation,
    AnnotationMetadata,
    AnnotationSentiment,
    AnnotationSource,
    AnnotationType,
    AnnotationValue,
    BoundingPoly,
    ImageBoundingPolyAnnotation,
    ImageClassificationAnnotation,
    ImagePolylineAnnotation,
    ImageSegmentationAnnotation,
    NormalizedBoundingPoly,
    NormalizedPolyline,
    NormalizedVertex,
    ObjectTrackingFrame,
    OperatorMetadata,
    Polyline,
    SequentialSegment,
    TextClassificationAnnotation,
    TextEntityExtractionAnnotation,
    TimeSegment,
    Vertex,
    VideoClassificationAnnotation,
    VideoEventAnnotation,
    VideoObjectTrackingAnnotation,
)
from google.cloud.datalabeling_v1beta1.types.annotation_spec_set import (
    AnnotationSpec,
    AnnotationSpecSet,
)
from google.cloud.datalabeling_v1beta1.types.data_labeling_service import (
    CreateAnnotationSpecSetRequest,
    CreateDatasetRequest,
    CreateEvaluationJobRequest,
    CreateInstructionRequest,
    DeleteAnnotatedDatasetRequest,
    DeleteAnnotationSpecSetRequest,
    DeleteDatasetRequest,
    DeleteEvaluationJobRequest,
    DeleteInstructionRequest,
    ExportDataRequest,
    GetAnnotatedDatasetRequest,
    GetAnnotationSpecSetRequest,
    GetDataItemRequest,
    GetDatasetRequest,
    GetEvaluationJobRequest,
    GetEvaluationRequest,
    GetExampleRequest,
    GetInstructionRequest,
    ImportDataRequest,
    LabelImageRequest,
    LabelTextRequest,
    LabelVideoRequest,
    ListAnnotatedDatasetsRequest,
    ListAnnotatedDatasetsResponse,
    ListAnnotationSpecSetsRequest,
    ListAnnotationSpecSetsResponse,
    ListDataItemsRequest,
    ListDataItemsResponse,
    ListDatasetsRequest,
    ListDatasetsResponse,
    ListEvaluationJobsRequest,
    ListEvaluationJobsResponse,
    ListExamplesRequest,
    ListExamplesResponse,
    ListInstructionsRequest,
    ListInstructionsResponse,
    PauseEvaluationJobRequest,
    ResumeEvaluationJobRequest,
    SearchEvaluationsRequest,
    SearchEvaluationsResponse,
    SearchExampleComparisonsRequest,
    SearchExampleComparisonsResponse,
    UpdateEvaluationJobRequest,
)
from google.cloud.datalabeling_v1beta1.types.data_payloads import (
    ImagePayload,
    TextPayload,
    VideoPayload,
    VideoThumbnail,
)
from google.cloud.datalabeling_v1beta1.types.dataset import (
    AnnotatedDataset,
    AnnotatedDatasetMetadata,
    BigQuerySource,
    ClassificationMetadata,
    DataItem,
    Dataset,
    DataType,
    Example,
    GcsDestination,
    GcsFolderDestination,
    GcsSource,
    InputConfig,
    LabelStats,
    OutputConfig,
    TextMetadata,
)
from google.cloud.datalabeling_v1beta1.types.evaluation import (
    BoundingBoxEvaluationOptions,
    ClassificationMetrics,
    ConfusionMatrix,
    Evaluation,
    EvaluationConfig,
    EvaluationMetrics,
    ObjectDetectionMetrics,
    PrCurve,
)
from google.cloud.datalabeling_v1beta1.types.evaluation_job import (
    Attempt,
    EvaluationJob,
    EvaluationJobAlertConfig,
    EvaluationJobConfig,
)
from google.cloud.datalabeling_v1beta1.types.human_annotation_config import (
    BoundingPolyConfig,
    EventConfig,
    HumanAnnotationConfig,
    ImageClassificationConfig,
    ObjectDetectionConfig,
    ObjectTrackingConfig,
    PolylineConfig,
    SegmentationConfig,
    SentimentConfig,
    StringAggregationType,
    TextClassificationConfig,
    TextEntityExtractionConfig,
    VideoClassificationConfig,
)
from google.cloud.datalabeling_v1beta1.types.instruction import (
    CsvInstruction,
    Instruction,
    PdfInstruction,
)
from google.cloud.datalabeling_v1beta1.types.operations import (
    CreateInstructionMetadata,
    ExportDataOperationMetadata,
    ExportDataOperationResponse,
    ImportDataOperationMetadata,
    ImportDataOperationResponse,
    LabelImageBoundingBoxOperationMetadata,
    LabelImageBoundingPolyOperationMetadata,
    LabelImageClassificationOperationMetadata,
    LabelImageOrientedBoundingBoxOperationMetadata,
    LabelImagePolylineOperationMetadata,
    LabelImageSegmentationOperationMetadata,
    LabelOperationMetadata,
    LabelTextClassificationOperationMetadata,
    LabelTextEntityExtractionOperationMetadata,
    LabelVideoClassificationOperationMetadata,
    LabelVideoEventOperationMetadata,
    LabelVideoObjectDetectionOperationMetadata,
    LabelVideoObjectTrackingOperationMetadata,
)

__all__ = (
    "DataLabelingServiceClient",
    "DataLabelingServiceAsyncClient",
    "Annotation",
    "AnnotationMetadata",
    "AnnotationValue",
    "BoundingPoly",
    "ImageBoundingPolyAnnotation",
    "ImageClassificationAnnotation",
    "ImagePolylineAnnotation",
    "ImageSegmentationAnnotation",
    "NormalizedBoundingPoly",
    "NormalizedPolyline",
    "NormalizedVertex",
    "ObjectTrackingFrame",
    "OperatorMetadata",
    "Polyline",
    "SequentialSegment",
    "TextClassificationAnnotation",
    "TextEntityExtractionAnnotation",
    "TimeSegment",
    "Vertex",
    "VideoClassificationAnnotation",
    "VideoEventAnnotation",
    "VideoObjectTrackingAnnotation",
    "AnnotationSentiment",
    "AnnotationSource",
    "AnnotationType",
    "AnnotationSpec",
    "AnnotationSpecSet",
    "CreateAnnotationSpecSetRequest",
    "CreateDatasetRequest",
    "CreateEvaluationJobRequest",
    "CreateInstructionRequest",
    "DeleteAnnotatedDatasetRequest",
    "DeleteAnnotationSpecSetRequest",
    "DeleteDatasetRequest",
    "DeleteEvaluationJobRequest",
    "DeleteInstructionRequest",
    "ExportDataRequest",
    "GetAnnotatedDatasetRequest",
    "GetAnnotationSpecSetRequest",
    "GetDataItemRequest",
    "GetDatasetRequest",
    "GetEvaluationJobRequest",
    "GetEvaluationRequest",
    "GetExampleRequest",
    "GetInstructionRequest",
    "ImportDataRequest",
    "LabelImageRequest",
    "LabelTextRequest",
    "LabelVideoRequest",
    "ListAnnotatedDatasetsRequest",
    "ListAnnotatedDatasetsResponse",
    "ListAnnotationSpecSetsRequest",
    "ListAnnotationSpecSetsResponse",
    "ListDataItemsRequest",
    "ListDataItemsResponse",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "ListEvaluationJobsRequest",
    "ListEvaluationJobsResponse",
    "ListExamplesRequest",
    "ListExamplesResponse",
    "ListInstructionsRequest",
    "ListInstructionsResponse",
    "PauseEvaluationJobRequest",
    "ResumeEvaluationJobRequest",
    "SearchEvaluationsRequest",
    "SearchEvaluationsResponse",
    "SearchExampleComparisonsRequest",
    "SearchExampleComparisonsResponse",
    "UpdateEvaluationJobRequest",
    "ImagePayload",
    "TextPayload",
    "VideoPayload",
    "VideoThumbnail",
    "AnnotatedDataset",
    "AnnotatedDatasetMetadata",
    "BigQuerySource",
    "ClassificationMetadata",
    "DataItem",
    "Dataset",
    "Example",
    "GcsDestination",
    "GcsFolderDestination",
    "GcsSource",
    "InputConfig",
    "LabelStats",
    "OutputConfig",
    "TextMetadata",
    "DataType",
    "BoundingBoxEvaluationOptions",
    "ClassificationMetrics",
    "ConfusionMatrix",
    "Evaluation",
    "EvaluationConfig",
    "EvaluationMetrics",
    "ObjectDetectionMetrics",
    "PrCurve",
    "Attempt",
    "EvaluationJob",
    "EvaluationJobAlertConfig",
    "EvaluationJobConfig",
    "BoundingPolyConfig",
    "EventConfig",
    "HumanAnnotationConfig",
    "ImageClassificationConfig",
    "ObjectDetectionConfig",
    "ObjectTrackingConfig",
    "PolylineConfig",
    "SegmentationConfig",
    "SentimentConfig",
    "TextClassificationConfig",
    "TextEntityExtractionConfig",
    "VideoClassificationConfig",
    "StringAggregationType",
    "CsvInstruction",
    "Instruction",
    "PdfInstruction",
    "CreateInstructionMetadata",
    "ExportDataOperationMetadata",
    "ExportDataOperationResponse",
    "ImportDataOperationMetadata",
    "ImportDataOperationResponse",
    "LabelImageBoundingBoxOperationMetadata",
    "LabelImageBoundingPolyOperationMetadata",
    "LabelImageClassificationOperationMetadata",
    "LabelImageOrientedBoundingBoxOperationMetadata",
    "LabelImagePolylineOperationMetadata",
    "LabelImageSegmentationOperationMetadata",
    "LabelOperationMetadata",
    "LabelTextClassificationOperationMetadata",
    "LabelTextEntityExtractionOperationMetadata",
    "LabelVideoClassificationOperationMetadata",
    "LabelVideoEventOperationMetadata",
    "LabelVideoObjectDetectionOperationMetadata",
    "LabelVideoObjectTrackingOperationMetadata",
)
