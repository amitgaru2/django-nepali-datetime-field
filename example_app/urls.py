from django.urls import path

from . import views

urlpatterns = [
    path('example/', views.ExampleListView.as_view(), name='example_list'),
    path('example/create', views.ExampleCreateView.as_view(), name='example_create'),
    path('example/<int:pk>/update/', views.ExampleUpdateView.as_view(), name='example_update'),
    path('example/<int:pk>/delete/', views.ExampleDeleteView.as_view(), name='example_delete'),
]
