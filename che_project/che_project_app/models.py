from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

class Brand(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

class Car_model(models.Model):
    model_name = models.CharField(max_length=255, null=False)

class Car_status(models.Model):
    status = models.CharField(max_length=255, null=False)

class Car(models.Model):
    id = models.AutoField
    user_id = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.ForeignKey(Car_model, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, null=False)
    capacity = models.IntegerField()
    price = models.IntegerField()
    plate_number = models.CharField(max_length=50, null=False)
    fuel = models.FloatField()
    rental_available = models.BooleanField()
    car_status = models.ForeignKey(Car_status, on_delete=models.CASCADE)
    lend_start_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    lend_end_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

class Purpose(models.Model):
    id = models.AutoField
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    type = models.IntegerField(default=1)
    # type=1 誰が, type=2 どこで, type=3 何をする
    name = models.CharField(max_length=255, null=False)

class Car_images(models.Model):
    id = models.AutoField
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    path = models.ImageField(upload_to='static/car_images')
    display_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

class Car_weekday(models.Model):
    id = models.AutoField
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    day = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
