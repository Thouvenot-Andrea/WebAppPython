<table>
    %for personne in personnage:
    <tr>
        <td>{{personne['nom']}} a travaillé {{personne['jours']}} jours, son taux journalier est de {{personne['taux']}} € et a gagné {{personne['salaire']}} €.</td>
    </tr>
    %end
    <h3>Il reste : {{budget_restant}}</h3>
</table>

