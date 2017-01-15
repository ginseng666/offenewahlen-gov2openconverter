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
- ```<parties>```: danach folgen spalte für spalte die Stimmen für die jeweiligen Parteien als Integer. Also wenn bei einer Wahl die drei Parteien SPÖ, ÖVP und FPÖ beteiligt waren, dann folgt eine Spalte mit ```spoe```, eine mit ```oevp``` und eine mit ```fpoe```. Die Reihenfolge ist dabei egal, es muss aber in der Headerzeile der Datei die korrekte Bezeichnung für die Partei verwendet werden. 
	- **Korrekte Partei-Bezeichnungen**
	- ```bzoe```
	- ```fpoe```
	- ```gruene```
	- ```kpoe```
	- ```neos```
	- ```oevp```
	- ```spoe```

