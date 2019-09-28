from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField
from bdtask.models import Contact

class ContactCreateSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'message',
            'isActive',
        ]

class ContactUpdateSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'message',
            'isActive',
        ]
        extra_kwargs = {
            'email': {
                'read_only': True
            }
        }

DETAIL_URL = HyperlinkedIdentityField(view_name = 'detail_api',)

class ContactDetailSerializer(ModelSerializer):
    url = DETAIL_URL
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'url',
            'email',
            'phone',
            'address',
            'message',
            'createdAt',
            'isActive',
        ]

class ContactListSerializer(ModelSerializer):
    url = DETAIL_URL
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'url',
            'email',
            'isActive',
        ]