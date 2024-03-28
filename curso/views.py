from django.shortcuts import render
from django.utils import timezone
from .models import Curso

def curso_list(request):
    cursos = Curso.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'curso/curso_list.html', {'cursos': cursos})
