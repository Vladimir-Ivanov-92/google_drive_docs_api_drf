from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FileSerializer
from .services import create_file_in_google_drive


class FileCreateAPIView(APIView):
    """Сервис, создающий в Google drive файл с переданными в запросе параметрами"""

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            data = serializer.validated_data.get("data")
            try:
                # Создание файла в Google drive
                create_file_in_google_drive(file_name=name, file_content=data)
                return Response(
                    {"status": f"File {name} created in Google Drive"},
                    status=status.HTTP_201_CREATED,
                )
            except Exception as ex:
                return Response(
                    {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
