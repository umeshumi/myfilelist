from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from . import views

app_name = 'docker'

urlpatterns = [
	path('', views.home, name='home'),
	path('signup/', views.SignUpView, name='signup'),
	path('docview/<int:userid>/', views.PersonDocumentView, name='docview'),
	path('docverify/<int:userid>/', views.DocVerify, name='docverify'),
	path('newdoc/', views.DocCreateView, name='newdoc'),
	path('userlist/', views.UserListView, name='userlist'),
	path('doclist/', views.DocumentListView, name='doclist'),
	path('docval/<int:docid>/', views.DeleteDoc, name='docdelete'),
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	
	path('logout/', views.LogotView, name='logout'),
	
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
