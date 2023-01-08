# Projektarbeit_GP2

Anforderungsliste der Projektarbeit GP 2
                         Samir Rais sfb Dietikon

In dieser Anforderungsliste wird Schrittweisse erklärt, wie die verschiedenen Funktionen auf der Streamlit Visualisierung funktionieren. Nach dem Öffnen meines erstellten Codes auf Streamlit, startet gleich die Begrüssung als erste Sidebar. Die danach folgenden Sidebars werden einzeln aufgelistet und erklärt.

Lichtsteuerung: Die Lichtsteuerung beinhalten eine Lampe, die mittels Schalter ein und wieder ausgeschalten werden kann. Beim Bedienen ändert sich auch das Bild.

Wetterdaten: Hier werden  die Wetterdaten von Jena zwischen 2009 und 2016 über kaggle als Excel-Datei heruntergeladen. Die Excel-Datei musste angepasst werden da es zu viele Daten sind. Jetz sind nur noch die jeweiligen Jahre und Temperaturen ersichtlich, was dies einiges Übersichtlicher macht.

Wetterdaten Diagramm:  Es werden wieder die gleichen Daten, jedoch in Form zwei verschiedener Diagramme dargestellt.

Heizungssteuerung: Die Heizung wird mittels Checkbox ein und ausgeschalten. Im jeweiligen Zustand ist ein Text zu lesen, ob die Heizung ein oder ausgeschalten ist. Der Text dient zur Kontrollanzeige.

Parkplatz: Hier werden wieder Checkboxen verwendet die als Sensor der Parkplätze funktionieren. Ist die Checkbox leer, sieht man das Bild einer grünen Ampel, umgekehrt sieht man das Bild einer Roten.

Alarmanlage: Bei der Alarmanlage simuliert ein Button den Alarmsensor. Wenn jemand einbricht, erscheint ein Video aus Youtube mit einer Polizeisirene. Mit dem Button Sicherheit kann man den Alarm Quittieren.

Gartenbewässerungsanlage: Die Gartenbewässerungsanlage läuft über eine Zeitschaltuhr, diese wird als Button dargestellt. Wenn sie eingeschalten ist, erscheint jede Sekunde ein Bild eines Sprinklers. Der Abstand der Bilder die schnell auf Streamlit erscheinen symbolisieren den Sprinkler.
