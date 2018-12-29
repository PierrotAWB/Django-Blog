from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
