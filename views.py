from django.http import HttpResponse
from django.shortcuts import render


from APP.models import Habits, Commande, Robebohemes, Tshirts, Tshirtfemmes, Tshirthommes, Sandal, Sandalsfemmes, \
    Sandalshommes, Message_provenant_de_la_page_de_contact, Top, Evenement, ContactDressShop, AproposDeNous, Partenaire
from APP.models import Robecourtes,Robelongues,Robesimples,Robesoirees
from APP.models import Periquenaturels,Periquebresiliennes,Periquehumainhairs,Periqueperruviennes,Periquesinthetiques,Leshautsfemmes,Leshautshommes,Jupecourtes,Jupelongues
from APP.models import Bijouxs,Bijouxfemmes,Bijouxhommes,Top_3,Top_1,Top_2,Top10
from APP.models import Basketsfemmes,Basketes,Basketshommes,Accesoiredemodes,Accessoiredemeubles,Machineelectroniques
from django.shortcuts import render, get_object_or_404,redirect


# Create your views here.


def product(request):
    return render(request,'product/produit.html')




def index(request):
    contact=ContactDressShop.objects.get()
    habits=Habits.objects.all()
    search=request.GET.get('search')
    if search !=''and search is not None:
        habits=Habits.objects.filter(nom__icontains=search)
    return render(request,'detail/index.html',{'habits':habits,'contact':contact})


def footere(request):
    contact=ContactDressShop.objects.get()
    return render(request,'bas.html',{'contact':contact})






def merci(request):
    return render(request,'detail/merci.html')








def detail(request,id):
    habits=get_object_or_404(Habits,id=id)
    if request.method=='POST':
        nom=request.POST["nom"]
        prenom=request.POST["Prenom"]
        telephone=request.POST["Tel"]
        Adresse=request.POST["Adresse"]
        Pays=request.POST["pays"]
        Ville=request.POST["ville"]
        Email=request.POST["email"]
        Produit=request.POST["produit"]
        quantite=request.POST["quantite"]
        message=request.POST["message"]
        user=Commande.objects.create(nom=nom,prenom=prenom,telephone=telephone,Adresse=Adresse,Pays=Pays,Ville=Ville,Email=Email,Produit=Produit,quantite=quantite,message=message)
        user.save()
        return redirect('merci')
       
    
    
    return render(request,'detail/page1.html',{'habits':habits})
























def Robe(request):
    search = request.GET.get('search')
    robebohemes=Robebohemes.objects.all()
    if search != '' and search is not None:
        robebohemes = Robebohemes.objects.filter(nom__icontains=search)

    robesimple=Robesimples.objects.all()
    if search != '' and search is not None:
        robesimple = Robesimples.objects.filter(nom__icontains=search)

    robesoiree=Robesoirees.objects.all()
    if search != '' and search is not None:
        robesoiree = Robesoirees.objects.filter(nom__icontains=search)

    robecourte=Robecourtes.objects.all()
    if search != '' and search is not None:
        robecourte = Robecourtes.objects.filter(nom__icontains=search)

    robelongue=Robelongues.objects.all()
    if search != '' and search is not None:
        robelongue = Robelongues.objects.filter(nom__icontains=search)

    return render(request,'product/Robe.html',{'robebohemes':robebohemes,'robesimples':robesimple,'robesoirees':robesoiree,'robelongues':robelongue,'robecourtes':robecourte})

def T_shirts(request):
    search = request.GET.get('search')
    t_shirt = Tshirts.objects.all()
    if search != '' and search is not None:
        t_shirt = Tshirts.objects.filter(nom__icontains=search)

    t_shirt_femme=Tshirtfemmes.objects.all()
    if search != '' and search is not None:
        t_shirt_femme= Tshirtfemmes.objects.filter(nom__icontains=search)

    t_shirt_homme = Tshirthommes.objects.all()
    if search != '' and search is not None:
        t_shirt_homme = Tshirthommes.objects.filter(nom__icontains=search)

    return render(request,'product/t-shirt.html',{'t_shirts':t_shirt,'t_shirts_femme':t_shirt_femme,'t_shirts_homme':t_shirt_homme})

