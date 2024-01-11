from django.shortcuts import render

# Create your views here.
def catalog(request):
    context = {
        'title': "Home - Каталог",
        'goods': [
            {
                'name': "The Tea from 3 table",
                'description': 'Котавыда ывдаоф23 овлао',
                'price': 157.00,
            },
            {
                'name': "The Tea from 2 table",
                'description': 'Котавыда ывдаоф23 овлао',
                'price': 100.00,
            },
        ]
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')