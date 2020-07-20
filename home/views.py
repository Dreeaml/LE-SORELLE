from django.shortcuts import render

def index(request):
    """ A view that displays the index page"""
    return render(request, 'index.html')
    
def faq(request):
    """ A view that displays the Frequent asked questions page"""
    return render(request, 'home/faq.html')

def sizes(request):
    """ A view that displays the Size guide page"""
    return render(request, 'size_guides.html')