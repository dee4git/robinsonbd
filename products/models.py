from django.db import models


# Create your models here.
class Category(models.Model):
    serial_number = models.IntegerField(unique=True)
    name = models.CharField(default='Category Name', max_length=1000, null=False, blank=False)
    description = models.CharField(default='category description', max_length=1000, null=False, blank=False)
    question_1 = models.CharField(default='---', max_length=1000, null=False, blank=False)
    answer_1 = models.CharField(default='---', max_length=1000, null=False, blank=False)
    question_2 = models.CharField(default='---', max_length=1000, null=False, blank=False)
    answer_2 = models.CharField(default='---', max_length=1000, null=False, blank=False)
    question_3 = models.CharField(default='---', max_length=1000, null=False, blank=False)
    answer_3 = models.CharField(default='---', max_length=1000, null=False, blank=False)
    photo = models.ImageField(upload_to='media/category-picture', null=True, blank=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    serial_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, default='Product Name', null=False, blank=False)
    pack_size = models.CharField(max_length=100, default='Product Name', null=False, blank=False)
    use_case = models.CharField(max_length=100, default='Product Name', null=False, blank=False)
    visibility = models.BooleanField(default=True)


class ProductCertification(models.Model):
    product = models.ForeignKey(Category, on_delete=models.CASCADE)
    serial_number = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='media/product-certifications')


class ProductHowToUse(models.Model):
    product = models.ForeignKey(Category, on_delete=models.CASCADE)
    step_number = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='media/product-how-to-use')