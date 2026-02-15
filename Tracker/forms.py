from django import forms
from .models import Transaction,Category

class TransactionForm(forms.ModelForm):
    category_name = forms.CharField(label="Category Name")
    category_type = forms.ChoiceField(
        choices=Category.Category_Type,
        label="Type"
    )
    class Meta:
        model=Transaction
        fields=['category_name','category_type','amount','description']

    def save(self,user=None,commit=True):
        category_name=self.cleaned_data['category_name']
        category_type=self.cleaned_data['category_type']

        category_obj,crated=Category.objects.get_or_create(
            name=category_name,
            user=user,
            defaults={'category':category_type}
        )
        transaction = super().save(commit=False)
        transaction.category = category_obj
        transaction.user = user

        if commit:
            transaction.save()

        return transaction    


    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user',None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['category'].queryset=Category.objects.filter(user=user)



