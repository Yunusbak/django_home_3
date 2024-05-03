from django.db import models

class Category(models.Model):
    info = models.CharField(max_length=250)

    class Meta:
        db_table = "category"

    def __str__(self) -> str:
        return f"{self.info}"
    

class Animal(models.Model):  # Изменил название класса на Animal
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    age = models.IntegerField()
    image = models.ImageField(upload_to="media/", blank=True, null=True)

    class Meta:
        db_table = "animals"

    def __str__(self) -> str:
        return f"{self.name}"
