from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST['ID']
        password = request.POST['PW']
        user = auth.authenticate(request, username=username, password=password)
        # 로그인 성공 시
        if user is not None:
            auth.login(request, user)
            return redirect('blog_home')
        # 로그인 실패 시
        else:
            context = {
                'error':'Check Username or Password!!!', 
                'ID':username
            }
            return render(request, 'accounts/login.html', context)
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')


# 로그인이 되어 있을 때만 실행
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')