import os
import base64
import requests
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

# Ladda in nycklarna från .env
load_dotenv()

app = Flask(__name__)

class VasttrafikClient:
    def __init__(self):
        self.key = os.getenv("VT_KEY")
        self.secret = os.getenv("VT_SECRET")
        self.token = self._fetch_token()

    def _fetch_token(self):
        if not self.key or not self.secret:
            print("Fel: VT_KEY eller VT_SECRET saknas i .env!")
            return None
            
        credentials = f"{self.key}:{self.secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        
        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        try:
            response = requests.post(
                "https://ext-api.vasttrafik.se/token", 
                headers=headers, 
                data={"grant_type": "client_credentials"},
                timeout=5
            )
            response.raise_for_status()
            return response.json().get("access_token")
        except Exception as e:
            print(f"Kunde inte hämta token: {e}")
            return None

    def get_departures(self, stop_id):
        # 1. Om vi inte har någon token alls från start, försök hämta en
        if not self.token:
            self.token = self._fetch_token()
            if not self.token:
                return {"error": "API-nycklar saknas eller är ogiltiga i .env"}

        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            # 2. Försök hämta avgångar
            response = requests.get(
                f"https://ext-api.vasttrafik.se/pr/v4/stop-areas/{stop_id}/departures",
                headers=headers,
                timeout=5
            )
            
            # 3. Om token har gått ut (HTTP 401), hämta en ny och försök IGEN direkt
            if response.status_code == 401:
                print("Token expired. Hämtar en ny automatiskt...")
                self.token = self._fetch_token()
                
                # Bygg nya headers med den nya nyckeln och gör anropet igen
                headers = {"Authorization": f"Bearer {self.token}"}
                response = requests.get(
                    f"https://ext-api.vasttrafik.se/pr/v4/stop-areas/{stop_id}/departures",
                    headers=headers,
                    timeout=5
                )
                
            response.raise_for_status()
            return response.json()
            
        except Exception as e:
            return {"error": str(e)}

# Initiera klienten
vt_client = VasttrafikClient()

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/departures')
def api_departures():
    stop_id = os.getenv("STOP_ID", "9021014001960000")
    return jsonify(vt_client.get_departures(stop_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
