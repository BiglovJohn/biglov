from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProfileListView, ProfileDetailView, ProfileEditFromView, ProfileFormView, \
    register_view, AnotherLoginView, AnotherLogoutView

urlpatterns = [
    path('', AnotherLoginView.as_view(), name='login'),
    path('profiles/', ProfileListView.as_view(), name='profiles'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profiles_detail'),
    path('profile/create', ProfileFormView.as_view(), name='create'),
    path('profile/<int:profile_id>/edit', ProfileEditFromView.as_view(), name='edit'),
    path('register/', register_view, name='register'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
