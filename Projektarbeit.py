from cProfile import label
from collections import Counter
from datetime import date
from lib2to3.pgen2.pgen import DFAState
from random import randint
from time import sleep
import streamlit as st
import pandas as pd
import os
import json
import datetime
import time
import altair as alt



st.title("Projektarbeit Programmieren 2") # Erstellen des Titels
st.header("Samir Rais sfb Dietikon 09.01.2023 ") # Erstellen des Untertitels



# Erstellen der Sidebar
sections = st.sidebar.radio("Auswahl", ("Begrüssung", "Lichtsteuerung", "Wetterdaten", "Wetterdaten Diagramm", "Heizungssteuerung", "Parkplatz", "Alarmanlage", "Gartenbewässerungsanlage"))


if sections == "Lichtsteuerung":
    


    st.write("Lichtsteuerung",)
    
    if st.button('EIN') and not st.button("AUS"): # Definieren was passiert wenn der Schalter Ein oder Ausgeschalten ist
     st.image('https://png.vector.me/files/images/1/5/156185/lightbulb_clip_art_preview.jpg')
    

    else:
     st.image('https://png.vector.me/files/images/1/0/101905/lightbulb_clip_art_preview.jpg')

    
     



elif sections == "Begrüssung":
    
    st.image("https://www.creativefabrica.com/wp-content/uploads/2019/09/24/Willkommen-1-580x386.jpg") # Hochladen eines Bild aus dem Netz








elif sections == "Wetterdaten":
    st.write("Wetterdaten Tabelle Jena 2009 - 2017")
    wetterdiagramm = pd.read_csv("/Users/samir/Desktop/SFB/Semester 3/Programmieren/jena_climate_2009_2016.csv", sep=";")
    
    
    
    
    st.table(wetterdiagramm)
    # Pfad von ordner.csv importieren der excel tabelle










elif sections == "Wetterdaten Diagramm":
    st.write("Wetterdaten Diagramm Jena 2009 - 2017")
    wetterdiagramm = pd.read_csv("/Users/samir/Desktop/SFB/Semester 3/Programmieren/jena_climate_2009_2016.csv", sep=";")
    

    

    st.line_chart(wetterdiagramm, x='Jahr', y='Temperatur')

    st.area_chart(wetterdiagramm, x='Jahr', y='Temperatur')

    

    
    





    

















elif sections == "Heizungssteuerung":
    st.write("Heizungssteuerung")
  

    
# Erstellen einer Checkbox
    Heizung_an = st.checkbox("Heizung einschalten")

# Erstellen eines Texts der als Kontrollanzeige dient ob die Heizung An oder Aus ist mit einem Bild
    if Heizung_an:
     st.text("Die Heizung ist eingeschaltet")
     st.image("https://www.co2online.de/fileadmin/co2/dossier/heizung/heizung-lucadp-Fotolia.jpg") 
    else:
     st.text("Die Heizung ist ausgeschaltet")
       












elif sections == "Parkplatz":
    st.write("Parkplatz")

    


   

# Definieren der Bilder mit dem Link aus dem Netz
    image_url_1_1 = "https://previews.123rf.com/images/rafaelbenari/rafaelbenari1708/rafaelbenari170800202/84076704-auto-parkplatz-sensoren-an-der-decke-kontrollleuchte-zeigen-parkplatz-unbesetzt-ist-gr%C3%BCn.jpg"
    image_url_1_2 = "https://www.stuttgarter-nachrichten.de/media.media.c6a8c007-efc5-46e1-918c-0ff636de5737.original1024.jpg"
    image_url_2_1 = "https://previews.123rf.com/images/rafaelbenari/rafaelbenari1708/rafaelbenari170800202/84076704-auto-parkplatz-sensoren-an-der-decke-kontrollleuchte-zeigen-parkplatz-unbesetzt-ist-gr%C3%BCn.jpg"
    image_url_2_2 = "https://www.stuttgarter-nachrichten.de/media.media.c6a8c007-efc5-46e1-918c-0ff636de5737.original1024.jpg"
    image_url_3_1 = "https://previews.123rf.com/images/rafaelbenari/rafaelbenari1708/rafaelbenari170800202/84076704-auto-parkplatz-sensoren-an-der-decke-kontrollleuchte-zeigen-parkplatz-unbesetzt-ist-gr%C3%BCn.jpg"
    image_url_3_2 = "https://www.stuttgarter-nachrichten.de/media.media.c6a8c007-efc5-46e1-918c-0ff636de5737.original1024.jpg"

    col1, col2, col3 = st.columns(3) #Erstellen von Columns damit es übersichtlich ist




# Die 3 columns

    with col1:
     if st.checkbox("Parkplatz 1") is True: # Die Checkboxen dienen als Sensor des Parkplatzes
      st.image(image_url_1_2)
     else:
      st.image(image_url_1_1)

    with col2:  
     if st.checkbox("Parkplatz 2") is True:
      st.image(image_url_2_2)
     else:
        st.image(image_url_2_1) 

    with col3:
     if st.checkbox("Parkplatz 3") is True:
      st.image(image_url_3_2)
     else:
      st.image(image_url_3_1)  


    

    

    











elif sections == "Alarmanlage":
    st.write("Alarmanlage") 

    
 


    video_url = 'https://www.youtube.com/watch?v=YYOQWw-4b0g'

# Variable für den Video
    video_shown = False

# Erstellen des Buttons Einbruch der ein Sensor der Alarmanlage ist
    button_breakin = st.button('Einbruch')

# Betätigung des Buttons Einbruch erscheint das Video von youtube
    if button_breakin:
      st.video(video_url)
      video_shown = True

# Erstellen des Buttons Sicherheit als Quittierung der Alarmanlage
    if video_shown:
     button_security = st.button('Sicherheit')

    # Wenn die Schaltfläche "Sicherheit" betätigt wird, entfernt sich das Video
     if button_security:
         st.write('')
         video_shown = False








elif sections == "Gartenbewässerungsanlage":
    st.write("Gartenbewässerungsanlage")

    # Definieren ob das Bild angezeigt wird oder nicht
    show_images = False

# Funktion, die die Bilder anzeigt und 1 Sekunde warten lässt, bevor das nächste Bild angezeigt wird
    def show_water_images():
       global show_images
       show_images = True
       for i in range(3):
        # URL des Bildes
         image_url = "https://www.mein-schoener-garten.de/sites/default/files/styles/achor_navigation_l/public/gartenbewaesserung-sprinkleranlage-3269262-blp-shutterstock-repina-valeriya.jpg?h=4a7d1ed4&itok=dIXsSWpX".format(i+1)
        # Anzeigen des Bildes. Die Bilder im Abstand Symbolisieren das Wasser
         st.image(image_url)
         time.sleep(1)

# Funktion, die die Bilder entfernt
    def hide_water_images():
     global show_images
     show_images = False
    # Entfernen aller Elemente im Sidebar und im Hauptbereich
     st.sidebar.empty()
     st.empty()

    st.title("Wasseranlage")

# Button der als Sensor zum Anzeigen der Bilder
    if st.button("Wasseranlage an"):
     show_water_images()

# Button der als Sensor gedacht ist zum Entfernen der Bilder
    if st.button("Wasseranlage aus"):
     hide_water_images()

# Wiederholte Anzeige der Bilder, solange show_images True ist
    while show_images:
     show_water_images()
    

    

        


 