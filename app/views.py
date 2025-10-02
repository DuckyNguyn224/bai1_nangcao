from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

from .models import Product, Banner, TeamMember

def home(request):
    banners = Banner.objects.filter(active=True)
    latest_products = Product.objects.filter(active=True).order_by('-created_at')[:6]
    return render(request, 'app/home.html', {'banners': banners, 'latest_products': latest_products})

def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'app/about.html', {'team_members': team_members})

def contact(request):
    return render(request, 'app/contact.html')

from .models import Product

def products(request):
    #sample
    from django.utils.timezone import now, timedelta
    from .models import Product

    if Product.objects.count() < 2:
        Product.objects.create(
            title="Sample Product 1",
            price=19.99,
            description="This is a sample product 1.",
            image="products/product_01.jpg",
            active=True,
            created_at=now() - timedelta(days=1),
            featured=True
        )
        Product.objects.create(
            title="Sample Product 2",
            price=29.99,
            description="This is a sample product 2.",
            image="products/product_02.jpg",
            active=True,
            created_at=now(),
            flash_deals=True
        )

    filter_param = request.GET.get('filter', 'all')

    if filter_param == 'featured':
        products = Product.objects.filter(active=True, featured=True).order_by('-created_at')
    elif filter_param == 'flash_deals':
        products = Product.objects.filter(active=True, flash_deals=True).order_by('-created_at')
    elif filter_param == 'last_minute':
        products = Product.objects.filter(active=True, last_minute=True).order_by('-created_at')
    else:
        products = Product.objects.filter(active=True).order_by('-created_at')

    return render(request, 'app/products.html', {'products': products})

def single_product(request):
    return render(request, 'app/single-product.html')


class ProductListView(ListView):
    model = Product
    template_name = 'app/product_list.html'
    context_object_name = 'products'
    ordering = ['-created_at']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'app/product_form.html'
    fields = ['title', 'price', 'description', 'image', 'active', 'featured', 'flash_deals', 'last_minute']
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'app/product_form.html'
    fields = ['title', 'price', 'description', 'image', 'active', 'featured', 'flash_deals', 'last_minute']
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'app/team_member_list.html'
    context_object_name = 'team_members'


class TeamMemberCreateView(CreateView):
    model = TeamMember
    template_name = 'app/team_member_form.html'
    fields = ['name', 'role', 'description', 'image', 'facebook', 'twitter', 'linkedin', 'behance']
    success_url = reverse_lazy('team_member_list')


class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    template_name = 'app/team_member_form.html'
    fields = ['name', 'role', 'description', 'image', 'facebook', 'twitter', 'linkedin', 'behance']
    success_url = reverse_lazy('team_member_list')


class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    template_name = 'app/team_member_confirm_delete.html'
    success_url = reverse_lazy('team_member_list')
