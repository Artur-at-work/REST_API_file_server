import pytest
import os

from crud.models import VideoModel

TEST_DIR = "test_media/"

filename = "sample-small.mp4"
filepath = "".join([TEST_DIR, filename])
filesize = os.stat(filepath).st_size
filetype = "video/mp4"


@pytest.fixture
def file_object():
    return VideoModel.objects.create(
        file=filepath,
        name=filename,
        size=filesize,
        mime_type=filetype
    )


@pytest.mark.django_db
def test_create_file(file_object):
    assert VideoModel.objects.filter(name=file_object.name).exists()
    assert file_object.fileid is not None
    assert file_object.created_at is not None  # TODO: within 60 sec
    assert file_object.name == filename
    assert file_object.size == filesize
    assert file_object.mime_type == filetype


@pytest.mark.django_db
def test_delete_file(file_object):
    VideoModel.objects.filter(fileid=file_object.fileid).delete()
    assert not VideoModel.objects.filter(fileid=file_object.fileid).exists()
    assert not VideoModel.objects.filter(name=file_object.name).exists()
