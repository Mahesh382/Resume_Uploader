from django.db import models

STATE_CHOICE = (
 ('	Bhojpur','	Bhojpur'),
 ('	Dhankuta','	Dhankuta'),
 ('Ilam','Ilam'),
 ('	Jhapa','Jhapa'),
 ('	Khotang','Khotang'),
 ('Morang','Morang'),
 ('Okhaldhunga','Okhaldhunga'),
 ('Panchthar','Panchthar'),
 ('Solukhumbu','Solukhumbu'),
 ('Sunsari','Sunsari'),
 ('Taplejung','Taplejung'),
 ('Dhanusa','Dhanusa'),
 ('Mahottari','Mahottari'),
 ('Parsa','Parsa'),
 ('Chitwan','Chitwan'),
 ('Bhaktapur','Bhaktapur'),
 ('Dhading','Dhading'),
 ('Dolakha','Dolakha'),
 ('Kathmandu','Kathmandu'),
 ('Kavrepalanchok','Kavrepalanchok'),
 ('Lalitpur','Lalitpur'),
 ('Makawanpur','Makawanpur'),
 ('Nuwakot','Nuwakot'),
 ('Ramechhap','Ramechhap'),
 ('	Rasuwa','Rasuwa'),
 ('Sindhuli','Sindhuli'),
 ('Sindhupalchok','Sindhupalchok'),
 ('	Baglung','Baglung'),
 ('Gorkha','Gorkha'),
 ('Lamjung','Lamjung'),
 ('Manang','Manang'),
 ('Mustang','Mustang'),
 ('Myagdi','Myagdi'),
 ('Nawalpur','Nawalpur'),
 ('Dadeldhura','Dadeldhura'),
 ('	Kanchanpur','Kanchanpur'),
)

class Resume(models.Model):
 name = models.CharField(max_length=100)
 dob = models.DateField(auto_now=False, auto_now_add=False)
 gender = models.CharField(max_length=100)
 locality = models.CharField(max_length=100)
 city = models.CharField(max_length=100)
 pin = models.PositiveIntegerField()
 state = models.CharField(choices=STATE_CHOICE, max_length=50)
 mobile = models.PositiveIntegerField()
 email = models.EmailField()
 job_city = models.CharField(max_length=50)
 profile_image = models.ImageField(upload_to='profileimg', blank=True)
 my_file = models.FileField(upload_to='doc', blank=True)


