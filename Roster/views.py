from django.views.generic import ListView
from multiprocessing import context
from django.shortcuts import redirect, render
from django_tables2 import SingleTableView

from Roster.tables import RosterTable

from .models import Roster


def home(request):
    #Home Page
    return render(request,'Roster/home.html')

def rosters(request):
    #Roster Page
    rosters = Roster.objects.order_by('start_time')
    context = {'roster':rosters}
    return render(request, 'Roster/rosters.html', context)

def roster(request, roster_id):
    #Show Specific Roster
    roster = Roster.objects.get(roster_id=roster_id)
    context = {'roster':roster}
    return render(request, 'Roster/roster.html',context)

def about(request):
    return render(request, 'Roster/about.html')

class RosterListView(SingleTableView):
    model = Roster
    table_class = RosterTable
    template_name = "Roster/rosters.html"


#def new_roster(request):
#    if request.method != 'POST':
#        form = RosterForm()
#    else:
#        form = RosterForm(data=request.POST)
#        if form.is_valid:
#            form.save()
#            return redirect('Roster/rosters.html')
#    context = {'form':form}
#    return render(request, 'Roster/new_roster.html',context)
    
