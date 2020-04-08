# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.datacatalog_v1.proto import (
    datacatalog_pb2 as google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2,
)
from google.cloud.datacatalog_v1.proto import (
    tags_pb2 as google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2,
)
from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DataCatalogStub(object):
    """Data Catalog API service allows clients to discover, understand, and manage
  their data.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.SearchCatalog = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/SearchCatalog",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.SearchCatalogRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.SearchCatalogResponse.FromString,
        )
        self.CreateEntryGroup = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/CreateEntryGroup",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateEntryGroupRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.EntryGroup.FromString,
        )
        self.GetEntryGroup = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/GetEntryGroup",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.GetEntryGroupRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.EntryGroup.FromString,
        )
        self.UpdateEntryGroup = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/UpdateEntryGroup",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateEntryGroupRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.EntryGroup.FromString,
        )
        self.DeleteEntryGroup = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/DeleteEntryGroup",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteEntryGroupRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.ListEntryGroups = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/ListEntryGroups",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListEntryGroupsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListEntryGroupsResponse.FromString,
        )
        self.CreateEntry = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/CreateEntry",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateEntryRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.Entry.FromString,
        )
        self.UpdateEntry = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/UpdateEntry",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateEntryRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.Entry.FromString,
        )
        self.DeleteEntry = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/DeleteEntry",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteEntryRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.GetEntry = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/GetEntry",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.GetEntryRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.Entry.FromString,
        )
        self.LookupEntry = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/LookupEntry",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.LookupEntryRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.Entry.FromString,
        )
        self.ListEntries = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/ListEntries",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListEntriesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListEntriesResponse.FromString,
        )
        self.CreateTagTemplate = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/CreateTagTemplate",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateTagTemplateRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplate.FromString,
        )
        self.GetTagTemplate = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/GetTagTemplate",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.GetTagTemplateRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplate.FromString,
        )
        self.UpdateTagTemplate = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/UpdateTagTemplate",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateTagTemplateRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplate.FromString,
        )
        self.DeleteTagTemplate = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/DeleteTagTemplate",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteTagTemplateRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.CreateTagTemplateField = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/CreateTagTemplateField",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateTagTemplateFieldRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplateField.FromString,
        )
        self.UpdateTagTemplateField = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/UpdateTagTemplateField",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateTagTemplateFieldRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplateField.FromString,
        )
        self.RenameTagTemplateField = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/RenameTagTemplateField",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.RenameTagTemplateFieldRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplateField.FromString,
        )
        self.DeleteTagTemplateField = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/DeleteTagTemplateField",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteTagTemplateFieldRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.CreateTag = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/CreateTag",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateTagRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.Tag.FromString,
        )
        self.UpdateTag = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/UpdateTag",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateTagRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.Tag.FromString,
        )
        self.DeleteTag = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/DeleteTag",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteTagRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.ListTags = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/ListTags",
            request_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListTagsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListTagsResponse.FromString,
        )
        self.SetIamPolicy = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/SetIamPolicy",
            request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString,
            response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString,
        )
        self.GetIamPolicy = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/GetIamPolicy",
            request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString,
            response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString,
        )
        self.TestIamPermissions = channel.unary_unary(
            "/google.cloud.datacatalog.v1.DataCatalog/TestIamPermissions",
            request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString,
            response_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString,
        )


class DataCatalogServicer(object):
    """Data Catalog API service allows clients to discover, understand, and manage
  their data.
  """

    def SearchCatalog(self, request, context):
        """Searches Data Catalog for multiple resources like entries, tags that
    match a query.

    This is a custom method
    (https://cloud.google.com/apis/design/custom_methods) and does not return
    the complete resource, only the resource identifier and high level
    fields. Clients can subsequentally call `Get` methods.

    Note that Data Catalog search queries do not guarantee full recall. Query
    results that match your query may not be returned, even in subsequent
    result pages. Also note that results returned (and not returned) can vary
    across repeated search queries.

    See [Data Catalog Search
    Syntax](/data-catalog/docs/how-to/search-reference) for more information.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateEntryGroup(self, request, context):
        """Creates an EntryGroup.

    An entry group contains logically related entries together with Cloud
    Identity and Access Management policies that specify the users who can
    create, edit, and view entries within the entry group.

    Data Catalog automatically creates an entry group for BigQuery entries
    ("@bigquery") and Pub/Sub topics ("@pubsub"). Users create their own entry
    group to contain Cloud Storage fileset entries or custom type entries,
    and the IAM policies associated with those entries. Entry groups, like
    entries, can be searched.

    A maximum of 10,000 entry groups may be created per organization across all
    locations.

    Users should enable the Data Catalog API in the project identified by
    the `parent` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetEntryGroup(self, request, context):
        """Gets an EntryGroup.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateEntryGroup(self, request, context):
        """Updates an EntryGroup. The user should enable the Data Catalog API in the
    project identified by the `entry_group.name` parameter (see [Data Catalog
    Resource Project] (/data-catalog/docs/concepts/resource-project) for more
    information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteEntryGroup(self, request, context):
        """Deletes an EntryGroup. Only entry groups that do not contain entries can be
    deleted. Users should enable the Data Catalog API in the project
    identified by the `name` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListEntryGroups(self, request, context):
        """Lists entry groups.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateEntry(self, request, context):
        """Creates an entry. Only entries of 'FILESET' type or user-specified type can
    be created.

    Users should enable the Data Catalog API in the project identified by
    the `parent` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).

    A maximum of 100,000 entries may be created per entry group.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateEntry(self, request, context):
        """Updates an existing entry.
    Users should enable the Data Catalog API in the project identified by
    the `entry.name` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteEntry(self, request, context):
        """Deletes an existing entry. Only entries created through
    [CreateEntry][google.cloud.datacatalog.v1.DataCatalog.CreateEntry]
    method can be deleted.
    Users should enable the Data Catalog API in the project identified by
    the `name` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetEntry(self, request, context):
        """Gets an entry.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LookupEntry(self, request, context):
        """Get an entry by target resource name. This method allows clients to use
    the resource name from the source Google Cloud Platform service to get the
    Data Catalog Entry.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListEntries(self, request, context):
        """Lists entries.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateTagTemplate(self, request, context):
        """Creates a tag template. The user should enable the Data Catalog API in
    the project identified by the `parent` parameter (see [Data Catalog
    Resource Project](/data-catalog/docs/concepts/resource-project) for more
    information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTagTemplate(self, request, context):
        """Gets a tag template.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateTagTemplate(self, request, context):
        """Updates a tag template. This method cannot be used to update the fields of
    a template. The tag template fields are represented as separate resources
    and should be updated using their own create/update/delete methods.
    Users should enable the Data Catalog API in the project identified by
    the `tag_template.name` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteTagTemplate(self, request, context):
        """Deletes a tag template and all tags using the template.
    Users should enable the Data Catalog API in the project identified by
    the `name` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateTagTemplateField(self, request, context):
        """Creates a field in a tag template. The user should enable the Data Catalog
    API in the project identified by the `parent` parameter (see
    [Data Catalog Resource
    Project](/data-catalog/docs/concepts/resource-project) for more
    information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateTagTemplateField(self, request, context):
        """Updates a field in a tag template. This method cannot be used to update the
    field type. Users should enable the Data Catalog API in the project
    identified by the `name` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RenameTagTemplateField(self, request, context):
        """Renames a field in a tag template. The user should enable the Data Catalog
    API in the project identified by the `name` parameter (see [Data Catalog
    Resource Project](/data-catalog/docs/concepts/resource-project) for more
    information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteTagTemplateField(self, request, context):
        """Deletes a field in a tag template and all uses of that field.
    Users should enable the Data Catalog API in the project identified by
    the `name` parameter (see [Data Catalog Resource Project]
    (/data-catalog/docs/concepts/resource-project) for more information).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateTag(self, request, context):
        """Creates a tag on an [Entry][google.cloud.datacatalog.v1.Entry].
    Note: The project identified by the `parent` parameter for the
    [tag](/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create#path-parameters)
    and the
    [tag
    template](/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create#path-parameters)
    used to create the tag must be from the same organization.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateTag(self, request, context):
        """Updates an existing tag.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteTag(self, request, context):
        """Deletes a tag.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListTags(self, request, context):
        """Lists the tags on an [Entry][google.cloud.datacatalog.v1.Entry].
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SetIamPolicy(self, request, context):
        """Sets the access control policy for a resource. Replaces any existing
    policy.
    Supported resources are:
    - Tag templates.
    - Entries.
    - Entry groups.
    Note, this method cannot be used to manage policies for BigQuery, Pub/Sub
    and any external Google Cloud Platform resources synced to Data Catalog.

    Callers must have following Google IAM permission
    - `datacatalog.tagTemplates.setIamPolicy` to set policies on tag
    templates.
    - `datacatalog.entries.setIamPolicy` to set policies on entries.
    - `datacatalog.entryGroups.setIamPolicy` to set policies on entry groups.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetIamPolicy(self, request, context):
        """Gets the access control policy for a resource. A `NOT_FOUND` error
    is returned if the resource does not exist. An empty policy is returned
    if the resource exists but does not have a policy set on it.

    Supported resources are:
    - Tag templates.
    - Entries.
    - Entry groups.
    Note, this method cannot be used to manage policies for BigQuery, Pub/Sub
    and any external Google Cloud Platform resources synced to Data Catalog.

    Callers must have following Google IAM permission
    - `datacatalog.tagTemplates.getIamPolicy` to get policies on tag
    templates.
    - `datacatalog.entries.getIamPolicy` to get policies on entries.
    - `datacatalog.entryGroups.getIamPolicy` to get policies on entry groups.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TestIamPermissions(self, request, context):
        """Returns the caller's permissions on a resource.
    If the resource does not exist, an empty set of permissions is returned
    (We don't return a `NOT_FOUND` error).

    Supported resources are:
    - Tag templates.
    - Entries.
    - Entry groups.
    Note, this method cannot be used to manage policies for BigQuery, Pub/Sub
    and any external Google Cloud Platform resources synced to Data Catalog.

    A caller is not required to have Google IAM permission to make this
    request.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DataCatalogServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SearchCatalog": grpc.unary_unary_rpc_method_handler(
            servicer.SearchCatalog,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.SearchCatalogRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.SearchCatalogResponse.SerializeToString,
        ),
        "CreateEntryGroup": grpc.unary_unary_rpc_method_handler(
            servicer.CreateEntryGroup,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateEntryGroupRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.EntryGroup.SerializeToString,
        ),
        "GetEntryGroup": grpc.unary_unary_rpc_method_handler(
            servicer.GetEntryGroup,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.GetEntryGroupRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.EntryGroup.SerializeToString,
        ),
        "UpdateEntryGroup": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateEntryGroup,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateEntryGroupRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.EntryGroup.SerializeToString,
        ),
        "DeleteEntryGroup": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteEntryGroup,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteEntryGroupRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "ListEntryGroups": grpc.unary_unary_rpc_method_handler(
            servicer.ListEntryGroups,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListEntryGroupsRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListEntryGroupsResponse.SerializeToString,
        ),
        "CreateEntry": grpc.unary_unary_rpc_method_handler(
            servicer.CreateEntry,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateEntryRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.Entry.SerializeToString,
        ),
        "UpdateEntry": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateEntry,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateEntryRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.Entry.SerializeToString,
        ),
        "DeleteEntry": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteEntry,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteEntryRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "GetEntry": grpc.unary_unary_rpc_method_handler(
            servicer.GetEntry,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.GetEntryRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.Entry.SerializeToString,
        ),
        "LookupEntry": grpc.unary_unary_rpc_method_handler(
            servicer.LookupEntry,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.LookupEntryRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.Entry.SerializeToString,
        ),
        "ListEntries": grpc.unary_unary_rpc_method_handler(
            servicer.ListEntries,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListEntriesRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListEntriesResponse.SerializeToString,
        ),
        "CreateTagTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.CreateTagTemplate,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateTagTemplateRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplate.SerializeToString,
        ),
        "GetTagTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.GetTagTemplate,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.GetTagTemplateRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplate.SerializeToString,
        ),
        "UpdateTagTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateTagTemplate,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateTagTemplateRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplate.SerializeToString,
        ),
        "DeleteTagTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteTagTemplate,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteTagTemplateRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "CreateTagTemplateField": grpc.unary_unary_rpc_method_handler(
            servicer.CreateTagTemplateField,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateTagTemplateFieldRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplateField.SerializeToString,
        ),
        "UpdateTagTemplateField": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateTagTemplateField,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateTagTemplateFieldRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplateField.SerializeToString,
        ),
        "RenameTagTemplateField": grpc.unary_unary_rpc_method_handler(
            servicer.RenameTagTemplateField,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.RenameTagTemplateFieldRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.TagTemplateField.SerializeToString,
        ),
        "DeleteTagTemplateField": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteTagTemplateField,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteTagTemplateFieldRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "CreateTag": grpc.unary_unary_rpc_method_handler(
            servicer.CreateTag,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.CreateTagRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.Tag.SerializeToString,
        ),
        "UpdateTag": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateTag,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.UpdateTagRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_tags__pb2.Tag.SerializeToString,
        ),
        "DeleteTag": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteTag,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.DeleteTagRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "ListTags": grpc.unary_unary_rpc_method_handler(
            servicer.ListTags,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListTagsRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_datacatalog__pb2.ListTagsResponse.SerializeToString,
        ),
        "SetIamPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.SetIamPolicy,
            request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.FromString,
            response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString,
        ),
        "GetIamPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.GetIamPolicy,
            request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.FromString,
            response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString,
        ),
        "TestIamPermissions": grpc.unary_unary_rpc_method_handler(
            servicer.TestIamPermissions,
            request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.FromString,
            response_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.datacatalog.v1.DataCatalog", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
