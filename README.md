# Projet-Transverse 🎮
[Lien vers le dépôt GitHub](https://github.com/justinegrng/Projet-Transverse.git) 

## Projet jeu : FC EFREI ⚽️

## Membres du projet
> Justine GARNUNG [![linkedin](https://github.com/justinegrng/Projet-Transverse/assets/89320065/eba91f42-9ed4-4ef3-8502-ca4925d64d8f)](https://www.linkedin.com/in/justine-garnung-674571232/)  
> Yéléna SAINTE-ROSE BRUNY [![linkedin](https://github.com/justinegrng/Projet-Transverse/assets/89320065/eba91f42-9ed4-4ef3-8502-ca4925d64d8f)](https://www.linkedin.com/in/yelesr/)  
> Maelle CHOLLET [![linkedin](https://github.com/justinegrng/Projet-Transverse/assets/89320065/eba91f42-9ed4-4ef3-8502-ca4925d64d8f)](https://www.linkedin.com/in/maelle-chollet-b7632a293/)  
> Virgile CURTAROLO OTAL [![linkedin](https://github.com/justinegrng/Projet-Transverse/assets/89320065/eba91f42-9ed4-4ef3-8502-ca4925d64d8f)](https://www.linkedin.com/in/virgile-curtarolo-otal-95261a293/)  
> Almha IMMACOLATO [![linkedin](https://github.com/justinegrng/Projet-Transverse/assets/89320065/eba91f42-9ed4-4ef3-8502-ca4925d64d8f)](https://www.linkedin.com/in/almha-immacolato-2754b3293/)  

## Files organization
> [!TIP]
> Il suffit de cliquer ci-dessous sur "📁 Projet Transverse S2" afin de visualiser l'arborescence de notre projet.


<details>
<summary> 📁 Projet Transverse S2 </summary>
  
- `main.py`
- `game.py`
- `display.py`
- `ball.py`
- `goal.py`
- `button.py`
- `trajectory.py`
<details>
<summary> 📁 assets </summary>
  
- `background.PNG`
- `ballon.PNG`
- `gardien.PNG`
- `button_credits.PNG`
- `button_play.PNG`
- `quit_button.PNG`
</details>
</details>

## But du jeu

Dans le cadre de notre projet transverse qui allie la programmation en python et la physique, nous avons créé un jeu de tir au but : FC EFREI.

Ce jeu consiste donc à lancer un ballon en paramétrant une direction et une force de tir afin de marquer un but dans la cage de foot tout en évitant le gardien.

Pour complexifier le jeu, nous avons mis le gardien en mouvement avec une vitesse constante.

## Comment jouer à FC EFREI ?

Ouvrez le jeu en cliquant sur la flèche verte en haut à droite de l'écran.

Une fois l'interface graphique ouverte, vous vous retrouvez avec le ballon centré au point de pénalty devant vous.


<img width="304" alt="image" src="https://github.com/justinegrng/Projet-Transverse/assets/150793383/b2ad8672-6685-412d-a5c7-8e4cc6a68e7f">




Il ne vous reste plus qu'à lancer le ballon. Mais comment faire pour éviter le gardien ?

Pour cela, vous pouvez paramétrer votre tir :

> Pour une direction de tir optimale, appuyez sur la touche "flèche gauche" ou "flèche droite" pour diriger votre tir.
  
> Pour une force de tir adaptée, maintenez appuyée la touche "flèche haut" plus ou moins longtemps pour une force plus ou moins forte. Pour avoir une indication de la force délivrée par votre tir, nous avons placé une jauge au dessus de la cage.
  
Il ne vous reste plus qu'à appuyer sur la touche "espace" pour lancer le ballon !

Si le ballon touche le gardien, vous avez perdu : ❌

Si le ballon rentre dans la cage : Bravo ! Vous avez gagné ! 🥇

> [!NOTE]
> Nous avons fait le choix d’avoir une interface graphique de face et non de profil. Nous avons fait ce choix pour que l’on ait cette impression de profondeur et de s’imaginer dans le décor. Pour respecter notre choix, nous avons dû effectuer une rotation de plan afin que notre jeu reste dans une dimension en 2D tout en donnant l’impression d’être en 3D.


