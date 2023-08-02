from django.db import models

# Create your models here.



class Robebohemes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',blank=False)
    description = models.TextField(default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Robeboheme'
        verbose_name_plural = 'Robeboheme'

    def __str__(self):
        return self.nom

class Top10(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    nom_du_partenaire = models.CharField(max_length=150)
    imageDuProduit = models.ImageField(upload_to='images')
    imageDuPartenaire = models.ImageField(upload_to='images')
    description = models.TextField(default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Top10'
        verbose_name_plural = 'Top10'

    def __str__(self):
        return self.nom



























class Evenement(models.Model):
    titre = models.CharField(max_length=150)
    Date=models.CharField(max_length=150)
    image=models.ImageField(upload_to='images')
    heure=models.CharField(max_length=150)
    description=models.TextField()

    class Meta:
        verbose_name='Evenement'
        verbose_name_plural='Evenement'
        ordering=['-Date']
    def __str__(self):
        return self.titre


class Partenaire(models.Model):
    name = models.CharField(max_length=150)
    proffesion=models.CharField(max_length=150)
    image=models.ImageField(upload_to='images')
    description=models.TextField()
    Date=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Partenaire'
        verbose_name_plural='Partenaires'
        ordering=['-Date']
    def __str__(self):
        return self.name


class AproposDeNous(models.Model):
    tonImage=models.ImageField(upload_to='images')
    introduction=models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    developpement = models.TextField()
    developpement1 = models.TextField()
    Date=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-Date']

    def __str__(self):
        return self.introduction











class Message_provenant_de_la_page_de_contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    subject=models.CharField(max_length=150)
    message=models.TextField()
    Date=models.DateField(auto_now=True)

    class Meta:
        verbose_name='Message_provenant_de_la_page_de_contact'
        verbose_name_plural='Message_provenant_de_la_page_de_contacts'
        ordering=['-Date']

    def __str__(self):
        return self.name






class Top(models.Model):
    titre = models.CharField(max_length=150)
    sous_titre = models.CharField(max_length=150)
    Date = models.DateTimeField(auto_now=True)
    titre_du_top_de_top = models.CharField(max_length=150)

    class Meta:
        verbose_name='Top'
        verbose_name_plural='Top'
        ordering=['-Date']
    def __str__(self):
        return self.titre






class Top_1(models.Model):
    name= models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Top_1'
        verbose_name_plural = 'Top_1'

    def __str__(self):
        return self.name



class Top_3(models.Model):
    name = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Top_3'
        verbose_name_plural = 'Top_3'

    def __str__(self):
        return self.name


class Top_2(models.Model):
    name = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Top_2'
        verbose_name_plural = 'Top_2'

    def __str__(self):
        return self.name






#class Dress_shop_contacts(models.Model):
#    email=models.CharField(max_length=150)
#    telephone=models.CharField(max_length=150)
#    adresse=models.CharField(max_length=150)
#    dress_shop_information=models.TextField()
 #   Date=models.DateTimeField(auto_now=True)


  #  class Meta:
  #      verbose_name='Dress_shop_contact'
  #      verbose_name_plural='Dress_shop_contacts'
   #     ordering=['-Date']


    #def __str__(self):
    #    return self.adresse







class ContactDressShop(models.Model):
    email=models.CharField(max_length=150)
    telephone=models.CharField(max_length=150)
    adresse=models.CharField(max_length=150)
    dress_shop_information=models.TextField()
    Date=models.DateTimeField(auto_now=True)



















class Habits(models.Model):
    nom=models.CharField(max_length=150)
    prix=models.IntegerField(default=0)
    categorie=models.CharField(max_length=150)
    image=models.ImageField(upload_to='images')
    img=models.ImageField(upload_to='images')
    img1 = models.ImageField(upload_to='images')
    affiche=models.TextField(default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil', blank=False)
    description=models.TextField(default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit', blank=False)
    Date=models.DateTimeField(auto_now=True)
    jour=models.DateField(auto_created=True)


    class Meta:
        ordering=['-Date']
        verbose_name='Habit'
        verbose_name_plural='Habits'

    def __str__(self):
        return self.nom
    




class Commande(models.Model):
    nom=models.CharField(max_length=150)
    prenom=models.CharField(max_length=150)
    telephone=models.CharField(max_length=150)
    Adresse=models.CharField(max_length=150)
    Pays=models.CharField(max_length=150)
    Ville=models.CharField(max_length=150)
    Email=models.EmailField()
    Produit=models.CharField(max_length=150)
    quantite=models.IntegerField(default=0)
    message=models.TextField()
    Date=models.DateField(auto_now=True)
    
    
    class Meta:
        verbose_name='Commande'
        verbose_name_plural='Commandes'
        ordering=['-Date']
        
    def __str__(self):
        return self.nom



class Robesoirees(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Robe_soiree'
        verbose_name_plural = 'Robe_soiree'

    def __str__(self):
        return self.nom


class Robesimples(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Robe_simple'
        verbose_name_plural = 'Robe_simple'

    def __str__(self):
        return self.nom


class Robecourtes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Robecourte'
        verbose_name_plural = 'Robecourtes'

    def __str__(self):
        return self.nom


class Robelongues(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Robelongue'
        verbose_name_plural = 'Robelongues'

    def __str__(self):
        return self.nom


class Jupecourtes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil', blank=False)
    description = models.TextField(default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit', blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Jupecourte'
        verbose_name_plural = 'Jupecourtes'

    def __str__(self):
        return self.nom


class Jupelongues(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Jupelongue'
        verbose_name_plural = 'Jupelongues'

    def __str__(self):
        return self.nom


class Tshirts(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'T-shirt'
        verbose_name_plural = 'T-shirts'

    def __str__(self):
        return self.nom


class Tshirthommes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'T-shirt-homme'
        verbose_name_plural = 'T-shirthommes'

    def __str__(self):
        return self.nom


class Tshirtfemmes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'T-shirtfemme'
        verbose_name_plural = 'T-shirtfemmes'

    def __str__(self):
        return self.nom


class Leshautsfemmes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Les-hautsfemme'
        verbose_name_plural = 'Les-hautsfemmes'

    def __str__(self):
        return self.nom


class Leshautshommes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Les_hautshomme'
        verbose_name_plural = 'Les_hautshommes'

    def __str__(self):
        return self.nom


class Sandal(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Sandal'
        verbose_name_plural = 'Sandals'

    def __str__(self):
        return self.nom


class Sandalshommes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Sandalshomme'
        verbose_name_plural = 'Sandalshommes'

    def __str__(self):
        return self.nom


class Sandalsfemmes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Sandalsfemme'
        verbose_name_plural = 'Sandalsfemmes'

    def __str__(self):
        return self.nom


class Basketes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Baskete'
        verbose_name_plural = 'Basketes'

    def __str__(self):
        return self.nom


class Basketsfemmes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Basketsfemme'
        verbose_name_plural = 'Basketsfemmes'

    def __str__(self):
        return self.nom


class Basketshommes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Basketshomme'
        verbose_name_plural = 'Basketshommes'

    def __str__(self):
        return self.nom


class Bijouxs(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Bijoux'
        verbose_name_plural = 'Bijoux'

    def __str__(self):
        return self.nom


class Bijouxfemmes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Bijouxfemme'
        verbose_name_plural = 'Bijouxfemmes'

    def __str__(self):
        return self.nom


class Bijouxhommes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Bijouxhomme'
        verbose_name_plural = 'Bijouxhommes'

    def __str__(self):
        return self.nom


class Accesoiredemodes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Accesoiredemode'
        verbose_name_plural = 'Accesoiresdemode'

    def __str__(self):
        return self.nom


class Accessoiredemeubles(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Accessoire_de_meuble'
        verbose_name_plural = 'Accessoires_de_meuble'

    def __str__(self):
        return self.nom


class Machineelectroniques(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Machine_electronique'
        verbose_name_plural = 'Machines_electronique'

    def __str__(self):
        return self.nom


class Periquenaturels(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Perique_naturel'
        verbose_name_plural = 'Perique_naturel'

    def __str__(self):
        return self.nom


class Periquehumainhairs(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Perique_humain_hair'
        verbose_name_plural = 'Perique_humain_hair'

    def __str__(self):
        return self.nom


class Periquebresiliennes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Perique_brezilienne'
        verbose_name_plural = 'Periques_brezilienne'

    def __str__(self):
        return self.nom


class Periquesinthetiques(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Perique_sinthetique'
        verbose_name_plural = 'Periques_sinthetique'

    def __str__(self):
        return self.nom


class Periqueperruviennes(models.Model):
    nom = models.CharField(max_length=150)
    prix = models.IntegerField(default=0)
    categorie = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    affiche = models.TextField(
        default='tu dois ecrire ce qui va etre afficher comme descrition premier du produit sur la page d\' d\'accueil',
        blank=False)
    description = models.TextField(
        default='je suis Agerish Programmeur , j\'aimerais que tu puisse remplir ce champs avec la description du produit',
        blank=False)
    Date = models.DateTimeField(auto_now=True)
    jour = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-Date']
        verbose_name = 'Perique_perruvienne'
        verbose_name_plural = 'Periques_perruvienne'

    def __str__(self):
        return self.nom

