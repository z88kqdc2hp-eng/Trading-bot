import requests

# Tes identifiants
TOKEN = "8448457738:AAHicFTHABh31trGrTVaCMzm15nnbdusEIk"
CHAT_ID = "1697906576"

def observer_marche():
    try:
        # 1. On récupère le prix du Bitcoin en direct
        res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        prix = float(res.json()['price'])
        
        # 2. Tes seuils de décision (virtuels)
        seuil_achat = 90000 # Si ça descend là, on simule un achat
        seuil_alerte = 100000 # Juste pour savoir s'il est très haut
        
        # 3. Le Bot analyse et décide
        if prix < seuil_achat:
            msg = f"🤖 DÉCISION : ACHAT (Virtuel)\n📉 Le BTC est à {prix}$, c'est une affaire !"
        elif prix > seuil_alerte:
            msg = f"🤖 DÉCISION : VENTE (Virtuelle)\n📈 Le BTC est à {prix}$, on prend les profits !"
        else:
            # Pour que tu saches qu'il travaille, il t'envoie un rapport calme
            msg = f"👀 Observation : BTC à {prix}$. Rien à signaler pour l'instant."

        # Envoi du message
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={"chat_id": CHAT_ID, "text": msg})
        
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    observer_marche()
