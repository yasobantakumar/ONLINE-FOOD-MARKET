from django.contrib import messages
from django.shortcuts import render, redirect

from yash.models import AdminLoginModel,StateModel1,CityModel1,CuisineModel


def showIndex(request):
    return render(request,"yash/login.html")


def login_check(request):

 if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("yash_username"),
                                                password=request.POST.get("yash_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "yash/login.html", {"error": "Invalid User"})
 else:
        request.session["admin_status"] = False
        return render(request, "yash/login.html", {"error": "Admin Logout Success"})
def welcome(request):
    return render(request,"yash/home.html")


def openstate(request):
    data=StateModel1.objects.all()
    return render(request,"yash/openstate1.html",{"DATA":data})


def opencity(request):
    sm = StateModel1.objects.all()
    cm = CityModel1.objects.all()
    return render(request, "yash/opencity.html", {'state': sm, 'city': cm})


def addingstate(request):
   s_name = request.POST.get("t1")
   s_photo= request.FILES["t2"]
   StateModel1(name=s_name,photo=s_photo,).save()
   return openstate(request)


def updatestate(request):
    sid = request.GET.get('id')
    sm = StateModel1.objects.get(id=sid)
    sm_all=StateModel1.objects.all()
    return render(request, 'yash/openstate1.html', {'update_state': sm,'data':sm_all})

def updatestateid(request):
    s_id = request.GET.get('state_id')
    s_name = request.POST.get('t1')
    s_photo = request.FILES.get('t2')
    StateModel1.objects.filter(id=s_id).update(name=s_name,photo=s_photo)
    return redirect('openstate')

def sdelete(request):
    s_id = request.GET.get('state_id')
    StateModel1.objects.filter(id=s_id).delete()
    messages.success(request, 'state is removed')
    return redirect('openstate')


def savecity(request):
    cid = request.POST.get('t2')
    name = request.POST.get('t1')
    print(cid, name)
    CityModel1(name=request.POST.get('t1'), photo=request.FILES["t3"], city_state_id=cid).save()
    messages.success(request, 'city is added')
    return redirect('opencity')

def updatecity(request):
    cm = CityModel1.objects.filter(id=request.GET.get('cid'))

    return render(request,'yash/opencity.html',{'ucity':cm})


def updatecityid(request):
    CityModel1.objects.filter(id=request.GET.get('cid')).update(name=request.POST.get('t1'),photo =request.FILES.get('t3'))
    messages.success(request,'updated success')
    return opencity(request)


def cdelete(request):
    CityModel1.objects.filter(id=request.GET.get('cid')).delete()
    messages.success(request, 'City deleted')
    return redirect('opencity')


def openCusine(request):
    cm = CuisineModel.objects.all()
    return render(request,"yash/opencuisine.html",{'data':cm})
def savecuisine(request):
    CuisineModel(type=request.POST.get('t1'),photo=request.FILES.get('t2')).save()
    messages.success(request,'cuisine saved')
    return openCusine(request)


def updatecuisine(request):
    cid = request.GET.get('cid')

    cm = CuisineModel.objects.filter(id=cid)
    return render(request,'yash/opencuisine.html',{'update':cm})


def updatecuisineid(request):
    CuisineModel.objects.filter(id=request.GET.get('cid')).update(type=request.POST.get('t1'),
                                                                photo=request.FILES.get('t2'))
    messages.success(request,'cuisine updated')
    return redirect('cuisine')


def dcuisine(request):
    CuisineModel.objects.filter(id=request.GET.get('cid')).delete()
    messages.success(request, 'cuisine deleted')
    return redirect('cuisine')


