# Dashboard-sensor
## Beschrijving
Het project zal via externe sensoren temperatuur, luchtvochtigheid, luchtdruk en CO2 meten en deze zichtbaar maken.
Het zichtbaar maken gebeurt grafisch zodat een 4-tal wijzers de waarden weergeven.
Intussen wordt voor later gebruik iedere x seconden de meting in een 2D array opgeslagen samen met een tijd.

## Bronnen
https://plotly.com/python/gauge-charts/
Deze site heeft de basis weer hoe een wijzer de gelezen waarde kan zichtbaar maken. De figuur is eenvoudig aan te passen voor eigen gebruik.


## Hardware
Voor dit project gebruiken we een BME680 (temperatuur, vochtigheid en luchtdruk) van Bosch en de SCD30 een CO2 meter met temperatur en vochtigheid. 
Beide worden via de I2C-bus uitgelezen.
 
## Software
De BME680 en de SCD30 sensoren worden via de I2C-bus aangesloten.
Beide sensoren worden geregeld uitgelezen en hun data opgeslagen in een file. Hiervoor maken we telkens gebruik van een array. Zo bekomen we een 2D array.
Deze data kan later uitgelezen worden om eventueel grafieken te maken. Voor dit project worden enkel wijzers gebruikt om de huidige waarden zichbaar te maken.
Om de data mooi voor te stellen wordt gebuik gemaakt van de PLOTLY libary. https://plotly.com/python/gauge-charts/
Een combinatie van 4 wijzers worden gebruikt om de volgende gegevens zichtbaar te maken: temperatuur, vochtigheid, luchtdruk en CO2.
Dit wordt zichtbaar gemaakt via een browser. Iedere update moet gebeuren op een afzonderlijke pagina. Hiervoor is nog geen oplossing gevonden.

### Eigen scripts en programma's
Zie in bijlage.
