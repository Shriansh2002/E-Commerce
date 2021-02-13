from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from accounts.models import MyUser
from products.models import Product

from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            user = MyUser.objects.get(email=request.user.email)
            order.user = user
            order.save()
            for item in cart:
                pro = Product.objects.get(nameProd=item['product'])
                pro.stock = pro.stock - item['quantity']
                pro.save()
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})


@login_required
def order_history(request):
    user = request.user
    purchases = Order.objects.filter(user_id=user.id)
    context = {
        'purchases': purchases
    }
    return render(request, 'orders/order/history.html', context)


@login_required
def order_history_list(request, id):
    template_name = 'orders/order/list.html'

    order_id = OrderItem.objects.filter(order=id)
    product = Product.objects.all()

    context = {
        'order_items': order_id,
        'product': product
    }

    return render(request, template_name, context)
