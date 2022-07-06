from rest_framework import APIView, permissions, status
from rest_framework.response import Response

# Create your views here.
class SignupView(APIView):
    def post(self, request):
        data = request.data

        return Response({}, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
