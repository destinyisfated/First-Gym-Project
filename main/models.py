from django.db import models
from django. utils.html  import mark_safe

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)
    details=models.TextField()
    img =models.ImageField(upload_to= "services/", null= True )
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />'% (self.img.url))

        
class Gallery(models.Model):
    title = models.CharField(max_length=255)
    details=models.TextField()
    img =models.ImageField(upload_to= "gallery/", null= True )
    time_tag= models.DateTimeField( auto_now_add=True, null= True)
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />'% (self.img.url))


class GalleryImage(models.Model):
    gallery= models.ForeignKey(Gallery, on_delete=models.CASCADE, null= True)
    alt_text = models.CharField(max_length=255)
    img =models.ImageField(upload_to= "galleryimage/", null= True )
    time_tag= models.DateTimeField( auto_now_add=True, null= True)

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />'% (self.img.url))
# Sbscription plan
class Subplan(models.Model):
    title=models.CharField(max_length=67)
    price =models.IntegerField()
    highlited=models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.title
# Subscription plan features.
class SubplanFeatures(models.Model):
    Subplan=models.ForeignKey(Subplan, on_delete=models.CASCADE)
    title=models.CharField(max_length=67)
    
class Trainer(models.Model):
    fullname=models.CharField(max_length=200)
    username= models.CharField(max_length=200)
    details= models.TextField(max_length=200)
    address= models.TextField(max_length=200)
    password=models.CharField(max_length=100)
    join_date=models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.fullname

class Session(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    start_time =models.TimeField()
    end_time =models.TimeField()
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="session/")

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />'% (self.image.url))
    

class Attendance(models.Model):
     date= models.DateTimeField(auto_now_add=True)
     login =models.CharField(max_length=200)
     logout =models.CharField(max_length=200)
     selectworkout =models.CharField(max_length=200)
     trainedby =models.CharField(max_length=200)
     def __str__(self):
         return self.date