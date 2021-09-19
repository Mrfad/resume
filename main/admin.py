from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

class AboutAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('header', 'img', 'title', 'intro',
                'bday', 'website', 'phone', 'city', 
                'age', 'degree', 'email', 'freelance',
                'long_description')
admin.site.register(About, AboutAdmin)

class SkillTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('name',)
admin.site.register(SkillType, SkillTypeAdmin)

class SkillAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_editable=('level',)
    list_display=('name', 'level')
admin.site.register(Skill, SkillAdmin)

class FactDescriptiontAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('description',)
admin.site.register(FactDescription, FactDescriptiontAdmin)

class FactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_editable=('number',)
    list_display=('fact_name', 'number')
admin.site.register(Fact, FactAdmin)

class ExperienceDEtailAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('duty',)
admin.site.register(ExperienceDEtail, ExperienceDEtailAdmin)

class ExperienceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_editable=('from_year', 'to_year')
    list_display=('company_name', 'title', 'from_year', 'to_year')
admin.site.register(Experience, ExperienceAdmin)

class CollegeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('college_name',)
admin.site.register(College, CollegeAdmin)

class CertificationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_editable=('cert_date', 'college')
    list_display=('cert_name', 'cert_date', 'college', 'description')
admin.site.register(Certification, CertificationAdmin)

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('name', 'email', 'subject', 'message_date', 'message')
admin.site.register(Contact, ContactAdmin)

