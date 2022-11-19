from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)

    def __str__(self):
        return self.question[:15]