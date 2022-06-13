from django.db import models


class InputAnt(models.Model):
    image = models.ImageField('Изображение', upload_to="media", null=True)
