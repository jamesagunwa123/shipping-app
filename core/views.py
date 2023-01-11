from django.shortcuts import render, redirect
from django.views import View
from .models import Product

from django.conf import settings
from django.views.static import serve

# Create your views here.

class Tracking(View):
	def get(self, request):
		return render(request, 'tracking.html', {'invalidcode': request.GET.get('track') == 'invalidcode'})


class Tracking1(View):
	def get(self, request):
		return render(request, 'tracking1.html', {})

	def post(self, request):
		trackcode = request.POST.get('trackcode')
		product = Product.objects.filter(tracking_code=trackcode).first()
		if product:
			return render(request, 'tracking1.html', {'product': product})
		return redirect('/tracking.php?track=invalidcode')



def serve_static(request, path):
    return serve(request, path, document_root=settings.STATICFILES_DIRS[0])
