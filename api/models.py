from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.email})"


class Order(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.title} for {self.user.name}"
