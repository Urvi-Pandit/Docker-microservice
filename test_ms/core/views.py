from django.shortcuts import render

# Create your views here.

def main(request):
    if request.method == "POST" and request.POST['num1'] != NULL and request.POST['num2'] != NULL:
        sum = request.POST['num1'] + request.POST['num2']
        return render(request, 'homepage.html', {'sum':sum})