from django.db import models

class Admins(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 500)
    email = models.EmailField(max_length = 500)
    password = models.CharField(max_length = 500)


    def registration(self):
        self.save()