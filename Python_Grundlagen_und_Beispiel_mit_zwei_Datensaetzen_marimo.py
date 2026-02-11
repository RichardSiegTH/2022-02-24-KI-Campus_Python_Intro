import marimo

__generated_with = "0.19.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python Grundlagen
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wie bereits angekündigt, wird in diesem Kurs Python über Jupyter Notebooks genutzt. Sie können innerhalb dieses Kurses auf die zum Kurs gehörenden Notebooks zugreifen ohne hierfür ein Software installieren zu müssen. Klicken Sie dazu einfach jeweils auf den Link des Notebooks, welches sie öffnen wollen. Dieses öffnet sich dann in einem anderen Browserfenster.

    Schauen Sie sich erst einmal im Jupyter Notebook um. Sie können neue Zellen erstellen und den Typ der Zellen auswählen. Dabei können Sie zwischen Code und Markdown unterscheiden. Mit Markdown können Sie Text formatieren. Zum Beispiel können Sie ein Wort durch Umklammerung mit einem Sternchen *kursiv* schreiben. Mit zwei Sternchen wird der Text **fett**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Einfache Rechenoperationen
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Beginnen Sie mit einer einfachen Rechenoperation und addieren 10 und 5.
    Dazu geben Sie `10`, `+` und `5` ein und führen die Zelle mit `Shift` und `Enter` aus.
    Alternativ können Sie den Run-Button in der Menueleiste klicken.
    Super - wir haben eine Taschenrechner.
    """)
    return


@app.cell
def _():
    10 + 5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Auch andere Operationen wie Divison funktionieren. Zum Beispiel 3 geteilt durch 2.
    """)
    return


@app.cell
def _():
    3 / 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Die print-Funktion
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Jetzt soll eine erste Python-Funktion genutzt werden. Beginnen Sie mit der `print`-Funktion, die Werte ausgibt. Für den Funktionsaufruf müssen Sie den Funktionsnamen und eine öffnende und eine schließende Klammer schreiben. In die Klammer schreiben Sie ein sogennantes Argument, in dem Fall eine Zeichenkette, was durch Anführungszeichen anzeigt wird.
    """)
    return


@app.cell
def _():
    print("Hello World")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Variablen-Zuweisungen
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ein wichtiges Konzept beim Programmieren mit Python sind die sogenannten Variablen. Variablen können viele unterschiedlichste Dinge enthalten, beispielsweise Zahlen, Worte, Sätze, Bilder, Listen. Um eine Variable zu definieren wird zunächst der Name der Variable, dann ein Gleichheitszeichen und dann das geschrieben, was die Variable enthalten soll.  Betrachten Sie die folgenden Beispiele.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hier wird der Variablen number_of_plants der Wert 20 - eine Ganzzahl auch Integer - zugeordnent.
    """)
    return


@app.cell
def _():
    number_of_plants = 20
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Im nächsten Beipiel weisen Sie eine Zeichenkette zu. Diese werden wie vorhin gesagt durch Anführungszeichen ein- und ausgeleitet.
    """)
    return


@app.cell
def _():
    wise_sentence = "All generalisations are wrong."
    return (wise_sentence,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Listen
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Als nächstes schauen Sie sich einen weiteren Python-Datentyp an. Hierbei handelt es sich um eine Liste, die verschiedene Objekte zusammenfasst:
    """)
    return


