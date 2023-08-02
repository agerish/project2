from django.contrib import admin
from APP.models import Habits,Commande,Robebohemes,Robelongues,Robesimples,Robesoirees,Evenement,Partenaire
from APP.models import Robecourtes,Jupecourtes,Jupelongues,Bijouxs,Bijouxfemmes,Bijouxhommes,Basketsfemmes,Basketes,Basketshommes,Periquebresiliennes,Periquenaturels,Periqueperruviennes,Periquesinthetiques,Periquehumainhairs,Accesoiredemodes,Accessoiredemeubles,Machineelectroniques,Sandalsfemmes,Sandal,Sandalshommes,Tshirtfemmes,Tshirts,Tshirthommes,Leshautsfemmes,Leshautshommes,Top
from APP.models import Message_provenant_de_la_page_de_contact,Top_1,Top_2,Top_3,ContactDressShop,AproposDeNous,Top10
# Register your models here.
#class Disposition(admin.ModelAdmin):
#    list_display('nom',)


admin.site.register(Top10)
admin.site.register(AproposDeNous)
admin.site.register(ContactDressShop)
admin.site.register(Partenaire)
admin.site.register(Evenement)
admin.site.register(Top)
admin.site.register(Top_1)
admin.site.register(Top_2)
admin.site.register(Top_3)
admin.site.register(Message_provenant_de_la_page_de_contact)

admin.site.register(Habits)
admin.site.register(Commande)
admin.site.register(Robesoirees)
admin.site.register(Robebohemes)
admin.site.register(Robesimples)
admin.site.register(Robelongues)
admin.site.register(Robecourtes)
admin.site.register(Accessoiredemeubles)
admin.site.register(Accesoiredemodes)
admin.site.register(Leshautshommes)
admin.site.register(Leshautsfemmes)
admin.site.register(Jupelongues)
admin.site.register(Jupecourtes)
admin.site.register(Basketes)
admin.site.register(Basketsfemmes)
admin.site.register(Basketshommes)
admin.site.register(Bijouxs)
admin.site.register(Bijouxhommes)
admin.site.register(Bijouxfemmes)
admin.site.register(Periquenaturels)
admin.site.register(Periquesinthetiques)
admin.site.register(Periqueperruviennes)
admin.site.register(Periquebresiliennes)
admin.site.register(Periquehumainhairs)
admin.site.register(Machineelectroniques)
admin.site.register(Sandal)
admin.site.register(Sandalshommes)
admin.site.register(Sandalsfemmes)
admin.site.register(Tshirts)
admin.site.register(Tshirthommes)
admin.site.register(Tshirtfemmes)



