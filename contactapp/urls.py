from django.urls import path, include
from .views import ContactViewSet, AuthorViewSet, BookViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("contacts", ContactViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = [path("", include(router.urls))]
