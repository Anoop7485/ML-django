from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoanApplicantSerializer
from .utils import model
from rest_framework import viewsets
import pandas as pd

class LoanPredictionViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = LoanApplicantSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            education_map = {'Graduate': 1, 'Not Graduate': 0}
            self_employed_map = {"Yes": 1, "No": 0}

            features = [[
                data['no_of_dependents'],
                education_map.get(data['education'], 0),
                self_employed_map.get(data['self_employed'], 0),
                data["income_annum"],
                data["loan_amount"],
                data["loan_term"],
                data["cibil_score"],
                data["residential_assets_value"],
                data["commercial_assets_value"],
                data["luxury_assets_value"],
                data["bank_asset_value"],
            ]]

            prediction = model.predict(features)[0]
            result = "Approved" if prediction == 1 else "Rejected"
            return Response({"prediction": result}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
