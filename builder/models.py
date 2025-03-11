from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=100)
    project_data = models.JSONField(default=dict, blank=True)  # Stores { components: html, styles: css }

    def __str__(self):
        return self.name
