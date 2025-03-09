from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    ...,
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),  # Token endpoint
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),I
    path('', include(router.urls)),
]


