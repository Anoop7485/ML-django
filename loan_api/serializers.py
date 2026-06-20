from rest_framework import serializers

class LoanApplicantSerializer(serializers.Serializer):
    no_of_dependents = serializers.IntegerField(required=False)
    education = serializers.CharField(required=False)
    self_employed = serializers.CharField(required=False)
    income_annum = serializers.FloatField(required=False)
    loan_amount = serializers.FloatField(required=False)
    loan_term = serializers.IntegerField(required=False)
    cibil_score = serializers.IntegerField(required=False)
    residential_assets_value = serializers.FloatField(required=False)
    commercial_assets_value = serializers.FloatField(required=False)
    luxury_assets_value = serializers.FloatField(required=False)
    bank_asset_value = serializers.FloatField(required=False)
