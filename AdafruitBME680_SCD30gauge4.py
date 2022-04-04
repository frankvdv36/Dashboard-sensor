# https://github.com/adafruit/Adafruit_CircuitPython_BME680
# "/usr/local/lib/python3/ is het pad waar de Modules te vinden zijn"
# https://campus.datacamp.com/courses/ (intro python)   voor cursus 'array' en plot data
'''
Plotly update figures / update graph 
https://plotly.com/python/v3/file-options/
DIT PROGRAMMA ZET NAAST TEMP, HUM, PRES, CO2 OOK DE TRENT OP HET SCHERM!
'''
import time
import board
import adafruit_bme680
import numpy as np                # niet aanwezig > pip3 install numpy
import plotly.graph_objects as go # Plot, tekent de 4 gauges
#import chart_studio.plotly as py
import adafruit_scd30             # pip3 install adafruit-circuitpython-scd30
#from datetime import datetime    # from datetime import datetime
#import os                         # remove files
#import plotly.plotly as py       
'''
" De BME680 is aangesloten op 3.3V voeding en gebruikt de I2C pinnen"
" De gemeten warden worden eerst omgezet naar nieuwe variabelen"
" Daarna weggescherven naar een afzonderlijke file"
'''
 
# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25       # correctie huidige luchtdruk
temperature_offset = -1                   # correctie op de sensor in °C

########################################################################
#-----------------------------------------------------------------------

# Deze functie plaatst 4 gauges op het scherm met de waarden: temp, hum, pres, gas
# https://plotly.com/python/indicator/
fig = go.Figure()
def dashboard(temp, tempOld, hum, humOld, pres, presOld, co2, co2Old):
    print(temp, tempOld, hum, humOld, pres, presOld, co2, co2Old) 
    #fig = go.Figure()
    fig = go.Figure(go.Indicator(               # temperatuur
    #fig.add_trace(go.Indicator(
        #domain = {'x': [0, 1], 'y': [0, 1]},
        domain = {'row': 0, 'column': 0},
        value = temp,
        mode = "gauge+number+delta",
        #mode = "gauge+number",
        #title = {'text': "temperatuur"},
        title = {'text': "Temperatuur °C", 'font': {'size': 40}},
        delta = {'reference': tempOld},              # print trent, delta, het verschil met value
        #gauge = {'axis': {'range': [None, 50]},
        gauge = {'axis': {'range': [-20, 50]},
                 'bar': {'color': "slategray"}, # darkblue, blue, 
                 #'bgcolor': "lavender", # 'bgcolor': "white",
                 'borderwidth': 2,
                 'bordercolor': "gray",
                 'steps' : [
                     {'range': [-20, 0], 'color': "lightblue"},
                     {'range': [0, 30], 'color': "palegreen"},
                     {'range': [30, 40], 'color': "tomato"},
                     {'range': [40, 50], 'color': "red"}],
                 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 22}}))


    #fig = go.Figure(go.Indicator(
    fig.add_trace(go.Indicator(                 # Vochtigheid
        #domain = {'x': [0, 1], 'y': [0, 1]},
        domain = {'row': 1, 'column': 0},
        value = hum,
        mode = "gauge+number+delta",
        #mode = "gauge+number",
        #title = {'text': "temperatuur"},
        title = {'text': "Vochtigheid %", 'font': {'size': 40}},
        delta = {'reference': humOld},
        #gauge = {'axis': {'range': [None, 50]},
        gauge = {'axis': {'range': [0, 100]},
                 'bar': {'color': "slategray"}, # darkblue, blue, 
                 #'bgcolor': "lavender", # 'bgcolor': "white",
                 'borderwidth': 2,
                 'bordercolor': "gray",
                 'steps' : [
                     {'range': [0, 30], 'color': "lightblue"},
                     {'range': [30, 70], 'color': "palegreen"},
                     {'range': [70, 100], 'color': "tomato"}],
                 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 50}}))


    #fig = go.Figure(go.Indicator(
    fig.add_trace(go.Indicator(                 # Luchtdruk
        #domain = {'x': [0, 1], 'y': [0, 1]},
        domain = {'row': 0, 'column': 1},
        value = round(pres),                    # anders 1,013.5 met komma
        mode = "gauge+number+delta",
        #mode = "gauge+number",
        #title = {'text': "luchtdruk hPa"},
        title = {'text': "Luchtdruk hPa", 'font': {'size': 40}},
        delta = {'reference': presOld},
        #gauge = {'axis': {'range': [None, 50]},
        gauge = {'axis': {'range': [970, 1060]},
                 'bar': {'color': "slategray"}, # darkblue, blue, 
                 #'bgcolor': "lavender", # 'bgcolor': "white",
                 'borderwidth': 2,
                 'bordercolor': "gray",
                 'steps' : [
                     {'range': [970, 1000], 'color': "lightblue"},
                     {'range': [1000, 1030], 'color': "palegreen"},
                     {'range': [1030, 1060], 'color': "tomato"}],
                 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 1013}}))    
        
    #fig = go.Figure(go.Indicator(
    fig.add_trace(go.Indicator(                 # Luchtkwaliteit CO2
        #domain = {'x': [0, 1], 'y': [0, 1]},
        domain = {'row': 1, 'column': 1},
        value = co2,
        mode = "gauge+number+delta",
        #mode = "gauge+number",
        #title = {'text': "temperatuur"},
        title = {'text': "CO2 ppm", 'font': {'size': 40}},
        delta = {'reference': co2Old},
        #gauge = {'axis': {'range': [None, 50]},
        gauge = {'axis': {'range': [400, 1800]},
                 'bar': {'color': "slategray"}, # darkblue, blue, 
                 #'bgcolor': "lavender", # 'bgcolor': "white",
                 'borderwidth': 2,
                 'bordercolor': "gray",
                 'steps' : [
                     {'range': [400, 400], 'color': "lightblue"},
                     {'range': [400, 900], 'color': "palegreen"},
                     {'range': [900, 1200], 'color': "navajoWhite"},
                     {'range': [1200, 1500], 'color': "tomato"},
                     {'range': [1500, 1800], 'color': "red"}],
                 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 900}}))    

    fig.update_layout(
        grid = {'rows': 2, 'columns': 2, 'pattern': "independent"},
        template = {'data' : {'indicator': [{
            'title': {'text': "Temperatuur"},
            'mode' : "number+delta+gauge",
            'delta' : {'reference': 90}}]
                             }})

    fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"}) # achtergrond,
    #fig.write_html('first_figure.html', auto_open=True)
    fig.show()
    # https://plotly.com/python/v3/file-options/#new-to-plotly      Nog te testen !!!!!
    # https://stackoverflow.com/questions/63716543/plotly-how-to-update-redraw-a-plotly-express-figure-with-new-data
    
