from django.views.generic import View
from django.shortcuts import redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth


class Login(View):
    TEMPLATE = 'dashboard/auth/login.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('dashboard_index'))
        to = request.GET.get('to', '')

        data = {'error': '', 'to': to}
        return render_to_response(request, self.TEMPLATE, data)

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        to = request.GET.get('to', '')
        exists = User.objects.filter(username=username).exists()
        data = {}
        if not exists:
            data['error'] = '不存在该用户'
            return render_to_response(request, self.TEMPLATE, data)

        user = authenticate(username=username, password=password)

        if not user:
            data['error'] = '密码错误'
            return render_to_response(request, self.TEMPLATE, data)

        if not user.is_superuser:
            data['error'] = '你无权登录管理后台'
            return render_to_response(request, self.TEMPLATE, data)

        login(request, user)
        if to:
            return redirect(to)
        return redirect(reverse('dashboard_index'))


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


class AdminManger(View):
    TEMPLATE = 'dashboard/auth/admin.html'

    @dashboard_auth
    def get(self, requet):
        data = {}
        users = User.objects.all()
        page = requet.GET.get('page', '1')
        p = Paginator(users, 1)
        total_page = p.num_pages

        if int(page) <= 1:
            page = 1
        print(page)
        current_page = p.get_page(int(page)).object_list

        data['users'] = current_page
        data['total'] = total_page
        data['page_num'] = int(page)
        return render_to_response(requet, self.TEMPLATE, data)


class UpdateAdminStatus(View):

    def get(self, request):
        status = request.GET.get('status', 'on')
        print('status', status)
        _status = True if status == 'on' else False
        print(_status)
        request.user.is_superuser = _status
        request.user.save()

        return redirect(reverse('admin_manger'))
