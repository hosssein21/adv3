from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serializers import RegistrationSerializer

class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                'email':serializer._validated_data['email']
            }
            return Response({'detail':data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    