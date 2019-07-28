from rest_framework import routers
from frstapp.api import api_views as myapp_views


router = routers.DefaultRouter()
router.register(r'dmodels',myapp_views.DModelViewset)

