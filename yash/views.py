from django.contrib import messages
from django.shortcuts import render, redirect

from yash.models import AdminLoginModel,StateModel1


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
    return render(request,"yash/opencity.html")


def addingstate(request):
   s_name = request.POST.get("t1")
   s_photo= request.FILES["t2"]
   StateModel1(name=s_name,photo=s_photo,).save()
   return openstate(request)


def updatestate(request):
    sid = request.GET.get('id')
    sm = StateModel1.objects.get(id=sid)

    return render(request, 'yash/openstate.html', {'update_state': sm})

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
