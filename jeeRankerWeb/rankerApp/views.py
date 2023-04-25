from django.shortcuts import render, redirect
from rankerApp.models import SignUp
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def getCollege(num):
    if num ==1:
        return "IIT Bombay"
    elif num ==2:
        return "IIT Madras"
    else:
        return "MIT Manipal"
    

def getBranch(num):
    if num==1:
        return "Computer Science & Engineering"
    elif num==2:
        return "Electrical & Electronics Engineering"
    else:
        return "Electrical & Communications Engineering"
    
def results(request):
    rank = int(request.POST.get('rank'))
    college_preference = int(request.POST.get('college'))
    branch_preference = int(request.POST.get('branch'))

    print(college_preference)
    print(branch_preference)
    
    if rank >= 1 and rank < 100:
        college = getCollege(college_preference)
        branch = getBranch(branch_preference)
    elif rank >= 100 and rank < 200:
        college = "IIT Madras"
        branch = getBranch(branch_preference)
    elif rank >= 200 and rank < 300:
        college = "MIT Manipal"
        branch = getBranch(branch_preference)
    elif rank >= 300 and rank < 400:
        college = getCollege(college_preference)
        branch = "Electrical & Electronics Engineering"
    elif rank >= 400 and rank < 500:
        college = "IIT Madras"
        branch = "Electrical & Electronics Engineering"
    elif rank >= 500 and rank < 600:
        college = "MIT Manipal"
        branch = "Electrical & Electronics Engineering"
    elif rank >= 600 and rank < 700:
        college = "IIT Bombay"
        branch = "Electrical & Communications Engineering"
    elif rank >= 700 and rank < 800:
        college = "IIT Madras"
        branch = "Electrical & Communications Engineering"
    elif rank >= 800 and rank < 900:
        college = "MIT Manipal"
        branch = "Electrical & Communications Engineering"
    else:
        college = "MIT Manipal"
        branch = "Electrical & Communications Engineering"
    # add more elif blocks for other rank ranges and college/branch allotments
    
    context = {'college': college, 'branch': branch, 'rank':rank}
    return render(request, 'results.html', context)

def index(request):
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print("Email:", email)
        # print("Password:", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid email or password')
    return render(request, 'login.html')

def signUp(request):
    if request.method == "POST":
        username= request.POST.get("username")
        email= request.POST.get("email")
        password= request.POST.get("password")

        userNew = User.objects.create_user(username= username, email= email, password=password)
        userNew.save()
        messages.success(request, "Details Added, You can login Now.")
    return render(request, 'newUser.html')


def dashboard(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'dashboard.html')

def logoutUser(request):
    logout(request)
    return render(request, "index.html")