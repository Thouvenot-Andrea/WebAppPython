<!DOCTYPE html>
<html>
<head>
    <title>Calcul du taux horaire</title>
</head>
<body>
<h1>Employés</h1>
<h3>Budget = {{budget}}€</h3>
<form method="post" action="/" target="result_frame">
    <label for="employe">Nom d'employés:</label>
    <input type="text" id="employe" name="employe" required><br>
    <label for="jours">Jours travaillés :</label>
    <input type="number" min="0" id="jours" name="jours" required><br>
    <label for="taux">Taux journalier :</label>
    <input type="number" min="0" step="0.01" id="taux" name="taux" required><br>
    <input type="submit" value="Soumettre">
</form>
<iframe name="result_frame" style="width:100%; height:300px; border:none;"></iframe>

</body>
</html>

