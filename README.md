# Dashboard-sensor
## Beschrijving
Het project zal via externe sensoren temperatuur, luchtvochtigheid, luchtdruk en CO2 meten en deze zichtbaar maken.
Het zichtbaar maken gebeurt grafisch een 4-tal wijzers geven de de waarden weer.
Intussen wordt voor later gebruik iedere x seconden de meting in een 2D array opgeslagen samen met een tijdsstempel.

## Bronnen
https://plotly.com/python/gauge-charts/
Deze site heeft de basis weer hoe een wijzer een gelezen waarde kan zichtbaar maken. De figuur is eenvoudig aan te passen voor eigen gebruik.

## Hardware
Voor dit project gebruiken we een BME680 (temperatuur, vochtigheid en luchtdruk) van Bosch en de SCD30 een CO2 meter met temperatur en vochtigheid. 
Beide worden via de I2C-bus uitgelezen.
 
## Software
De BME680 en de SCD30 sensoren worden via de I2C-bus aangesloten.
https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython en
https://pypi.org/project/adafruit-circuitpython-scd30/
Bij het opstarten wordt eerst gevraagd hoeveel metingen er moeten gebeuren. 
Beide sensoren worden dan een x-aantal keer uitgelezen en hun data opgeslagen in een file. Hiervoor maken we telkens gebruik van een array. 
Zo bekomen we een 2D array of een array in een array. Deze data kan later uitgelezen worden om eventueel grafieken te maken. 
Voor dit project worden wijzers gebruikt om de huidige waarden zichbaar te maken.
Om de data mooi voor te stellen wordt gebuik gemaakt van de PLOTLY libary. https://plotly.com/python/gauge-charts/
Een combinatie van 4 wijzers worden gebruikt om de volgende gegevens zichtbaar te maken: temperatuur, vochtigheid, luchtdruk en CO2.
Dit wordt zichtbaar gemaakt via een browser. Iedere update moet gebeuren op een afzonderlijke pagina. 
Nadeel is dat op den duur vele pagina's openstaan. Een live update gaat nog niet hiervoor is nog geen oplossing gevonden.

### Eigen scripts en programma's
Zie in bijlage.
