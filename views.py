from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Unit
from django.db.models import Q
from . form import UnitForms

def firstpage(request):
    return render(request, 'report/firstpage.html', {})


def units(request):
    search_query = request.GET.get('search', '')
    if search_query:
        units = Unit.objects.filter(Q(cinnoSid__icontains=search_query) | Q(imei__icontains=search_query))
    else:
        units = Unit.objects.filter(repairDate__lte=timezone.now()).order_by('repairDate')

    return render(request, 'report/units.html', {'units' : units})

def unit_detail(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    fields = UnitForms
    article = Unit.objects.get(pk=pk)
    form = fields(initial={'headline' : 'Initial headline'}, instance=article)
    if request.method == 'POST':
        un = UnitForms(request.POST)
        vd = un.is_valid()
        print(vd)
    return render(request, 'report/totalunit.html', {'form': form, 'unit' : unit})
