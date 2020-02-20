# comment contribuer 

## architecture du projets 

l'architecture du projets est composé de deux branche "majeur" et des branche "mineur".

les deux branche "majeur":
* master , sur cette branche nous stockerons les version stable de notre plateforme , il est interdit de contribuer/push directement sur cette branche.
* dev , où l'on stockeras la version de dévellopement.

les branche "mineur" qui aurons une durée de vie asser courte en comparaison avec dev & Master , sur lesquelles vous travaillerais en isolation 
afin de minimiser les conflits avec les autres menbre du projet.

## Nomenclature & règle de contribution 

A chaque fois que vous voulez developper un nouveau composant pour le projet vous devez:
1- crée une "issue" afin de décrire le problème , les amélioration ... , voir l'onglet "issues" de l'interface web.
2- crée une branche avec comme nom : **#[Numero de l'issue]titre_de_mon_issue** , attention de bien la crée à partir de la branche dev.
3- lorsque vous voudrez envoyer votre contribution sur le projets vous devez faire une pull request , voir l'onglet "pull requests" il y a un boutton pour crée une pull request.
4- attendre que quelqu'un d'autre que vous "review" votre code , CAD relire le code & proposer si besoin des amlioration du code à envoyer , vu que nous travallons en binome l'autre membre du binome pourais s'en occuper.

Lorsque nous considèrerons que la version de la branche dev est stable nous ferrons des pull request de dev vers master.
