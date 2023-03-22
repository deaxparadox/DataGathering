from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import QuerySet
from django.urls import reverse

class TimeAll(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class Status(models.TextChoices):
    PENDING = "PD", _("Pending") 
    START = "ST", _("Start")
    DONE = "DN", _("Done")

class PendingManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Status.PENDING)

class DoneManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Status.DONE)

class Site(TimeAll):
    url = models.URLField(unique=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    domain = models.CharField(max_length=120)
    status = models.CharField(
        max_length=2, 
        choices=Status.choices,
        default=Status.PENDING,
    )
    objects = models.Manager()
    pending = PendingManager()
    done = DoneManager()

    def __str__(self) -> str:
        return self.url 

    def get_absolute_url(self):
        return reverse("scrapper:details", kwargs={"id": self.id})
    

class Data(TimeAll):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="data")
    text = models.TextField()

    def __str__(self):
        return f"{self.text[:30]}"