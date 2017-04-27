# Kaffeehaus
Ein Kaffeehaus möchte es seinen Kunden ermöglichen Kaffee online zu bestellen.
Der Kunde nutzt dazu seinen eigenen Rechner und sendet eine Bestellung an das Kaffeehaus, dort wird die Bestellung notiert und aufgehoben, bis der Kunde diese bezahlt.

## Abschnitt 1
### Grundanforderungen
Im ersten Schritt sollen Bestellungen als Text zwischen Kunde und Kaffeehaus übertragen werden. Der Kunde wird dabei als Client und das Kaffeehaus als Server betrachtet.

**Client**
* IP Adresse und Port des Kaffees werden als Kommandozeilenparameter übergeben
* Die Bestellungen werden Zeilenweise an das Kaffee übertragen

**Server**
* IP Adresse und Port werden ebenfalls über die Kommandozeile festgelegt
* Es wird auf Anfragen von Clients gehorcht
* Der Administrator kann am Server Befehle ausführen, so soll zum Beispiel über den Befehl "/clients" ausgegeben werden, wie viele Clients gerade mit dem Server verbunden sind.

**Sonstige**
* Fehler sollen Ordnungsgemäß behandelt werden
* Der Quelltext soll sauber dokumentiert werden
* Alle Verbindungen sollen sauber geschlossen werden

### Erweiterungen 
**Server**
* Protokolliert die gesendeten Nachrichten in einem gemeinsamen Log Datei, wobei das Loggen in einer Thread-sicheren Methode passiert.
* Über das Log Datei soll ausgelesen werden können, welche Produkte wie oft bestellt wurden.
* Jeder Client wird separat verwaltet, ein Server kann also mehrere Clients annehmen.

**Sonstige**
* Erstelle eine Dokumentation mittels Sphinx für alle Module.

### Protokoll
Die Einzelnen Arbeitsschritte sollen Stichwortartig dokumentiert werden.

## Abschnitt 2
### Grundanforderungen
Im nächsten Schritt soll es möglich sein die Anfragen des Kunden zu überprüfen, das Kaffeehaus gibt dafür eine Produktliste bekannt. Befindet sich das angefragte Produkt nicht auf der Liste, wird die Bestellung verweigert. Es gibt dabei eine begrenzte Anzahl an Basisprodukten (Bsp.: Kaffee, Tee, Semmel, ...) und diverse Zusatzprodukte zu diesen (Bsp.: Milch, Zucker, Honig, Wurst, ...).

**Client**
1. Der Kunde gibt den Namen eines Produktes ein und sendet diesen an das Kaffeehaus. Zusätzlich kann der Kunde, durch Leerzeichen getrennt, beliebig viele Zusatzprodukte angeben.
2. Ist das Produkt, sowie alle Zusatzprodukte verfügbar, kann er seine Bestellung bestätigen oder ablehnen.

**Server**
* Das Kaffeehaus hat eine Liste von verfügbaren Basisprodukten, sowie Zusatzprodukten. Folgende sollen in dieser Aufgabe implementiert werden:
    * Kaffee        (2.60€)
        - Milch     (0.40€)
        - Zucker    (0.15€)
    * Tee           (2.00€)
        - Honig     (0.15€)
    * Semmel        (0.80€)
        - Butter    (0.15€)
        - Marmelade (0.15€)
        - Schinken  (0.40€)
* Der Gesamtpreis der Bestellung wird, anhand der Basis- und Zusatzprodukte, bereits am Server berechnet.
* Erhält der Server die Eingabe eines Kunden, wird geprüft ob die Basis- und Zusatzprodukte verfügbar sind. Ist dies der Fall wird der Preis als Antwort gesendet und nach eine Bestätigung gefragt. Andernfalls wird angegeben, dass ein Produkt nicht verfügbar ist.

### Erweiterungen
**Client**
* Typische Fehlerfälle durch Benutzereingaben werden bereits im Client verhindert.
**Server**
* Es soll möglich sein mehrere Zusatzprodukte zu einem Produkt zu bestellen.
* Bei einer ungültigen Eingabe soll dem Kunden mitgeteilt werden, welches Produkt nicht verfügbar ist.

### Beispiel
**Gültige Eingabe**
```
KUNDE:      Kaffee Milch Milch
KAFFEEHAUS: 3.40€ (y/n)
KUNDE:      y
KAFFEEHAUS: Bestellung bestätigt!
```

**Falsche Eingabe**
```
KUNDE:      Kaffee Keks Nein
KAFFEEHAUS: Keks nicht verfügbar!
```
