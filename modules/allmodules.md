# Introduction à la technique
## Principe

Les ondes ultras-sonores sont des ondes acoustiques (>20 kHz), elle peuvent se propager au travers du corps humain. La propagation du signal est fonction des propriétés des tissus traversés. La formation du signal échographique est composé de la réflexion des ondes sur une interface tissulaire de densité différente, et la diffusion des ondes ultras sonores sur les petites particules.

Pour former une image, l’échographe utilise le principe de réflexion des ultrasons : une sonde émet une salve d’ultrasons puis se met à l’écoute des échos réfléchis. Une image échographique est composé de l'ensemble des effets d'atténuation, de réflexion, réfraction et de dispersion. Le corps humain étant un milieu principalement constitué d’eau, les ultrasons s’y déplacent à une vitesse de 1460 m.s-1. Lorsque les ultrasons rencontrent des tissus, graisses ou organes, leur vitesse de propagation change, elle peut alors varier entre 1480 et 1600 m.s-1.  

Milieu | Vitesse de propagation (m/s)  
------ | ------  
Air | 330  
Eau | 1500  
Tissus mous | 1450-1700  
Os | 3000-4000  
*Table 1 : La vitesse de propagation des ultrasons pour les médias différents et leur densité dans l'image CT [1].*  

Grâce à ces différences de vitesse de propagation, couplées à la masse volumique de l'organe, chaque organe de notre corps a une impédance acoustique* qui lui est propre. Cela permet donc une réflexion partielle des ultrasons entre deux tissus de caractéristiques acoustiques différentes


Milieu | Impédance acoustique ($kg.m^{-2}.s{-1}\times 10^{-6}$)  
------ | ------  
Air | 0,0004  
Poumon | 0,26  
Squelette | 3,8-7,4  
Tissus mous | 1,3-1,7  
Eau | 1,5  
*Table 2 : Impédances acoustiques caractéristiques de différentes parties du corps [2].*

Ces valeurs montrent qu’il peut y avoir de grandes différences d’impédance dans le corps telle qu’entre les tissus mous et de l'air et entre les tissus mous et des tissus durs (os, pierres, corps étrangers). Ces interfaces sont très réfléchissante ou très "échogènes" (générateurs d'écho). Derrière ces interfaces, une zone d'ombre apparaît sur les images échographiques du fait que le signal sonore a été quasiment entièrement réfléchi..


## Architecture du système entier


L'appareil permettant de réaliser des échographies est appelé échographe. Il est constitué :  
- D’un transducteur permettant l'émission et la réception d'ultrasons  
- Du système analogique et numérique qui transforme le signal reçu en image  
- D'une console de commande permettant d’effectuer différents réglages   
- D'un système d'alimentation et de gestion des données des données.  

![analyse fonctionnelle](/images/functional_analysis.jpg)

Pour réaliser une échographie, le médecin applique un gel sur la peau, ce gel est appelé gel de couplage. Ce gel permet d’améliorer la transmission du son entre la sonde et le corps.


## Histoire de l'échographie en temps réel

Le premier scanner temps réel en deux dimensions (ou B-scanner) a été développé par Walter Krause et Richard Soldner. Il est commercialisé sous l'appellation Vidoson® par Siemens Medical Systems Allemagne en 1965. Le Vidoson® construit l’image échographique à l’aide de trois transducteurs rotatifs placés face à un miroir parabolique (ainsi le milieu est scanné selon des lignes parallèles). Les transducteurs et le miroir sont couplés ensemble par de l’eau, on a ainsi une bonne adaptation d’impédance avec le corps. Les images sont constituées de 120 lignes et la cadence est de 15 images par seconde.  
XPROBLEME  
James Griffith et Walter Henry ont produit un échographe temps réel à balayage mécanique en 1973. Le transducteur insone un secteur de 30 degrés, avec une image de bonne qualité. Le design de cette sonde a été décrite comme l'une des étapes clé dans le développement de l'échocardiographie. Le premier échographe commercial équipé d’une barrette linéaire de transducteurs, le "Multiscan system", a été produit en 1972 par Nicolaas Bom, Paul Hugenholtz en collaboration avec une société néerlandaise (Organon Teknika). Cet échographe était principalement utilisé en cardiologie.

