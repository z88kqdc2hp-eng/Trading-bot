import requests

# Tes accès Telegram
TOKEN = "8448457738:AAHicFTHABh31trGrTVaCMzm15nnbdusEIk"
CHAT_ID = "1697906576"

def check_crypto():
    # 1. On récupère le prix du Bitcoin
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url).json()
    prix = float(response['price'])
    
    # 2. Ta règle d'alerte (Seuil à 105 000 pour être sûr que ça sonne au test)
    seuil = 105000 
    
    if prix < seuil:
        message = f"📉 Alerte ! Le Bitcoin est à {prix}$. Prépare tes 4€ !"
        send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(send_url)

if __name__ == "__main__":
    check_crypto()
