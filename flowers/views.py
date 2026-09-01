from django.shortcuts import render

# Create your views here.

def f_index(request):

    content = {
        'range_12': range(12)
    }
    return render(request, 'flower/index.html', content)

# def User