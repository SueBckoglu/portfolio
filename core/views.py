from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from core.models import GeneralSetting, Skill, Experience, Education, SocialMedia, Language, Reference, Project

def index(request):
    # Genel ayarlar
    general_settings = GeneralSetting.objects.filter(name__in=[
        'site_title', 'about', 'name', 'pronoun', 'about_me',
        'age', 'degree', 'email', 'freelance_status',
        'website', 'phone', 'city', 'about_me_details'
    ])
    settings_dict = {setting.name: setting.parameter for setting in general_settings}

    # Yetenekler
    frontend_skills = Skill.objects.filter(category='Frontend Development').order_by('order')
    backend_skills = Skill.objects.filter(category='Backend Development').order_by('order')
    programming_skills = Skill.objects.filter(category='Programming & Scripting').order_by('order')
    soft_skills = Skill.objects.filter(category='Professional & Soft Skills').order_by('order')

    # Deneyimler, Eğitimler, Sosyal Medya, Diller, Referanslar ve Projeler
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    social_medias = SocialMedia.objects.all()
    languages = Language.objects.all()
    references = Reference.objects.all()
    projects = Project.objects.all()

    context = {
        **settings_dict,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'programming_skills': programming_skills,
        'soft_skills': soft_skills,
        'experiences': experiences,
        'educations': educations,
        'social_medias': social_medias,
        'languages': languages,
        'references': references,
        'projects': projects,
    }
    return render(request, 'index.html', context=context)

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # E-posta gönderme işlemi
        send_mail(
            f"Message from {subject}",
            f"Name: {name}\nEmail: {email}\n\n{message}",
            settings.DEFAULT_FROM_EMAIL,
            ['suebckoglu@gmail.com'],
        )

        return render(request, 'index.html', {"message_name": name})
    else:
        return render(request, 'index.html', {"message_name": "sa"})
