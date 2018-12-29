from django.db import models
from django.contrib.auth.models import User

# create a one-to-one relationship
# between users and their profile pictures
class Profile(models.Model):
	# cascade: if the user is deleted, delete the profile
	# note, this is one-to-one, meaning that deleting a profile
	# won't delete the user. This makes sense.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'