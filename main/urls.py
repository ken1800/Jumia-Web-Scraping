from main import views
from django.urls import path,include


urlpatterns = [

    path('',views.home,name='home'),
    path('',views.get_more_tables,name='get_more_tables'),
    # path('delete/<task_id>',views.delete_task,name='delete'),
    # path('complete/<task_id>',views.complete_task,name='complete'),
    # path('edit/<task_id>',views.edit_task,name='edit'),
    # path('about',views.about,name='about'),
    # path('contact',views.contact,name='contact'),

]
