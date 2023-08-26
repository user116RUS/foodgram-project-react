from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    RecipeViewSet,
    IngredientViewSet,
    TagViewSet,
    CustomUserViewSet,
    FavoriteView,
)


app_name = 'api'

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = (
    path('', include(router.urls)),
    path(
        'recipes/<int:id>/favorite/',
        FavoriteView.as_view(),
        name='favorite'
    ),
    path('auth/', include('djoser.urls.authtoken')),
)
