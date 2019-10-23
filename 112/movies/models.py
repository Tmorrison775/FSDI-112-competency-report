from django.db import models

# Create your models here.



class Genre(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Movie(models.Model):
    def __str__(self):
        return str(self.id) + "   |   " + str(self.release_year) + "   |   " + self.title
    title = models.CharField(max_length=250) 
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    duration_min = models.IntegerField() 
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

class Series(models.Model):

    class Meta:
        verbose_name_plural = 'Series'
    def __str__(self):
        return str(self.id) + " | " + str(self.title) + " | " + str(self.seasons)  
    title = models.CharField(max_length=250) 
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    seasons = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)