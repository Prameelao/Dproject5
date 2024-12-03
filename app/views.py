from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Varsha','age':'22','city':'Nellore'}
    return render(request,'jinja_print.html',context=d)
