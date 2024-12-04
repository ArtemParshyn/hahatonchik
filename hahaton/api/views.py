import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from api.models import Employee, Project


# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def search_page(request):
    data = json.loads(request.body)
    print(data)
    experience = int(data.get("experience"))
    position = data.get("post")
    project = data.get("project")
    zavisit = data.get('department')
    salary = int(data.get('salary'))
    print(experience, position, project, zavisit, salary)
    employees = Employee.objects.all().filter(stazh=experience,
                                              position=position,
                                              project=Project.objects.all().get(name=project),
                                              zevisit=Employee.objects.all().get(fio=zavisit),
                                              salary=salary).values('id', 'fio', 'age', 'date_of_birth')
    empl = []
    for i in employees:
        print(i)
        empl.append({
            'id': i['id'],
            'fio': i['fio'],
            'age': i['age'],
            'date_of_birth': i['date_of_birth'],
        })
    return JsonResponse({"employees": empl})


# Страница поиска сотрудников
def services(request):
    return render(request, 'services.html', context={"dolzhns": Employee.objects.distinct().values('position'),
                                                     "departs": Employee.objects.distinct(),
                                                     'projects': Project.objects.all()})


# Страница со списком всех сотрудников
def all_employees(request):
    return render(request, 'all_employees.html')


# Страница "О нас"
def about(request):
    return render(request, 'about.html')
