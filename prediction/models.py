from django.db import models

# Create your models here.

class CsvUpload(models.Model):
    csv_file = models.FileField(upload_to='csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.csv_file.name

class TeamName(models.Model):
    team = models.CharField(max_length=200, unique = True)
    def __str__(self):
        return self.team