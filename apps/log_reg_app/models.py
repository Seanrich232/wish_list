from __future__ import unicode_literals
from django.db import models
import bcrypt
class UserManager(models.Manager):
    def validateRegistration(self, postData):
        response = {
            'status' : False,
            'errors' : [],
        }
        if len(postData['name']) < 3:
            response['errors'].append("first name is too short")
        if len(postData['username']) < 3:
            response['errors'].append("last name is too short")
        if len(postData['password']) < 8:
            response['errors'].append("your password is too short")
        if postData['password'] != postData['confirm']:
            response['errors'].append("password dose not match")
        if User.objects.filter(username = postData['username']):
            response['errors'].append("username is takin")
        if len(response['errors']) == 0:
            response['status'] = True
            response['user_id'] = User.objects.create(
                name = postData['name'],
                username = postData['username'],
                hiredate = postData['hiredate'],
                password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            )
        return response
    def validateLogin(self, postData):
        response = {
            'status' : False,
            'errors' : [],
        }
        existing_users = User.objects.filter(username = postData['username'])
        if len(existing_users) == 0:
            response['errors'].append('invalid Username / password')
        else:
            if bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
                response['status'] = True
                response['user_id'] = existing_users[0]
            else:
                response['errors'].append('invalid Username / password')
        return response
        
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hiredate = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()