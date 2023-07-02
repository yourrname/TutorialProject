from django.urls import path
from . import views

urlpatterns=[

    path('',views.index, name="index"),
    path('polls/', views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]