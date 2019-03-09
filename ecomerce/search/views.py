from django.shortcuts import render
from products.models import Product
# Create your views here.
def searchproductview(request):
	query = request.GET.get('q')
	if query is not None:
		queryset = Product.objects.filter(title__icontains=query)
	else:
		queryset = Product.objects.none()
	context = {
	'object_list':queryset
	}
	return render(request,"products/list.html", context)