from django.shortcuts import render
from django.db.utils import IntegrityError
import openpyxl
from clients.models import Client, Organization
from bills.models import Bill


def get_table_data(excel_file):
    data = {}
    sheet_names = []
    wb = openpyxl.load_workbook(excel_file)
    sheets = wb.sheetnames
    for sheet in sheets:
        sheet_names.append(sheet)
        worksheet = wb[sheet]
        data[sheet] = []
        for row in worksheet.iter_rows():
            row_data = [i.value for i in row if i.value is not None]
            data[sheet].append(row_data)
        data[sheet] = data[sheet][1:]
    return data, sheet_names


def load_client_org(request):
    if "GET" == request.method:
        return render(request, 'load_client_org.html', {})
    else:
        data = {}
        excel_file = request.FILES["excel_file"]
        table_data, sheet_names = get_table_data(excel_file)
        clients = table_data[sheet_names[0]]
        for client in clients:
            client_ = Client(client_name=client[0])
            try:
                client_.save()
            except IntegrityError:
                pass
        organizations = table_data[sheet_names[1]]
        for organization in organizations:
            client = Client.objects.get(client_name=organization[0])
            if client:
                org = Organization(
                    client=client,
                    organization_name=organization[1]
                )
                try:
                    org.save()
                except IntegrityError:
                    pass
        return render(request, 'load_client_org.html')


def load_bills(request):
    if "GET" == request.method:
        return render(request, 'load_bills.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        table_data, sheet_names = get_table_data(excel_file)
        bills = table_data[sheet_names[0]]
        for bill in bills:
            client_org = Organization.objects.get(organization_name=bill[0])
            if client_org:
                new_bill = Bill(
                    client_org=client_org,
                    bill_number=bill[1],
                    bill_sum=bill[2],
                    bill_date=bill[3]
                )
                try:
                    new_bill.save()
                except IntegrityError:
                    pass

        return render(request, 'load_bills.html')
