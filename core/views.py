from django.shortcuts import render
from .models import Category,Waifu
# from django.
# Create your views here.
def homepage(request):
    data=Waifu.objects.select_related('category').filter(category__is_nsfw=False)[:12]
    return render(request,"core/homepage.html",context=dict(waifus=data))

def shop(request):
    active_category = request.GET.get("category","")
    query = request.GET.get("query","")
    if active_category:
        q1_res = Waifu.objects.select_related("category").filter(category__slug=active_category)
    if query :
        q2_res = Waifu.objects.filter(name__contains=query)
    if active_category and query:
        data = q1_res & q2_res
    elif active_category:
        data = q1_res
    elif query:
        data= q2_res
    else :
        data=Waifu.objects.select_related('category').filter(category__is_nsfw=False)
    if data :
        data = data[:12]
    else :
        data = None
    catergoris = Category.objects.filter(is_nsfw=False).all()
    return render(request,"core/shop.html",context=dict(waifus=data,categories=catergoris,active_category=active_category))
    # return render(request)
def product(request):
    return render(request,"core/product.html")