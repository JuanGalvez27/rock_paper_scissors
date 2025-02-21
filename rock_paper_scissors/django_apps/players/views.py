from django_apps.players.models import Player
from django_apps.players.serializers import (
    PlayerSerializer,
)
from django_apps.responses import HTTP_response_400, HTTP_response_500, HTTP_response_404
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PlayerCreateAPIView(APIView):

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
    

class PlayerRetrieveAPIView(APIView):

    @extend_schema(
        tags=["Player"],
        methods=["GET"],
        summary="Get Player info",
        responses={
            200: OpenApiResponse(
                response=PlayerSerializer,
                description="OK",
            ),
            404: HTTP_response_404,
            500: HTTP_response_500,
        },
    )
    def get(self, request, id, *args, **kwargs):
        """Get Player

        Returns:

            {
                "id": "aaf93a6c-91e4-4799-a9be-bc3f22cc5082"
                "name": "John Doe",
            }

        """
        try:
            player = Player.objects.get(id=id)
        except Player.DoesNotExist:
            return Response(
                {"message": "No player found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = PlayerSerializer(player)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
