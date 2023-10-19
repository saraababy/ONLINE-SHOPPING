from django.shortcuts import render, redirect
from Backend.models import CategoryDB, ProductDB
from Frondend.models import MessagesDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def adminHome(request):
    return render(request, 'index.html')

def Add_category(request):
    return render(request, 'AddCategory.html')

def submitCategory(request):
    if request.method=="POST":
        na=request.POST.get("catname")
        de=request.POST.get("desc")
        img=request.FILES['img']
        obj=CategoryDB(CatName=na,Description=de, Image=img)
        obj.save()
        messages.success(request, "Category saved successfully..!")
        return redirect('Add_category')

def Display_category(request):
    cat = CategoryDB.objects.all()
    return render(request, 'DisplayCategory.html',{'cat':cat})

def EditCategory(request, dataid):
   data=CategoryDB.objects.get(id=dataid)
   return  render(request, 'EditCategory.html', {'data':data})

def updateCategory(request, dataid):
    if request.method == "POST":
        na = request.POST.get('catname')
        de = request.POST.get('desc')
        try:
            im = request.FILES['img2']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Image
        CategoryDB.objects.filter(id=dataid).update(CatName=na, Description=de, Image=file)
        # messages.success(request, "Category updated successfully..!")
        return redirect(Display_category)

def DeleteCategory(request, dataid):
   data=CategoryDB.objects.filter(id=dataid)
   data.delete()
   # messages.success(request, "Category successfully removed from the system..!")

   return redirect(Display_category)

def AddProduct(request):
   cat=CategoryDB.objects.all()
   return render(request, 'AddProduct.html', {'cat':cat})

def submitProduct(request):
   if request.method=="POST":
      na=request.POST.get('catName')
      pn=request.POST.get('proname')
      pr=request.POST.get('proprice')
      pd=request.POST.get('prodesc')
      im=request.FILES['img1']
      im1=request.FILES['img2']
      im2=request.FILES['img3']
      qt=request.POST.get('qty')
      ob=ProductDB(CatName=na, ProName=pn, Image=im, Image1=im1,Image2=im2,Description=pd,Proprice=pr,StockQty=qt)
      ob.save()
      # messages.success(request, "Product saved successfully..!")

      return redirect(AddProduct)

def DisplayProduct(request):
   pro=ProductDB.objects.all()
   return  render(request, 'DisplayProduct.html', {'pro':pro})

def EditProduct(request, dataid):
   cat=CategoryDB.objects.all()
   pro=ProductDB.objects.get(id=dataid)
   return  render(request, 'EditProduct.html', {'pro':pro, 'cat':cat} )


def updateProduct(request, dataid):
   if request.method=="POST":
      na = request.POST.get('catName')
      pn = request.POST.get('proname')
      pr = request.POST.get('proprice')
      pd = request.POST.get('prodesc')
      try:
         im = request.FILES['img1']
         fs = FileSystemStorage()
         file = fs.save(im.name, im)
      except MultiValueDictKeyError:
         file = ProductDB.objects.get(id=dataid).Image
      try:
         im = request.FILES['img2']
         fs = FileSystemStorage()
         filee = fs.save(im.name, im)
      except MultiValueDictKeyError:
         filee = ProductDB.objects.get(id=dataid).Image1
      try:
          im = request.FILES['img3']
          fs = FileSystemStorage()
          fileee = fs.save(im.name, im)
      except MultiValueDictKeyError:
          fileee = ProductDB.objects.get(id=dataid).Image2
      ProductDB.objects.filter(id=dataid).update(CatName=na, ProName=pn, Description=pd,Proprice=pr,Image=file,Image1=filee,Image2=fileee)
      # messages.success(request, "Product updated successfully..!")
      return redirect(DisplayProduct)

def DeleteProduct(request, dataid):
   pro=ProductDB.objects.filter(id=dataid)
   pro.delete()
   # messages.success(request, "Product successfully removed from the system..!")

   return redirect(DisplayProduct)

def adminLogin(request):
   return render(request, 'AdminLogin.html')

def admin_login(request):
   if request.method=="POST":
      uname=request.POST.get('username')
      pw=request.POST.get('pass')
      if User.objects.filter(username__contains=uname).exists():
         user = authenticate(username=uname, password=pw)
         if user is not None:
            login(request, user)
            request.session['username']=uname
            request.session['password']=pw

            return redirect(adminHome)
         else:
            # messages.error(request, "Invalid username/password")

            return redirect(adminLogin)
      else:
          # messages.error(request, "Invalid username/password")

          return redirect(adminLogin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    # messages.success(request, "Successfully logged out..!")
    return redirect(adminLogin)

def messages(request):
    msg = MessagesDB.objects.all()
    return render(request, 'Messages.html',{'msg':msg})