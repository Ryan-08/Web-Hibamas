from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('Beranda', views.index, name='index'),
    path('Dokumentasi', views.dokumentasi, name='dokumentasi'),
    path('Pengajuan', views.pengajuan, name='pengajuan'),
    path('Pengajuan/item/<int:item_id>', views.item, name='item'),
    path('Pengumuman', views.pengumuman, name='pengumuman'),
    path('Hubungi', views.contact, name='contact'),
    path('Dashboard', views.menu, name='menu'),

    url(r'^upload-doc/$', views.up_dokumentasi, name='upload_doc'),
    url(r'^upload-prop/$', views.up_proposal, name='upload_prop'),
    url(r'^upload-umum/$', views.up_pengumuman, name='upload_umum'),

    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]