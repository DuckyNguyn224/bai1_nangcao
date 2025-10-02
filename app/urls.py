from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('single-product/', views.single_product, name='single_product'),

    # Product CRUD URLs
    path('product-crud/', views.ProductListView.as_view(), name='product_list'),
    path('product-crud/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product-crud/add/', views.ProductCreateView.as_view(), name='product_add'),
    path('product-crud/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product-crud/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # Team Member CRUD URLs
    path('team-member-crud/', views.TeamMemberListView.as_view(), name='team_member_list'),
    path('team-member-crud/add/', views.TeamMemberCreateView.as_view(), name='team_member_add'),
    path('team-member-crud/<int:pk>/edit/', views.TeamMemberUpdateView.as_view(), name='team_member_edit'),
    path('team-member-crud/<int:pk>/delete/', views.TeamMemberDeleteView.as_view(), name='team_member_delete'),
]
