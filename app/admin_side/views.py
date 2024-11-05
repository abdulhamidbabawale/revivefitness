from django.shortcuts import render
from app.site_data.models import Classes

# Create your views here.

def admin_classes(request):
    if request.method == 'POST':
        classs_img = request.FILES.get('classs_img')
        class_name=request.POST.get('class_name')
        decription=request.POST.get('decription')

        class_data=Classes.objects.create(classs_img=classs_img,class_name=class_name,decription=decription)
        class_data.save()

    all_class = Classes.objects.all().values()
    # image_urls = [img.url for img in all_class]
    # all_class = [
    #     {
    #         'class_name': obj.class_name,
    #         'decription': obj.decription,
    #         'classs_img': obj.classs_img.url if obj.classs_img else None  # Retrieve URL if image exists
    #     }
    #     for obj in classes
    # ]
    return render(request,f'admin_classes.html',{'all_class':all_class})
    # image_urls = [img.url for img in all_class]  # Access the URL of each Cloudinary resource

    # Pass the URLs to the template
    # return render(request, 'admin_classes.html', {'image_urls': image_urls})
