from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    Category_Type=(
        ('income','Income'),
        ('expense','Expense'),
    )

    name=models.CharField(max_length=200)
    category=models.CharField(max_length=200,choices=Category_Type)

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.category})"
    

class Transaction(models.Model):
    

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    amount=models.DecimalField(max_digits=10,decimal_places=5)

    date=models.DateTimeField()

    description=models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}-{self.amount}-{self.transaction}"
