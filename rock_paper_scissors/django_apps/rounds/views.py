from django_apps.rounds.models import Round
from django_apps.rounds.serializers import RoundSerializer
from django_apps.responses import (
    HTTP_response_400,
    HTTP_response_500,
)
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RoundCreateAPIView(APIView):

    @extend_schema(
        tags=["Round"],
        methods=["POST"],
        summary="Create a Round",
        request=RoundSerializer,
        responses={
            201: OpenApiResponse(
                response=RoundSerializer,
                description="Created",
            ),
            400: HTTP_response_400,
            500: HTTP_response_500,
        },
    )
    def post(self, request, *args, **kwargs):
        """Create Round

        Args:
            game: UUID, UUID of the game
            round_time: int,  Round number
            move_player_1: int, Move of the player 1
            move_player_2: int, Move of the player 2

        Example:

            {
                "game": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "round_time": 1,
                "move_player_1": 2,
                "move_player_2": 1,
            }

        Returns:

            JSON with data of the created Round.

        """
        data = request.data
        serializer = RoundSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

