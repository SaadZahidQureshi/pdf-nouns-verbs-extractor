from djongo import models

class ExtractedData(models.Model):
    email = models.EmailField(unique=True)
    nouns = models.JSONField()
    verbs = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
