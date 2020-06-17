from rest_framework import routers
from me import api as me_api

router = routers.DefaultRouter()
router.register(r'me',  me_api.MeViewset)
