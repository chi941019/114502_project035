from django.shortcuts import render
#######################################
from django.shortcuts import render


from rest_framework import serializers, viewsets
from .models import ButtonConfig

class ButtonConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonConfig
        fields = '__all__'

class ButtonConfigViewSet(viewsets.ModelViewSet):
    queryset = ButtonConfig.objects.all()
    serializer_class = ButtonConfigSerializer


def edit_buttons(request):
    return render(request, 'edit_buttons.html')


def login_page(request):
    return render(request, '001_login.html')

def home(request):
    return render(request, 'home.html')

def auto_dial(request):
    return render(request, 'auto-dial.html')

def chat_room(request):
    return render(request, 'chat-room.html')

def safety_info(request):
    return render(request, 'safety-info.html')

def map_view(request):
    return render(request, 'map.html')

def board(request):
    return render(request, 'board.html')

def settings(request):
    return render(request, 'settings.html')

def form_view(request):
    return render(request, 'form.html')

##########################################

def index(request):
    return render(request, 'index.html')  # 確保 index.html 在 templates/ 內

# 表格頁面
def tables(request):
    return render(request, 'tables.html')

# 註冊頁面
def register(request):
    return render(request, 'register.html')

# 密碼頁面
def password(request):
    return render(request, 'password.html')

# 登入頁面
def login(request):
    return render(request, 'login.html')

# 布局 - 靜態頁面
def layout_static(request):
    return render(request, 'layout-static.html')

# 布局 - 輕量側邊欄頁面
def layout_sidenav_light(request):
    return render(request, 'layout-sidenav-light.html')

# 圖表頁面
def charts(request):
    return render(request, 'charts.html')

# 500 錯誤頁面
def error_500(request):
    return render(request, '500.html')

# 500 錯誤頁面
def error_401(request):
    return render(request, '401.html')

# 500 錯誤頁面
def error_404(request):
    return render(request, '404.html')



# 原本沒有這些