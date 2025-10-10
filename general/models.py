from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
# Create your models here.
class User(models.Model):
  email = models.EmailField()
  full_name = models.CharField(max_length=150)
  password = models.CharField(max_length=50)
  date_regist = models.DateField()
        
  def __str__(self):
    return f"{self.full_name.title()}"
    
class Genres(models.Model):
  
  genre = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.genre.title()}"
  
class Movies(models.Model):
  genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  producer = models.CharField(max_length=150)
  year = models.CharField(blank=True,max_length=10)

  def __str__(self):
    return f"{self.name.title()}"
  
class WatchHistory(models.Model):
  rating = [
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars')
  ]
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_history')
  movie = models.ForeignKey(Movies, on_delete=models.CASCADE) 
  watched_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(null=True, blank=True, choices=rating)

  def __str__(self):
    return f"{self.movie.title()}"

class Subscriptions(models.Model):
  type_sub = [
    ('1', 'base'),
    ('2','standart'),
    ('3', 'premium')
  ]

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  plan = models.CharField(choices=type_sub, max_length=50)
  start_date = models.DateTimeField(auto_now_add=True)
  end_date = models.DateTimeField(null=True, blank=True)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return f"{self.plan.title()}"
  
class Payments(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  subscription = models.ForeignKey(Subscriptions, on_delete=models.CASCADE)
  payment_date = models.DateTimeField(auto_now_add=True)
  amount = models.PositiveIntegerField(default=0)

  def __str__(self):
    return f"{self.user}"