def Sandals(request):
    search = request.GET.get('search')
    sandal = Sandal.objects.all()
    if search != '' and search is not None:
        sandal =Sandal.objects.filter(nom__icontains=search)

    sandal_femme = Sandalsfemmes.objects.all()
    if search != '' and search is not None:
        sandal_femme = Sandalsfemmes.objects.filter(nom__icontains=search)

    sandal_homme = Sandalshommes.objects.all()
    if search != '' and search is not None:
        sandal_homme = Sandalshommes.objects.filter(nom__icontains=search)

    return render(request, 'product/sandal.html',
                  {'sandals': sandal, 'sandals_femme': sandal_femme, 'sandals_homme': sandal_homme})


def sandaldetail(request,id):
    sandal =get_object_or_404(Sandal,id=id)
    if request.method=='POST':
        nom=request.POST["nom"]
        prenom=request.POST["Prenom"]
        telephone=request.POST["Tel"]
        Adresse=request.POST["Adresse"]
        Pays=request.POST["pays"]
        Ville=request.POST["ville"]
        Email=request.POST["email"]
        Produit=request.POST["produit"]
        quantite=request.POST["quantite"]
        message=request.POST["message"]
        user=Commande.objects.create(nom=nom,prenom=prenom,telephone=telephone,Adresse=Adresse,Pays=Pays,Ville=Ville,Email=Email,Produit=Produit,quantite=quantite,message=message)
        user.save()
        return redirect('merci')
    return render(request,'detail/sandaldetail.html',{'sandal': sandal})


