from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="posts-index"),
    # # path("list",views.ListView.as_view()),
    # path("create",views.create, name="blog-create"),
    # path("posts",views.posts, name="blog-posts"),
    # path("posts/<slug:slug>",views.single_post, name="posts-single-post"),
    # path("customer/create",views.create_customer, name="create-customer")
]