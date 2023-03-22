from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.SiteListView.as_view(), name="site"),
    path("pending/", views.SitePendingListView.as_view(), name="site_pending"),
    path("done/", views.SiteDoneListView.as_view(), name="site_done"),
    path("put/<int:id>/", views.SiteUpdateView.as_view(), name='site_update'),
    path("get/", views.GetPendingSite.as_view(), name='get_pending'),
    path("post/", views.SiteCreateView.as_view(), name="site_create")
]
