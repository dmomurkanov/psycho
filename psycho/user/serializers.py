

from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'phone_number', 'age', 'social_status', 'school']
        #DELETE PHONE_NUMBER NOT TO SHOW TO USER

        # extra_kwargs = {
        #     'phone_number' : {'write_only':True}
        # }
        #
        # def create(self, validated_data):
        #     phone_number = validated_data.pop('phone_number', None)
        #     instance = self.Meta.model(**validated_data)
        #     if phone_number is not None:
        #         instance.set_password(phone_number)
        #     instance.save()
        #     return instance

