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
    mentor = models.ForeignKey(User, related_name='mentor_pair')
    mentee = models.ForeignKey(User, related_name='mentee_pair')
    admin = models.ForeignKey(User, related_name='admin_pair')
    streak = models.IntegerField(default=0)
    word_count = models.IntegerField(default=0)
    
class Message(models.Model):
    pair = models.ForeignKey(Pair, related_name='pair')
    user_from = models.ForeignKey(User, related_name='user_from')
    user_to = models.ForeignKey(User)
    text = models.TextField()
    time = models.DateTimeField(default=datetime.now())
    
class Badge(models.Model):
    name = models.CharField(max_length=50)
    num_awarded = models.IntegerField()
    
    