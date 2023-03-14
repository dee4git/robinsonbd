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

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    serial_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=1000, default='Product Name', null=False, blank=False)
    pack_size = models.CharField(max_length=1000, default='pack size', null=False, blank=False)
    use_case = models.CharField(max_length=1000, default='use case', null=False, blank=False)
    dose = models.CharField(max_length=1000, default='dose', null=False, blank=False)
    show_at_homepage = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CategoryCertification(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    serial_number = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='media/product-certifications')

    def __str__(self):
        return self.serial_number


class CategoryFeatures(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    serial_number = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='media/product-certifications')

    def __str__(self):
        return self.serial_number


class CategoryHowToUse(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    step_number = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='media/product-how-to-use')

    def __str__(self):
        return self.step_number
