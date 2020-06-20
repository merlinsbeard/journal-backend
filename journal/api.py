from rest_framework import routers
from me import api as me_api
from works import api as works_api

router = routers.DefaultRouter()
router.register(r'me',  me_api.MeViewset)
router.register(r'works', works_api.WorkViewset)
