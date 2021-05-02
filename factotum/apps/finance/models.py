from django.db import models
from internationalflavor.iban.models import IBANField
from enum import Enum


class TransactionKind(Enum):
    TRANSFER = "PRZELEW"
    ORDER = "ST.ZLEC"
    BLIK = "TR.BLIK"
    CARD = "TR.KART"

    @classmethod
    def choices(cls):
        return [(k.name, k.value) for k in cls]


class Transaction(models.Model):
    trade_date = models.DateField()
    booking_date = models.DateField()
    contractor_data = models.CharField(max_length=255)
    description = models.CharField(max_length=140)
    contractor_account_number = IBANField()
    contractor_bank_name = models.CharField(max_length=70)
    kind = models.CharField(max_length=15, choices=TransactionKind.choices())
    number = models.CharField(max_length=50)
    account_number = IBANField()
