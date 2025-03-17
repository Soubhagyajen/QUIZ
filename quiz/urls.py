from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.quiz_list, name='quiz_list'),  # Home page showing quizzes
    path('add_quiz/',views.add_quiz,name='add_quiz'),
    path('attempt/<int:quiz_id>/', views.attempt_quiz, name='attempt_quiz'),
    path('dashboard/', views.dashboard, name='dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)