from django.db import models


class Users(models.Model):
    user_name  = models.CharField(unique=True, max_length=45)
    password   = models.CharField(max_length=200)
    name       = models.CharField(max_length=45)
    email      = models.CharField(unique=True, max_length=100)
    is_active  = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'