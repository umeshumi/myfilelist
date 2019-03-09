from django.db import models
import os
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.core.exceptions import ValidationError

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.user.username, filename)


def validate_file_extension(value):
	ext = os.path.splitext(value.name)[1]  
	valid_extensions = ['.pdf']
	if not ext.lower() in valid_extensions:
		raise ValidationError(u'Please Upload PDF file only')

class Documents(models.Model):
	user 				=	models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	Birth_Certificate 	=   models.FileField(upload_to=user_directory_path, validators=[validate_file_extension])
	Degree_Certificate 	=   models.FileField(upload_to=user_directory_path, validators=[validate_file_extension])
	Verification 		=	models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

@receiver(models.signals.post_delete, sender=Documents)
def auto_delete_file_on_delete(sender, instance, **kwargs):
	if (instance.Birth_Certificate or Degree_Certificate):
		if os.path.isfile(instance.Birth_Certificate.path or instance.Degree_Certificate.path):
			os.remove(instance.Birth_Certificate.path)
			os.remove(instance.Degree_Certificate.path)


	
# Create your models here.
