import pandas as pd
import plotly.express as px

# Charger le jeu de données
ventes = pd.read_csv("ventes.csv")

# Exemple / graphique : ventes par région
ventes_par_region = (
    ventes.groupby("region", as_index=False)["qte"]
    .sum()
)
fig_region = px.bar(
    ventes_par_region,
    x="region",
    y="qte",
    title="Ventes par région",
    labels={"region": "Région", "qte": "Quantité vendue"},
)
fig_region.write_html("ventes-par-region.html")

# Graphique demandé 1 : ventes par produit
ventes_par_produit = (
    ventes.groupby("produit", as_index=False)["qte"]
    .sum()
)
fig_produit = px.bar(
    ventes_par_produit,
    x="produit",
    y="qte",
    title="Ventes par produit",
    labels={"produit": "Produit", "qte": "Quantité vendue"},
)
fig_produit.write_html("ventes-par-produit.html")

# Graphique demandé 2 : chiffre d'affaires par produit
ventes["chiffre_affaires"] = ventes["prix"] * ventes["qte"]
ca_par_produit = (
    ventes.groupby("produit", as_index=False)["chiffre_affaires"]
    .sum()
)
fig_ca = px.bar(
    ca_par_produit,
    x="produit",
    y="chiffre_affaires",
    title="Chiffre d'affaires par produit",
    labels={
        "produit": "Produit",
        "chiffre_affaires": "Chiffre d'affaires (€)",
    },
)
fig_ca.write_html("chiffre-affaires-par-produit.html")

print("Graphiques générés avec succès.")
