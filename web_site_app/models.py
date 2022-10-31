from django.db import models


# Create your models here.
class CarType(models.Model):
    type = models.CharField(max_length=60)

    def __str__(self):
        return self.type


class Services(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField()
    description = models.TextField(max_length=500, null=False)

    def __str__(self):
        return self.name


class Price(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=False)
    type = models.ForeignKey(CarType, on_delete=models.CASCADE, null=False)
    price = models.CharField(max_length=20, null=False)


class Gallery(models.Model):
    car = models.CharField(max_length=20, null=False)
    car_picture = models.ImageField()
    works = models.TextField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=False)


class CarImages(models.Model):
    car = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    car_images = models.ImageField()


class CarWork(models.Model):
    car = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    car_work = models.CharField(max_length=60)
