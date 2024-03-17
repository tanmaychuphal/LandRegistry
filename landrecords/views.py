from unittest import loader
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
import qrcode
from django.template import loader
from landrecords.models import loginData, newEntry
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# import pdb
# Create your views here.

def generated_qr(request,data_dict):
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
    for data in data_dict:
        qr.add_data(data)
    qr.make(fit=True)        
    img = qr.make_image(fill_color="black", back_color="white")
    # img.save()
    return render(request,'landrecords/generated_qr.html',data_dict)

def LogoutPage(request):
    logout(request)
    return redirect('login')

# pdb.set_trace()
@login_required(login_url='login',redirect_field_name='home')
def HomePage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        # fname=request.POST.get('fname')
        state=request.POST.get('state')
        # district=request.POST.get('district')
        pincode=request.POST.get('pincode')
        data_dict={'name':name,'state':state,'pincode':pincode}
        if(newEntry.objects.filter(name=name,state=state,pincode=pincode).exists()):
            print("ALready exists")
            return HttpResponse("data already exists")
        else:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(name)
            qr.add_data(state)            
            qr.add_data(pincode)
            qr.make(fit=True)        
            img = qr.make_image(fill_color="black", back_color="white")
            # template = loader.get_template('qr_code.html')
            # context = {'qr_code': img, 'name': name, 'state':state,'pincode':pincode}
            # rendered_template = template.render(context)
            # response = HttpResponse(rendered_template)
            response = HttpResponse(content_type="image/png")
            img.save(response, "PNG")
            return response
            # image.save("PNG")
            # data=newEntry(name=name,state=state,pincode=pincode,image=image)
            # data.save()
            # return HttpResponse("WELL")
    return render (request,'landrecords/home.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'landrecords/login.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request,'landrecords/signup.html')

