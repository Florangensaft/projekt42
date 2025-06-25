## Statische IP-Adresse vergeben

```bash
sudo nmtui
```

  Du startest ein einfaches grafisches Menü im Terminal zur Netzwerkkonfiguration.

  1. Wähle **„Edit a connection“** (Verbindung bearbeiten)
  2. Wähle z. B. **„eth0“** oder **„wlan0“**
  3. Stelle den IPv4-Modus auf **„Manual“**
  4. Gib deine gewünschte IP-Adresse ein, z. B.:
     * IP: `192.168.24.110`
     * Gateway: `192.168.24.254`
     * DNS: `8.8.8.8`
  5. Speichern und zurück zum Hauptmenü
  6. **Verbindung neu aktivieren**, damit die Einstellung übernommen wird

---

## Benutzer `willi` erstellen

```bash
useradd willi -m -s /bin/bash
passwd willi
```

  * `useradd willi` – erstellt den Benutzer `willi`
  * `-m` – erzeugt ein eigenes Home-Verzeichnis (`/home/willi`)
  * `-s /bin/bash` – legt die Bash als Standardshell fest
  * `passwd willi` – du wirst aufgefordert, ein Passwort zu vergeben

---

## Benutzer `fernzugriff` mit Adminrechten erstellen

```bash
useradd fernzugriff -m -s /bin/bash -G sudo
passwd fernzugriff
```

  * Erstellt den Benutzer `fernzugriff` genau wie oben
  * `-G sudo` – fügt ihn zur **Gruppe `sudo`** hinzu. Er darf administrative Befehle mit `sudo` ausführen
  * `passwd fernzugriff` – Passwort setzen
---
## Docker installieren

```bash
sudo apt install docker.io
```

  * Docker wird über die Paketverwaltung installiert
  * `docker.io` ist die Version aus den Ubuntu/Debian-Repos
---
## Docker starten

```bash
sudo systemctl start docker.service
```

  * Startet den Docker-Dienst (die Software, die die Container verwaltet)

---
## Python installieren

```bash
sudo apt update
sudo apt install python3
```

  * `apt update` aktualisiert die Liste der verfügbaren Pakete
  * `apt install python3` installiert Python 3
  ___
## Git Clonen
```bash
git clone https://github.com/Florangensaft/projekt42.git
```
- Der Befehl lädt das vollständige Repository `projekt42`in ein gleichnamiges Verzeichnis auf deinem lokalen System.
## In das Projektverzeichnis wechseln
Navigiere in das geklonte Projektverzeichnis
```bash
cd projekt42
```
## Docker-Image bauen
```bash
docker build -t projekt42 .
```
- `-t projekt42`gibt dem Image den Namen `projekt42`
- Der Punkt gibt an, dass die aktuelle Verzeichnisstruktur als Kontext für den Build verwendet wird (inkl. Dockerfile)
___
## Dockerfile starten
Nach dem erfolgreichen Build des Docker-Images kann die Anwendung mit folgendem Befehl gestartet werden:
```bash
docker run -d -p 5000:5000 projekt42
```
- `docker run`: Startet einen neuen Container auf Basis eines Images
- `-d`: Führt den Container im `Detached-Modus`aus. Der bedeutet, dass der Container im Hintergrund läuft.
- `-p 5000:5000`: Leitet den Port **5000** des Hosts (linker Wert) auf den Port **5000** im Container (rechter Wert) weiter
- `projekt43`: Der Name des Docker-Images, das beim Build-Vorgang erstellt wurde

## Erste Testabfrage
Nach erfolgreichem Setup kann die erste Testabfrage gestartet werden - dazu eignen sich Tools wie z.B. postman diese kann z.B. an den Endpunkt (IP Anpassen)
```url
https://192.168.24.110:5000/todo-list
```
mit dem Body
```json
{
  "name":"Meine erste Liste"
}
```
gesendet werden.
