from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime, date
from blog.models import Document, DocumentForm, Article, Login
from django.db.models import Q
from django.core.exceptions import PermissionDenied
import smtplib
import email.utils
from email.mime.text import MIMEText
import random


def base(request):
    return render(request, 'blog/base.html')

def acc(request, pseudo):
    #récupère tous les articles déjà en ligne
    articles = Article.objects.all()
    #si clic depuis le lien acheter, affiche tous les articles
    if pseudo.find("-accueil")!=-1: 
        try:
            del request.session['filtre']
        except KeyError:
            pass  
        return HttpResponseRedirect('/blog/accueil/'+request.session['member_name'])     
    #après visite de la page détail, ce code permet de revenir à la page précédente dans le cas où une recherche par mot clé a été faite juste avant
    pseudo = ""
    try:        
        try:
            recherche1 = request.session['filtre']
            articles = Article.objects.filter(Q(libelle__icontains=recherche1)|Q(marque__icontains=recherche1)|Q(description__icontains=recherche1))                                
        except Article.DoesNotExist:
            raise Http404            
    except KeyError:
        pass
    #récupère les informations de l'utilisateur connecté, revient à la page login si personne 'est connecté'
    try:        
        if not request.session['member_id']:
            raise PermissionDenied
        else:
            try:
                logd = Login.objects.filter(id=request.session['member_id'])
                for user in logd:
                    pseudo = user.pseudo                
            except Login.DoesNotExist:
                raise Http404            
    except KeyError:
        return HttpResponseRedirect('/blog/login')
    #traitement d'une recherche par mot clé
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        recherche = request.POST['recherche']
        request.session['filtre'] = recherche
        try:
            #filtre la base selon le mot clé contenu dans recherche (récupéré depus le formulaire)
            articles = Article.objects.filter(Q(libelle__icontains=recherche)|Q(marque__icontains=recherche)|Q(description__icontains=recherche))
            return render(request, 'blog/accueil.html', {'articles':articles,'pseudo1': pseudo,'ido':request.session['member_id']})
        except Article.DoesNotExist:
            raise Http404
    #si pas de redirection jusqu'ici, ouvre la page d'accueil pour afficher l'intégralité des articles déjà en ligne
    return render(request, 'blog/accueil.html', {'articles':articles,'pseudo1': pseudo,'ido':request.session['member_id']})

def vente(request):
    pseudo = """"""
    #instancier l'objet logd 
    logd = Login.objects.filter(id=1)
    #revenir à la page login si non connecté, sinon résupérer les informations de l'utilisateur connecté
    try:        
        if not request.session['member_id']:
            raise PermissionDenied
        else:
            try:
                #recuperer les informations de l'utilisateur connecté
                logd = Login.objects.filter(id=request.session['member_id'])
                for user in logd:
                    pseudo = user.pseudo                
            except Login.DoesNotExist:
                raise Http404  
    except KeyError:
        return HttpResponseRedirect('/blog/login')
    #traitement des données envoyées par l'utilisateur, liées à l'insertion d'un article qu'il veut vendre
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #récupère les données du formulaire et enregistre l'article dans la base
            prix = request.POST['prix']
            couleur = request.POST['couleur']
            etat = request.POST['etat']
            marque = request.POST['marque']
            categorie = request.POST['categorie']
            libelle = request.POST['libelle']
            description = request.POST['description']
            today=date.today()
            artcl = Article (docfile=request.FILES['docfile'],prix=prix,couleur=couleur,etat=etat,marque=marque,categorie=categorie,libelle=libelle,description=description,user_id=request.session['member_id'],date=today)
            artcl.save()
            id_article = 43        
            return HttpResponseRedirect('accueil/'+pseudo)
    else:
        form = DocumentForm()
    #documents contient les balises pour l'uplod de l'image
    documents = Document.objects.all()

    return render(request, 'blog/vente.html', {'documents': documents,'form': form,'logd':logd})

