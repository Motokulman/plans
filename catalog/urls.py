from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plans/', views.PlansListView.as_view(), name='plans'),
    path('approved_plans/', views.ApprovedPlansListView.as_view(), name='approved_plans'),
    path('plan/<int:pk>', views.PlanDetailView.as_view(), name='plan-detail'),
    path('myapplyedplans/', views.PlansApplyedByConsumerListView.as_view(), name='my-applyed-plans'),
    path('architectmanageplans/', views.ArchitectManagePlans.as_view(), name='architect-manage-plans'), 
    path('plan/create/', views.PlanCreate.as_view(), name='plan_create'),
    path('plan/<int:pk>/update/', views.PlanUpdate.as_view(), name='plan_update'),
    path('plan/<int:pk>/delete/', views.PlanDelete.as_view(), name='plan_delete'),

]