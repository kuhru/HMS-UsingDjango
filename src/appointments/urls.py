from django.urls import path
from .views import (
    aptmt_list_view,
    aptmt_create_view,
    aptmt_details_view,
    aptmt_update_view,
    aptmt_delete_view,
)

urlpatterns = [
    path('', aptmt_list_view),
    path('details/', aptmt_list_view),
    path('new/', aptmt_create_view),
    path('details/<int:id>/', aptmt_details_view),
    path('update/<int:id>/', aptmt_update_view),
    path('details/<int:id>/update', aptmt_update_view),
    path('delete/<int:id>/', aptmt_delete_view),
    path('details/<int:id>/delete', aptmt_delete_view),
]
