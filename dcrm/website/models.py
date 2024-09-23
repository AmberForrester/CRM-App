from django.db import models

#68 - Create a class, and abstract away to create the DB code on the backend for whatever DB you are using - behind the scenes. 

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # Time stamp auto create.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=20)
    
#69 - Calling one of these records defined above will only call the first and lastname. 
    def __str__(self):
        return(f'{self.first_name} {self.last_name}')