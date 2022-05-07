from django.db import models


class Client(models.Model):

    client_name = models.CharField(
        max_length=30,
        default='',
        verbose_name='клиент',
        unique=True
    )

    def __str__(self):
        return self.client_name


class Organization(models.Model):

    client = models.ForeignKey(
        Client,
        verbose_name='клиент',
        on_delete=models.CASCADE
    )

    organization_name = models.CharField(
        max_length=50,
        default='',
        verbose_name='наименование организации',
        unique=True
    )

    class Meta:
        unique_together = (("client", "organization_name"),)

    def __str__(self):
        return self.organization_name




