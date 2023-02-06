from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from wsgiref.util import FileWrapper
from django.http import HttpResponse

from .models import VideoModel
from .serializers import VideoSerializer


class HealthApiView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        Return the health of the service as HTTP 200 status. Useful to check if everything is configured correctly.
        '''
        # TODO: django heartbeat?

        return Response(status=status.HTTP_200_OK)


class FilesApiView(APIView):

    # parser_classes = (MultiPartParser,)

    def get(self, request, *args, **kwargs):
        '''
        List uploaded files
        '''
        videos = VideoModel.objects.all()
        serializer = VideoSerializer(videos, many=True)

        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Upload a video file
        '''

        if request.FILES:
            serializer = VideoSerializer(data=request.FILES)
            if serializer.is_valid():

                content_type = request.FILES['data'].content_type
                if content_type not in settings.ALLOWED_CONTENT_TYPE:
                    return Response({"res": "Unsupported Media Type"},
                                    status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

                video_obj = VideoModel.objects.filter(name=request.FILES['data'].name)
                if video_obj.exists():
                    return Response({"res": "File exists"},
                                    status=status.HTTP_409_CONFLICT)

                serializer.save(
                    file=request.FILES['data'],
                    size=request.FILES['data'].size,
                    name=request.FILES['data'].name,
                    mime_type=request.FILES['data'].content_type
                    )
                response = HttpResponse({"status": "File uploaded"},
                                        serializer.data['fileid'],
                                        status=status.HTTP_201_CREATED)
                response['Location'] = "".join([settings.MEDIA_URL, serializer.data['fileid']])
                return response

        return Response({"status": "File not found"},
                        status=status.HTTP_400_BAD_REQUEST)


class FilesDetailsApiView(APIView):
    def get_object(self, fileid):
        '''
        Helper method to get the object with the given file id
        '''
        try:
            return VideoModel.objects.get(fileid=fileid)
        except VideoModel.DoesNotExist:
            return None

    def get(self, request, fileid, *args, **kwargs):
        '''
        Retrieves the video with given file id
        '''
        video_obj = self.get_object(fileid)
        if video_obj:
            video_file = open("".join([settings.MEDIA_ROOT, str(video_obj.file)]), 'rb')

            response = HttpResponse(FileWrapper(video_file),
                                    content_type=video_obj.mime_type,
                                    status=status.HTTP_200_OK)
            response['Content-Disposition'] = 'attachment; filename="%s"' % video_obj.name
            return response

        return Response(
            {"res": "File not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, fileid, *args, **kwargs):
        '''
        Deletes the video with given file id
        '''
        video_obj = self.get_object(fileid)
        if video_obj:
            video_obj.delete()
            return Response(
                {"res": "File was successfully removed"},
                status=status.HTTP_204_NO_CONTENT
                )

        return Response(
            {"res": "File not found"},
            status=status.HTTP_404_NOT_FOUND
            )
