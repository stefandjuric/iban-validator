from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .serializers import IbanHistorySerializer, SuggestedIbanSerializer
from .models import IbanHistory

# API view for validating an IBAN without saving it to the database
@csrf_exempt
@api_view(['POST'])
def first_task_view(request):
    serializer = IbanHistorySerializer(data=request.data)

    # Check if the provided IBAN data is valid according to the serializer's validation rules
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view for validating and saving an IBAN to the database
@csrf_exempt
@api_view(['POST'])
def second_task_view(request):
    serializer = IbanHistorySerializer(data=request.data)

    # Validate and save the IBAN to the database if valid
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view to retrieve the history of all validated IBANs, ordered by timestamp
@csrf_exempt
@api_view(['GET'])
def get_iban_history(request):
    all_records = IbanHistory.objects.all().order_by('-timestamp')
    all_records_serializer = IbanHistorySerializer(all_records, many=True)
    
    # Return the serialized list of all IBAN history records
    return Response(all_records_serializer.data, status=status.HTTP_200_OK)

# API view similar to first_task_view, but reserved for a different task or validation process
@csrf_exempt
@api_view(['POST'])
def third_task_view(request):
    serializer = IbanHistorySerializer(data=request.data)

    # Validate the provided IBAN data and return the result
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view for validating an IBAN and suggesting a correction if it is invalid
@csrf_exempt
@api_view(['POST'])
def fourth_task_view(request):
    serializer = SuggestedIbanSerializer(data=request.data)

    # Validate the IBAN, suggest corrections if necessary, and return the result
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