@app.cell
def _():
    bag_of_things = [3, "sky", "unicorns", 6.23]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dictionaries
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ein weiterer häufig verwendeter Datentyp sind die Dictionaries in denen Schlüssel- und Werte-Paare gespeichert werden. Hier Beispielweise die Namen von Früchten und ihren Farben.
    """)
    return


@app.cell
def _():
    fruits_and_colors = {"banana": "yellow",
                         "strawberry": "red",
                         "blueberry": "blue"}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nutzung weiterer Funktionen und Methoden
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python beinhaltet viele vorgefertigte Befehle, um mit den Variablen zu hantieren. Hierbei unterscheiden sich sogenannte Funktionen von Methoden. Eine Funktion wird angewendet indem ihr Name geschrieben wird und dahinter in runden Klammern das Objekt, auf das die Funktion angewendet werden soll. Eine Methode ist ein spezielle Funktion die an eine bestimmtes Objekt - wie zum Beispiel eine Zeichenketten - geknüpft ist. Eine Methode wird angewendet, indem hinter das Objekt, ein Punkt und dann der Name für die Methode mit abschließenden runden Klammern geschrieben wird. Den Unterschied zeigt das folgende Beispiel.

    Hier nutzen Sie die Funktion len um die Länge einer Zeichenkette zu berechnen
    """)
    return


@app.cell
def _(wise_sentence):
    len(wise_sentence)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hier nutzen Sie die Methode `upper`, die alle Zeichenketten-Objekte besitzen um alle Zeichen der Zeichenkette großgeschrieben zurückgeben zu lassen.
    """)
    return


@app.cell
def _(wise_sentence):
    wise_sentence.upper()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Die vorherige Methode benötigt kein zusätzliche Argument. Jetzt werden Sie die Methode `count` nutzen um ein Zeichenkette in einer anderen zu suchen.
    Die Suchzeichenkette ist in diesem Falle ein "e".
    """)
    return


@app.cell
def _(wise_sentence):
    wise_sentence.count("e")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Jetzt werden Sie die Methode `replace` nutzen, die nicht nur ein sondern gleich zwei
    Argumente benötigt. Zuerst die Zeichenkette die ersetzt werden soll, und dann
    die Zeichenkette, die stattdessen eingefügt wird.
    """)
    return


@app.cell
def _(wise_sentence):
    wise_sentence.replace("wrong", "right")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Bisher haben Sie nur die Kern-Sprachelement von Python genutzt. Python bringt aber eine reichhaltige Sammlung an Erweiterungen mit sich.

    Hier nutzen Sie zum Beipsiel das Package `math`. Dieses laden Sie in das momentan genutzte Jupyter Notebook mit dem Keyword `import` und dem Namen des Packages.
    """)
    return


@app.cell
def _():
    import math

    return (math,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Das Package bring nun mathematische Konstanten und Operationen mit.
    Zum Beispiel die Zahl pi:
    """)
    return


@app.cell
def _(math):
    math.pi
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ... oder die mögliche die Möglichkeit den Cosinus zu berechnen.
    """)
    return


@app.cell
def _(math):
    math.cos(math.pi)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Luftqualität und Wetter-Daten kombinieren
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mit ihren grundlegenden Python-Fähigkeiten sollen Sie jetzt eine kleine Analyse von zwei Datensätzen durchführen.

    Hierbei nutzen Sie das populäre Package `panda`, das besonder zum einlesen und bearbeiten von tabelarischen Daten sinnvoll ist. Häufig werden hier Abkürzungen für die geladenen Packages vergeben. Für `panda` ist `pd` üblich.
    """)
    return


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Zu allererst nutzen Sie die Funktion `read_csv` aus `pandas`, was Sie mit pd abgekürzt haben
    um die Date `weather_cologne_selected.csv` einzulesen. In diesem Fall
    trennt der Punkt nicht Objekt von einer Methode ab, sondern den Package-Namen
    bzw. dessen Abkürzung von einer Funktion.
    """)
    return


@app.cell
def _(pd):
    weather = pd.read_csv("weather_cologne_selected.csv")
    return (weather,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Die Funktion gibt eine Datenstruktur, die DataFrame genannt wird, zurück, die Sie in
    der Variablen `weather` ablegen. Diese können Sie sich jetzt anzeigen lassen. Dabei
    werden nur die ersten 5 und letzten 5 Zeilen dargestellt.
    """)
    return


@app.cell
def _(weather):
    weather
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mit der Methode describe können Sie sich für alle numerischen Spalten - in diesem Fall `tmin` für die Minimaltemperatur und `tmax` für die Maximaltemperatur -  statistische Kennziffern wie den Mittelwert (`mean`), die Standardabweichtung (`std`) u.ä.  anzeigen lassen.
    """)
    return


