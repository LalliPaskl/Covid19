from django.shortcuts import render, redirect
from .models import RegisterData,Medstoringsupplier,Medmedicalshop,Supquantmanagmnt,Medicalquantmgnt
from .forms import RegisterForm,LoginForm,medstoringsupForm,medmedicalshopForm,supquantmanagmntForm,medicalquantmgntForm
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
import json
from django.core.mail import send_mail


# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def regview(request):
    """ registration for supplier ,customer and owner"""
    if request.method == 'POST':
        rform = RegisterForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            password2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            mobile = request.POST.get('mobile', '')
            customer = request.POST.get('customer', '')
            docfile = request.FILES.get('docfile', '')
            # if not email:
            #     messages.error(request, "Email cannot be blank")
            #     return redirect("/")
            # elif not EMAIL_REGEX.match(request.POST['email']):
            #     messages.error(request, "Must be a valid email")
            #     return redirect("/")
            #
            # request.session['email'] = email
            # Email.objects.create(email=email)
            data = RegisterData(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                password2=password2,
                email=email,
                mobile=mobile,
                customer=customer,
                docfile=docfile
            )
            data.save()
            rform = RegisterForm()
            return render(request, 'reg.html', {'rform': rform})
        else:
            return HttpResponse ("Not valid")

    else:

        rform = RegisterForm()
        return render(request, 'reg.html', {'rform': rform})




def logview(request):
    """ login form after registration according to the user """
    if request.method == 'POST':
        lform = LoginForm(request.POST)
        mmedical = medmedicalshopForm(request.POST)
        if lform.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            customer = request.POST.get('customer', '')
            user = RegisterData.objects.filter(username=username)
            pwd = RegisterData.objects.filter(password=password)
            cust = RegisterData.objects.filter(customer=customer)

            # if user and pwd:
            # user1 = authenticate(username=username, password=password)
            # if user1 is not None:
            #     login(request, user1)
            if user and pwd:
                if cust and (customer == 'Admin') :
                    return render(request, 'index.html', {'mmedical': mmedical})
                elif cust and (customer == 'Supplier') :
                    return render(request, 'supplier.html', {'mmedical': mmedical})
                elif cust and (customer == 'Customer') :
                    return render(request, 'owner.html', {'mmedical': mmedical})
                else:
                    return HttpResponse("not admin")

            # if username in admin:
            #     if admin[username] == password:
            #         return HttpResponse('admin logged in')
            # elif username in supplier:
            #     if supplier[username] == password:
            #         return HttpResponse('supplier logged in')
            # elif username in customerdt:
            #
            #     if customerdt[username] == password:
            #         return HttpResponse('customer logged in')

            else:
                return HttpResponse('invalid credentials')
        else:
            return HttpResponse("form not valid")

    else:

        lform = LoginForm()
        return render(request, 'login.html', {'lform': lform})


def medstoringsupview(request):
    """ form to store medicine for a supplier"""
    if request.method == 'POST':
        mform = medstoringsupForm(request.POST)
        if mform.is_valid():
            tabletname = request.POST.get('tabletname', '')
            brandname = request.POST.get('brandname', '')
            components = request.POST.get('components', '')
            price = request.POST.get('price', '')

            msdata = Medstoringsupplier(
                tabletname=tabletname,
                brandname=brandname,
                components=components,
                price=price
            )
            msdata.save()
            mform = medstoringsupForm()

            return render(request, 'medsupplier.html', {'mform': mform})
        else:
            return HttpResponse ("Not valid")

    else:

        mform = medstoringsupForm()
        return render(request, 'medsupplier.html', {'mform': mform})




def suptotaltablets(request):
    """ displaying available medicine of a supplier"""
    suptablets = Medstoringsupplier.objects.all()
    return render(request, 'suptablets.html', {'suptablets': suptablets})



def medmedicalshopview(request):
    """ form for storing medicines of a medical store"""
    if request.method == 'POST':
        sform = medmedicalshopForm(request.POST)
        if sform.is_valid():
            tabletname = request.POST.get('tabletname', '')
            brandname = request.POST.get('brandname', '')
            components = request.POST.get('components', '')
            price = request.POST.get('price', '')

            sdata = Medstoringsupplier(
                tabletname=tabletname,
                brandname=brandname,
                components=components,
                price=price
            )
            sdata.save()
            sform = medmedicalshopForm()
            return render(request, 'medmedical.html', {'sform': sform})
        else:
            return HttpResponse ("Not valid")

    else:

        sform = medmedicalshopForm()
        return render(request, 'medmedical.html', {'sform': sform})

from django.core.mail import send_mail
from django.conf import settings

def supemailsending(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        send_mail('Email Sending',
                  message,
                  settings.EMAIL_HOST_USER,
                  [email],
                  fail_silently=False)

    return render(request, 'email_sending.html')



