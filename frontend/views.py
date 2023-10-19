from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def main(request):
    return render(request,'main.html')

from joblib import load
from django.shortcuts import render
from django.http import HttpResponse

model = load('./savedmodel/model.joblib')

def diabetes(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        pphone = request.POST.get('pphone')
        history = request.POST.get('history')
        gender = request.POST.get('gender')
        bp = request.POST.get('bp')
        smoke = request.POST.get('smoke')
        exe = request.POST.get('exe')
        diet = request.POST.get('diet')
        bmi = request.POST.get('bmi')
        fbs = request.POST.get('fbs')
        hba = request.POST.get('hba')

        # Prepare the data for prediction, and make sure to convert input values to the appropriate data types.
        # You'll need to adapt this code based on your model's input requirements.
        # For example, if your model expects numerical values, you should convert the input data to floats or integers.
        input_data = [history, gender, bp, smoke, exe, diet, float(bmi), float(fbs), float(hba)]
        
        # Make a prediction using the model (replace '[]' with the actual input data).
        y_pred = model.predict([input_data])

        if y_pred[0] == 0:
            y_pred = 'not having diabetes'
        else:
            y_pred = 'having diabetes'
        print(y_pred)
        # You can pass the result to the template for display.
        return render(request, 'diabetes.html', {'result': y_pred, 'pname': pname, 'pphone': pphone})

    return render(request, 'diabetes.html')
