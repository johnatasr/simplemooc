from django.shortcuts import redirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_list_or_404
from .models import Course
from .forms import ContactCourse
from django.conf import settings
from django.http import HttpResponse, JsonResponse



def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

# def details(request, pk):
#      course = get_list_or_404(Course, pk=pk)
#      if request.method == 'POST':
#         form = ContactCourse(request.POST)
#      else:
#         form = ContactCourse()
#
#      context = {
#          'course': course,
#           'form' : form
#      }
#      template_name = 'courses/details.html'
#
#      return render(request, template_name, context)
#
# def details(request, slug):
#     course = get_list_or_404(Course, slug=slug)
#     context = {}
#     if request.method == 'POST':
#         form = ContactCourse(request.POST)
#         if form.is_valid:
#             context['is_valid'] = True
#             form.send_mail(course)
#             #print(form.cleaned_data['message'])
#             #form = ContactCourse()
#
#     else:
#         form = ContactCourse()
#
#     context['course'] = course
#     context['form'] = form
#     template_name = 'courses/details.html'
#
#     return render(request, template_name, context)

def details(request, slug):

    course = Course.objects.get(slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            subject = '[%s] Contato' % course
            # email = form.cleaned_data['email']
            # name = form.cleaned_data['name']
            # message = form.cleaned_data['message']
            # try:
            #     send_mail(subject, message, email, [settings.CONTACT_EMAIL])
            # except BadHeaderError:
            #     return HttpResponse('Cabeçalho errado !')
            form.send_mail(course)
    else:
        form = ContactCourse()


    context['course'] = course
    context['form'] = form
    template_name = 'courses/details.html'

    return render(request, template_name, context)










