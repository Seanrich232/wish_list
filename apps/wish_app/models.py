from django.db import models
from ..log_reg_app.models import User
from datetime import datetime

class WishManager(models.Manager):
    def createWish(self, postData, user_id):
        response = {
            'status' : False,
            'errors' : [],
        }
        if len(postData['product']) < 4:
            response['errors'].append('please fill out the form completely')
        if len(response['errors']) == 0:
            response['status']=True
            me = User.objects.get(id=user_id)
            wish = Wish.objects.create(
                product = postData['product'],
                wish_creator = me
            )
            wish.wisher.add(me)
            wish.save()
        return response
    def joinWishlist(self, wish_id, user_id):
        me = User.objects.get(id=user_id)
        wish = Wish.objects.get(id=wish_id)
        wish.wisher.add(me)
        wish.save()
    def removewishlist(self, wish_id, user_id):
        me = User.objects.get(id=user_id)
        wish = Wish.objects.get(id=wish_id)
        wish.wisher.remove(me)
        wish.save()
class Wish(models.Model):
    product = models.CharField(max_length=255)
    wisher = models.ManyToManyField(User, related_name="wisher_wish")
    wish_creator = models.ForeignKey(User, related_name="created_wish", on_delete=models.CACADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()