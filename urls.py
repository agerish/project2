from django.contrib import admin
from django.urls import path
from APP.views import index
from django.conf import settings
from django.conf.urls.static import static
from .views import detail

from APP import views



urlpatterns = [
    path('',index,name='home'),
    path('about/',views.about,name='about'),
    path('footer/', views.footere, name='footer'),
    path('partenaire/', views.trainer, name='trainer'),
    path('evenement/', views.event, name='event'),
path('top/', views.top, name='top'),
path('contact-us/', views.contactus, name='contactus'),
path('info/<int:id>/',views.infodetail,name='infodetail'),
path('call/<int:id>/',views.infodetaile,name='A'),
path('cool/<int:id>/',views.infodetailes,name='B'),
path('push/<int:id>/',views.infodetailee,name='C'),
path('info4/<int:id>/',views.infodetail4,name='infodetail4'),
path('info5/<int:id>',views.infodetail5,name='infodetail5'),
path('info6/<int:id>',views.infodetail6,name='infodetail6'),
path('info7/<int:id>',views.infodetail7,name='infodetail7'),
path('info8/<int:id>',views.infodetail8,name='infodetail8'),
path('info9/<int:id>',views.infodetail9,name='infodetail9'),
path('info10/<int:id>',views.infodetail10,name='infodetail10'),
path('info11/<int:id>',views.infodetail11,name='infodetail11'),
path('info12/<int:id>',views.infodetail12,name='infodetail12'),
path('info13/<int:id>',views.infodetail13,name='infodetail13'),
path('info14/<int:id>',views.infodetail14,name='infodetail14'),
path('info15/<int:id>',views.infodetail15,name='infodetail15'),
path('info16/<int:id>',views.infodetail16,name='infodetail16'),
path('info17/<int:id>',views.infodetail17,name='infodetail17'),
path('info18/<int:id>',views.infodetail18,name='infodetail18'),
path('info19/<int:id>',views.infodetail19,name='infodetail19'),
path('info20/<int:id>',views.infodetail20,name='infodetail20'),
path('info21/<int:id>',views.infodetail21,name='infodetail21'),
path('info22/<int:id>',views.infodetail22,name='infodetail22'),
path('info23/<int:id>',views.infodetail23,name='infodetail23'),
path('info24/<int:id>',views.infodetail24,name='infodetail24'),
path('info25/<int:id>',views.infodetail25,name='infodetail25'),
path('info26/<int:id>',views.infodetail26,name='infodetail26'),
    path('info1/<int:id>',views.infodetailrobe,name='infodetailrobe'),
    path('info/',views.info,name='info'),
    path('RobeAgerish/',views.Robe, name='Robe'),
    path('product/',views.product,name='product'),
    path('<int:id>/',views.detail,name='detail'),
    path('produit/<int:id>/', views.sandaldetail, name='SandalDetail'),
    path('produite/<int:id>/', views.sandaldetailfemme, name='SandalDetailfemme'),
    path('produits/<int:id>/', views.sandaldetailhomme, name='SandalDetailhomme'),
    path('t-shirts/<int:id>/', views.tshirt, name='tshirt'),
    path('t-shirts-femme/<int:id>/', views.tshirtfemme, name='tshirtfemme'),
    path('t-shirts-homme/<int:id>/', views.tshirthomme, name='tshirthomme'),

    path('robe/<int:id>/', views.robeboheme, name='robeboheme'),
    path('robe0/<int:id>/', views.robecourte, name='robecourte'),
    path('robe2/<int:id>/', views.robesimple, name='robesimple'),
    path('robe1/<int:id>/', views.robelongue, name='robelongue'),

    path('perique/<int:id>/', views.periquenaturel, name='periquenaturel'),
    path('perique0/<int:id>/', views.periquehumainhair, name='periquehumainhair'),
    path('perique2/<int:id>/', views.periquesinthetique, name='periquesinthetique'),
    path('perique1/<int:id>/', views.periqueperuvienne, name='periqueperuvienne'),

    path('jupelongue/<int:id>/', views.jupelongue, name='jupelongue'),
    path('jupecourte/<int:id>/', views.jupecourte, name='jupecourte'),

    path('Haut0/<int:id>/', views.hauthomme, name='hauthomme'),
    path('Haut/<int:id>/', views.hautfemme, name='hautfemme'),

    path('basket/<int:id>/', views.basket, name='basket'),
    path('basket_femme/<int:id>/', views.basket_femme, name='basket_femme'),
    path('basket_homme/<int:id>/', views.basket_homme, name='basket_homme'),

    path('bijoux/<int:id>/', views.bijoux, name='bijoux'),
    path('bijoux_femme/<int:id>/', views.bijoux_femme, name='bijoux_femme'),
    path('bijoux_homme/<int:id>/', views.bijoux_homme, name='bijoux_homme'),

path('merci/',views.merci,name='merci'),
path('T-shirts_Agerish/',views.T_shirts,name='T-shirts'),
path('Sandals_Agerish/',views.Sandals,name='Sandals'),
path('Periques_Agerish/',views.Perique,name='Perique'),
path('Les_hauts_Agerish/',views.Hauts,name='Hauts'),
path('Jupe_longue_Agerish/',views.Jupe,name='Jupe'),
path('Bijoux_Agerish/',views.Bijoux,name='Bijoux'),
path('Baskets_Agerish/',views.Baskets,name='Baskets'),
path('Accessoires_Agerish/',views.Accessoires,name='Accessoires'),
    path('signup/',views.signup,name='signup')

   ]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)