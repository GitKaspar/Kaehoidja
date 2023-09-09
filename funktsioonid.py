from math import ceil

import PySimpleGUI as sg

# Funktsioon avab akna, millel on joonis western blot membraanile ülekandmisest. 

def ülekanne():
    akna_kujundus = [[sg.Text('Membraanile ülekanne', font=('Helvetica', 18))],      
                 [sg.Image("Ülekanne.png")]]
    aken = sg.Window('Membraanile ülekanne', akna_kujundus, size=(530,275))   
    sündmused, väärtused = aken.read()    
    aken.close()
    
# Funktsioon avab akna, millel on joonis kokkupandud geeliraamist.

def geeliraam():
    akna_kujundus = [[sg.Text('Kokkupandud geeliraam', font=('Helvetica', 18))],      
                 [sg.Image("Raami_kokkupanek.png")]]
    aken = sg.Window('Geeliraami kokkupanek', akna_kujundus, size=(700,650))   
    sündmused, väärtused = aken.read()    
    aken.close()

# Funktsioon avab akna, millel on joonis western blot visualiseerimise põhimõttest. 

def antikeha():
    akna_kujundus = [[sg.Text('Kolorimeetriline reaktsioon', font=('Helvetica', 18))],      
                 [sg.Image("Antikeha.png")]]
    aken = sg.Window('Kolorimeetriline reaktsioon', akna_kujundus, size=(880,450))   
    sündmused, väärtused = aken.read()    
    aken.close()

# Funktsioon avab akna, millel on joonis Pageruler pikkusmarkerist.

def pikkusmarker():
    akna_kujundus = [[sg.Text('Pageruler pikkusmarker', font=('Helvetica', 18))],      
                 [sg.Image("Pikkusmarker.png")]]
    aken = sg.Window('Pageruler pikkusmarker', akna_kujundus, size=(320,700))   
    sündmused, väärtused = aken.read()
    aken.close()
    
# Funktsioon avab akna, millel on tutvustav tekst western blot proovide ettevalmistamisest.

def proovide_ettevalmistamine():
    akna_kujundus = [[sg.Text("Proovide ettevalmistus", font=('Helvetica', 18))],      
                    [sg.Text("Et valke oleks võimalik molekulaarmassi järgi analüüsida on esmalt vaja lõhkuda nende sekundaarstruktuur\n"
                              "Meie kasutame selleks DTT/laemmli puhvrit.\n"
                              "\n"
                              "DTT redutseerib väävlisildade moodustamiseks vajalikud -SH rühmad, destabiliseerides nii valkude sekundaarstruktuuri.\n"
                              "\n"
                              "Laemlli olulisemad komponendid on SDS, broomfenoolsinine ja glütserool.\n"
                              "\n"
                              "1. SDS lineariseerib valgud ja annab neile negatiivse laengu, mis võimaldab neid ainult molekulaarmassi alusel geelil jooksutada.\n"
                              "2. Broomfenoolsinine võimaldab jälgida proovi liikumist geelis.\n"
                              "3. Glütserool tagab oma suure tiheduse tõttu proovide vajumise aukude põhja.\n"
                              "\n"
                              "Kui puhvrid on lisatud, siis tuleb segu kuumutada 100 °C juures 10 min. Rakulüsaati säilta -20 °C juures.", font=('Helvetica', 12))]]
    aken = sg.Window('Membraanile ülekanne', akna_kujundus, size=(950,300))
    sündmused, väärtused = aken.read()    
    aken.close()

# Arvutab geelide arvu ja protsendi järgi vajaminevad kogused 5 ml lahutava geeli jaoks.

def running_gel(mitu, protsent):
    akrüülamiid = round(((mitu*5*protsent)/30),2)
    tris_8_8 = mitu*1.3
    SDS = mitu*0.05
    APS = mitu*0.05
    TEMED = 2*round((mitu*(0.011-(protsent*0.001))),4)
    MQ = round((mitu*5-(akrüülamiid+tris_8_8+SDS+APS+TEMED)),2)
    return (MQ,akrüülamiid,tris_8_8,SDS,APS,TEMED)

#Arvutab geelide arvu järgi vajaminevad kogused 2 ml kontsentreeriva geeli jaoks.

def stacking_gel(mitu):
    MQ = mitu*0.68
    akrüülamiid = mitu*0.17
    tris_8_8 = mitu*0.13
    SDS = mitu*0.01
    APS = mitu*0.01
    TEMED = mitu*0.001
    return (MQ,akrüülamiid,tris_8_8,SDS,APS,TEMED)

# Loeb failist juhise sisu.

def loe_failist(failinimi):
    fail = open(failinimi, encoding='utf-8')
    sisu = fail.read()
    fail.close()
    return sisu
