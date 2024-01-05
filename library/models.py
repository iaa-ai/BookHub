from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id=models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.CharField(max_length=500, null=True, blank=True)
    user_image = models.ImageField(upload_to='data/image/user/', null=True, blank=True)
    def __str__(self):
        return self.user.username
    
class Author(BaseModel):
    name = models.CharField(max_length=100)
    birth_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name

class Member(BaseModel):
    ROLE_CHOICES = (
        ('Administrator', 'Administrator'),
        ('Moderator', 'Moderator'),
        ('Librarian', 'Librarian'),
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Staff', 'Staff'),
        ('Other', 'Other'),
    )
    mID = models.IntegerField(null=True,blank=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name

class Book(BaseModel):
    GENRE_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Biography', 'Biography'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('Film-Noir', 'Film-Noir'),
        ('History', 'History'),
        ('Horror', 'Horror'),
        ('Music', 'Music'),
        ('Musical', 'Musical'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Sport', 'Sport'),
        ('Thriller', 'Thriller'),
        ('War', 'War'),
        ('Western', 'Western'),
        ('Education', 'Education'),
        ('Kids', 'Kids'),
    )
    title = models.CharField(max_length=200)
    edition = models.CharField(max_length=50,null=True,blank=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    publication_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='data/image/books/', null=True, blank=True)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,blank=True)
    publisher = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    serial_number = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.title

class BookInstance(BaseModel):
    CONDITION_CHOICES = (
        ('New', 'New'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
        ('Damaged', 'Damaged'),
        ('Lost', 'Lost'),
    )
    book = models.ForeignKey(Book,on_delete=models.CASCADE,blank=True,null=True)
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE,blank=True,null=True)
    access_count = models.IntegerField(default=0)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=10, blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    check_in = models.DateField(blank=True, null=True)

# class BookImage(BaseModel):
#     image = models.ImageField(upload_to='images/user_images')
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.image.url