def inscr(request):
    #revient à la page accueil si déjà connecté, sinon retourne à la page d'accueil
    try:
        if request.session['member_id']:
            try:
                logd = Login.objects.filter(id=request.session['member_id'])
                for user in logd:
                    pseudo = user.pseudo                
                return HttpResponseRedirect('accueil/' + pseudo)
            except Login.DoesNotExist:
                raise Http404
    except KeyError:
        pass
    nom1 = """"""
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        #mdp = request.POST['mdp']
        #crée un mot de passe
        element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!"
        mdp = ""         
        for i in range(20): mdp = mdp + element[random.randint(0, len(element) - 1)]
        #récupère les informations         
        pseudo1 = request.POST['pseudo']
        nom1 = request.POST['nom']
        tel1 = request.POST['tel']
        mail1 = request.POST['mail']
        adresse1 = request.POST['adresse']
        lg = Login(pseudo=pseudo1,motdpass=mdp,adresse=adresse1,tel=tel1,mail=mail1,nom=nom1)
        lg.save()
        request.session['nom1'] = pseudo1            
        #construire le message
        msg = MIMEText('Voici votre mot de passe pour VEL '+pseudo1+': '+mdp+' (Ne répondez pas à ce mail automatique)')
        msg['From'] = 'webmaster@vel.com'
        msg['To'] = mail1
        msg['Subject'] = 'VEL : Mot de passe'
        #configuration du serveur mail
        mailserver = smtplib.SMTP('smtp.gmail.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('tanguystevenbi@gmail.com', 'tanguystevenbi2')
        #envoi le mot de pass par mail
        mailserver.sendmail('tanguystevenbi@gmail.com',mail1,msg.as_string())
        mailserver.quit()
            
        return HttpResponseRedirect('login')
    else:
        form = DocumentForm()
    return render(request, 'blog/inscription.html')

def view_article(request, id_article, id_user):
    #revient à la page login si non connecté
    try:        
        if not request.session['member_id']:
            raise PermissionDenied           
    except KeyError:
        return HttpResponseRedirect('/blog/login')
    #Récupère les informations sur l'articles sélectionné depuis la page d'accueil
    try:
        articles = Article.objects.filter(id=id_article)
        iduser = 0
        for art in articles:
            iduser = art.user_id
        try:
            #récupère les données de l'utilisateur qui a mis l'article en ligne
            logd = Login.objects.filter(id=iduser) 
            for user in logd:
                pseudo = user.pseudo
            return render(request, 'blog/article.html', {'articles':articles,'logd':logd,'pseudo':pseudo})
        except Login.DoesNotExist:
            raise Http404
    except Article.DoesNotExist:
        raise Http404

def login(request):
    #revient à la page accueil si déjà connecté
    try:
        if request.session['member_id']:
            try:
                logd = Login.objects.filter(id=request.session['member_id'])
                for user in logd:
                    pseudo = user.pseudo                
                return HttpResponseRedirect('accueil/' + pseudo)
            except Login.DoesNotExist:
                raise Http404
    except KeyError:
        pass
    login_errone = ""
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        #récupère et vérifie le pseudo et mot de passe
        pseudo = request.POST['pseudo']
        mdp = request.POST['mdp']
        try:
            utilisateur = Login.objects.filter(pseudo=pseudo,motdpass=mdp)
            if utilisateur:
                pseudo = ""
                for user in utilisateur:
                    pseudo = user.pseudo
                    request.session['member_id'] = user.id
                    request.session['member_name'] = user.nom
                #va à la page d'accueil après authentification
                return HttpResponseRedirect('accueil/' + pseudo)
            else:
                login_errone = """ Login erroné, recommencez!"""
                return render(request, 'blog/login.html', {'login_errone': login_errone})
        except Login.DoesNotExist:
            raise Http404
    #revient à la page de connexion si echec 
    return render(request, 'blog/login.html', {'login_errone': login_errone})

def logot(request):
    #détruit les variables de session (déconnecte)
    try:
        del request.session['member_id']
        del request.session['member_name']
    except KeyError:
        pass
    return HttpResponseRedirect('login')







