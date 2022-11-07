from django.shortcuts import render
from django.http import  HttpResponse

TEMPLATE_DIRS=(
    'os.path.join(BASE_DIR,"templates"),'
)

def index(request):
    return render(request,"index.html")

def charts(request):
    return render(request,"charts.html")

def tables(request):
    return render(request,"tables.html")
def login(request):
    return render(request,"login.html")