from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.deletion import CASCADE

User = get_user_model()


class Slideshow(models.Model):
    slideName = models.CharField(max_length=100)
    images = models.ImageField(upload_to="Slideshow")
    slug = models.SlugField()

    def __str__(self):
        return self.slideName


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_slug = models.SlugField(default=False, null=True)
    category_img = models.ImageField(upload_to='category_image')
    category_description = models.TextField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_image = models.ImageField(upload_to='product_image')
    product_image1 = models.ImageField(upload_to='product_image')
    product_Name = models.CharField(max_length=200, blank=True)
    prices = models.FloatField(default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_description = models.TextField(max_length=100)

    class ConditionChoices(models.TextChoices):
        NEW = 'N', 'New'
        LIKE_NEW = 'ULN', 'Used-like New'
        NEW_GOOD = 'NG', 'New-Good'
        USED_FAIR = 'UF', 'Used-Fair'

    Condition = models.CharField(
        max_length=5,
        choices=ConditionChoices.choices,
        default=ConditionChoices.NEW
    )
    location = models.CharField(max_length=200, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # validators should be a list
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True,
                                    blank=True)
    facebook_userName = models.CharField(max_length=200, null=True, blank=True)
    whatsapp_number = models.IntegerField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    owner = models.ForeignKey(User, related_name='owner', null=True, on_delete=CASCADE)

    def __str__(self) -> str:
        return f'owner: {self.owner} product_Name: {self.product_Name}'
