from django import forms
from accueil.models import *

class FourniseurForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(FourniseurForm, self).__init__(*args,**kwargs)
        for name in self.fields.keys():
                self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['nom'].label = "Raison Social"
        self.fields['nif'].label = "Numéro d'indentification fiscal"
        self.fields['adresse'].label = "Adresse"
        self.fields['mrc'].label = "Mode de reception commande"
        self.fields['mail'].label = "E-mail"
        self.fields['logo'].label = "Logo"
        self.fields['passe'].label = "Mot de passe"
        self.fields['login'].label = "Login"
        self.fields['numero_tel'].label = "N° de téléphone"
    class Meta:
        model = Fournisseur
        fields = (
            'nom',
            'nif',
            'adresse',
            'mrc',
            'mail',
            'logo',
            'passe',
            'login',
            'numero_tel',
            )
        
class ProduitForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProduitForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['intitule'].label = "Intitulé"
        self.fields['prix'].label = "Prix"
        self.fields['image'].label = "Image"
        self.fields['description'].label = "Description"
        self.fields['mu'].label = "Mode d'usage"
        self.fields['dp'].label = "Date de péremption"
        self.fields['marque'].label = "De marque"
        self.fields['fabriquant'].label = "Fabriquant"
        self.fields['made_in'].label = "Made in"
        self.fields['pp'].label = "Priorité de publicité"
        self.fields['vue'].label = "Nombre de vue"
        self.fields['fournisseur'].label = "Fournisseur"
        class Meta:
            model = Produit
            fields = (
                'intitule',
                'prix',
                'image'
                'description',
                'mu',
                'dp',
                'marque',
                'fabriquant',
                'made_in',
                'pp',
                'fournisseur',
            )
            
class ConsomateurForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(ConsomateurForm, self).__init__(*args, **kwargs)
        
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
                'id':name,
            })
        self.fields['nom'].label = "Nom"
        self.fields['prenom'].label = "Prénom"
        self.fields['numero_tel'].label = "N° téléphone"
        self.fields['adresse'].label = "Adresse"
        self.fields['login'].label = "Login"
        self.fields['password'].label = "Mot de passe"
        self.fields['email'].label = "E-email"
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs.update({
                'class':'form-control',
                'id':'password',
            })
    class Meta:
            
        model = Consommateur
        fields = (
                'nom', 
                'prenom',
                'numero_tel',
                'adresse',
                'login',
                'email',
                'password',
            )
            
class CommentaireForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(CommentaireForm, self).__init__(*args, **kwargs)
        
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['consommateur'].label = "Client"
        self.fields['produit'].label = "Article"
        self.fields['commentaire'].label = "Avis"
        class Meta:
            model = Commentaire
            fields = (
                'consommateur',
                'produit',
                'commentaire',
                )
class LivreurForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(LivreurForm, self).__init__(*args, **kwargs)
        
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })
        self.fields['nom'].label = "Nom"
        self.fields['prenom'].label = "Prénom"
        self.fields['contact'].label = "Contact"
        self.fields['mail'].label = "E-mail"
        self.fields['adresse'].label = "Adresse"
        
        class Meta:
            model = Livreur
            
            fields = (
                'nom',
                'prenom',
                'contact',
                'mail',
                'adresse',
            )
class PubliciteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PubliciteForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })
            
        self.fields['nom_entreprise'].label = "Entreprise"
        self.fields['duree'].label = "Durée"
        self.fields['tarif'].label = "Tarif en F CFA"
        self.fields['contact'].label = "Contact"
        self.fields['date_debut'].label = "Date de debut"
        self.fields['date_fin'].label = "Date de fin"
    class Meta:
        model = Publicite
        fields = (
            'nom_entreprise',
            'duree',
            'tarif',
            'contact',
            'date_debut',
            'date_fin',
            )
class ClientLoginForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ClientLoginForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs.update({
                'class':'form-control',
            })
        self.fields['password'].label = "Mot de passe"
    class Meta:
        model = Consommateur
        
        fields = ('login','password')
        