from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from PriorityLanguageModel import predicting as pd

@api_view(['POST'])
def takeComplaints(request):
    try:
        complaint_type = request.data.get('complaint_type', '')
        complaint_description = request.data.get('complaint_description', '')

        processed_data = pd.predict(complaint_type, complaint_description)
        
        return Response({'result':str(processed_data)}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
