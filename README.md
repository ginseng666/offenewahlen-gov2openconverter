# Offene Wahlen Österreich Data Converter
Konvertiert die Wahldaten von öffentlicher Stelle in eine einheitlich strukturierte CSV Datei.

## Daten
- [Gemeinderatswahl Graz 2003](http://data.graz.gv.at/daten/package/wahlergebnis-der-gemeinderatswahl-2008-in-der-stadt-graz) (Datenquelle: Stadt Graz - [data.graz.gv.at](http://data.graz.gv.at/) - CC BY 3.0 AT)
- [Gemeinderatswahl Graz 2008](http://data.graz.gv.at/daten/package/wahlergebnis-der-gemeinderatswahl-2008-in-der-stadt-graz) (Datenquelle: Stadt Graz - [data.graz.gv.at](http://data.graz.gv.at/) - CC BY 3.0 AT)
- Gemeinderatswahl Graz 2012() (Datenquelle: Stadt Graz - [data.graz.gv.at](http://data.graz.gv.at/) - CC BY 3.0 AT)
- [EU Wahl 2014](https://www.data.gv.at/katalog/dataset/2b10a91b-51d5-4e34-b992-8fd3a3121f0d) (Datenquelle: BMI - data.gv.at - CC BY 3.0 AT)
- [Nationalratswahl 2013](https://www.data.gv.at/katalog/dataset/09716341-2bea-4298-9525-e936d8247d19) (Datenquelle: BMI - data.gv.at - CC BY 3.0 AT)

## Data Output
Ziel ist es, immer eine CSV Datei mit der selben Struktur zu exportieren. Die CSV-Datei muss ein ```;``` (Semikolon) als Trennzeichen haben, keine Quote-Chars, in UTF-8 encodiert sein und folgende Spalten haben. Wichtig ist dabei, dass die Spaltenbezeichnung in der ersten Header-Zeile der CSV Datei genau passt, die Reihenfolge der Spalten ist dabei aber egal.
- ```spatial_id```: die räumliche Kennzahl Sprengelkennzahl, Gemeindekennzahl, Bezirkskennzahl als String, je nach dem was verwendet wird.
- ```votes```: Zahl der abgegebenen Stimmen als Integer
- ```invalid```: ungültige Stimmen als Integer
- ```valid```: gültige Stimmen als Integer
- ```<party>```: danach folgen Spalte für Spalte die Stimmen für die jeweiligen Parteien als Integer. Als konkretes Beispiel: Wenn bei einer Wahl die folgenden drei Parteien SPÖ, ÖVP und FPÖ zur Wahl standen, dann folgt eine Spalte mit ```spoe```, eine mit ```oevp``` und eine mit ```fpoe```. Hier ist ebenfalls die Reihenfolge egal, aber ebenfalls die korrekte Bezeichnung in der Headerzeile der Datei wichtig. 
	- **Korrekte Partei-Bezeichnungen**
	- ```bbb```: Betty Baloo Bande
	- ```bzoe``` BZÖ
	- ```cpg```
	- ```cpoe```
	- ```ekw```
	- ```eustop```
	- ```fpoe``` FPÖ
	- ```gruene``` Grüne
	- ```gvp```
	- ```kpoe``` KPÖ
	- ```lif```
	- ```m```
	- ```neos``` Neos
	- ```oeabp```
	- ```oevp``` ÖVP
	- ```rwa```
	- ```spoe``` SPÖ
	- ```stronach``` Team Stronach
	- ```salz```
	- ```slp```
	- ```wandl```
	- ```weg```
	- ```wir```
	- ```zpa```

**Beispiel**

| spatial_id     | votes       | invalid | valid | spoe | oevp | fpoe |
|---------------|--------------|--------------|--------------|--------------|--------------|--------------|
| 101 | 345 | 4 | 341 | 181 | 152 | 12 |
| 102 | 412 | 5 | 407 | 31 | 188 | 188 |
| ... | ... | ... | ... | ... | ... | ... |



Unter [data/output/](data/output/) sind die konvertierten CSV-Dateien gespeichert.


**Viewer**

Unter [viewer](viewer/) findet sich ein d3-Script zum einfachen Betrachten der csv-Ergebnisdaten. Live-Version siehe [hier](http://drawingdata.net/owviewer/)

