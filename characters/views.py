from random import choice

from django.db.models import QuerySet
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, generics, pagination
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from characters.models import Character
from characters.serializers import CharacterSerializer


@extend_schema(responses={status.HTTP_200_OK: CharacterSerializer})
@api_view(["GET"])
def get_random_character_view(request: Request) -> Response:
    """Get a random character from Rick & Morty world!"""
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    pagination_class = CharacterListPagination

    def get_queryset(self) -> QuerySet:
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filter by name insensitive contains",
                type=OpenApiTypes.STR,
                required=False,
            )
        ]
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        """List of characters with filter by name"""
        return super().get(request, *args, **kwargs)
