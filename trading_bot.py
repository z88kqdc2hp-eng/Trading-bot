import requests

# Tes identifiants vérifiés
TOKEN = "8448457738:AAHicFTHABh31trGrTVaCMzm15nnbdusEIk"
CHAT_ID = "1697906576"

def check_crypto():
    try:
        # 1. Récupération du prix
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        response.raise_for_status() # Vérifie si la connexion internet est OK
        data = response.json()
        prix = float(data['price'])
        
        # 2. Seuil de test (105 000 pour forcer l'alerte maintenant)
        seuil = 105000 
        
        if prix < seuil:
            message = f"📉 Alerte ! Le Bitcoin est à {prix}$. Prépare tes 4€ !"
            send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            params = {"chat_id": CHAT_ID, "text": message}
            requests.get(send_url, params=params)
            print("Message envoyé avec succès !")
        else:
            print(f"Prix actuel : {prix}$. Pas d'alerte nécessaire.")
            
    except Exception as e:
        print(f"Erreur rencontrée : {e}")

if __name__ == "__main__":
    check_crypto()
