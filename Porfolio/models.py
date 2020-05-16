from django.db import models
from django.urls import reverse

# Create your models here.


class Member(models.Model):
    emple_id = models.IntegerField(blank=False)
    first_name = models.CharField(max_length=50)
    midle_i = models.CharField(max_length=1)
    last_name = models.CharField(max_length= 30)
    emails = models.CharField(max_length= 50, default=False)
    fun_fac = models.TextField(blank=True)


    def get_absolute_urls(self):
        return reverse("Porfolio:member_info", kwargs={'id': self.id})


