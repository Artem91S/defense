from django.shortcuts import render, redirect
from django.views.generic import CreateView
import pandas as pd
from uuid import uuid4

from .models import Client
from .form import CreditForm
import time
from analysing_data.training_of_model import pipeline


def success(request):
    user = Client.objects.last()
    print(user.promo_code)
    return render(request, 'success.html', context={'promo': user.promo_code, 'title': 'Success page'})


def unsuccess(request):
    return render(request, 'unsuccess.html', context={'title': 'Unsuccess page'})


class GetDataUser(CreateView):
    form_class = CreditForm
    template_name = 'index.html'
    success_url = ''
    extra_context = {
        'title': 'Main Page'
    }

    def form_valid(self, form):
        data = form.save(commit=False)
        name = form.cleaned_data.pop('name')
        df = pd.DataFrame([form.cleaned_data])
        promo = uuid4()
        p = pipeline.predict(df)

        if p[0] == 1:
            print("Кредит схвалено")
            data.promo_code = promo
            data.name = name
            form.save(data)
            return redirect('success', )
        else:
            print("Кредит не схвалено")
            return redirect('unsuccess', )
