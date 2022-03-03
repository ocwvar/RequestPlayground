from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status as _status


def give_error_response(message: str):
    return Response(data={"error_message": message}, status=_status.HTTP_500_INTERNAL_SERVER_ERROR)


def give_success_response(message: str):
    return Response(data={"message": message}, status=_status.HTTP_200_OK)


def give_success_response_with_object(object):
    return Response(data={"data": object}, status=_status.HTTP_200_OK)
