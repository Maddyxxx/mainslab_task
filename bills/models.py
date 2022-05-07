from django.db import models
from clients.models import Organization


class Bill(models.Model):

    client_org = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name='организация клиента',
    )

    bill_number = models.IntegerField(
        default=1,
        verbose_name='номер счета',
    )

    bill_sum = models.IntegerField(
        default=1,
        verbose_name='сумма по счету'
    )

    bill_date = models.DateField(
        verbose_name='дата счета'
    )

    class Meta:
        unique_together = (("client_org", "bill_number"),)

    def __str__(self):
        return f'{self.bill_number}'
