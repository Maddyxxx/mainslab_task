from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, Organization
from .serializers import ClientSerializer
from bills.models import Bill


class GetClientInfoView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients.html'

    def get(self, request):
        client_info = []
        clients = Client.objects.all()
        for client in clients:
            bills_sum = 0
            organizations = Organization.objects.filter(client=client)
            for organization in organizations:
                bills = Bill.objects.filter(client_org=organization)
                for bill in bills:
                    bills_sum += bill.bill_sum

            data = {
                'client_name': client.client_name,
                'organization_count': organizations.count(),
                'bills_sum': bills_sum
            }

            client_info.append(data)

        client_for_queryset = ClientSerializer(
            instance=client_info,
            many=True
        )
        return Response({'clients': client_for_queryset.data})
