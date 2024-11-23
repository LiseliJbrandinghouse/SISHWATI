from django.shortcuts import redirect, render
from .models import Product, ProductImage
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta


def homepage(request):
    new_arrivals = Product.objects.filter(is_new_arrival=True).order_by('-created_at')[:10]  # Limit to 10 new arrivals
    return render(request, 'index.html', {'new_arrivals': new_arrivals})


def arrivals_page(request):
    all_products = Product.objects.all().order_by('-created_at')
    return render(request, 'arrivals.html', {'all_products': all_products})
def store_page(request):
    category = request.GET.get('category', 'All').lower()
    now = timezone.now()

    # Filter products based on the category and whether they are launched
    if category == 'all':
        products = Product.objects.filter(launch_date__lte=now).order_by('-created_at')
    elif category == 'new-launch':
        # Show products that are recently launched and still considered new (e.g., within 30 days)
        products = Product.objects.filter(is_new_launch=True, launch_date__lte=now).filter(
            launch_date__gte=now - timedelta(days=30)
        ).order_by('-launch_date')
    else:
        products = Product.objects.filter(category__iexact=category, launch_date__lte=now).order_by('-created_at')

    return render(request, 'store.html', {'products': products, 'category': category})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    color = request.POST.get('color', 'default')
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})

    total_price = product.price * quantity

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
        cart[str(product_id)]['total_price'] = str(float(cart[str(product_id)]['price']) * cart[str(product_id)]['quantity'])
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': quantity,
            'color': color,
            'image': product.image.url,
            'total_price': str(total_price),
        }

    # Save the cart back to the session
    request.session['cart'] = cart

    # Handle AJAX request to return updated cart count
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'message': 'Item added to cart',
            'cart_count': sum(item['quantity'] for item in cart.values())
        })

    # Redirect to store page after adding to cart for non-AJAX request
    return redirect('store')

def cart_view(request):
    # Get the cart from the session
    cart = request.session.get('cart', {})

    # Calculate the total price of all items in the cart
    total_price = sum(float(item['total_price']) for item in cart.values())

    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_images = ProductImage.objects.filter(product=product)

    return render(request, 'product_detail.html', {
        'product': product,
        'product_images': product_images,
        'is_cart_page': False,  # Setting this to False
    })

def clear_cart(request):
    # Clear the cart session
    request.session['cart'] = {}
    return redirect('cart')

def remove_from_cart(request, product_id):
    # Get the cart from the session
    cart = request.session.get('cart', {})

    # Remove the specific product from the cart
    if str(product_id) in cart:
        del cart[str(product_id)]
    
    # Save the updated cart back to the session
    request.session['cart'] = cart

    return redirect('cart')

def about(request):
    return render(request, 'about.html')     