from django.shortcuts import render

def summary(request):
    return render(
        request,
        'safeinfo/summary.html'
    )

def cctv(request):
    return render(
        request,
        'safeinfo/cctv.html'
    )

def cctv_category(request):
    return render(
        request,
        'safeinfo/cctv_category.html'
    )
    
def data(request):
    return render(
        request,
        'safeinfo/data.html'
    )