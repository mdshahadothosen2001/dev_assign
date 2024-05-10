from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from user.models import UserAccount
from utils.utils import tokenValidation
from ..serializers.profile import ProfileSerializer


class ProfileoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        customer = get_object_or_404(
            UserAccount, phone_number=tokenValidation(request)["phone_number"]
        )
        serializer = ProfileSerializer(customer)
        return Response(serializer.data)
