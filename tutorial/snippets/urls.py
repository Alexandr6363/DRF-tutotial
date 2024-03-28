from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include

app_name = "snippet"
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)