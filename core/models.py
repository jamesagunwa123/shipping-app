from django.db import models

# Create your models here.

class Product(models.Model): 
    tracking_code = models.CharField(max_length=250, blank=True, null=True, default='')
    current_status = models.CharField(max_length=250, blank=True, null=True, default='')
    current_location = models.CharField(max_length=250, blank=True, null=True, default='')
    amount_paid = models.CharField(max_length=250, blank=True, null=True, default='')
    origin = models.CharField(max_length=250, blank=True, null=True, default='')
    destination = models.CharField(max_length=250, blank=True, null=True, default='')
    services = models.CharField(max_length=250, blank=True, null=True, default='')
    type = models.CharField(max_length=250, blank=True, null=True, default='')
    weight = models.CharField(max_length=250, blank=True, null=True, default='')
    description = models.CharField(max_length=250, blank=True, null=True, default='')
    date_sent = models.CharField(max_length=250, blank=True, null=True, default='')
    expected_delivery_date = models.CharField(max_length=250, blank=True, null=True, default='')
    comments = models.CharField(max_length=250, blank=True, null=True, default='')
    sender_name = models.CharField(max_length=250, blank=True, null=True, default='')
    sender_country = models.CharField(max_length=250, blank=True, null=True, default='')
    consignee_name = models.CharField(max_length=250, blank=True, null=True, default='')
    consignee_address = models.CharField(max_length=250, blank=True, null=True, default='')
    consignee_country = models.CharField(max_length=250, blank=True, null=True, default='')

    def __str__(self):
        return self.tracking_code
