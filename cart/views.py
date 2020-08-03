from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from jewelry_store.models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm, MAX_AMOUNT
# Create your views here.


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id_product=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        amount = cd['quantity'] + cart.check_product(pk)
        if amount <= MAX_AMOUNT and amount <= product.amount_storage:
            cart.add(product=product,
                     quantity=cd['quantity'])
        elif amount > MAX_AMOUNT:
            cart.add(product=product,
                     quantity=MAX_AMOUNT - cart.check_product(pk))
        elif amount > product.amount_storage:
            cart.add(product=product,
                     quantity=product.amount_storage - cart.check_product(pk))
        cart.save()
    return redirect('product_detail', pk=pk)


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id_product=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
