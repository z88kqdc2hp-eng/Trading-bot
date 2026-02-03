import requests

TOKEN = "8448457738:AAHicFTHABh31trGrTVaCMzm15nnbdusEIk"
CHAT_ID = "1697906576"

def test_envoi():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": "✅ Test réussi ! Ton robot trading est prêt pour tes 4€."}
    r = requests.get(url, params=params)
    print(r.json()) # Ceci s'affichera dans les logs GitHub

if __name__ == "__main__":
    test_envoi()
