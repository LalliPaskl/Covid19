from django.conf.urls import url
from besant_medical_app import views
from django.urls import path
urlpatterns = [
path('', views.logview,name="homepage"),
# path('registration/', views.regview),
url(r'^regview/', views.regview, name="regview"),
url(r'^medsupplier/', views.medstoringsupview, name="medsupplier"),
url(r'^medmedical/', views.medmedicalshopview, name="medmedical"),
url(r'^suptablets/', views.suptotaltablets, name="suptablets"),
url(r'^email/', views.supemailsending, name="supemailsending"),
# url(r'^email/', views.admemailsending, name="admemailsending"),
]