from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tour(models.Model):
    #  author is linked to a registered user in the "auth_user" table
    title_general_info = models.CharField(max_length=300)
    general_content_info = models.TextField(default='')
    culture_title_history = models.CharField(max_length=300)
    culture_content_history = models.TextField(default='')
    culture_title_second_part = models.CharField(max_length=300)
    culture_content_second_part = models.TextField(default='')
    first_night_clubs_image = models.ImageField(upload_to="images", blank=True, null=True)
    first_title_1night_clubs_image = models.CharField(max_length=300)
    second_night_clubs_image = models.ImageField(upload_to="images", blank=True, null=True)
    second_title_night_clubs_image = models.CharField(max_length=300)
    #######################################################################################################
    third_night_clubs_image = models.ImageField(upload_to="images", blank=True, null=True)
    title_night_clubs_image = models.CharField(max_length=300)
    4night_clubs_image = models.ImageField(upload_to="images", blank=True, null=True)
    title_4night_clubs_image = models.CharField(max_length=300)
    night_clubs_content_info = models.TextField(default='')
    gastronomy_general_info = models.CharField(max_length=300)
    gastronomy_content_info = models.TextField(default='')
    weather_title = models.CharField(max_length=300)
    weather_content_info = models.TextField(default='')


    general_content_info = models.TextField()

    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title