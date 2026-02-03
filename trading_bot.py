import requests
import os

TOKEN = "8448457738:AAHicFTHABh31trGrTVaCMzm15nnbdusEIk"
CHAT_ID = "1697906576"
FILE_PATH = "dernier_prix.txt"

def envoyer_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": message})

def check_market():
    # 1. Chercher le prix actuel
    res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    prix_actuel = float(res.json()['price'])

    # 2. Lire le prix précédent (s'il existe)
    prix_precedent = prix_actuel
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            prix_precedent = float(f.read())

    # 3. Calculer la variation en %
    variation = ((prix_actuel - prix_precedent) / prix_precedent) * 100

    # 4. Prendre une décision
    if variation <= -2.0:
        envoyer_telegram(f"🤖 DÉCISION : ACHAT VIRTUEL\n📉 Le prix a chuté de {variation:.2f}%\n💰 Prix : {prix_actuel}$")
    elif variation >= 3.0:
        envoyer_telegram(f"🤖 DÉCISION : VENTE VIRTUELLE\n📈 Le prix a grimpé de {variation:.2f}%\n💰 Prix : {prix_actuel}$")
    else:
        print(f"Observation : BTC à {prix_actuel}$ (Variation: {variation:.2f}%). Pas d'action.")

    # 5. Sauvegarder le prix pour la prochaine fois
    with open(FILE_PATH, "w") as f:
        f.write(str(prix_actuel))

if __name__ == "__main__":
    check_market()
