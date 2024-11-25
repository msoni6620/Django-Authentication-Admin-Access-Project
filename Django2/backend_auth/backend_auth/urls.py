from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import register, admin_view, index_view,register_view,registerview

urlpatterns = [
    path('', index_view, name='home'),
    path('register/', registerview, name='register'),  # Corrected this
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('admin/', admin_view, name='admin_view'),
    path('admin/', admin.site.urls),
]
