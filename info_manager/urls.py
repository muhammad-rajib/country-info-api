from django.conf.urls import url
from info_manager import views

urlpatterns = [
    url('create/country-info', views.create_country_info),
    url('update/country-info', views.update_country_info),
    # url('delete/country-info', views.delete_country_info),
    url('view/country-info/list', views.country_info_list),
    url('view/country-details', views.country_details),
]
