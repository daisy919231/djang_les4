from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=70, unique=True)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    
    name=models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    price=models.FloatField()
    category=models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    quantity=models.IntegerField(default=0)
    rating=models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
    discount=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to='products', null=True, blank=True)


    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1-self.discount/100)
        return self.price

    def __str__(self):
        return self.name
    
    @property
    def get_image(self):
        if self.image:
            return self.image.url
        return None
    
# User degan table ham yaratilishi kerak #

# class User(models.Model):
#     name=models.CharField(max_length=100)
#     address=models.TextField()
#     phone_number=models.TextField()


# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=100)
    email=models.TextField()
    product=models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    comment=models.TextField()
   

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['product_id', 'user_id'], name='unique_product_user_comment')
#         ]

#     def __str__(self):
#         return f'Comment {self.comment_id} by {self.user_id} on {self.product_id}'

# class Order(models.Model):
#     name=models.CharField(max_length=100)
#     phone_number=models.TextField()
#     user=models.ForeignKey('User', on_delete=models.CASCADE, related_name='users')


#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['user_id'], name='unique_user_order')
#         ]




    