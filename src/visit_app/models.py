from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    @property
    def is_authenticated(self):
        return True


class Store(models.Model):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Visit(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.employee.name} visit to {self.store.name} at {self.timestamp}"
