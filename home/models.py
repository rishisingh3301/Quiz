from django.db import models

# Create your models here.


class registration(models.Model):

    name = models.CharField(primary_key=True, max_length=100)
    email = models.EmailField(max_length=254)
    grade = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    about = models.TextField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name + "  -->  " + self.email


class question(models.Model):
    qid = models.CharField(primary_key=True, max_length=100)
    qtype = models.CharField(max_length=100)
    qtext = models.TextField()


#  class score(models.Model):
#     name = models.ForeignKey(registration, on_delete=models.CASCADE)
#     score = models.IntegerField(default=0)
