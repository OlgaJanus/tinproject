from django.db import models
from django.utils import timezone


class Difficulty(models.Model):

    NAMES = (
        ('łatwe','łatwe'),
        ('średnie','średnie'),
        ('trudne','trudne'),
    )
    name = models.CharField(max_length=20, choices=NAMES)

    def __str__(self):
        return self.name

class Category(models.Model):
    NAMES = (
        ('mięsne', 'mięsne'),
        ('wegańskie', 'wegańskie'),
        ('wegetariańskie', 'wegetariańskie'),
        ('dietetyczne', 'dietetyczne'),
        ('pikantne', 'pikantne'),
        ('orientalne', 'orientalne'),
        ('dla dzieci', 'dla dzieci')
    )
    name = models.CharField(max_length=20, blank=True, choices=NAMES)

    def __str__(self):
        return self.name

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    difficulty=models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title