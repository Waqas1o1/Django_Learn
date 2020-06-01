from django.shortcuts import render,HttpResponse
import json
import re
from .models import User
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
# Create your views here.
def Registration(request):
    return render(request,'registration\index.html')
def HandleRegistration(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        age = request.POST['age'] 
        birthday = request.POST['birthday'] 
        email = request.POST['email']
        phone = request.POST['phone']
        
        Message = {'status':True}
        if(User.objects.filter(email = email)):
            Message = {'message':'Already Registered with : '+email,'status':False}  
        else:
            if int(age) > 100:
                Message = {'message':'Sorry Wrong age','status':False}

            if len(phone) != 11:
                Message = {'message':'Phone is valid','status':False} 
            
            
        if Message['status'] == True:
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if re.search(regex,email):                           
                plaintext = get_template('registration/email/email.txt')
                htmly     = get_template('registration/email/email.html')
                # d = Context({ 'name': 'Waqas' })
                poster_link = 'www.goole.com'
                RegistrationSite_Link = 'www.youtube.com'
                document_link = 'www.google.com'
                d = {'name':name,'Poster':poster_link,'document':document_link,'Site_link':RegistrationSite_Link}
                subject, from_email, to = 'Registration', 'waqasdevolper@gmail.com', email
                text_content = plaintext.render(d)
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                user = User(name=name,email=email,phone=phone,age=age)
                user.save()
                Message = {'message':'Thanks! for registration..... /n an confermation email is send u at : '+ email}
            else:
                Message = {'message':"Invalid Email"}

        alart = json.dumps(Message)
        return HttpResponse(alart)
