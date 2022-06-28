from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Roster.views import RosterListView

app_name = 'wowraid'
urlpatterns=[
    #Home Page
    path('',views.home, name='home'),
    #Roster Page
    #path('rosters/',views.rosters, name='rosters'),
    path('rosters/', RosterListView.as_view(), name="rosters"),
    #Specific Roster
    path('rosters/<int:roster_id>/',views.roster, name='roster'),
    #About
    path('about/', views.about, name='about'),
    #Creating a Roster
    #path('new_roster/',views.new_roster, name='new_roster')
]
urlpatterns += staticfiles_urlpatterns()