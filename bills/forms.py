from django import forms


class BillSortTypeForm(forms.Form):
    sorted_type = forms.ChoiceField(
        choices=((1, 'Организация клиента'), (2, 'Номер счета'), (3, 'Сумма по счету'), (4, 'Дата счета')),
        label='Тип сортировки'
    )