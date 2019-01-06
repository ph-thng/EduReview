from django.db import models
import numpy as np

class Schools(models.Model):
    
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    like = models.BigIntegerField()
    dislike = models.BigIntegerField()
    educators = models.CharField(max_length=100)
    
    def __str__(self):
        return(f"{self.name} : {self.address}, {self.city}, {self.location}")
    
    def average_rating(self):
        
        try:
            all_ratings = map(lambda x: x.rating, self.review_set.all())
            return np.mean(all_ratings)
        except Exception as rating_error:
            print(rating_error)


class SchoolReviews(models.Model):
    rating_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    school = models.ForeignKey(Schools, on_delete= models.CASCADE)
    # Rating categories
    reputation = models.IntegerField(choices= rating_choices, )
    reputation = models.IntegerField(choices= rating_choices)
    location = models.IntegerField(choices= rating_choices)
    food = models.IntegerField(choices= rating_choices)
    facility = models.IntegerField(choices= rating_choices)
    rules = models.IntegerField(choices= rating_choices)
    ec_activity = models.IntegerField(choices= rating_choices)
    happiness = models.IntegerField(choices= rating_choices)
    safety = models.IntegerField(choices= rating_choices)
    # User's review
    user_name = models.CharField(max_length=30)
    comment = models.CharField(max_length=350)


    

            


    


