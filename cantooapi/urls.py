from django.urls import path
from cantooapi.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tag/', views.TagList.as_view(), name='tag_upload'),
    path('interestTag/', views.InterestTagList.as_view(), name='interestTag_upload'),
]