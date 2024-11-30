import json

from django.shortcuts import render

from api.models import Employee


# Create your views here.
def index(request):
    return render(request, 'index.html',
                  context={"dolzhn": Employee.objects.all().distinct('position'),
                           })


def search_page(request):
    data = json.loads(request.body)
    experience = data.get("experience")
    position = data.get("post")
    project = data.get("project")
    zavisit = data.get('department')
    salary = data.get('salary')
    employees = Employee.objects.all().filter(stazh=experience,
                                              position=position,
                                              project=project,
                                              zavisit=zavisit,
                                              salary=salary).values('id', 'fio', 'age', 'date_of_birth')


    return JsonResponse({"employees": fgkjldfhipgpsdfjghp})