def sandaldetailfemme(request, id):
    sandalfemme = get_object_or_404(Sandalsfemmes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/sandaldetailfemme.html', {'sandaldetailfemme': sandalfemme})


def sandaldetailhomme(request, id):
    sandalhomme = get_object_or_404(Sandalshommes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/sandaldetailhomme.html', {'sandaldetailhomme': sandalhomme})
def tshirt(request, id):
    sandalhomme = get_object_or_404(Tshirts, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/t-shirt.html', {'sandaldetailhomme': sandalhomme})

def tshirthomme(request, id):
    sandalhomme = get_object_or_404(Tshirthommes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/t-shirt-homme.html', {'sandaldetailhomme': sandalhomme})

def tshirtfemme(request, id):
    sandalhomme = get_object_or_404(Tshirtfemmes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/t-shirt-femme.html', {'sandaldetailhomme': sandalhomme})



def robeboheme(request, id):
    sandalhomme = get_object_or_404(Robebohemes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/robeboheme.html', {'sandaldetailhomme': sandalhomme})

def robecourte(request, id):
    sandalhomme = get_object_or_404(Robecourtes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/robecourte.html', {'sandaldetailhomme': sandalhomme})


def robesimple(request, id):
    sandalhomme = get_object_or_404(Robesimples, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/robesimple.html', {'sandaldetailhomme': sandalhomme})

def robelongue(request, id):
    sandalhomme = get_object_or_404(Robelongues, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/robelongue.html', {'sandaldetailhomme': sandalhomme})


def periquenaturel(request, id):
    sandalhomme = get_object_or_404(Periquenaturels, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/periquenaturel.html', {'sandaldetailhomme': sandalhomme})

def periquehumainhair(request, id):
    sandalhomme = get_object_or_404(Periquehumainhairs, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/periquehumainhair.html', {'sandaldetailhomme': sandalhomme})


def periquesinthetique(request, id):
    sandalhomme = get_object_or_404(Periquesinthetiques, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/jupelongue.html', {'sandaldetailhomme': sandalhomme})

def jupecourte(request, id):
    sandalhomme = get_object_or_404(Jupecourtes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/jupecourte.html', {'sandaldetailhomme': sandalhomme})



def jupelongue(request, id):
    sandalhomme = get_object_or_404(Jupelongues, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/periqueperuvienne.html', {'sandaldetailhomme': sandalhomme})



def periqueperuvienne(request, id):
    sandalhomme = get_object_or_404(Periqueperruviennes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/periqueperuvienne.html', {'sandaldetailhomme': sandalhomme})


def hauthomme(request, id):
    sandalhomme = get_object_or_404(Leshautshommes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/hauthomme.html', {'sandaldetailhomme': sandalhomme})


def hautfemme(request, id):
    sandalhomme = get_object_or_404(Leshautsfemmes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/hautfemme.html', {'sandaldetailhomme': sandalhomme})





def basket(request, id):
    sandalhomme = get_object_or_404(Basketes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/basket.html', {'sandaldetailhomme': sandalhomme})


def basket_femme(request, id):
    sandalhomme = get_object_or_404(Basketsfemmes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/basketfemme.html', {'sandaldetailhomme': sandalhomme})


def basket_homme(request, id):
    sandalhomme = get_object_or_404(Bijouxhommes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/baskethomme.html', {'sandaldetailhomme': sandalhomme})


def bijoux(request, id):
    sandalhomme = get_object_or_404(Bijouxs, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/bijoux.html', {'sandaldetailhomme': sandalhomme})

def bijoux_femme(request, id):
    sandalhomme = get_object_or_404(Basketsfemmes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/bijouxfemme.html', {'sandaldetailhomme': sandalhomme})

def bijoux_homme(request, id):
    sandalhomme = get_object_or_404(Bijouxfemmes, id=id)
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["Prenom"]
        telephone = request.POST["Tel"]
        Adresse = request.POST["Adresse"]
        Pays = request.POST["pays"]
        Ville = request.POST["ville"]
        Email = request.POST["email"]
        Produit = request.POST["produit"]
        quantite = request.POST["quantite"]
        message = request.POST["message"]
        user = Commande.objects.create(nom=nom, prenom=prenom, telephone=telephone, Adresse=Adresse, Pays=Pays,
                                       Ville=Ville, Email=Email, Produit=Produit, quantite=quantite, message=message)
        user.save()
        return redirect('merci')

    return render(request, 'detail/bijouxhomme.html', {'sandaldetailhomme': sandalhomme})











def Perique(request):
    search = request.GET.get('search')
    periquenaturel=Periquenaturels.objects.all()
    if search != '' and search is not None:
        periquenaturel = Periquenaturels.objects.filter(nom__icontains=search)

    periqueperruvienne=Periqueperruviennes.objects.all()
    if search != '' and search is not None:
        periqueperruvienne = Periqueperruviennes.objects.filter(nom__icontains=search)

    periquehumainhair=Periquehumainhairs.objects.all()
    if search != '' and search is not None:
        periquehumainhair = Periquehumainhairs.objects.filter(nom__icontains=search)

    periquesinthetique=Periquesinthetiques.objects.all()
    if search != '' and search is not None:
        periquesinthetique = Periquesinthetiques.objects.filter(nom__icontains=search)

    periquebresilienne=Periquebresiliennes.objects.all()
    if search != '' and search is not None:
        periquebresilienne = Periquebresiliennes.objects.filter(nom__icontains=search)
    return render(request,'product/perique.html',{'periquenaturels':periquenaturel,'periquehumainhairs':periquehumainhair,'periquebresiliennes':periquebresilienne,'periquesinthetiques':periquesinthetique,'periqueperruviennes':periqueperruvienne})



def Hauts(request):
    search = request.GET.get('search')
    haut_femme = Leshautsfemmes.objects.all()
    if search != '' and search is not None:
        haut_femme = Leshautsfemmes.objects.filter(nom__icontains=search)

    haut_homme = Leshautshommes.objects.all()
    if search != '' and search is not None:
        haut_homme= Leshautshommes.objects.filter(nom__icontains=search)
    return render(request, 'product/haut.html',
                  {'hautshomme': haut_homme, 'hautsfemme':haut_femme})


def Jupe(request):
    search = request.GET.get('search')
    jupe_longue= Jupelongues.objects.all()
    if search != '' and search is not None:
        jupe_longue = Jupelongues.objects.filter(nom__icontains=search)
    jupe_courte= Jupecourtes.objects.all()
    if search != '' and search is not None:
        jupe_courte = Jupecourtes.objects.filter(nom__icontains=search)
    return render(request, 'product/jupe.html',
                  {'jupelongues':jupe_longue, 'jupecourtes':jupe_courte})




def Bijoux(request):
    search = request.GET.get('search')
    bijoux = Bijouxs.objects.all()
    if search != '' and search is not None:
        bijoux  = Bijouxs.objects.filter(nom__icontains=search)

    bijoux_femme = Bijouxfemmes.objects.all()
    if search != '' and search is not None:
        bijoux_femme = Bijouxfemmes.objects.filter(nom__icontains=search)
    bijoux_homme = Bijouxhommes.objects.all()
    if search != '' and search is not None:
        bijoux_homme  = Bijouxhommes.objects.filter(nom__icontains=search)
    return render(request, 'product/bijoux.html',
                  {'bijouxs':bijoux, 'bijouxs_femme':bijoux_femme, 'bijouxs_homme':bijoux_homme})

def Baskets(request):
    search = request.GET.get('search')
    basket = Basketes.objects.all()
    if search != '' and search is not None:
        basket = Basketes.objects.filter(nom__icontains=search)
    basket_femme = Basketsfemmes.objects.all()
    if search != '' and search is not None:
        basket_femme = Basketsfemmes.objects.filter(nom__icontains=search)
    basket_homme = Basketshommes.objects.all()
    if search != '' and search is not None:
        basket_homme = Basketshommes.objects.filter(nom__icontains=search)
    return render(request, 'product/basket.html',
                  {'baskets':basket, 'baskets_femme':basket_femme, 'baskets_homme':basket_homme})





def Accessoires(request):
    search = request.GET.get('search')
    accessoire_de_meuble=Accessoiredemeubles.objects.all()
    if search != '' and search is not None:
        accessoire_de_meuble = Accessoiredemeubles.objects.filter(nom__icontains=search)


    accesoire_de_mode= Accesoiredemodes.objects.all()
    if search != '' and search is not None:
        accesoire_de_mode = Accesoiredemodes.objects.filter(nom__icontains=search)
    Machines_electronique=Machineelectroniques.objects.all()
    if search != '' and search is not None:
        Machines_electronique = Machineelectroniques.objects.filter(nom__icontains=search)


    return render(request, 'product/accessoire.html',
                  {'accessoire_de_meubles':accessoire_de_meuble, 'accesoire_de_modes':accesoire_de_mode,'Machines_electroniques':Machines_electronique})

























def info(request):
    return render(request,'detail/portaflo.html')

def infodetail(request,id):
    habits=get_object_or_404(Habits,id=id)
    return render(request,'detail/portaflo.html',{'habits':habits})

def infodetailrobe(request,id):
    habits=get_object_or_404(Robelongues,id=id)
    return render(request,'detail/infodetailrobe.html',{'habits':habits})


def infodetaile(request,id):
    habits=get_object_or_404(Machineelectroniques,id=id)
    return render(request,'detail/infodetail1.html',{'habits':habits})



def infodetailes(request,id):
    habits=get_object_or_404(Accessoiredemeubles,id=id)
    return render(request,'detail/infodetail2.html',{'habits':habits})

def infodetailrobe(request,id):
    habits=get_object_or_404(Tshirthommes,id=id)
    return render(request,'detail/infodetailrobe.html',{'habits':habits})

def infodetailee(request,id):
    habits=get_object_or_404(Accesoiredemodes,id=id)
    return render(request,'detail/infodetail3.html',{'habits':habits})

def infodetail4(request,id):
    habits=get_object_or_404(Sandalsfemmes,id=id)
    return render(request,'detail/infodetail4.html',{'habits':habits})

def infodetail5(request,id):
    habits=get_object_or_404(Sandalshommes,id=id)
    return render(request,'detail/infodetail5.html',{'habits':habits})






def infodetail6(request,id):
    habits=get_object_or_404(Robesimples,id=id)
    return render(request,'detail/infodetail6.html',{'habits':habits})

def infodetail7(request,id):
    habits=get_object_or_404(Robecourtes,id=id)
    return render(request,'detail/infodetail7.html',{'habits':habits})

def infodetail8(request,id):
    habits=get_object_or_404(Robesoirees,id=id)
    return render(request,'detail/infodetail8.html',{'habits':habits})












def infodetail9(request,id):
    habits=get_object_or_404(Periquenaturels,id=id)
    return render(request,'detail/infodetail9.html',{'habits':habits})

def infodetail10(request,id):
    habits=get_object_or_404(Periquebresiliennes,id=id)
    return render(request,'detail/infodetail10.html',{'habits':habits})

def infodetail11(request,id):
    habits=get_object_or_404(Periquehumainhairs,id=id)
    return render(request,'detail/infodetail11.html',{'habits':habits})

def infodetail12(request,id):
    habits=get_object_or_404(Periqueperruviennes,id=id)
    return render(request,'detail/infodetail12.html',{'habits':habits})

def infodetail13(request,id):
    habits=get_object_or_404(Leshautsfemmes,id=id)
    return render(request,'detail/infodetail13.html',{'habits':habits})

def infodetail14(request,id):
    habits=get_object_or_404(Periquesinthetiques,id=id)
    return render(request,'detail/infodetail14.html',{'habits':habits})

def infodetail15(request,id):
    habits=get_object_or_404(Leshautshommes,id=id)
    return render(request,'detail/infodetail15.html',{'habits':habits})

def infodetail16(request,id):
    habits=get_object_or_404(Jupecourtes,id=id)
    return render(request,'detail/infodetail16.html',{'habits':habits})

def infodetail17(request,id):
    habits=get_object_or_404(Jupelongues,id=id)
    return render(request,'detail/infodetail17.html',{'habits':habits})









def infodetail18(request,id):
    habits=get_object_or_404(Bijouxs,id=id)
    return render(request,'detail/infodetail18.html',{'habits':habits})

def infodetail19(request,id):
    habits=get_object_or_404(Bijouxfemmes,id=id)
    return render(request,'detail/infodetail19.html',{'habits':habits})

def infodetail20(request,id):
    habits=get_object_or_404(Bijouxhommes,id=id)
    return render(request,'detail/infodetail20.html',{'habits':habits})






def infodetail21(request,id):
    habits=get_object_or_404(Basketsfemmes,id=id)
    return render(request,'detail/infodetail21.html',{'habits':habits})

def infodetail22(request,id):
    habits=get_object_or_404(Basketes,id=id)
    return render(request,'detail/infodetail22.html',{'habits':habits})

def infodetail23(request,id):
    habits=get_object_or_404(Basketshommes,id=id)
    return render(request,'detail/infodetail23.html',{'habits':habits})

def infodetail24(request,id):
    habits=get_object_or_404(Accesoiredemodes,id=id)
    return render(request,'detail/infodetail24.html',{'habits':habits})


def infodetail26(request,id):
    habits=get_object_or_404(Accessoiredemeubles,id=id)
    return render(request,'detail/infodetail26.html',{'habits':habits})

def infodetail25(request,id):
    habits=get_object_or_404(Machineelectroniques,id=id)
    return render(request,'detail/infodetail25.html',{'habits':habits})







def signup(request):
    return HttpResponse('hello')

def about(request):
    contact = ContactDressShop.objects.get()
    paire=AproposDeNous.objects.all()
    toptop = Top10.objects.all()
    return render(request,'about.html',{'contact':contact,'pairedes':paire,'toptops':toptop})




def trainer(request):
    trainer=Partenaire.objects.all()
    contact = ContactDressShop.objects.get()
    return render(request,'trainer.html',{'contact':contact,'trainers':trainer})

def event(request):
    contact = ContactDressShop.objects.get()
    evenement=Evenement.objects.all()
    return render(request,'event.html',{'contact':contact,'evenements': evenement})


def contactus(request):
    contacte=ContactDressShop.objects.get()
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        user=Message_provenant_de_la_page_de_contact.objects.create(name=name,email=email,subject=subject,message=message)
        user.save()

        return redirect('contactus')

    return render(request,'contactus.html',{'contact': contacte})

def top(request):
    contacte = ContactDressShop.objects.get()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        user = Message_provenant_de_la_page_de_contact.objects.create(name=name, email=email, subject=subject,
                                                                      message=message)
        user.save()

        return redirect('top')
    top_1=Top_1.objects.all()
    top_2 = Top_2.objects.all()
    top_3 = Top_3.objects.all()
    top=Top.objects.get()

    return render(request,'top.html',{'contact':contacte,'tops_1':top_1,'tops_2':top_2,'tops_3':top_3,'top':top})

