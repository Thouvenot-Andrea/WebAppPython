<!DOCTYPE html>
<html>
<head>
    <title>Calcul du taux horaire</title>
</head>
<body>
<h1>Employés</h1>
<form method="post" action="/" target="result_frame">
    <label for="employe">Nom d'employés:</label>
    <input type="text" id="employe" name="employe" required><br>
    <label for="jours">Jours travaillés :</label>
    <input type="text" id="jours" name="jours" required><br>
    <input type="submit" value="Soumettre">
</form>
<iframe name="result_frame" style="width:100%; height:300px; border:none;"></iframe>

</body>
</html>
