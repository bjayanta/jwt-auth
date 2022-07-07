from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import AccountCreateSerializer

# Create your views here.
class SignupView(APIView):
    def post(self, request):
        data = request.data
        serializer = AccountCreateSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        account = serializer.create(serializer.validated_data)
        account = AccountCreateSerializer(account)

        return Response(account.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
