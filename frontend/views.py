from django.shortcuts import render
import requests
from joblib import load
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from account.models import User 
from django.shortcuts import render, redirect


model = load('./savedmodel/knn_model.joblib')
# Create your views here.
def index(request):
    return render(request,'index.html')
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = request.POST

        # Extract data from the request
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('password2')
        contact = data.get('contno')
        address = data.get('address')
        city = data.get('district')
        state = data.get('state')
        pincode = data.get('pincode')
        date_of_birth = data.get('date_of_birth')
        add_type = data.get('add_type')
        nation = data.get('nation')
        nationality = data.get('nationality')
        id_type = data.get('id_type')
        id_no = data.get('id_number')
        issue_date = data.get('issue_date')
        id_issue = data.get('id_issue')
        gender = data.get('gender')
        occupation = data.get('occupation')
        issue_state = data.get('issue_state')
        

        # Create a new user instance
        new_user = User(
            name=name,
            email=email,
            password=password,
            confirm_password=confirm_password,
            contact=contact,
            add_type=add_type,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            date_of_birth=date_of_birth,
            nation=nation,
            nationality=nationality,
            id_type=id_type,
            id_no=id_no,
            issue_date=issue_date,
            issue_state=issue_state,
            id_issue=id_issue,
            gender=gender,
            occupation=occupation,    
        )

        # Save the user to the database
        new_user.save()
        return redirect('login')
        #return JsonResponse({'message': 'User registered successfully'})

    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def main(request):
    return render(request,'main.html')


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
