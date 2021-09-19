from main.admin import SkillAdmin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from datetime import date, datetime
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
import json
import urllib

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

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
 
            if result['success']:
                form.save()
                messages.success(request, 'Comment sent successfully')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            # return HttpResponseRedirect(request.path_info)

    form = ContactForm()
    
    context = {'about':about, 'skills':skills, 'age':age,
                'facts':facts, 'fact_text':fact_text,
                'experience':experience, 'certs':certs,
                'form':form}
    return render(request, 'home.html', context)
