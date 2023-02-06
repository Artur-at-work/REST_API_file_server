## Description
REST API example for file uploads.<br>
Built with django-rest-framework (DRF) and SQLite.<br>

TODO: add FE forms

## Installation
Pre-requisite: docker-compose<br>

Starting the project in containers:
```
$ ls
docker-compose.yml  README.md  video_server
$ docker-compose up
Creating network "file_server_default" with the default driver
Building web
Step 1/10 : FROM python:3.8-alpine
3.8-alpine: Pulling from library/python
8921db27df28: Pull complete
3fd9832a787c: Pull complete
e1be48db60b9: Pull complete
dfc797a791f3: Pull complete
f4c61d4ff607: Pull complete
Digest: sha256:6474f4b68e968cfa067e29f69c78c72d186d97183041160e47b8afca74105b66
Status: Downloaded newer image for python:3.8-alpine
 ---> 0ccdcbe88eaa
...
```
SQLite db comes with th Django dev environment and runs in the same container.<br>
On startup, contaier executes "python manage migrate" to apply any models' changes stored in crud/migrations directory.<br>
Then starts the web API on localhost:8080<br>

### Storage
By default, uploaded files are saved in "media" directory inside the project fs. This path and allowed file formats are specified in settings.py<br>
```
# Destination for uploaded video files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
ALLOWED_CONTENT_TYPE = ['image/png', 'image/webp', 'video/mp4', 'video/mpeg']
```

Each file has a unique 'fileid' generated automatically by uuid module.<br>

## Unit Tests
test_urls - covers some GET url pathes and successfull responses.
test_models - covers object creation/deletion in VideoModel table via ORM.
TODO: test_views

Executing UTs manually with pytest:
```
$ ls
docker-compose.yml  README.md  video_server
$ cd video_server/tests/
$ pytest --cov
=============================================================== test session starts ================================================================
platform linux -- Python 3.8.10, pytest-7.2.0, pluggy-1.0.0
django: settings: video_server.settings (from ini)
rootdir: /video_server, configfile: pytest.ini
plugins: cov-4.0.0, django-4.5.2
collected 6 items                                                                                                                                  

test_model.py ..                                                                                                                             [ 33%]
test_urls.py ....                                                                                                                            [100%]

---------- coverage: platform linux, python 3.8.10-final-0 -----------
Name                                                                                                                     Stmts   Miss  Cover
--------------------------------------------------------------------------------------------------------------------------------------------
/video_server/crud/__init__.py                                                                           0      0   100%
/video_server/crud/admin.py                                                                              3      0   100%
/video_server/crud/apps.py                                                                               4      0   100%
/video_server/crud/migrations/0001_initial.py                                                            5      0   100%
/video_server/crud/migrations/0002_rename_file_id_videomodel_fileid_and_more.py                          5      0   100%
/video_server/crud/migrations/0003_alter_videomodel_name_alter_videomodel_size.py                        4      0   100%
/video_server/crud/migrations/0004_videomodel_video_file.py                                              4      0   100%
/video_server/crud/migrations/0005_remove_videomodel_created_at_remove_videomodel_name_and_more.py       4      0   100%
/video_server/crud/migrations/0006_rename_video_file_videomodel_file_and_more.py                         5      0   100%
/video_server/crud/migrations/0007_videomodel_name_videomodel_size.py                                    4      0   100%
/video_server/crud/migrations/0008_alter_videomodel_name.py                                              4      0   100%
/video_server/crud/migrations/0009_alter_videomodel_file.py                                              4      0   100%
/video_server/crud/migrations/0010_alter_videomodel_file.py                                              5      0   100%
/video_server/crud/migrations/0011_alter_videomodel_file.py                                              5      0   100%
/video_server/crud/migrations/0012_alter_videomodel_file.py                                              4      0   100%
/video_server/crud/migrations/0013_remove_videomodel_fileid_videomodel_id.py                             4      0   100%
/video_server/crud/migrations/0014_remove_videomodel_id_videomodel_fileid.py                             4      0   100%
/video_server/crud/migrations/0015_remove_videomodel_fileid_videomodel_id.py                             4      0   100%
/video_server/crud/migrations/0016_remove_videomodel_id_videomodel_fileid.py                             4      0   100%
/video_server/crud/migrations/0017_videomodel_mime_type.py                                               4      0   100%
/video_server/crud/migrations/__init__.py                                                                0      0   100%
/video_server/crud/models.py                                                                            17      1    94%
/video_server/crud/serializers.py                                                                        9      1    89%
/video_server/crud/urls.py                                                                               3      0   100%
/video_server/crud/views.py                                                                             51     30    41%
/video_server/video_server/settings.py                                                                  24      0   100%
/video_server/video_server/urls.py                                                                       6      0   100%
test_model.py                                                                                                               24      0   100%
test_urls.py                                                                                                                20      0   100%
--------------------------------------------------------------------------------------------------------------------------------------------
TOTAL                                                                                                                      234     32    86%


================================================================ 6 passed in 1.10s =================================================================

```

## Documentation
documentation.html contains the list of available endpoints<br>

Example:
```
$ curl -I localhost:8080/v5/files
HTTP/1.1 200 OK
Date: Mon, 06 Feb 2023 08:22:58 GMT
Server: WSGIServer/0.2 CPython/3.8.16
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 2
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
```
<br>
![image](https://user-images.githubusercontent.com/40683252/216925706-80409d43-c6b2-4710-b631-2e1acb104bd9.png)
