from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
#from cart.cart import Cart

# Create your views here.
def product_list(request, category_slug=None):
    template_name = 'shop/product/list.html'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(Category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request,template_name, context)


def search(request, category_slug=None):
    try:
        q = request.GET.get('q')
    except:
        q = None

    category = None
    categories = Category.objects.all()    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    

    if q:
        product = Product.objects.filter(nameProd__icontains=q)
        context = {'products': product, 'category': category, 'categories': categories}
    else:
        context = {}

    template_name = 'shop/product/list.html'
    return render(request, template_name, context)



def product_detail(request, id, slug):
    template_name = 'shop/product/detail.html'
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, template_name, context)

