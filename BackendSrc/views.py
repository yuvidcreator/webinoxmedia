from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.mail import message, send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sitemaps.views import sitemap


def HomePage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')

        context = {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'website' : website
        }
        print(context)
        message = '''
            Customer Enquiry from WebinoxMedia's Home Page. 

            Customer Name: {}
            Customer Email: {}
            Customer Phone: {}
            Customer Website: {}

        '''.format(context['name'], context['email'], context['phone'], context['website'])
        send_mail(context['email'], message, '', ['webinoxmedia@gmail.com'])        
        return redirect('Thanks Page')

    return render(request, 'frontend/index.html')


def ServicesPage(request):
    return render(request, 'frontend/services.html')


def ContactPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('websitelink')
        message = request.POST.get('message')

        context = {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'website' : website,
            'message' : message
        }
        print(context)
        eml_message = '''
            Customer Enquiry from WebinoxMedia's Contact Page. 

            Customer Name: {}
            Customer Email: {}
            Customer Phone: {}
            Customer Website: {}
            Message: {}

        '''.format(context['name'], context['email'], context['phone'], context['website'], context['message'])
        send_mail(context['email'], eml_message, '', ['webinoxmedia@gmail.com'])        
        return redirect('Thanks Page')

    return render(request, 'frontend/contact.html')


def ThanksPage(request):
    return render(request, 'frontend/thanks.html')


def FaqPage(request):
    return render(request, 'frontend/faq.html')


def AboutPage(request):
    return render(request, 'frontend/about.html')


def CaseStudiesPage(request):
    return render(request, 'frontend/casestudies.html')
