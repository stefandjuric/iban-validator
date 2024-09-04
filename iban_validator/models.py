from django.db import models

class IbanHistory(models.Model):
    iban = models.CharField(max_length=34)
    is_valid = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.iban


class SuggestedIban(models.Model):
    iban = models.CharField(max_length=34)
    is_valid = models.BooleanField()
    suggested_iban = models.CharField(max_length=34)

    def __str__(self):
        return self.iban