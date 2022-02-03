from django.db import models

class Project(models.Model):
    """
    Fields required to store project details.
    """
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

    #details = SeparatedVlauesField()

    def __str__(self):
        return self.title

