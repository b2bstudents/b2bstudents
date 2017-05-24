from django.db import models
from django import forms

class Article(models.Model):
    id = models.IntegerField(null=False,primary_key=True)
    libelle = models.CharField(max_length=100)
    categorie = models.CharField(max_length=42)
    user_id = models.IntegerField(null=False)
    marque = models.CharField(max_length=42)
    couleur = models.CharField(max_length=42)
    etat = models.CharField(max_length=42)
    prix = models.IntegerField(null=False)
    description = models.TextField(null=True)
    #chemin_image = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de publication")
    docfile = models.FileField(upload_to='Images')
    
    def __str__(self):
        return """ """ + str(self.id) + """ """ + str(self.user_id) + """ """ + self.libelle + """ """ + self.categorie + """ """ + self.marque + """ """ + self.couleur + """ """ + self.etat + """ """ + str(self.prix)

class Login(models.Model):    
    id = models.IntegerField(null=False,primary_key=True)
    pseudo = models.CharField(max_length=42)
    nom = models.CharField(max_length=42)
    adresse = models.CharField(max_length=42)
    mail = models.CharField(max_length=42)
    tel = models.IntegerField(null=False)
    motdpass = models.CharField(max_length=42,null=False)
    def __str__(self):
        return """ """ + str(self.id) + """ """ + self.pseudo + """ """ + self.nom + """ """ + self.adresse + """ """ + self.mail + """ """ + str(self.tel) + """ """ + self.motdpass + """ """
    
class Document(models.Model):
    docfile = models.FileField(upload_to='MaBiblio')

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Selectionner un fichier',
                          help_text='Taille max.: 42 megabytes')
# Create your models here.
