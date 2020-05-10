from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
# Create your views here.


class UpTest(APIView):
    # serializer_class = FileSerializer
    # parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    # queryset = ProjectInfo.objects.all()

    def get(self, request, *args, **kwargs):
        pro_list = ProjectInfo.objects.all()
        ser = FileSerializer(instance=pro_list, many=True, context={'request': request})
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        ser = FileSerializer(data=request.data)
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)
        return Response(ser.validated_data)


def modify_input_for_multiple_files(project, image):
    dict = {}
    dict['project'] = project
    dict['image'] = image
    return dict


class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        project = request.data['project_id']

        # converts querydict to original dict
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(project,
                                                            img_name)
            if not isinstance(modified_data, dict):
                return Response('不是字典')
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)