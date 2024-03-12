from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Airlines(models.Model):
    ranking=models.IntegerField()
    name=models.CharField(max_length=100)
    airhelp=models.FloatField(max_length=10)
    ponctualite=models.FloatField(max_length=10)
    avis=models.FloatField(max_length=10)
    service=models.FloatField(max_length=10)

    def __str__(self):
        return(f"{self.ranking} - Compagnie: {self.name}, AirHelp Score: {self.airhelp}, Ponctualité: {self.ponctualite}, Avis client: {self.avis}, Efficacité service client: {self.service}")
