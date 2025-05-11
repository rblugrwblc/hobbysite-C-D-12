from django.shortcuts import render, get_object_or_404
from .models import Commission, Comment

def commission_list(request):
    commissions = Commission.objects.all()
    return render(request, 'commissions_list.html', {'commissions': commissions})

def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    comments = Comment.objects.filter(commission=commission)
    return render(request, 'commissions_detail.html',
        {'commission': commission,
         "comments":comments
    })
