from django.urls import  path
from .views import FAQview


urlpatterns = [
    path('',  FAQview.as_view()), 
]

# from django.urls import path
# from .views import FAQview
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('category', FAQview)
# # router.register('brand', BrandView)

# urlpatterns = [

# ] + router.urls