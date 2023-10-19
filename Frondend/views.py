from django.shortcuts import render, redirect
from Backend.models import CategoryDB, ProductDB
from Frondend.models import UserDB, CartDB, MessagesDB
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def Home_admin(request):
    cat = CategoryDB.objects.all()
    pro= ProductDB.objects.all()
    return render(request, 'homepage.html', {'cat': cat, 'pro':pro})

def shop_now(request):
    cat = CategoryDB.objects.all()
    pro= ProductDB.objects.all()
    return render(request, 'shop.html', {'cat': cat, 'pro':pro})

def login_Reg(request):
    return render(request, 'loginReg.html')

def signup(request):
    if request.method=="POST":
        na=request.POST.get("username")
        fn=request.POST.get("fullname")
        em=request.POST.get("email")
        mo=request.POST.get("contact")
        pw=request.POST.get("password")
        cpw=request.POST.get("cpassword")
        if(pw==cpw):
            obj=UserDB(UserName=na,FullName=fn,Email=em, ContactNumber=mo, Password=pw)
            obj.save()
            messages.success(request,"Sign up done Successfully.. Please Login now..")
            return redirect('login_Reg')
        else:
            messages.error(request, "Please try after sometime...!")
            return redirect('login_Reg')

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pw=request.POST.get('pass')
        if UserDB.objects.filter(UserName=uname, Password=pw).exists():
            request.session['UserName']=uname
            request.session['Password']=pw
            messages.success(request, "Welcome..!")
            return redirect(Home_admin)
        else:
            messages.error(request, "Please check Credentials..!")
            return redirect(login_Reg)
    return redirect(login_Reg)


def user_logout(request):
   del request.session['UserName']
   del request.session['Password']
   return redirect(login_Reg)

def about_us(request):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.all()
    return render(request, 'about.html', {'cat': cat, 'pro': pro})

def contact_us(request):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.all()
    return render(request, 'contactus.html', {'cat': cat, 'pro': pro})

def pro_details(request, dataid):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.all()
    data=ProductDB.objects.get(id=dataid)
    flag=False
    if data.StockQty==0:
        flag=True
    cat_data=CategoryDB.objects.get(CatName=data.CatName)
    cat_data_all=ProductDB.objects.filter(CatName=data.CatName)
    return render(request, 'prodetails.html', {'cat': cat, 'pro': pro, 'data':data, 'cat_data':cat_data,'cat_data_all':cat_data_all, 'flag':flag})

def submitCart(request):
    if request.method=="POST":
        useN = request.POST.get("userName")
        proN = request.POST.get("proName")
        prodes = request.POST.get("proDesc")
        price = request.POST.get("price")
        pp=int(price)
        qt = request.POST.get("qty")
        img=request.POST.get("img")
        print(img)
        qtt=int(qt)
        to = pp*qtt

        obj=CartDB(UserName=useN,ProName=proN,Description=prodes, Quantity=qt, TotalPrice=to, Image=img, Status="carted")
        obj.save()
        messages.success(request, "Item added to the cart..!")
        return redirect('DisplayCart')

def DisplayCart(request):
    cart = CartDB.objects.all()
    cat = CategoryDB.objects.all()
    data=CartDB.objects.filter(UserName=request.session['UserName'],Status="carted")
    cart_count=data.count()
    total_price=0
    for i in data:
        total_price = total_price+i.TotalPrice
    return render(request, 'cart.html', {'cart':cart, 'data':data, 'cat':cat, 'total_price':total_price, 'cart_count':cart_count})

def DeleteItem(request, dataid):
   pro=CartDB.objects.filter(id=dataid)
   pro.delete()
   messages.error(request, "Item removed from the cart..!")
   return redirect(DisplayCart)

def checkout(request):
    data=CartDB.objects.filter(UserName=request.session['UserName'])
    for i in data:
        qty=i.Quantity
        print(qty)
        print(i.id)
        pro=ProductDB.objects.get(ProName=i.ProName)
        print(pro.StockQty)
        proqty = pro.StockQty-qty
        print(pro.ProName)
        ProductDB.objects.filter(id=pro.id).update(StockQty=proqty)
        print(proqty)
    CartDB.objects.filter(UserName=request.session['UserName']).update(Status="placed")
    messages.success(request,"Order Placed Successfully")
    return redirect(Home_admin)

def orders(request):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.all()
    order_items=CartDB.objects.filter(UserName=request.session['UserName'], Status="placed")
    return render(request, 'YourOrders.html', {'cat': cat, 'pro': pro,'order_items':order_items})

def profile(request):

    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.all()
    data=UserDB.objects.get(UserName=request.session['UserName'])
    return render(request, 'myProfile.html', {'cat': cat, 'pro': pro, 'data':data})

def update_profile(request, dataid):
    if request.method == "POST":
        na = request.POST.get('full_name')
        em = request.POST.get('email')
        mo = request.POST.get('mobile')
        ad = request.POST.get('address')
        UserDB.objects.filter(id=dataid).update(FullName=na, Email=em, ContactNumber=mo,Address=ad)
        messages.success(request, "Profile updated successfully..!")
        return redirect(profile)

def update_profileimage(request, dataid):
    if request.method == "POST":
        try:
            im = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Image
        UserDB.objects.filter(id=dataid).update(Image=file)
        messages.success(request, "Profile Image updated successfully..!")
        return redirect(profile)

def send_msg(request):
    if request.method == "POST":
        em=request.POST.get('email')
        ms=request.POST.get('msg')
        print("aaaa")
        print(em)
        print(ms)
        obj = MessagesDB(Email=em,Message=ms)
        obj.save()
        messages.success(request, "Thank you for Contacting Us....!")
        return redirect(contact_us)