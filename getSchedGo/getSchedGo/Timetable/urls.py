from django.conf.urls import url
from . import views
app_name = 'Timetable'
urlpatterns = [
    url(r"^$", views.EventList, name="EventList"),
    url(r"^create/$", views.CreateEvent, name="CreateEvent"),
    url(r"^(?P<pk>[0-9]+)/edit$", views.CreateEvent, name="EditEvent"),
]
