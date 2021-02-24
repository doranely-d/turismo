from django.db import models


class DisplayManager(models.Manager):

    def display(self):
        return self.filter(display=True)
