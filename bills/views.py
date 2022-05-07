from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bill
from .forms import BillSortTypeForm
from .serializers import BillSerializer


class GetBillsInfoView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bills.html'

    def get(self, request):
        bills = Bill.objects.all()
        form = BillSortTypeForm()

        bills_for_queryset = BillSerializer(
            instance=bills,
            many=True
        )
        return Response({'bills': bills_for_queryset.data, 'form': form})

    def post(self, request):
        sorted_types = {
            '1': 'client_org',
            '2': 'bill_number',
            '3': 'bill_sum',
            '4': 'bill_date'
        }

        form = BillSortTypeForm(request.POST)
        if form.is_valid():
            sorted_type = form.cleaned_data['sorted_type']
            bills = Bill.objects.order_by(sorted_types[sorted_type])

            bills_for_queryset = BillSerializer(
                instance=bills,
                many=True
            )
            form = BillSortTypeForm()
            return Response({'bills': bills_for_queryset.data, 'form': form})