Vers le milieu des années 1980, les transducteurs abdominaux curvilignes ou convexes sont apparus sur le marché. Ils ont l’avantage d’avoir un meilleur ajustement au niveau de l'abdomen et d’avoir un champ de vision plus large. Les sondes curvilignes ont complètement remplacé les sondes linéaires à la fin des années 1980. Ensuite, l’amélioration de la résolution et de la qualité globale de l'image c’est concentrée principalement sur l'augmentation du nombre de transducteurs (de 64 à 128). Des travaux ont également été fait sur la technologie des transducteurs (large bande et large gamme dynamique), l’ouverture des barrettes (plus de transducteurs tirent en même temps), des rapidités de calcul plus importantes, les algorithmes de focalisation en réception (augmentation du nombre de tâches focales le long de la ligne de mesure), incorporation du TGC (contrôle du gain temps réel) [3].  

Dans les années 1990 les avancées importantes ont été [4]:  

- Le traitement du signal est devenu entièrement analogique. On a la chaîne suivante :
 **[transducteur] -> [beamformer] -> [traitement du signal] -> [convertisseur d’image] -> [moniteur]**

- L'utilisation de transducteurs larges bandes avec une grande ouverture. Le nombre de canaux dans les systèmes haut de gamme va jusqu'à 256 et plus récemment  1024 (barrette 2-D).  


- La phase des échos est traitée en plus de l'amplitude avec la reconstruction cohérente des images. La technique améliore de deux fois la quantité des données donnant des images haute résolution. La cadence d’imagerie est également augmentée.  


- L'avènement de la technique d’imagerie utilisant les harmoniques (multiples de la fréquence de travail) phénomène non-linéaire dû à la propagation des ondes dans les tissus.  

![différentes dimensions](/images/diffecho.jpg)

Les progrès technologiques ont eu un impact significatif sur l’évolution des échographies, en ce qui concerne le traitement d'image et les sondes [5],[6]. La technologie des sondes en particulier, qui a évolué des systèmes mono-éléments (sonde sectorielle mécanique) à des barrettes linéaires et finalement des systèmes 3D en temps réel.

Récemment sont apparues les sondes compatibles avec un smartphone (2009) [7],[8]. Elle est uniquement compatible avec Windows (Microsoft, Redmond, Washington). Les défis technologiques qui ont dus être surmontés étaient principalement la consommation d'énergie de la batterie et la vitesse de transfert des données. Le second était la création des algorithmes nécessaires à l'affichage de l'image sur l'écran du smartphone. Un dispositif a été approuvé pour une utilisation par la Food and Drug Administration (FDA) en 2011 après avoir rencontré des exigences réglementaires strictes pour les applications médicales [9],[10]. Aujourd'hui une variété de sondes spécialisées ont été développées  couvrant une gamme de fréquences de 2 à 18 MHz.

Utilisation médicale des ultrasons
L'échographie permet d’étudier de nombreux organes de l'abdomen, du petit bassin, du cou (thyroïde, foie, rate, pancréas, reins, vessie) ainsi que les vaisseaux sanguins, les ligaments et le cœur. Elle permet plus précisément de rechercher des anomalies (telles que des tumeurs, des kystes et des malformations) et de guider des prélèvements (ponctions).

Thérapeutique :  


- Lithotriteur (désintégration de calculs rénaux)  
- Le traitement thermique (ligaments, tendons, etc.)  	
- Ultrasons focalisés à haute intensité (chirurgie, par exemple dans le cerveau profond)  

Diagnostic :  

