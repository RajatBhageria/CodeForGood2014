'''
Created on Sep 26, 2014

@author: Matthew
'''
from django.db import models
from datetime import datetime

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=15)
    type = models.IntegerField() # 0 for mentee 1 for mentor 2 for admin
    
class Pair(models.Model):
    mentor = models.OneToOneField(User, primary_key=User)
    mentee = models.OneToOneField(User, primary_key=User)
    admin = models.ForeignKey(User)
    streak = models.IntegerField()
    word_count = models.IntegerField()
    
class Message(models.Model):
    pair = models.ForeignKey(Pair)
    user_from = models.ForeignKey(User)
    user_to = models.ForeignKey(User)
    text = models.TextField()
    time = models.DateTimeField(default=datetime.now())
    
class Badge(models.Model):
    name = models.CharField(max_length=50)
    num_awarded = models.IntegerField()
    
    