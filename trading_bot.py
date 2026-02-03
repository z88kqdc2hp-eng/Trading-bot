import requests
import os

# Tes accès
TOKEN = "8448457738:AAHicFTHABh31trGrTVaCMzm15nnbdusEIk"
CHAT_ID = "1697906576"
MEMOIRE_PRIX = "dernier_prix.txt"

def envoyer_decision(texte):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": texte})

def observer_et_decider():
    # 1. On regarde le prix actuel sur Binance
    res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    prix_actuel = float(res.json()['price'])
    
    # 2. On récupère le prix de l'heure dernière si on l'a
    prix_avant = prix_actuel
    if os.path.exists(MEMOIRE_PRIX):
        with open(MEMOIRE_PRIX, "r") as f:
            prix_avant = float(f.read())

    # 3. Calcul de la variation
    variation = ((prix_actuel - prix_avant) / prix_avant) * 100

    # 4. Prise de décision (Seuil de 1% pour le test)
    if variation <= -1.0:
        envoyer_decision(f"🤖 DÉCISION : ACHAT (Virtuel)\n📉 Le prix a chuté de {variation:.2f}%\n💰 Prix : {prix_actuel}$")
    elif variation >= 1.0:
        envoyer_decision(f"🤖 DÉCISION : VENTE (Virtuelle)\n📈 Le prix a grimpé de {variation:.2f}%\n💰 Prix : {prix_actuel}$")
    else:
        print(f"Observation : BTC à {prix_actuel}$ ({variation:.2f}%). Rien à faire.")

    # 5. On note le prix pour la prochaine fois
    with open(MEMOIRE_PRIX, "w") as f:
        f.write(str(prix_actuel))

if __name__ == "__main__":
    observer_et_decider()
