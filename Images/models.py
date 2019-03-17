from django.db import models
class ImageFiles(models.Model):
    Title=models.TextField()
    Description=models.TextField()
    def __str__(self):
	       return self.Title+" "+self.Description+" "

class Image_Attachment(models.Model):
    key = models.ForeignKey(ImageFiles)
    file = models.TextField( null=True, blank=True)
