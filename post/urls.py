from django.urls import path
from . import views
from .views import (PostListView_ug,PostDetailView,PostListView_scholl,PostListView_puc,
                    PostListView_ug,PostListView_pg,PostListView_total,PostListView_category,
                    PostListView_backward,PostListView_minorities,PostListView_sc,PostListView_offline,PostDetailView_offline,test)

urlpatterns=[
    path('',views.home_page,name='home'),
    path('test/',views.test,name='test'),
    path('post/',views.PostListView_total.as_view(),name='total'),
    path('post/offline',views.PostListView_offline.as_view(),name='offline'),
    path('post/scholl/',views.PostListView_scholl.as_view(),name='scholl'),
    path('post/puc/',views.PostListView_puc.as_view(),name='puc'),
    path('post/ug/',views.PostListView_ug.as_view(),name='ug'),
    path('post/pg/',views.PostListView_pg.as_view(),name='pg'),
    path('post/category/',views.PostListView_category.as_view(),name='category'),
    path('post/category/sc',views.PostListView_sc.as_view(),name='sc'),
    path('post/category/minorities',views.PostListView_minorities.as_view(),name='minorities'),
    path('post/category/backward',views.PostListView_backward.as_view(),name='backward'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('post/<int:pk>/offline',views.PostDetailView_offline.as_view(),name='detail_offline'),

]