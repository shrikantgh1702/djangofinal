from django.shortcuts import render
from .models import customersDetailsModel
from .forms import customerDetailForm
from django.http import HttpResponse
from .common import *
from .predection_pipeline import PredictionPipeline,CustomData

# Create your views here.

def details_view(r):
    form = customerDetailForm()
    if r.method == 'POST':
        form = customerDetailForm(r.POST)
        if form.is_valid():
            data_dict = form.cleaned_data
            #form.save()
            #print(data_dict)
            #print("*"* 50)


            CustomData_obj = CustomData(**data_dict)
            df = CustomData_obj.get_data_as_data_frame()

            PredictionPipeline_obj = PredictionPipeline()


            pred = PredictionPipeline_obj.predict(df)
            print(pred)

            if pred[0]:
                return HttpResponse("""<h1 align> There is a good chance that this customer will choose a term deposit. </h1> <br>
                                    <h1> You should contact this customer.  </h1>""")
            else:
                return HttpResponse("""<h1 align> There is a low chance that this customer will choose a term deposit. </h1> <br>
                                                    <h1> You should skip this customer.  </h1>""")
            #print(df)





            return HttpResponse(f"Form Submitted and result {output}")

    return render(r,'customerdetails.html',{'form': form},)



