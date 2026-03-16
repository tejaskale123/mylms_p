from django.shortcuts import render, redirect
from .models import Users  # We only need Users, because it links to UserTypes automatically
import bcrypt

# --- THE LOGIN LOGIC ---
def login_view(request):
    if request.method == "POST":
        username_input = request.POST.get('username_input')
        password_input = request.POST.get('password_input')

        try:
            user = Users.objects.get(user_name=username_input)

            if user.password == password_input:

                role_code = user.user_type.user_type

                request.session['user_id'] = user.id
                request.session['role'] = role_code

                if role_code == 'a':
                    return redirect('admin_dash')
                elif role_code == 's':
                    return redirect('student_dash')
                elif role_code == 'p':
                    return redirect('principal_dash')
                else:
                    return render(request, 'login.html', {'error': 'Invalid role'})

            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})

        except Users.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


# --- THE DASHBOARDS ---
# These functions simply show the HTML files you created earlier
def admin_dashboard(request):
    return render(request, 'admin_home.html')

def student_dashboard(request):
    return render(request, 'student_home.html')

def principal_dashboard(request):
    return render(request, 'principal_home.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')