from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
  return render(request, 'home.html', {
    'new_riddle_question': request.POST.get('riddle_question', ''),
  })
