from django.db import models


# Create your models her
   
    

class Transaction(models.Model):

    category_type=(
        ('income','Income'),
        ('expense','Expense')
    )
    

    
    name=models.CharField(max_length=200)

    category=models.CharField(max_length=200,choices=category_type)

    amount=models.DecimalField(max_digits=10,decimal_places=2)

    date=models.DateTimeField(auto_now_add=True)

    description=models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}-{self.category}-{self.amount}"
