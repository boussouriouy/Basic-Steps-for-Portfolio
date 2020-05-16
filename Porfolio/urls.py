from django.urls import path
from .views import home_view, about_view, contact_view, information_view, register_view, member_view, member_details
app_name = 'Porfolio'

urlpatterns = [
   path('home/', home_view),
   path('about/', about_view),
   path('cont/', contact_view),
   path('info/', information_view),
   path('join/', register_view),
   path('list/', member_view),
   path('detail/<int:id>/', member_details, name='member_info'),

]
