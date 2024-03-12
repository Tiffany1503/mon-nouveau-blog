from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('airline_ranking/', views.airline_ranking, name='airline_ranking'),
    path('airline_ranking/', views.airline_ranking, name='airline_ranking'),
    path('ranking_by_country/', views.ranking_by_country, name='ranking_by_country'),
    path('ranking_by_country/be.html', views.be, name='be'),
    path('ranking_by_country/br.html', views.br, name='br'),
    path('ranking_by_country/ca.html', views.ca, name='ca'),
    path('ranking_by_country/da.html', views.da, name='da'),
    path('ranking_by_country/fr.html', views.fr, name='fr'),
    path('ranking_by_country/al.html', views.al, name='al'),
    path('ranking_by_country/gr.html', views.gr, name='gr'),
    path('ranking_by_country/ir.html', views.ir, name='ir'),
    path('ranking_by_country/it.html', views.it, name='it'),
    path('ranking_by_country/ja.html', views.ja, name='ja'),
    path('ranking_by_country/me.html', views.me, name='me'),
    path('ranking_by_country/pb.html', views.pb, name='pb'),
    path('ranking_by_country/no.html', views.no, name='no'),
    path('ranking_by_country/pol.html', views.pol, name='pol'),
    path('ranking_by_country/por.html', views.por, name='por'),
    path('ranking_by_country/es.html', views.es, name='es'),
    path('ranking_by_country/su.html', views.su, name='su'),
    path('ranking_by_country/tu.html', views.tu, name='tu'),
    path('ranking_by_country/eau.html', views.eau, name='eau'),
    path('ranking_by_country/uk.html', views.uk, name='uk'),
    path('ranking_by_country/usa.html', views.usa, name='usa'),
    path('airline', views.airline, name='airline'),
]
