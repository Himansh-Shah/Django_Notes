from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Difficulty(models.Model):
    difficulty = models.CharField(max_length = 20)

    def __str__(self):
        return self.difficulty

class Question(models.Model):
    title = models.CharField(max_length = 200)
    topics = models.ManyToManyField(Topic)
    difficulty = models.ForeignKey(Difficulty, verbose_name=("difficulty"), on_delete=models.CASCADE)
    note = models.CharField(max_length = 500)
    code = models.CharField(max_length = 1000)


    def __str__(self):
        return self.title

