import re
from .models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    mobile = serializers.SerializerMethodField()

    def mobile_number_validator(value):
        """
        NOTE: it checks for only indian mobile number
        check if mobile_number is valid or not
        :param value: mobile number
        :return: mobile number if valid
        """
        value = value.strip()
        mobile_pattern = re.compile(r"^[6-9]\d{9}$")
        if re.match(mobile_pattern, value):
            return value
        raise serializers.ValidationError("Enter a valid Mobile Number")

    def get_mobile(self, Contact):
        return self.mobile_number_validator(mobile)

    class Meta:
        model = Contact
        fields = ('email', 'mobile')