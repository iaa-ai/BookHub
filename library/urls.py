from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('home', HomeView.as_view(), name='home_view'),
    path('books/', BookListView.as_view(), name='books_view'),
    path('authors/', AuthorListView.as_view(), name='authors_view'),
    path('info/', UserInfoListView.as_view(), name='uinfo_view'),
    path('info/edit', edit_user_info, name='uinfo_edit'),
    # path('genres/', GenreListView.as_view(), name='genres_view'),
    path('members/', MemberListView.as_view(), name='members_view'),
    path('bookinstances/', BookInstanceListView.as_view(), name='bookinstances_view'),
    path('author/add/', AuthorAdd.as_view(), name='author_add'),
    path('author/edit/<int:pk>/', AuthorUpdate.as_view(), name='author_edit'),
    path('author/delete/<int:pk>/', AuthorDelete.as_view(), name='author_delete'),
    path('book/add/', book_create, name='book_add'),
    path('members/add/', MemberCreate.as_view(), name='member_add'),
    path('members/edit/<int:pk>/', MemberUpdate.as_view(), name='member_edit'),
    path('members/delete/<int:pk>/', MemberDelete.as_view(), name='member_delete'),
    path('bookinstance/add/', BookInstanceCreate.as_view(), name='bookinstance_add'),
    path('bookinstance/edit/<int:pk>/', BookInstanceUpdate.as_view(), name='bookinstance_edit'),
    path('bookinstance/delete/<int:pk>/', BookInstanceDelete.as_view(), name='bookinstance_delete'),
    path('book/<int:pk>/', book_create, name='book-detail'),
    path('book/update/<int:pk>/', book_update, name='book_update'),
    path('book/delete/<int:pk>/', BookDelete.as_view(), name='book_delete'),
    path('author/update/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('toppicks/', TopPicksView.as_view(), name='toppicker_view'),
    path('users/',UserListView.as_view(),name='users_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)