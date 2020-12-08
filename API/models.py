
from django.db import models
from django.core.validators import validate_image_file_extension
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user')
    avatar = models.ImageField(verbose_name = 'Image', upload_to='media/', 
    validators=[validate_image_file_extension], blank=True, null = True)

    class Meta:
        verbose_name = "Profile"     
        verbose_name_plural = "Profiles"
        db_table = "profiles"

    def __str__(self):
        return self.user.get_full_name()



class Book(models.Model):
    user = models.ForeignKey(User, verbose_name = "User", on_delete = models.CASCADE)
    name = models.CharField(max_length = 255, verbose_name=("Name"))
    pages = models.IntegerField(verbose_name=("Pages"))
    date = models.DateTimeField(max_length = 255, verbose_name=("Date"),auto_now = True)
    author2 = models.CharField(max_length = 255, verbose_name=("Author 2"))
    description = models.TextField(verbose_name=("Description"))

    class Meta:
        verbose_name = "Book"     
        verbose_name_plural = "Books"
        db_table = "books"

    def __str__(self):
        return self.name



class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name = "User", on_delete = models.CASCADE)
    content = models.TextField(verbose_name=("Content"))
    date = models.DateTimeField(max_length = 255, verbose_name=("Date"), auto_now = True)

    class Meta:
        verbose_name = "Comment"     
        verbose_name_plural = "Comments"
        db_table = "comments"

    def __str__(self):
        return self.content


class Rating(models.Model):
    user = models.ForeignKey(User, verbose_name = "User", on_delete = models.CASCADE)
    book = models.ForeignKey(Book,verbose_name = "Book", on_delete = models.CASCADE)
    rate = models.IntegerField(verbose_name="Rate")

    class Meta:
        verbose_name = "Rating"     
        verbose_name_plural = "Ratings"
        db_table = "ratings"

    def __str__(self):
        return self.rate


class Reviews(models.Model):
    user = models.ForeignKey(User, verbose_name = "User", on_delete = models.CASCADE)
    book = models.ForeignKey(Book,verbose_name = "Book", on_delete = models.CASCADE)
    content = models.TextField(verbose_name=("Content"))
    date = models.DateTimeField(max_length = 255, verbose_name=("Date"), auto_now = True)

    class Meta:
        verbose_name = "Review"     
        verbose_name_plural = "Review"
        db_table = "reviews"

    def __str__(self):
        return self.content


class Messages(models.Model):
    user_from = models.ManyToManyField(User, verbose_name = "From User")
    user_to = models.ManyToManyField(Book,verbose_name = "To User")
    message = models.TextField(verbose_name=("Message"))
    created_at = models.DateTimeField(max_length = 255, verbose_name=("Created At"), auto_now = True)


    class Meta:
        verbose_name = "Message"     
        verbose_name_plural = "Message"
        db_table = "message"

    def __str__(self):
        return self.message



"""
Model to return word translation
"""
class Translation(models.Model):
    books = models.ManyToManyField(Book, verbose_name="Books")
