from main.admin import SkillAdmin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from datetime import date, datetime
from .forms import ContactForm

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def home(request):
    id = request.user.id
    about = About.objects.get(id=1)
    facts = Fact.objects.all()
    certs = Certification.objects.all()
    experience = Experience.objects.all()
    fact_text = FactDescription.objects.get(id=1)
    born = about.bday
    age = calculate_age(born)
    skills = Skill.objects.all()
    msg = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Message submitted successfuly'
            # return HttpResponseRedirect(request.path_info)
    form = ContactForm()
    
    context = {'about':about, 'skills':skills, 'age':age,
                'facts':facts, 'fact_text':fact_text,
                'experience':experience, 'certs':certs,
                'msg':msg, 'form':form}
    return render(request, 'home.html', context)
