import pytest
import os

from django.test import Client
from crud.models import VideoModel
from rest_framework import status

client = Client()

def test_health():
    response = client.get(f'/v5/health')
    assert response.status_code == status.HTTP_200_OK

def test_health_slash():
    response = client.get(f'/v5/health/')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_files():
    response = client.get(f'/v5/files')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_files_slash():
    response = client.get(f'/v5/files/')
    assert response.status_code == status.HTTP_200_OK


# TEST_DIR = "test_media/"
# filename = "sample-small.mp4"
# filepath = "".join([TEST_DIR, filename])
# filesize = os.stat(filepath).st_size
# filetype = "video/mp4"


# @pytest.fixture
# def file_object():
#     return VideoModel.objects.create(
#         file=filepath,
#         name=filename,
#         size=filesize,
#         mime_type=filetype
#     )

# @pytest.mark.django_db
# def test_files_fileid(file_object):
#     response = client.get(f'/v5/files/{file_object.fileid}')
#     # TODO: views to search file TEST_DIR not in MEDIA_ROOT
#     assert response.status_code == status.HTTP_200_OK