@app.cell
def _(weather):
    weather.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mit pandas können Sie sogar Graphiken erzeugen. Hier können Sie zum Beispiel den Zusammenhang von der Minimal- und Maximaltemperatur eines Tages durch ein Streudiagramm visualisieren.
    """)
    return


@app.cell
def _(weather):
    fig = weather.plot.scatter(x="tmin", y="tmax")
    fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nun soll ein zweiter Datensatz zur Luftqualität hinzugefügt werden. Auch hier nutzen Sie die Funktion `read_cs` von `panda` um die Daten aus der Datei `air_qualities_cologne.csv` einzulesen.
    """)
    return


@app.cell
def _(pd):
    air_quality = pd.read_csv("air_qualities_cologne.csv")
    return (air_quality,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Schauen Sie sich den Inhalt des Dataframes an. Hier sind neben Datum und Uhrzeiten unter anderen Feinstaub- und Ozonwerte zu finden.
    """)
    return


@app.cell
def _(air_quality):
    air_quality
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Auch hier können Sie sich für die numerischen Spalten die statistischen Kennzahlen anzeigen lassen.
    """)
    return


@app.cell
def _(air_quality):
    air_quality.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Einzelne Spalten, in pandas Series genannt, können durch eckige Klammern und den Spaltennamen angesprochen werden. Hier am Beispiel der Feinstaubspalte.
    """)
    return


@app.cell
def _(air_quality):
    air_quality["Feinstaub"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Einzelne Spalten besitzen eine Methode names `hist`, mit der die Verteilung der Werte als Histogramm dargestellt werden können. Dabei wird der Wertebereich alle Werte in der Spalte in 10 gleich große Bereiche aufgeteilt. Es wird dann gezählt wie viele der Werte in den jeweiligen Bereich fallen und dies als Balkenlänge dargestellt.
    """)
    return


@app.cell
def _(air_quality):
    fig_2 = air_quality["Feinstaub"].hist()
    fig_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Als letzte werden die beiden DataFrames an Hand einer gemeinsamen Spalte, hier die Datums-Spalte, zusammengefügt. Dabei ist zu beachten, dass der DataFrame mit den Luftqualitätsdaten sehr viel mehr Einträge besitzt als der Temperatur-DataFrame.

    Hierzu nutzen Sie die Methode `merge` des DataFrames `air_quality` und übergeben den anderen DataFrame weather als erstes Argument. Als sogenannte Keyword-Argumente geben Sie die Namen der beiden Spalten mit. `left_on` mit dem Spaltennamen  im `air_quality`-DataFrame und `right_on` mit dem Spaltennamen im `weather`-DataFrame.
    """)
    return


@app.cell
def _(air_quality, weather):
    air_quality_and_weather = air_quality.merge(weather, left_on="Datum", right_on="date")
    return (air_quality_and_weather,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Das Ergebnis speichern Sie in der Variable `air_quality_and_weather`. Schauen Sie sich das Ergebnis einmal an.
    """)
    return


@app.cell
def _(air_quality_and_weather):
    air_quality_and_weather
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Jetzt können Sie Wert beider Datensätze in Zusammenhang bringen. Ist bei hoher Temperatur, der Feinstaubgehalt hoch? Dies scheint nicht der Fall zu sein.
    """)
    return


@app.cell
def _(air_quality_and_weather):
    fig_3 = air_quality_and_weather.plot.scatter(x="Feinstaub", y="tmin")
    fig_3
    return


if __name__ == "__main__":
    app.run()
