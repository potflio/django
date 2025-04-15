from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from .models import Photo

def upload(request):
    return render(request, 'upload.html')

@csrf_exempt  # Only for dev, better to handle CSRF token in AJAX (which we do above)
def submit(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        images = request.FILES.getlist('images')

        for image in images:
            Photo.objects.create(title=title, image=image)

        return JsonResponse({'message': 'Images uploaded successfully'})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
