import uuid
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class VideoModel(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    fileid = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
    file = models.FileField(null=True, verbose_name="")
    size = models.IntegerField(null=True, help_text="file size (bytes)")
    name = models.CharField(max_length=260, null=True, default="", help_text="filename")
    created_at = models.DateTimeField(default=now, null=True, blank=True, help_text="Time when data was saved on server")
    mime_type = models.CharField(max_length=255, null=True, help_text="Content's MIME Type")

    def __str__(self):
        return (self.fileid,
                self.name,
                self.size,
                self.created_at,
                str(self.file))


@receiver(pre_delete, sender=VideoModel)
def remove_file(**kwargs):
    '''Removes the file from file system after instance was deleted from DB'''
    instance = kwargs.get('instance')
    instance.file.delete(save=False)
