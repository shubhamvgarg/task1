from django.db import models
#table to store image description and title , generated key will be used as foreign key
class ImageFiles(models.Model):
    Title=models.TextField()
    Description=models.TextField()
    def __str__(self):
	       return self.Title+" "+self.Description+" "
#stores the url for the uploaded files and foreign key 
class Image_Attachment(models.Model):
    key = models.ForeignKey(ImageFiles)
    file = models.TextField( null=True, blank=True)
