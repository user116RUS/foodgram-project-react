from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import RecipeViewSet
from tags_ingr.views import IngredientViewSet, TagViewSet
from users.views import CustomUserViewSet


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', CustomUserViewSet, basename='users')
router_v1.register('recipes', RecipeViewSet, basename='recipes')
router_v1.register('tags', TagViewSet, basename='tags')
router_v1.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = (
    path("", include(router_v1.urls)),
    path("auth/", include("djoser.urls.authtoken")),
)
