from django_apps.games.serializers import (
    GameSerializer,
)
from django_apps.responses import (
    HTTP_response_400,
    HTTP_response_500,
)
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class GameCreateAPIView(APIView):

    @extend_schema(
        tags=["Game"],
        methods=["POST"],
        summary="Create a Game",
        request=GameSerializer,
        responses={
            201: OpenApiResponse(
                response=GameSerializer,
                description="Created",
            ),
            400: HTTP_response_400,
            500: HTTP_response_500,
        },
    )
    def post(self, request, *args, **kwargs):
        """Create Game

        Args:
            player1: Player 1 uuid
            player2: Player 2 uuid
            winner: Winner uuid

        Example:

            {
                "player1_id": "757d3fb7-17e1-47e2-a389-a4ef7743d58f",
                "player2_id": "db3e67ee-7fc2-4dc9-b7dd-cd8f725ff6d9",
                "winner_id": null
            }

        Returns:

            JSON with data of the created game.

        """
        data = request.data
        serializer = GameSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
