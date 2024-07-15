from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, RarityViewSet, TypeViewSet, SkillViewSet, ItemViewSet, ArtifactViewSet, CharacterViewSet

router = DefaultRouter()
router.register(r'classes', ClassViewSet)
router.register(r'rarities', RarityViewSet)
router.register(r'types', TypeViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'items', ItemViewSet)
router.register(r'artifacts', ArtifactViewSet)
router.register(r'characters', CharacterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
