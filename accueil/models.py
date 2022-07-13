from django.db import models
import os

def renommage(instance, nom):
    nom_fichier = os.path.splitext(nom)[0] # on retire l'extension 
    return "{}-{}".format(instance.id, nom_fichier)

class Ville(models.Model):
    ville = models.CharField(max_length=100)
    def __str__(self):
        return self.ville

class Quartier(models.Model):
    quartier = models.CharField(max_length=100)
    ville    = models.ForeignKey(Ville,on_delete=models.CASCADE)
    def __str__(self):
        return self.quartier
        
class Administrateur(models.Model):
    login  = models.CharField(max_length=100)
    passe  = models.CharField(max_length=30)
    mail   = models.CharField(max_length=100)
    photo  = models.ImageField(upload_to='mk_administrateur/')
    insert = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    update = models.BooleanField(default=False)
    read   = models.BooleanField(default=False)
    def __str__(self):
        return self.login
    
class Categorie(models.Model):
    type_c = models.CharField(max_length=100)
    def __str__(self) :
        return self.type_c

class CategorieProduit(models.Model):
    categorie = models.CharField(max_length=100)
    icon      = models.ImageField(upload_to='mk_icon_categorie/')
    def __str__(self):
        return self.categorie

class Payement(models.Model):
    type_p = models.CharField(max_length=100)
    def __str__(self):
        return self.type_p
class Fournisseur(models.Model):
    MRC_CHOICE = (
        ('SMS', 'Message'),
        ('CALL', 'Appel'),
        ('MAIL', 'E-Mail')
    )
    nom = models.CharField(max_length=100)
    nif = models.IntegerField(verbose_name="Numero d'Identification Fiscal")
    adresse = models.CharField(max_length=150)
    mrc = models.CharField(max_length=30, verbose_name="Mode de reception commande", choices=MRC_CHOICE)
    mail = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='mk_fournisseur/')
    passe = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    numero_tel = models.CharField(max_length=100)
    def __str__(self):
        return self.nom
class Produit(models.Model):
    intitule    = models.CharField(max_length=100)
    prix        = models.FloatField(max_length=11)
    image       = models.ImageField(upload_to='mk_produits/')
    description = models.CharField(max_length=255)
    mu          = models.CharField(max_length=100, verbose_name="Mode d'Utilisation")
    dp          = models.DateTimeField(auto_now_add=False, verbose_name="Date d'expiration") 
    marque      = models.CharField(max_length=50)
    fabriquant  = models.CharField(max_length=100)
    made_in     = models.CharField(max_length=50)
    pp          = models.CharField(max_length=2, verbose_name="Priorité de présentation")
    vue         = models.IntegerField()
    fournisseur = models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    categorie_produit = models.ForeignKey(CategorieProduit,on_delete=models.CASCADE)
    def __str__(self):
        return self.intitule

class Consommateur(models.Model):
    nom        = models.CharField(max_length=100)
    prenom     = models.CharField(max_length=100)
    numero_tel = models.CharField(max_length=50)
    adresse    = models.CharField(max_length=200)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.nom
class TypeService(models.Model):
    service    = models.CharField(max_length=100)
    def __str__(self):
        return self.service
class Solliciter(models.Model):
    type_service = models.ForeignKey(TypeService,on_delete=models.CASCADE)
    consommateur = models.ForeignKey(Consommateur, on_delete=models.CASCADE)
    def __str__(self):
        return self.consommateur+":"+self.type_service
class Livreur(models.Model):
    nom     = models.CharField(max_length=100)
    prenom  = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    mail    = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom+" "+self.prenom

class Commentaire(models.Model) :
    consommateur = models.ForeignKey(Consommateur,on_delete=models.CASCADE)
    produit      = models.ForeignKey(Produit,on_delete=models.CASCADE)
    commentaire  = models.TextField(max_length=2048)
    date         = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date de Publication')
    
    def __str__(self): 
        return self.consommateur+":"+self.commentaire
    
class Resrevation(models.Model):
    client   = models.ForeignKey(Consommateur,on_delete=models.CASCADE)
    payement = models.ForeignKey(Payement,on_delete=models.CASCADE)
    livreur  = models.ForeignKey(Livreur,on_delete=models.CASCADE)
    produit  = models.ForeignKey(Produit,on_delete=models.CASCADE)
    date     = models.DateTimeField(auto_now_add=True,auto_now=False)
    quantite = models.IntegerField(default=0)
    def __str__(self):
        return self.client+":"+self.produit+":"+self.livreur
    
class Publicite(models.Model):
    nom_entreprise = models.CharField(max_length=100, verbose_name="nom")
    duree          = models.IntegerField(default=30)
    tarif          = models.FloatField(max_length=21,default=0.0)
    contact        = models.CharField(max_length=100)
    photo          = models.ImageField(upload_to='mk_pubs/')
    date_debut     = models.DateField(auto_now_add=False, auto_now=False)
    date_fin       = models.DateField(auto_now_add=False, auto_now=False)
    def __str__(self):
        return self.nom_entreprise
    
class Administrer(models.Model):
    publicite      = models.ForeignKey(Publicite,on_delete=models.CASCADE)
    administrateur = models.ForeignKey(Administrateur,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.publicite+":"+self.administrateur
    
class ModeDePayementFournisseur(models.Model):

    fournisseur   = models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    mode_payement = models.ForeignKey(Payement,on_delete=models.CASCADE)

    def __str__(self):
        return self.fournisseur+":"+self.mode_payement

class Partenaire (models.Model) : 
    designation = models.TextField(max_length=150)
    logo        = models.ImageField(upload_to='mk_partenaire/')
    contact     = models.TextField(max_length=100)

    def __str__(self):
        return self.designation


class Service (models.Model) : 
    service = models.TextField(max_length=150)

    def __str__(self):
        return self.service