#-----------------------------------------------------------------------

# Deze functie leest 2 sensoren uit. BME680 (0x77) en SCD30 (0x62). 

def readSensor():
    i2c = board.I2C()               # uses board.SCL and board.SDA
    scd = adafruit_scd30.SCD30(i2c) # address is 0x62 Zie 'sudo i2cdetect -y'
    if scd.data_available:
        scdData = [round(scd.CO2,2), round(scd.temperature,2), round(scd.relative_humidity,2)]
        co2 = scdData[0]; temp2 = scdData[1]; hum2 = scdData[2]
        temp2 = temp2 -1.5          # correctie op de temperatuur
        print('CO2: ',co2); print('temp2: ',temp2); print('hum2: ',hum2)

    global now
    global mylist
    now = int( time.time() )        # neem tijd in time in s
    now = now * 1000                # moet in ms staan niet in sec. (of ns)
    
    temp = bme680.temperature       # 
    hum = bme680.relative_humidity  # address is 0x77 Zie 'sudo i2cdetect -y'   
    pres = bme680.pressure          # "Alle 4 zijn is een float"
    air = bme680.gas
    temp = round (temp,2); hum = round (hum,2); pres = round (pres,2); 
    air = round (air); now = round(now)
    mylist = [now, temp, hum, pres, air, co2, temp2, hum2]    
    print (mylist)
    return
    

#-----------------------------------------------------------------------    

# Deze functie schrijft een 1D array en zet ze op 'mylistx.txt' x= a,b,c,d,e
# https://www.tutorialspoint.com/python3/python_files_io.htm

def fileW(xyz, txt):             # wat tussen haakjes staat wordt lokaal gebruikt. 
                                 # mag een ander enaam zijn dan opdrachtregel fileW(np_pres)
    # Open a file
    ml = open(txt, "w")
    ml.write(str(xyz))
    # Close opend file
    ml.close()   

