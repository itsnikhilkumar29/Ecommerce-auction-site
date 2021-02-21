from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    pass

class Listing(models.Model):
	name=models.CharField(max_length=200)
	user=models.ForeignKey(User,related_name="listings",on_delete=models.CASCADE)
	available=models.BooleanField()
	startbid=models.IntegerField()
	# currentbid=models.ForeignKey(Bid)
	time=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Bid(models.Model):
	listing=models.ForeignKey(Listing,related_name="bids",on_delete=models.CASCADE)
	user=models.ForeignKey(User,related_name="bids",on_delete=models.CASCADE)
	amount=models.IntegerField()
	def __str__(self):
		return f"{self.listing},{self.amount}"

class Comment(models.Model):
	listing=models.ForeignKey(Listing,related_name="comments",on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	time=models.DateTimeField(auto_now=True)
	comment=models.CharField(max_length=123123)
	def __str__(self):
		return self.comment

class Winner(models.Model):
	listing=models.ForeignKey(Listing,related_name="winner",on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	amount=models.IntegerField()
	def __str__(self):
		return f'{self.user} won {self.listing} for {self.amount}'