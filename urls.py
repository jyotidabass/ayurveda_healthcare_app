from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required

from webapp.apps import WebappConfig

app_name = WebappConfig.name

urlpatterns = [
    path(
        'favicon.ico',
        RedirectView.as_view(url=staticfiles_storage.url('webapp/favicon.png'))
    ),
    path(
        '', TemplateView.as_view(template_name='webapp/index.html'),
        name='index'),
    path(
        'about-rasayu',
        TemplateView.as_view(template_name='webapp/about_rasayu.html'),
        name='about_rasayu'),
    path(
        'about',
        TemplateView.as_view(template_name='webapp/about.html'),
        name='about'),
    path(
        'tos',
        TemplateView.as_view(template_name='webapp/tos.html'),
        name='tos'),
    path(
        'wellness-assessment',
        login_required(
            TemplateView.as_view(
                template_name='webapp/wellness_assessment.html')),
        name='wellness_assessment'),
    path(
        'svasthya-questionnaire',
        login_required(
            TemplateView.as_view(
                template_name='webapp/svasthya_questionnaire.html')),
        name='svasthya_questionnaire'),
    path(
        'svasthya-questionnaire/<int:pk>/',
        login_required(
            TemplateView.as_view(
                template_name='webapp/svasthya_questionnaire.html')),
        name='svasthya_questionnaire'),
    path(
        'prakriti-assessment',
        login_required(
            TemplateView.as_view(
                template_name='webapp/prakriti_assessment.html')),
        name='prakriti_assessment'),
]
