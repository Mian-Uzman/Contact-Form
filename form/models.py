from django.db import models

# Create your models here.


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=200)
    comments = models.CharField(max_length=500)

    def __str__(self):
        return self.name
