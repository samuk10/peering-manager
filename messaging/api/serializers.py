from django.contrib.contenttypes.models import ContentType
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from messaging.models import Contact, ContactAssignment, ContactRole
from peering_manager.api import ContentTypeField, PrimaryModelSerializer
from utils.api import get_serializer_for_model

from .nested_serializers import *

__all__ = (
    "ContactSerializer",
    "NestedContactSerializer",
    "ContactRoleSerializer",
    "NestedContactRoleSerializer",
    "ContactAssignmentSerializer",
    "NestedContactAssignmentSerializer",
)


class ContactRoleSerializer(PrimaryModelSerializer):
    class Meta:
        model = ContactRole
        fields = ["id", "display", "name", "slug", "description", "tags"]


class ContactSerializer(PrimaryModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "display",
            "name",
            "title",
            "phone",
            "email",
            "address",
            "comments",
            "created",
            "updated",
        ]


class ContactAssignmentSerializer(PrimaryModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="messaging-api:contactassignment-detail"
    )
    content_type = ContentTypeField(queryset=ContentType.objects.all())
    object = serializers.SerializerMethodField(read_only=True)
    contact = NestedContactSerializer()
    role = NestedContactRoleSerializer(required=False, allow_null=True)

    class Meta:
        model = ContactAssignment
        fields = [
            "id",
            "url",
            "display",
            "content_type",
            "object_id",
            "object",
            "contact",
            "role",
            "created",
            "updated",
        ]

    @extend_schema_field(NestedContactSerializer)
    def get_object(self, instance):
        context = {"request": self.context["request"]}
        return NestedContactSerializer(instance.object, context=context).data