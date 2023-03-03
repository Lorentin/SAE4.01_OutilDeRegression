# SAE4.01_OutilDeRegression

<h1>Algorithme de régression linéaire par résolution analytique</h1>
  <h2>Calcul des indicateurs de la variance et de la covariance</h2>
  <ul>
    <li>variance = moyenne quadratique de x (x^2) - (moyenne de x)^2</li>
    <li>covariance = moyenne xy - (moyenne x * moyenne Y)</li>
  </ul>
  <h2>Calcul de alpha et beta</h2>
  <ul>
    <li>alpha = covariance / variance</li>
    <li>beta = moyenne des y - alpha * moyenne des x</li>
  </ul>
  <h2>Determination du model de calcul</h2>
  <ul>
    <li>y = alpha * x + beta</li>
  </ul>

<h1>Algorithme de régression linéaire par descente de gradient</h1>
  <h2>Objectif</h2>
  <p>Trouver le minimium locale d'un modéle donnée a partir d'un jeu de données a l'aide d'une descente de gradient</p>
  <ul>
    <li>sommeYc = somme de la colonne des Y au carré</li>
    <li>sommeXY = somme de la colonne des Y * X</li>
    <li>sommeY = somme de la colonne des Y</li>
    <li>sommeXc = somme de la colonne des X au carré</li>
    <li>sommeX = somme de la colonne des X</li>
    <li>tailleX</li>
  </ul>
  <h2>Calcul de coût</h2>
    <ul>
      <li>cout = sommeYc - (2 * a * sommeXY) - (2 * b * sommeY) + (a**2 * sommeXc) + (2 * a * b * sommeX) + n * b**2</li>
    </ul>
  <h2>Calcul gradient de A à partir de sa dérivée partielle</h2>
    <ul>
      <li>gradA = 2 * (a * sommeXc + b * sommeX - sommeXY)</li>
    </ul>
  <h2>Calcul gradient de B à partir de sa dérivée partielle</h2>
    <ul>
      <li>gradB = 2 * (a * sommeX + b * tailleX - sommeY)</li>
    </ul>
  <h2>Ajustement du A et B</h2>
    <ul>
      <li>a = a - pas * gradA</li>
      <li>b = b - pas * gradB</li>
    </ul>
