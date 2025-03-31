from . import views
#login介面調整
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ButtonConfigViewSet

router = DefaultRouter()
router.register(r'buttons', ButtonConfigViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
from .views import edit_buttons


urlpatterns = [
    path('', views.login_page, name='login_page'),  # 預設首頁
    path('001_login/', views.login_page, name='login_page'),  # 讓 /001_login 也能對應
    path('tables.html', views.tables, name='tables'),
    path('register.html', views.register, name='register'),
    path('password.html', views.password, name='password'),
    path('login.html', views.login, name='login'),
    path('layout-static.html', views.layout_static, name='layout-static'),
    path('layout-sidenav-light.html', views.layout_sidenav_light, name='layout-sidenav-light'),
    path('charts.html', views.charts, name='charts'),
    path('500.html', views.error_500, name='500'),
    path('401.html', views.error_401, name='401'),
    path('404.html', views.error_404, name='404'),
    path('home/', views.home, name='home'),
    path('auto-dial/', views.auto_dial, name='auto_dial'),
    path('chat-room/', views.chat_room, name='chat_room'),
    path('safety-info/', views.safety_info, name='safety_info'),
    path('map/', views.map_view, name='map'),
    path('board/', views.board, name='board'),
    path('settings/', views.settings, name='settings'),
    path('form/', views.form_view, name='form_view'),
    path('api/', include(router.urls)),
    path('edit-buttons/', edit_buttons, name='edit_buttons'),
]


# urlpatterns = [
#     path('', views.login_page, name='login_page'),  # 預設首頁
#     path('001_login.html', views.login_page, name='login_page'),
    
#     path('tables.html', views.tables, name='tables'),
#     path('register.html', views.register, name='register'),
#     path('password.html', views.password, name='password'),
#     path('layout-static.html', views.layout_static, name='layout-static'),
#     path('layout-sidenav-light.html', views.layout_sidenav_light, name='layout-sidenav-light'),
#     path('charts.html', views.charts, name='charts'),
#     path('500.html', views.error_500, name='500'),
#     path('401.html', views.error_401, name='401'),
#     path('404.html', views.error_404, name='404'),
    
#     path('home/', views.home, name='home'),
#     path('auto-dial/', views.auto_dial, name='auto_dial'),
#     path('chat-room/', views.chat_room, name='chat_room'),
#     path('safety-info/', views.safety_info, name='safety_info'),
#     path('map/', views.map_view, name='map'),
#     path('board/', views.board, name='board'),
#     path('settings/', views.settings, name='settings'),
#     path('form/', views.form_view, name='form_view'),
# ]


# urlpatterns = [
#     path('', views.index, name='home'),
#     path('index.html', views.index, name='index'),
#     # path('index.html', views.index, name='index')
#     # 對,我也不知道有時換這個反而能跑,有時又不能跑    
#     path('tables.html', views.tables, name='tables'),
#     path('register.html', views.register, name='register'),
#     path('password.html', views.password, name='password'),
#     path('login.html', views.login, name='login'),
#     path('layout-static.html', views.layout_static, name='layout-static'),
#     path('layout-sidenav-light.html', views.layout_sidenav_light, name='layout-sidenav-light'),
#     path('charts.html', views.charts, name='charts'),
#     path('500.html', views.error_500, name='500'),
#     path('401.html', views.error_401, name='401'),
#     path('404.html', views.error_404, name='404')
# ]

# 原本沒有這些路徑