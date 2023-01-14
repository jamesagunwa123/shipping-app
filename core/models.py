from django.db import models

# Create your models here.

class Product(models.Model): 
    tracking_code = models.CharField(max_length=250, null=False, unique=True)
    current_status = models.CharField(max_length=250, blank=True, null=True)
    current_location = models.CharField(max_length=250, blank=True, null=True)
    amount_paid = models.CharField(max_length=250, blank=True, null=True)
    origin = models.CharField(max_length=250, blank=True, null=True)
    destination = models.CharField(max_length=250, blank=True, null=True)
    services = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=250, blank=True, null=True)
    weight = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    date_sent = models.CharField(max_length=250, blank=True, null=True)
    expected_delivery_date = models.CharField(max_length=250, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    sender_name = models.CharField(max_length=250, blank=True, null=True)
    sender_country = models.CharField(max_length=250, blank=True, null=True)
    consignee_name = models.CharField(max_length=250, blank=True, null=True)
    consignee_address = models.CharField(max_length=250, blank=True, null=True)
    consignee_country = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.tracking_code