#-----------------------------------------------------------------------

# Deze functie leest de info uit een file + van string naar float omzetten
# https://www.tutorialspoint.com/python3/python_files_io.htm

def fileR(txt):
    global mylistfile
    # Open a file
    ml = open(txt, "r+")
    mylistfile = ml.read()   # tussen () pointer vanaf x lezen, leeg = auto (vanaf begin)
    # Close opened file
    ml.close()
    return(mylistfile)
    
#-----------------------------------------------------------------------
########################################################################
######################################################################## 

# Hoofdprogramma

# Declair variablen
now =0      # tijd en datum in 1 getal
temp =0     # BME680
hum = 0
pres =0
air =0 
press =0
co2 =0      # SCD30
temp2 =0
hum2 =0
tempOld =0
humOld =0
presOld =0
co2Old =0

# Create 2D np.array
np_myarray = np.zeros([1, 8])       # maak een 2D-array 1 row 8 cols en een np.array

# Geeft op toetsenbord het aantal metingen in.
x = 0
#n = 3
n = int(input("Enter aantal metingen: "))

while x < n :                       # Doe het gevaagde aantal metingen
    x = x + 1                       
    print(x,n)
    readSensor()
    #readBME680(now, temp, hum, pres, air)                    # Doe een meting en zet ze in een lijst
    #readSCD30(co2, temp2, hum2)                              # Doe een meting en zet ze in een lijst
    #mylist = [now, temp, hum, pres, air, co2, temp2, hum2]
    print('mylist: ',mylist)        # print de meting (now, temp, hum, pres, gas)
    np_myarray = np.insert(np_myarray, -1, np.array((mylist)), axis=0)   # voer een nieuwe array in 2D array (0 vooraan) (-1 achteraan), possitie laatste 0 in X-as
    print ("np_myarray 1:8 cols: "); print (np_myarray[:, 1:8])          # print 2D array(temp, hum, pres, gas, co2, temp2, hum2)
    print('-------------------------------------------------------------')
    time.sleep(3)      # aantal seconden

else:
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})          # converteert scientific to decimal met 6 cijfers na de komma
    np_now = (np_myarray[:,0])        # Slice an array
    np_temp = (np_myarray[:,1])       # selecteer een col uit array 
    np_hum = (np_myarray[:,2])        # https://www.w3schools.com/python/numpy/trypython.asp?filename=demo_numpy_array_slicing_2d
    np_pres = (np_myarray[:,3]) 
    np_gas = (np_myarray[:,4]) 
    np_co2 = (np_myarray[:,5])
    np_temp2 = (np_myarray[:,6])
    np_hum2 = (np_myarray[:,7])
    print ("np_now: ", np_now); print ("np_temp: ", np_temp)
    print ("np_hum: ", np_hum); print ("np_pres: ", np_pres)
    print ("np_gas: ", np_gas); print ("np_co2: ", np_co2); 
    print ("np_temp2: ", np_temp2); print ("np_hum2: ", np_hum2)
    print ("np_myarray: ", np_myarray); print(type(np_myarray))
    fileW(np_now, "mylista.txt") 
    fileW(np_temp, "mylistb.txt")     # schijf 1D array weg op file tussen haakjes
    fileW(np_hum, "mylistc.txt") 
    fileW(np_pres, "mylistd.txt") 
    fileW(np_gas, "myliste.txt")
    fileW(np_co2, "mylistf.txt")
    fileW(np_temp2, "mylistg.txt")
    fileW(np_hum2, "mylisth.txt") 
    fileW(np_myarray, "myarray.txt")
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

   
fileR("mylistf.txt")                  # lees file tussen haakjes
print ('mylistfile: ',mylistfile)     # print geselecteerde file               
tempOld = np_temp2[-2]; humOld = np_hum2[-2]; presOld = np_pres[-2]; co2Old = np_co2[-2]
dashboard(np_temp2[0], tempOld, np_hum2[0], humOld, np_pres[0], presOld, np_co2[0], co2Old) # Start dashboard
#dashboard(np_temp[1], tempOld, np_hum[1], humOld, np_pres[1], presOld, np_co2[1], co2Old) # Start dashboard
print('=============================================================')
print('einde')
