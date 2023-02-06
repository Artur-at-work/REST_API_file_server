from .views import HealthApiView, FilesApiView, FilesDetailsApiView
from django.urls import re_path


urlpatterns = [
    re_path(r'^health/?$', HealthApiView.as_view()),
    re_path(r'^files/?$', FilesApiView.as_view()),
    re_path(r'^files/(?P<fileid>.+)/?$', FilesDetailsApiView.as_view())
]