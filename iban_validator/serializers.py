from rest_framework import serializers
from .models import IbanHistory, SuggestedIban
from .utils import is_valid_iban, suggest_correct_iban

class IbanHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IbanHistory
        fields = ['iban', 'is_valid', 'timestamp']
        read_only_fields = ['is_valid', 'timestamp']  # 'is_valid' and 'timestamp' are read-only

    def validate(self, data):
        iban = data['iban'].upper()  # Convert IBAN to uppercase for consistency

        # Check if the IBAN is valid
        if not is_valid_iban(iban):
            data['is_valid'] = False  # Set 'is_valid' to False if IBAN is invalid
        else:
            data['is_valid'] = True  # Set 'is_valid' to True if IBAN is valid
        return data

class SuggestedIbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestedIban
        fields = ['iban', 'is_valid', 'suggested_iban']
        read_only_fields = ['is_valid', 'suggested_iban']  # 'is_valid' and 'suggested_iban' are read-only

    def validate(self, data):
        iban = data['iban'].upper()  # Convert IBAN to uppercase for consistency

        # Check if the IBAN is valid
        if not is_valid_iban(iban):
            data['is_valid'] = False  # Set 'is_valid' to False if IBAN is invalid
            data['suggested_iban'] = suggest_correct_iban(iban)  # Suggest a corrected IBAN
        else:
            data['is_valid'] = True  # Set 'is_valid' to True if IBAN is valid

        return data
