from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'category'
        
    def __str__(self) -> str:
        return self.name

# Create your models here.
class telephone(models.Model):
    category = models.ForeignKey(to = "Category", on_delete=models.CASCADE)
    model = models.CharField(max_length=150)
    company = models.CharField(max_length=180)
    price = models.IntegerField()
    info = models.CharField(max_length=250)
    image = models.ImageField(upload_to="media/", blank=True, null=True)

    class Meta:
        db_table = "telephone"

    def __str__(self) -> str:
        return f"{self.model}"