- L'échographie (cadence > 30 images / seconde))  
- Technique Doppler (mesure de la vitesse d'écoulement du sang) de densitométrie osseuse (200 kHz 800 kHz)  





# Réalisation de la sonde

Pour clarifier la dimension technique du dispositif nous avons divisé la sonde en plusieurs fonctions qu’elle doit accomplir.

![analyse fonctionnelle](/images/functional_analysis.jpg)  
*analyse fonctionnelle*

##Fonction détection

Dans un premier temps, il faut produire le signal qui va sonder le milieu et de récupérer l’écho réfléchi par les tissus rencontrés, sur toute la zone étudiée. Il faut réaliser les sous-fonctions émission et réception qui se font par l’intermédiaire d’un transducteur (partie acoustique). La sous-fonction balayage du milieu est réalisée par un moteur qui permet d’orienter le transducteur dans différentes directions (partie mécanique). Les commandes de ces sous-fonctions sont décrites dans la partie électronique.

![analyse fonctionnelle de la partie détection](/images/sensing.png)  
*analyse fonctionnelle de la partie détection*

###Réalisation de la partie acoustique

####Transducteur

![conversion électro-mécanique](/images/transducer.png)  
*conversation électromécanique*

Un transducteur à ultrasons permet de convertir un signal électrique en un signal ultrasonore et inversement. Ceci est permis par l’intermédiaire d’un matériau piézo-électrique, qui a la capacité de se dilater et se contracter lorsqu’on lui applique une différence de potentiel. Le milieu qui entoure le piézoélectrique est alors affecté par cette déformation, et une onde s’y propage, comme lorsqu’on fait tomber une pierre dans l’eau. On peut ainsi créer une onde acoustique (ultrasonore-quelques MHz) à partir d’une différence de potentiel (partie émission). Réciproquement, lorsque le matériau piézoélectrique est déformé (quand une onde acoustique le traverse par exemple) une différence de potentiel apparaît entre ses deux faces. La déformation du milieu est traduite par un signal électrique: le piézoélectrique fait alors office de capteur (partie réception).

Le piézoélectrique peut être traité comme un réseau à trois ports, avec deux ports mécaniques représentant l'avant et l'arrière de l'élément piézo-électrique ainsi que d'un port électrique représentant la connexion électrique de l'élément piézo-électrique à l'électronique du système [11], [12]. 
Le choix du piézoélectrique est important: il fixe la fréquence des ultrasons émis. Celle-ci correspond au gain maximal dans le spectre d’émission/réception du transducteur donné par le fabricant, eti dépend de la géométrie du matériau. La fréquence va déterminer la profondeur de pénétration de l’onde. Plus la fréquence est élevée, plus l’atténuation est importante pour une même distance.

Fréquence des ultrasons (MHz) | Profondeur d’exploration maximale (cm)   
------ | ------  
2,5 - 3,5 | >15  
5 | 10  
7,5 | 5-6  
10-12 | 2-3  
*Table 3: Profondeur maximale de l'exploration échographique pour différentes fréquences [2].*

Lorsqu’il n’est pas en train d’émettre un signal, le transducteur passe en mode écoute: l’onde émise va être réfléchie, réfractée, dispersée et absorbée par les tissus. Une partie du signal émis est ainsi renvoyée dans la direction de la sonde et fait vibrer le transducteur, qui va convertir ce signal mécanique en signal électrique.   

Le matériau piézoélectrique excité par un pulse* analogique vibre de part et d’autre de ses faces, or l’onde qui est recherchée est celle qui se propage vers le milieu à explorer. Il faut donc absorber l’onde se propageant dans l’autre direction, d’autant plus qu’elle peut brouiller le signal si elle se réfléchit et revient vers le capteur piézoélectrique. Cette atténuation se fait à l’aide d’un backing.  

![backing](/images/need_backing.png)  
*ondes se propageant de part et d'autre du piézoélectrique*

Il y a désadaptation d’impédance* entre le piézoélectrique et le milieu à explorer. Pour éviter des pertes d’énergie par réflexion à l’interface entre ces deux milieux, on dispose d’une couche d’adaptation d’impédance* disposée sur la surface du piézoélectrique orientée vers le milieu à explorer.   

Enfin, il faut assurer la focalisation du faisceau d’onde. Pour les dispositifs usuels qui sont composés d’une rangée de transducteurs, la focalisation se fait par interférences entre les différentes ondes [13]. Cependant lorsqu’il n’y a qu’une seule source d’émission (cas d’EchOpen), on ne peut créer d’interférences. La focalisation se fait avec la forme même de la sortie. Une forme concave permet de focaliser le faisceau. La distance focale est déterminée en fonction de la fréquence caractéristique du piézoélectrique, qui est liée à la profondeur de pénétration. Cette forme concave peut être obtenue grâce au matériaux piézoélectrique lui-même, la couche d’adaptation d’impédance, ou une lentille.  

![Fonctionnement du transducteur](/images/transudcer_action.png)  
*Fonctionnement du transducteur [14], [15]*

#####Sélection du matériau piézoélectrique

Le composant le plus important du transducteur est l'élément piézoélectrique. Beaucoup de matières actives différentes peuvent être utilisées dans la conception d’un transducteur ; tous ont leurs avantages et leurs inconvénients. Les différents matériaux piézo-électriques utilisés sont les piézoceramics [16], [17], les polymères piézoélectriques [18], [19], et les monocristaux [20]. Les polymères piézo-électriques tel que le poly (fluorure de vinylidène) PV [PVDF] et co-polymère (DFTrFE) ont une faible impédance acoustique (~ 4 MRayl) qui est idéal pour l’adaptation d’impédance acoustique entre le transducteur et le tissu humain (~ 1,5 MRayl).[21]
Comme chaque matériau piézoélectrique a une fréquence de résonance propre qui détermine la profondeur de pénétration, on peut disposer plusieurs transducteurs sur la sonde afin d’avoir un éventail de fréquences de travail. La qualité du matériau est importante: il faut que la réponse électromécanique varie peu d'un milieu à l'autre.


![graphique piézos](/images/piezoelement.png)


Piézoélectriques | polymères | Monocristaux | Piézocéramiques  
------ | ------ | ------ | ------  
Avantages | **Impédance acoustique faible**: (~4 MRayl. Idéal pour l’adaptation d’impédance entre le transducteur et les tissus (~1,5 MRayl)  **Constante diélectrique faible** idéal pour l’adaptation d’impédance électrique | **Bon couplage électromécanique** Meilleur contraste de l’image  **Constante diélectrique faible**  idéal pour les transducteurs mono-éléments sensibles à grande ouverture |  **Coefficients de couplage électromécanique élevés**  
Défauts | **Coefficients de couplage faibles** | **Impédance acoustique importante** |**Impédance acoustique élevée** **grandes constantes diélectriques** 
*comparaison des propriétés de différents matériaux piézoélectriques*

#####Sélection du backing

On cherche à atténuer au maximum les ondes se propageant du mauvais côté du piézoélectrique. Il faut pour cela un matériau fortement inhomogène. Les résultats de Desilet et al [22] et expériences d’EchOpen montrent qu’il faut privilégier un matériau de faible impédance. (de 3 à 5 MRayl) pour améliorer la forme du pulse.

#####Sélection de l’adaptation d’impédance

Elle permet d’éviter une réflexion de l’onde à l’interface piézoélectrique/surface à sonder. La valeur de l’impédance du milieu d’adaptation, dans le case de régime impulsionnel, pour une seule lame d’adaptation, doit vérifier:

 ![formule adaptation d'impédance](images/impendance.png)

Les lames généralement utilisées sont des lames quart d’onde: l’épaisseur correspond au quart de la longueur d’onde caractéristique du piézoélectrique dans le milieu de propagation à explorer.



### Réalisation de la partie mécanique

#### Sonde à balayage

![sonde à balayage](/images/sonde_a_balayage.png)  

Lorsque les ultrasons ne sont envoyés que dans une seule direction (un seul transducteur, un seul tir), l’échographe n’obtient qu’une ligne d’image. Afin d’avoir une image complète, il faut effectuer un balayage sur la surface à échographier. Si, autrefois, c’était au praticien de faire le balayage, de nos jours les sondes le font automatiquement. C'est grâce à l'automatisme du balayage que l'on dit souvent que l'échographie est "dynamique".

#### Moteur

Le moteur permet d’effectuer le balayage de la surface à explorer. Il faut adapter le type de moteur au balayage choisi [23]. On fixe le (ou les) transducteurs sur la tête du moteur. Il faut savoir qu'un balayage oscillant par le moteur implique des accélérations et des décelerations qui bruitent le signal. On peut néanmoins transformer la rotation du moteur en mouvement pendulaire.

Le moteur utilisé doit être asservi en vitesse, angle, précision angulaire.
Un moteur à courant continu peut être utilisé, à condition d’avoir un bon encodeur pour toujours connaître précisément la position. Le moteur synchrone pas-à-pas est moins contraignant en terme d’asservissement et permet une grande précision angulaire, car on peut faire des micro-pas.


*vitesse de balayage*: constante, 7,5 tours/sec  
*déplacement*: horaire et anti-horaire (oscillations)  
*précision*: de 30 à 1060 pas en 60°  

![cahier des charges du moteur](/images/charges_motor.png)  
*exemple de cahier des charges*

### Réalisation de la partie électronique

#### Alimentations

##### Alimentation générale

Pour les tests, il faut privilégier une alimentation continue de laboratoire plutôt qu’une pile. En effet le débit de courant étant contrôlé, on évite de griller les composants au cours du montage avec une telle alimentation. En revanche, le pile sera préférable à terme, une fois la sonde fonctionnelle,  car il y a moins de bruits. 

##### Circuit d’adaptation

Tous les composants qui seront utilisés par la suite ne fonctionnent pas à la même tension, il faut donc un circuit pour diviser la tension d’entrée qui est de l’ordre de 18V.
![cahier des charges alimentation](/images/converter_DC.png)  
*Fonction attendue, exemples de valeurs.*  

##### Commande du moteur

Le moteur est commandé par un microcontrôleur, qui intervient dans d’autres sous-fonctions afin de synchroniser les sous-fonctions. Par exemple l’émission du pulse et la commande du moteur peuvent être synchronisées.
Il faut faire attention au courant d’alimentation au cours des tests pour ne pas griller le moteur!

![fonction attendue](/images/commande_moteur.png)  
*Fonction attendue*

#####Commande du pulse

![fonction attendue](/images/pulsing.png)  
*Fonction attendue*

######Circuit haut voltage

Pour produire le pulse qui va simuler le piézoélectrique, il faut atteindre -100V car le gain de la fonction caractéristique du transducteur est faible. Si on veut produire une onde acoustique de l’ordre de 10% de la pression atmosphérique, il faut une telle tension en entrée. [24]

![fonction attendue](/images/hvc.png)  
*Fonction attendue*


######Pulser

A partir d’une commande sous forme d’un pulse logique et d’une alimentation continue de -100V, on génère un pulse de -100V de la même durée. On doit passer par l’intermédiaire d’un pulser car les circuits de commande qui permettent de créer un pulse logique ne fonctionnent pas à des tensions si élevées.

![fonction attendue](/images/pulser.png)  
*Fonction attendue*


######Commande du pulser

La durée du pulse doit correspondre à la moitié de la période caractéristique du transducteur pour obtenir le meilleur taux de conversion (la réponse attendue est sous forme d’un pulse ultra-sonore).
La fréquence d’émission de pulse est choisie en fonction de la vitesse du moteur, et de la précision souhaitée. Pour un moteur pas-à-pas on peu décider d’envoyer un pulse tous les X pas. La commande du pulse doit alors être couplée à la commande du moteur. Elle est contrôlée par un microcontrôleur.


###Mode réception

####Premier filtrage

Réponse d’un transducteur à un pulse électrique:  
![réponse pulse](/images/reponse_reans.png)  

**Explication**: la conversion de l’énergie électrique en énergie mécanique n’est pas totale: lorsqu’on envoie un pulse sur le piézoélectrique, une grande partie de l’énergie électrique est réfléchie. La réponse impulsionnelle électrique sous simulation électrique du transducteur n’est pas une impulsion pure: il y a une résonance de temps caractéristique long. Il est si long que lorsque les échos en retour de l’onde sonore, qui vont exciter le piézoélectrique, vont produire une réponse qui va s’ajouter à celle de résonance. Or ce sont ces échos qui nous intéressent. Comme la fréquence de résonance est faible, on utilise un filtre passe-haut pour couper la résonance et ne récupérer que le signal d'intérêt. Il faut absolument effectuer ce premier filtrage car la résonance basse-fréquence est de forte amplitude et risque de griller les composants des circuits suivants.

![Signal d’intérêt](/images/reponse_filtre.jpg)  
*Signal d'intérêt*  

On ne veut analyser que l’écho retransmis par les tissus après qu’on ait envoyé un pulse. Tout le reste n’est que du bruit. L’acquisition de données est géré par un microprocesseur. Une solution est de synchroniser le début de l’acquisition avec l’émission d’un pulse, et de fixer la durée d’écoute dt en fonction de la profondeur de pénétration de l’onde dans les tissus (liée à la fréquence fc), en considérant comme vitesse moyenne de propagation de l’onde sonore dans les tissus la vitesse d’une onde acoustique dans l’eau. De plus, il faut protéger les circuits suivants de la réponse électrique du transducteur au pulse (cette réponse est de l’ordre de 100V et les hautes fréquences du pulse de réponse n’ont pas été filtrées par le passe-haut). On utilise pour cela un T/R switch.

![emission_reception](/images/ER_modes.png)  
*Différents modes du circuit analogique*

## Fonction analyse du signal

![Analyse fonctionnelle](/images/functional_analysis.png)  
*Analyse fonctionnelle*  

L’approche présentée ici maximise l’utilisation de traitement analogique du signal, afin de réduire la fréquence d’échantillonnage nécessaire pour la partie numérique, pour avoir un moindre coût et une moindre consommation. Le circuit est sensible aux bruits. Le traitement analogique permettrait un traitement du signal accessible plus facilement et l’ouverture sur de nouvelles techniques, comme l’echosthétoscopie Doppler.  

### Amplification TGC

Lorsque le son se propage dans les tissus mous, il est atténué. Cette atténuation augmente linéairement avec la fréquence, donc plus la fréquence de travail est importante, plus la profondeur de pénétration du son sera faible. Dans l’échographe, on compense cette atténuation avec une compensation de gain temporel (Time Gain Compensation). L’atténuation dans un tissu uniforme suit une loi exponentielle décroissante de la distance parcourue. Le TGC doit donc être une fonction exponentielle croissante de la distance pour que le produit soit une constante, et qu’on s’affranchisse de la perte de signal due à la distance. Dans le cas de l’échosthétoscope, les tissus traversés sont d’impédance différentes, la loi d’atténuation n’est pas une simple exponentielle. On note en revanche qu’une approximation linéaire pour le TGC est convenable.  
![exemple de TGC](/images/tgc.png)  
*Exemple de TGC*  


### Second filtrage

Les signal de départ est bruité, et le passage par l’amplificateur TGC rajoute du bruit. Il faut filtrer le signal avec un filtre passe bande de fréquence de résonance proche de fc. On ne pouvait pas utiliser un filtre passe-bande dès le début car les trop grandes différences d’amplitude entre la résonance basse-fréquence et les échos superposés auraient posé problème pour choisir les composants.

![ensemble des signaux](/images/signals.png)  
*étapes du traitement du signal*

### Détection d’enveloppe

On s’intéresse à l’énergie du signal reçu en écho, qui est caractéristique des tissus rencontrés par l’onde et qui l’ont réfléchie (le coefficient de réflexion dépend en effet du type d’interface rencontré). Il faut récupérer l’énergie du signal, contenue dans l’enveloppe.  
![Détection d'enveloppe](/images/detection_enveloppe.png)  
*Détection d'enveloppe*


### Conversion analogique numérique et calcul de pixels

La sortie du détecteur d’enveloppe est ensuite échantillonnée pour être analysée et envoyée sous forme numérique à une application en interface avec l’utilisateur. On utilise pour ça un CAN, dont il faut judicieusement choisir la fréquence d'échantillonnage.  

Pour chaque pulse envoyé et chaque slave d’échos correspondants reçus, on va tracer une ligne de pixels correspondant à la ligne dans l’espace qui a été sondée. Le temps d’arrivée d’une slave va correspondre à la distance qui a été parcourue. Grâce au temps de trajet entre l’émission et la réception des ultrasons, et connaissant les vitesses de propagation dans les tissus, on peut déterminer la distance qui sépare les différentes interfaces. On peut donc cartographier le milieu traversé par l’onde en fonction de la profondeur, et ce pour chaque ligne d’acquisition. 

![pixels](/images/pixels.png)  
*exemple de résultat*

On remarque que la valeur pour chaque point échantillonné suffit, plutôt que de calculer l’intégrale entre deux points échantillonnés. En effet, c’est la différence entre les valeurs de l’énergie contenue dans l’enveloppe (donc la différence des milieux traversés) qui nous intéresse, et non la valeur entière de l’intégrale. à revoir: intensité acoustique prop au log de la pression acoustique
On peut aussi intégrer un programme pour passer le la forme conique de l’image reconstruite (due à la position unique du transducteur qui balaye en rotation) à une forme rectangulaire.

## Fonction interface

### Affichage de l’image en temps réel
### Interface utilisateur

## Bac de test

### Aquarium
Il faut respecter la distance de focalisation déterminée par le transducteur. Le bac doit être transparent pour voir ce qu’on manipule. 

### Fantômes
On utilise des "fantômes" pour reproduire les variations de propagation suivant les tissus.

### Milieu de propagation

Le milieu de propagation principal est choisi pour une bonne propagation des ondes, une adaptation d’impédance avec le piézo, une similarité avec les tissus qu’on observera

# Glossaire

[echosthétoscopie Doppler]: méthode d'échosthétoscopie permettant d'observer les flux sanguins en utilisant l'effet Doppler. 

[focaliser]: concentrer l’énergie acoustique de l’onde dans une zone réstreinte de l’espace, celle qu’on désire étudier.  

[impédance acoustique]: cette grandeur caractérise l’oppostion d’un milieu au passage d’une onde  

- [désadaptation d’impédance]: une interface entre deux milieux présente une désadaptation d’impédance si la différence d’impédance entre ces deux milieux est importante. Cette désadaptation est à l’origine d’une réflexion de l’onde à l’interface, ce qui amoindri l’énergie du signal transmis.  

- [adaptation d’impédance]: en acoustique, c’est une méthode qui consiste à insérer, entre deux matériaux d’impédance désadaptées, un matériau d’impédance intermédiaire, afin de diminuer la réflexion à l’interface.  
matière active (ici): matériau permettant de convertir une forme d’énergie en une autre.  


[pulse]: signal singulier se propageant dans un milieu. On distingue le pulse analogique (signal électrique) qui vient exciter le matériau piézoélectrique du pulse acoustique (déformation mécanique) qui est produit par le piézoélectique suite à une excitation.  

# Bibliographie
 
[1]: http://www.google.com/patents/WO2006077338A1?cl=en 
[2]: http://www.google.com/patents/WO2006077338A1?cl=en  
[3]: http://www.google.com/patents/WO2006077338A1?cl=en  
[4]: http://www.google.com/patents/WO2006077338A1?cl=en  
[5]: http://www.ncbi.nlm.nih.gov/pubmed/9602842
[6]: http://www.brl.uiuc.edu/Publications/1998/OBrien-JJAP-2781-1998.pdf
[7]: http://uix.sagepub.com/content/30/1/21.short
[8]: https://www.technologyreview.com/s/413222/ultrasound-to-go/  
[9]: http://mobihealthnews.com/10165/fda-approves-mobisantes-smartphone-ultrasound/    
[10]: http://www.engineeringforchange.org/ultrasound-is-now-on-smart-phones-engineering-for-change/
[11]:https://www.amazon.com/Acoustic-Waves-Devices-Processing-Prentice-Hall/dp/0130030473/168-7062977-8650263?ie=UTF8&*Version*=1&*entries*=0  
[12]: http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=544509&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D544509  
[13]: http://www.ob-ultrasound.net/lineararrays.html  
[14]: https://facmed.univ-rennes1.fr/wkf/stock/RENNES20090317042111cpiszkorUS2009.pdf  
[15]: https://hal.archives-ouvertes.fr/file/index/docid/54260/filename/Memoire_these_Wilm.pdf  
[16]: http://www.med.nyu.edu/skirball-lab/turnbulllab/PDFS/LockwoodIEEEUFFC94.pdf  
[17]: http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=655629&url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel3%2F58%2F14299%2F00655629.pdf%3Farnumber%3D655629  
[18]: http://www.sciencedirect.com/science/article/pii/0161734689900011    
[19]: http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=985701&url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F58%2F21244%2F00985701.pdf%3Farnumber%3D985701  
[20]:  http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=883543&url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F58%2F19117%2F00883543.pdf%3Farnumber%3D883543  
[21]: http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=1251138&url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F58%2F28006%2F01251138.pdf%3Farnumber%3D1251138    
[22]: C. DESILETS, J. FRAZER et G. S. KINO : The design of efficient broadband piezoelectric transducers. IEEE Trans. Son. Ultrason., 25:115–125, 1978.  
[23]: http://echopen.org/index.php/Balayage  
[24]: http://www.sfrnet.org/rc/org/sfrnet/htm/Article/2011/20110524-112842-171/src/htm_fullText/fr/polyBasesPhysiques_14.pdf  
