from django_apps.players.models import Player
from django_apps.players.serializers import (
    PlayerSerializer,
)
from django_apps.responses import HTTP_response_400, HTTP_response_500
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PlayerAPIView(APIView):

    @extend_schema(
        tags=["Player"],
        methods=["POST"],
        summary="Create a Player",
        request=PlayerSerializer,
        responses={
            201: OpenApiResponse(
                response=PlayerSerializer,
                description="Created",
            ),
            400: HTTP_response_400,
            500: HTTP_response_500,
        },
    )
    def post(self, request, *args, **kwargs):
        """Create Player

        Args:

            name: Name of the player

        Example:

            {
                "name": "John Doe",
            }

        Returns:

            {
                "id": "aaf93a6c-91e4-4799-a9be-bc3f22cc5082"
                "name": "John Doe",
            }

        """
        player_data = request.data
        player_serializer = PlayerSerializer(data=player_data)
        if player_serializer.is_valid():
            player_serializer.save()
            return Response(player_serializer.data, status=status.HTTP_201_CREATED)
        return Response(player_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
