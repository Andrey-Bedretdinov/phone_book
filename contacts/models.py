from django.db import models


class LastName(models.Model):
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name


class FirstName(models.Model):
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class MiddleName(models.Model):
    middle_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.middle_name


class Street(models.Model):
    street_name = models.CharField(max_length=150)

    def __str__(self):
        return self.street_name


class Contact(models.Model):
    last_name = models.ForeignKey(LastName, on_delete=models.CASCADE)
    first_name = models.ForeignKey(FirstName, on_delete=models.CASCADE)
    middle_name = models.ForeignKey(MiddleName, on_delete=models.CASCADE, blank=True, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building_number = models.CharField(max_length=10)
    building_unit = models.CharField(max_length=10, blank=True, null=True)
    apartment = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.phone}"
