# Offene Wahlen Österreich Data Converter
Konvertiert die Wahldaten von öffentlicher Stelle in eine einheitlich strukturierte CSV Datei.

## Daten
- Gemeinderatswahl Graz 2012 (Datenquelle: Stadt Graz - [data.graz.gv.at](http://data.graz.gv.at/) - CC BY 3.0 AT)

## Data Output
Ziel ist es, immer eine CSV Datei mit der selben Struktur zu exportieren. Die CSV-Datei muss ein ```;``` (Semikolon) als Trennzeichen haben, in UTF-8 encodiert sein und folgende Spalten haben. Wichtig ist dabei, dass die Spaltenbezeichnung in der ersten Header-Zeile der CSV Datei genau passt.
- ```spatial_id```: die räumliche Kennzahl Sprengelkennzahl, Gemeindekennzahl, Bezirkskennzahl als Integer - je nach dem was verwendet wird.
- ```eligible```: Zahl der Wahlbereichtigten als Integer
- ```invalid```: ungültige Stimmen als Integer
- ```valid```: gültige Stimmen als Integer
- ```<party>```: danach folgen Spalte für Spalte die Stimmen für die jeweiligen Parteien als Integer. Als konkretes Beispiel: Wenn bei einer Wahl die folgenden drei Parteien SPÖ, ÖVP und FPÖ zur Wahl standen, dann folgt eine Spalte mit ```spoe```, eine mit ```oevp``` und eine mit ```fpoe```. Hier ist ebenfalls die Reihenfolge egal, aber ebenfalls die korrekte Bezeichnung in der Headerzeile der Datei wichtig. 
	- **Korrekte Partei-Bezeichnungen**
	- ```bzoe```
	- ```fpoe```
	- ```gruene```
	- ```kpoe```
	- ```neos```
	- ```oevp```
	- ```spoe```

**Beispiel**

| spatial_id     | eligible       | invalid | valid | spoe | oevp | fpoe |
|---------------|--------------|--------------|--------------|--------------|--------------|--------------|
| 101 | 345 | 4 | 341 | 181 | 152 | 12 |
| 102 | 412 | 5 | 407 | 31 | 188 | 188 |
| ... | ... | ... | ... | ... | ... | ... |



Unter [data/output/](data/output/) sind die konvertierten CSV-Dateien gespeichert.

