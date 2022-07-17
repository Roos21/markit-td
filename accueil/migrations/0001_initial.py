# Generated by Django 4.0 on 2022-07-16 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('passe', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='mk_administrateur/')),
                ('insert', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('update', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_c', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CategorieProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='mk_icon_categorie/')),
            ],
        ),
        migrations.CreateModel(
            name='Consommateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('numero_tel', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=200)),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('nif', models.IntegerField(verbose_name="Numero d'Identification Fiscal")),
                ('adresse', models.CharField(max_length=150)),
                ('mrc', models.CharField(choices=[('SMS', 'Message'), ('CALL', 'Appel'), ('MAIL', 'E-Mail')], max_length=30, verbose_name='Mode de reception commande')),
                ('mail', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='mk_fournisseur/')),
                ('passe', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100)),
                ('numero_tel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livreur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('disponilité', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.TextField(max_length=150)),
                ('logo', models.ImageField(upload_to='mk_partenaire/')),
                ('contact', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_p', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('note', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='mk_plat_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0.0, max_length=11)),
                ('quantite', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='mk_produits/')),
                ('description', models.CharField(max_length=255)),
                ('mu', models.CharField(max_length=100, verbose_name="Mode d'Utilisation")),
                ('dp', models.DateTimeField(verbose_name="Date d'expiration")),
                ('marque', models.CharField(max_length=50)),
                ('fabriquant', models.CharField(max_length=100)),
                ('made_in', models.CharField(max_length=50)),
                ('pp', models.CharField(max_length=2, verbose_name='Priorité de présentation')),
                ('vue', models.IntegerField(default=0)),
                ('categorie_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.categorieproduit')),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_entreprise', models.CharField(max_length=100, verbose_name='nom')),
                ('duree', models.IntegerField(default=30)),
                ('tarif', models.FloatField(default=0.0, max_length=21)),
                ('contact', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='mk_pubs/')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='mk_restaurant_logo/')),
                ('email', models.EmailField(max_length=100)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('specialite', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2048)),
                ('image', models.ImageField(upload_to='mk_service/')),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solliciter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probleme', models.CharField(max_length=250)),
                ('lieu', models.CharField(max_length=250)),
                ('contact', models.IntegerField()),
                ('consommateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.consommateur')),
                ('type_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.typeservice')),
            ],
        ),
        migrations.CreateModel(
            name='Resrevation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantite', models.IntegerField(default=0)),
                ('reglement', models.IntegerField(default=1)),
                ('livrer', models.IntegerField(default=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.consommateur')),
                ('livreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.livreur')),
                ('payement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.payement')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.produit')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationPlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livrer', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantite', models.IntegerField(default=0)),
                ('reglement', models.IntegerField(default=1)),
                ('consommateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.consommateur')),
                ('livreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.livreur')),
                ('payement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.payement')),
                ('plat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.plat')),
            ],
        ),
        migrations.CreateModel(
            name='Quartier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quartier', models.CharField(max_length=100)),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.ville')),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantite', models.IntegerField(default=1)),
                ('consommateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.consommateur')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.produit')),
            ],
        ),
        migrations.CreateModel(
            name='ModeDePayementFournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.fournisseur')),
                ('mode_payement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.payement')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField(max_length=2048)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de Publication')),
                ('consommateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.consommateur')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Administrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.administrateur')),
                ('publicite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.publicite')),
            ],
        ),
    ]
