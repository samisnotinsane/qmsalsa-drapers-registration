from django.db import models

# Ask for the following fields from guests:
# First name
# Surname
# Email
# Instagram
# Have you done any salsa before?
# Amount paid

class Guest():
    first_name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    email = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    is_new_to_salsa = models.BooleanField(default=True)
    amount_paid = models.DecimalField(null=False, max_digits=3, decimal_places=2)

