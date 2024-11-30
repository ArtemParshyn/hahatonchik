from django.shortcuts import render

# Главная страница
def index(request):
    return render(request, 'index.html')

# Страница поиска сотрудников
def services(request):
    return render(request, 'services.html')

# Страница со списком всех сотрудников
def all_employees(request):
    return render(request, 'all_employees.html')

# Страница "О нас"
def about(request):
    return render(request, 'about.html')
