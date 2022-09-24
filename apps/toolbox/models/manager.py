from django.db import models


class ToolBoxManager(models.Manager):
    def published(self):
        return self.filter(status=self.model.publish)
