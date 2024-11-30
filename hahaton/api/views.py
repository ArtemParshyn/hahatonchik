import json

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def search_page(request):
    data = json.loads(request.body)
    fio = data.get("fio")
    stazh = data.get("stazh")
    dolzhnost = data.get("dolzhnost")
    number = data.get("number")
    mail = data.get("mail")



