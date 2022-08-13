# from django.contrib import admin
from django.urls import path
from job.views import job_details,job_list
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',job_list),
    path('<int:id>',job_details),
]