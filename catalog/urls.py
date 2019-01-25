from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plans/', views.PlansListView.as_view(), name='plans'),
    path('approved_plans/', views.ApprovedPlansListView.as_view(), name='approved_plans'),
    path('plan/<uuid:pk>/', views.PlanDetailView.as_view(), name='plan-detail'),
    path('architect/<pk>/', views.ArchitectDetailView.as_view(), name='architect-detail'),
    #re_path(r'^plan/(?P<pk>\d+)$', views.PlanDetailView.as_view(), name='plan-detail'),
    path('myapplyedplans/', views.PlansApplyedByConsumerListView.as_view(), name='my-applyed-plans'),
    path('architectmanageplans/', views.ArchitectManagePlans.as_view(), name='architect-manage-plans'), 
    path('plan/create/', views.PlanCreate.as_view(), name='plan_create'),
    #path('plan/<uuid:pk>/update/', views.PlanUpdate.as_view(), name='plan_update'),
    #path('plan/<uuid:pk>/delete/', views.PlanDelete.as_view(), name='plan_delete'),
    path('plan/<uuid:pk>/edit/', views.edit_plan_architect, name='edit-plan-architect'),
    path('plan/<uuid:pk>/edit/like_plan/', views.like_plan, name='like_plan'),

]