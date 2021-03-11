from django.conf import settings
from django.db import models
from django.utils import timezone

WARANTY_IW = 'IW'
WARANTY_OOW = 'OOW'
WARANTY_TBD = 'TBD'
WARANTY_CHOICE = (
    (WARANTY_IW, (u'IW')),
    (WARANTY_OOW, (u'OOW')),
    (WARANTY_TBD, (u'TBD')),
)

STATUS_1 = 'Shipped'
STATUS_2 = 'Waiting for Shipping'
STATUS_3 = 'Waiting for Quotation'
STATUS_4 = 'Waiting for Spare Parts'
STATUS_5 = 'Waiting for Testing'
STATUS_6 = 'Waiting for Repair'
STATUS_7 = 'No need Repair'
STATUS_CHOICE = (
    (STATUS_1, (u'Shipped')),
    (STATUS_2, (u'Waiting for Shipping')),
    (STATUS_3, (u'Waiting for Quotation')),
    (STATUS_4, (u'Waiting for Spare Parts')),
    (STATUS_5, (u'Waiting for Testing')),
    (STATUS_6, (u'Waiting for Repair')),
    (STATUS_7, (u'No need Repair')),
)

REPAIR_METHOD1 = 'Return without Repair'
REPAIR_METHOD2 = 'Replace parts'
REPAIR_METHOD3 = 'Software upgrade'
REPAIR_METHOD4 = 'Reassemblee'
REPAIR_METHOD_CHOICE = (
    (REPAIR_METHOD1, (u'Return without Repair')),
    (REPAIR_METHOD2, (u'Replace parts')),
    (REPAIR_METHOD3, (u'Software upgrade')),
    (REPAIR_METHOD4, (u'Reassemblee')),
)

ENGENIEER1 = 'Nikolai'
ENGENIEER2 = 'Vlad'
ENGENIEER3 = 'Lyon'
ENGENIEER_CHOICE = (
    (ENGENIEER1, (u'Nikolai')),
    (ENGENIEER2, (u'Vlad')),
    (ENGENIEER3, (u'Lyon')),
)
class Unit(models.Model):
    NO = models.AutoField(primary_key=True)
    model = models.CharField(max_length=5)
    imei = models.CharField(max_length=20)
    cinnoSid = models.CharField(max_length=25)
    customer = models.CharField(max_length=20)
    rma = models.CharField(max_length=20)
    reciveDate = models.DateField()
    userContact = models.CharField(max_length=20)
    acessoryList = models.CharField(max_length=50)
    trackNumberInn = models.CharField(max_length=20)
    warantyType = models.CharField(max_length=10, choices=WARANTY_CHOICE)
    faultDescription = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)
    repairDate = models.DateField()
    repairMethod = models.CharField(max_length=50, choices=REPAIR_METHOD_CHOICE)
    waitingParts = models.CharField(max_length=70)
    replacedParts = models.CharField(max_length=70)
    engenieer = models.CharField(max_length=10, choices=ENGENIEER_CHOICE)
    shipDate = models.DateField()
    trackNumberOutt = models.CharField(max_length=20)
    notes = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.cinnoSid
