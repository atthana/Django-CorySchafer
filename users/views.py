from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # ต้องมีบรรทัดนี้นะจึง save to database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! {username} are able to login')
            return redirect('login')  # หลังจาก register แล้วก้อต้องให้วิ่งไปที่หน้า login นะ
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

