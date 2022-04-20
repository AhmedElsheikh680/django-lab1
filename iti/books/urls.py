from django.urls import path
from .views import index,show


urlpatterns = [
  path('', index, name="index"),
    path('<int:book_id>', show, name="show")

    # path('<int:book_id>', welcome, name="book_profile")

    # path('<int:book_id>', welcome)

];
