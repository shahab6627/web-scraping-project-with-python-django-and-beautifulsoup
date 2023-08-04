from django.shortcuts import render, redirect
from django.http import HttpResponse
from .froms import ItmePriceModelForm, UserRegForm, LoginForm
from django.contrib import messages
from .models import ItmePrice
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def home(request):
    return render(request, 'price_tracker/index.html')



def userRegistration(request):
    if request.method == "POST":
        password = request.POST.get('password')
        conf_passwprd = request.POST.get('password_confirmation')
        username = request.POST.get('username')
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        
        checkuser = User.objects.filter(username = username).exists()
        if checkuser:
            
            messages.add_message(request, messages.WARNING, f'given username "{username}" already taken ')
            return redirect('register')
        
        
        if password != conf_passwprd:
            messages.add_message(request, messages.WARNING, 'passwords are not matching...')
            return redirect('register')
        form = UserRegForm(request.POST)
        if form.is_valid:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=f_name,last_name=l_name)
            
            user.save()
        
            return redirect('register')
    
    form = UserRegForm()
    
    dict = {
        'form':form
    }
    return render(request, 'price_tracker/register.html', dict)
    
    

def loginUser(request):
    # if user already logged-in 
    
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password=password)
        # if user exists then complete login 
        if user is not None:
            login(request, user)
            return redirect('profile')
        
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request, 'price_tracker/login.html', context)

@login_required(login_url='login')
def profile(request):
    if request.method == "POST":
        
        # if url is belongs to flipkart then 
        url = request.POST.get('url')
        if not "https://www.flipkart.com/" in url:
            messages.add_message(request, messages.WARNING, "Url must be of filpkart url")
            return redirect('home')
        
        # if url already exists 
        check = ItmePrice.objects.filter(url=url, user=request.user).exists()
        
        if check:
            messages.add_message(request, messages.ERROR, "item already exists")
            return redirect('profile')
        
        #  if form is valid 
        form = ItmePriceModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            form.save()
            checkitem = ItmePrice.objects.filter(url = url).exists()
            if checkitem:
                messages.add_message(request, messages.SUCCESS, 'item added to the list...')
                return redirect('profile')
            else:
                messages.add_message(request, messages.SUCCESS, 'this is url is not working...')
                return redirect('profile')
                
    
            
    discounted_items = 0
    q = ItmePrice.objects.filter(user=request.user)
    
    count_item = q.count()
    
    for item in q:
        if item.old_price > item.current_price:
            discounted_items+=1
    
    form = ItmePriceModelForm()
    dict = {
        'items':q,
        'total_items':count_item,
        'discounted_items':discounted_items,
        'form':form
    }
    return render(request, 'price_tracker/profile.html', dict)
        

def logoutuser(request):
    logout(request)
    
    return redirect('home')

def updateItems(request):
    items = ItmePrice.objects.filter(user = request.user)
    for i in items:
        i.save()
    messages.add_message(request, messages.SUCCESS, 'all items are refreshed')
    return redirect('profile')


def deleteItem(requeest, id):
    item = ItmePrice.objects.get(id=id)
    if item:
        item.delete()
        
        return redirect('profile')