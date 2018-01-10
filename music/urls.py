from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'music'
urlpatterns = [
	# /music/
	path('', views.IndexView.as_view(), name='index' ),
	#/music/ablum
	path('<pk>/', views.DetailView.as_view(), name='detail'),

	path('register/', views.UserFormView.as_view(), name='register'),

	path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

	path('album/<pk>/', views.AlbumUpdate.as_view(), name='album-update'),

	path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='delete-album'),

	path('<pk>/song/create_song/', views.SongCreate.as_view(), name='create_song')
]
