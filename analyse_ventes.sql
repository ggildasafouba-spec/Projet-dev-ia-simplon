-- Projet Dev IA Simplon - Analyse des ventes d'une PME

-- Vérification de l'import
SELECT * FROM ventes;

-- 3.a Chiffre d'affaires total
SELECT
    SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;

-- 3.b Ventes par produit (quantités vendues)
SELECT
    produit,
    SUM(qte) AS quantite_vendue
FROM ventes
GROUP BY produit
ORDER BY quantite_vendue DESC;

-- 3.c Ventes par région (quantités vendues)
SELECT
    region,
    SUM(qte) AS quantite_vendue
FROM ventes
GROUP BY region
ORDER BY quantite_vendue DESC;

-- Analyse complémentaire utile au graphique demandé :
-- chiffre d'affaires par produit
SELECT
    produit,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit
ORDER BY chiffre_affaires DESC;
