from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plans/', views.PlansListView.as_view(), name='plans'),
    path('finalized_plans/', views.FinalizedPlansListView.as_view(), name='finalized_plans'),
    path('plan/<int:pk>', views.PlanDetailView.as_view(), name='plan-detail'),
]