from django.db import models


class CountryInformation(models.Model):
    """ Models to store informations of all Countries """
    country_name    = models.CharField(max_length=25, unique=True)
    country_code    = models.CharField(max_length=15)
    iso_code        = models.CharField(max_length=10)
    population      = models.CharField(max_length=20)
    area            = models.CharField(max_length=20)
    flag            = models.ImageField(null=True, upload_to='images')

    def __str__(self):
        return self.country_name

    def save(self, *args, **kwargs):
        self.country_name = self.country_name.upper()
        self.iso_code = self.iso_code.upper()
        return super(CountryInformation, self).save(*args, **kwargs)
