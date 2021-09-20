from django.shortcuts import render , redirect
from advanced_form.settings import EMAIL_HOST, EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site

from django.urls import reverse, reverse_lazy
import random
from apps.student.models import Student, Language
from django.contrib import messages

# Create your views here.

def home(request):


	if request.method == "POST":
		if request.POST['email']:

			email =  request.POST.get('email')
			email_from = EMAIL_HOST_USER
			subject = "Please verify your email address by click this link"
			
			domain = get_current_site(request).domain
			verification_code = random.randint(1000, 10000)
			request.session["email_"+str(verification_code)] = email
			request.session["verification_code"] = verification_code
			message = ''.join(['http://', get_current_site(request).domain,reverse('verification', args=(email,request.session["verification_code"]))])
			try:
				send_mail(subject, message , email_from, [email,])		
			
			except error:
				return HttpResponse("Email not found or Server is busy now")

			return HttpResponse(r"<html><body><p style='margin:50px;color:blue'>please! verify your Email first</p></body></html>")

			

	return render(request,"index.html")

def verification(request,email,code=0):

	if request.method == "GET":
		if email == request.session["email_"+str(code)] and request.session["verification_code"] == code:
			return render(request,'registration.html',context = {'email':email,'code':code})

def load_languages(request):

	language = Language.objects.all()

	return render(request, 'language_option_list.html', {'languages': language})

def registration(request):
	
	if request.method == "POST":
	
		email = request.POST.get('email')
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		language_list = request.POST.getlist('languages')

		if name is not None and email is not None and phone is not None and len(language_list) > 0:
			
			p1 = Student(name=name,email=email,phone=phone)
			p1.save()
			for language in language_list:
				l = Language.objects.filter(language_name=language)[0].pk
				p1.languages.add(l)
			
			p1.save()
			
			return redirect(reverse_lazy('thanks_view'))
		
		else:
			messages.error(request,"Please Fill Up the all field")

	email = request.POST.get('email')

	if email is not None:
		link = ''.join(['http://', get_current_site(request).domain,reverse('verification', args=(email,request.session["verification_code"]))])

		return HttpResponseRedirect(link)
	
	return redirect(reverse_lazy('home'))
	
def thanks_view(request):
	return render(request,'thanks.html')

