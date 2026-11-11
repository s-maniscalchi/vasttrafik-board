# Västtrafik Kiosk Dashboard 

Detta projekt är en lokal, minimalistisk webbserver byggd med Python (Flask) som förvandlar en skärm (i mitt fall en Raspberry Pi skärm) till en smart, automatisk tidtabell för vilken hållplats hos Västtrafik du vill.

Systemet hämtar realtidsdata via Västtrafiks öppna API och med hjälp av html och css får man en ren och färgglad-design men motsvarande färg för linjer. 

Idén föddes när jag såg att caféet på Chalmers har en liknande skärm för sin hållplats. Jag tänkte: "Det där borde man ju kunna ha hemma vid dörren". Resultatet blev denna dashboard som hämtar realtidsdata via Västtrafiks öppna API och ritar upp det i ett rent, klassiskt gränssnitt med rätt färger för rätt fordonsslag.

## Funktioner
*   **Realtidsdata:** Hämtar och uppdaterar avgångstider var 15:e sekund.
*   **Smart Autentisering:** Inbyggd och automatisk hantering av OAuth2-tokens i backend.
*   **Västtrafik-Design:** Färgkodade linjer (Blå spårvagnar, Gröna expressbussar, Gula tåg etc.) för snabb överblick, skrivet i ren HTML/CSS.
*   **IoT & Kiosk-redo:** Byggt och optimerat för att köras i ett grafiskt "kiosk"-läge vid boot på en Raspberry Pi.

## Teknisk Stack
*   **Backend:** Python 3, Flask, Requests, python-dotenv
*   **Frontend:** HTML, CSS, JavaScript (Fetch API)
*   **Infrastruktur:** Körs på Linux (Raspberry Pi OS)

## Installation & Användning

### 1. Klona och installera
Börja med att klona projektet och installera beroendena i en virtuell miljö:

```bash
git clone [https://github.com/s-maniscalchi/vasttrafik-board.git](https://github.com/s-maniscalchi/vasttrafik-board.git)
cd vasttrafik-board
python3 -m venv venv
source venv/bin/activate
pip install flask requests python-dotenv

### 2. Konfiguera API-nycklar
Du behöver skapa ett konto på Västrafiks Utvecklarportal och skapa en app för att få dina API-nycklar.

Skapa en .env fil i huvudmappen och lägg in dina nycklar och önskad hållplats-ID:
```bash
VT_KEY=din_client_id_här
VT_SECRET=din_client_secret_här
STOP_ID=9021014001960000 # Standard: Chalmers

### 3. Starta Servern
3.1 python3 app.py

3.2 Gå in på http://localhost:5000

3.3 Hinn med linjen du letar efter.


## Motivation att skapa det.
- Såg på Chalmers att de har en tidtabell för Chalmers-hållplatsen i ett café och funderade på om jag kan ha det hemma.
- Älskar att pilla med raspberry pi:s.
- Frågade AI om det var möjligt, som berättade om Västrafik Developer sida som jag snabbt gick in på och läste mer. Såg att man kunde filtrera hur mycket som helst. Vilka linjer man ville ha, vilket läge, om man vill ha tåg, spårvagnar, osv.


## Lärdommar från bygger
- Lärt mig hur man interagerar och hanterar API:er.
- Lärt mig mer om hur Linux är uppbyggt, hur man redigerar i boot-filerna.
- Hur man effektivt jobbat med SSH från datorn till raspberry:n på lokala nätet.




