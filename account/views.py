from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import AccountCreateSerializer, AccountSerializer, VerifyAccountSerializer
from .email import *

# Create your views here.
class SignupView(APIView):
    def post(self, request):
        data = request.data
        serializer = AccountCreateSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        account = serializer.create(serializer.validated_data)
        # account = AccountCreateSerializer(account)
        account = AccountSerializer(account)

        # send otp via email
        # send_otp_via_email(account.data['email'])
        send_otp_via_email_template(account.data['email'])

        return Response(account.data, status=status.HTTP_201_CREATED)

class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            email = serializer.data['email']
            otp = serializer.data['otp']
            user = User.objects.filter(email = email)

            if not user.exists():
                return Response({
                    'message': "User not exists."
                }, status=status.HTTP_400_BAD_REQUEST)

            if user[0].otp != otp:
                return Response({
                    'message': 'Wrong OTP'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            user.first().is_verified = True
            user.first().save()

            return Response({
                'message': 'Account verified.'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        account = request.user
        account = AccountSerializer(account)

        return Response(account.data, status=status.HTTP_200_OK)
