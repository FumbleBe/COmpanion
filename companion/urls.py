from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from actors.views import *
from rules.views import *
from items.views import *


router = routers.SimpleRouter()
router.register('characters', CharacterViewset, basename='characters')
router.register("capacities", CapacityViewset, basename="capacities")
router.register("paths", PathViewset, basename="paths")
router.register("profiles", ProfileViewset, basename="profiles")
router.register("species", SpeciesViewset, basename="species")
router.register("items", ItemViewset, basename="items")
router.register(r"equipments/(?P<actor_id>[0-9]+)", EquipmentViewset, basename="equipments")

# router.register('admin/category', AdminCategoryViewset, basename='admin-category')
# router.register('admin/article', AdminArticleViewset, basename='admin-article')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
