from django.urls import path
from .views import LoadBills, LoadClientOrg

urlpatterns = [
    path('load_client_org', LoadClientOrg.as_view(), name='загрузка файла с клиентами и компаниями'),
    path('load_bills', LoadBills.as_view(), name='загрузка файла со счетами'),
]
