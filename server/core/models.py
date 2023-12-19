from django.db import models
import datetime

# Create your models here.
def upload_to(instance, filename):
    today = datetime.datetime.now().strftime("%m-%d-%Y")
    return f"uploads/{today}/{filename}"

class File(models.Model):
    file_type = models.CharField(max_length=20, default="pcap", blank=True)
    file = models.FileField(upload_to=upload_to, null=True, blank=True)
    upload_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.file and not self.upload_date:
            self.upload_date = datetime.datetime.now().date()

        super(File, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.file.name