from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class Vendor(models.Model):
	uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=15)

	def __str__(self):
		return 'Vendor ' + str(self.id)



class Post(models.Model):
	uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
	offer_text = models.CharField(max_length=200)
	vendor = models.ForeignKey(Vendor, null=False, default=1)
	timeout = models.FloatField(default=30)
	status = models.CharField(max_length=10, default="OPEN")
	timeout_date = models.DateTimeField(blank=True, null=True)

	def close(self):
		self.timeout_date = timezone.now()
		self.save()

	def __str__(self):
		return 'Post ' + str(self.id)