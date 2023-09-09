import PySimpleGUI as sg
import random
import winsound
from stopper import *
from funktsioonid import *

sg.theme('DarkTeal12')

# Piltide kasutamiseks nuppude asemel tahab PysimpleGui, et need oleks teisendatud 64 bitiseks. Allolevasse muutujasse on säilitaud 64 bitine luubi kujutis.

luup = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAFkElEQVR4Xu2XW0wcVRjHv529sCy7SwuUllZAoMU0LAlFWLAJDwia7YYCvWiv2MTQ9MFofNHSujT0prb6ojEmwluLPLRxW31QXprGEKtIaZq0dltrWaw0igtycVn2NjP+vymz2YaFXvahL57kl3PYMzPf//y/75wZNLIs09NsAj3lplMHO3fupPgmSRJFo1ESBGF5enp6gcFgsIbD4empqSkv5kZ1Oh3mnlx/T0/Pwg6IosjBLfn5+S319fWfNjc3f75ly5ZPuOe/8/LyWnge1yXvQKLger2+srGxsaOiosJpMplIo9EQN+7XodXW1r7a39//bW9vb0ckEhnQarXJ10B88N27d3fX1NQ4MSbGaDRSSkoKjxURLKqurs65a9eubhabjBNCfM4hwOpwOA6vXbu2mMVkZmZSamoq8Qo53wznnoXw9WVlZcW4/gjfl7QAWKlBbpsqKys3hEIhysrK4sCq9Ryc+xgsgkXa7XYH7mtGTSQnACtbYbPZNqEnq9WqBEBTV55QBAs0m81UUlLCAp5oS2g7OjqUwYULF8qrqqpa8MDs+NWrxBdi/G+8cjgmXr9+3Y0Jvzr/MLCrHnSA9zkKzYghB1etTugA+hh8khrRINiU1DbkQwYrCaK4+KEcQC1ONRU8VoPGfudxEA31EEhKwMTExO2RkZHbOHxsfr+fsrOzuTDjA8ZEqC5BsDK+d2/kN4z/NsBAWV4gBRpFLZASC0Au/7px48bX69ev3+Tz+SgjI4ODcKUv6EAgEMB9YtjjuekWdAYpRZBo8RJA+gwm7ucLQNXLw8PD5wYHB7dXV1c77ty5Q6tXr1a3GweMFSA7Mz4+Tjqtjot3qP/ylfPrcgy0YdUMQVpCF2RJJG2qmQp3fMz9fAGwl22dxvF6CLugsKioqNjj8SipsFgsHFwRwunBC4m4Xj3XrtDNH78rDgVm2sxR/3tLDFoKRBBckOYLIAjQynyKQkDaPAHxeR04ffp0i9PpPFxeXu6YnJyksbExFhA7CblduvTD+e7uL8cKl8itdbblB1cK4/awJJ9B6C5K5ABs18h030mw4PcAArDFP7vd7m1dXV17+vr6zt69e/fq6OjoraGhoasXL14829nZueerc+dbnrVE95rFyS57xjSV5ejqZUHfCaGupN6GqhNgGoFPeb3eUzgjlkGYCYUawHb1Cch9mkGgpmdmySRQb0QK7Q1HlHvYoaO4jgv12GMJQEXHu8DEW+5Td4PyIoLFoWCAIqFZihj1bph6AgWyX+Z7IQLcF0F07JHfBU1NTYxyRJaWlvLJyMUXE8fAXuXsX5JuJcfGzbT0uRdIjIRJCs+2EdEJCSI5MC5UnNAQuR5bQENDA7W2tpLL5WJ4zL/Ffm9vb6e2tv20cWMjFWx2Uf4rx8lcWEmSGG4Tw7MfsghxnojHTAFWyqvnPLIb/BWkHlYK3IKzfL0GwSvIXFBOfu8VGhtwH/B7B+FKsI2Mafdraa4miNOR4As89lmOY5ieuPEW1Rv5tFGE+H46c/zfoYGDepNVqQmOEJ6ZelNnzvxszetfkABxq1bmxDmwOJo4tECIG3PPZzPXAb8+ZUuRXUzLLT30xzcfGCc9378NJwQSwzKcMmVVbSMhFc6KkYf+X6AFRmAFWSAXrAE2YAe1wAm2gtfAPvAWhLwjhmZcJAhHc5sOBDIrm2+J0QhZbS9fztt65Lal8PkyBOdnLipAA3RzAswgHSwFmWAZWA5ywCqQDwpAMSgFFaBGFqMNMGd7zov7Ugt2nPwn56U3ViBJJ8VQ4F3MlwDNYgJkEAVB4AdTYAKMAx8YBX+Ce+B34AW/gmvgMugDvbIkutH3pOXaTiI178tSdD/mPgK/ABksWgPiHMFHqYH4N/4cEhCRkogUDS/6tfr/P6dPXcB/hV+WxtPEgeoAAAAASUVORK5CYIIxNDgx'

# Sõnastik on vajalik selleks, et märkida Western blot protokollis juba varem avatud lehed - avamata ja praegu käimasoleva lehe väärtus on True, suletud lehe väärtus False. Siin vastab võti 1 lehekülg ühele, võti 2 lehekülg kahele jne. Süsteem vajalik selleks, et tsükli lõpetamisel ei minda tagasi vana tsükli juurde.

lehtede_indeksid = {1:True,2:True ,3:False,4:False,5:False,6:False,7:False, 8:False, 9:False,10:False}

# Western blot programmis valitakse korduvalt allolevast järjendist sõne, mis kasutajale kuvatakse.

kiitused = ["Fantastiline", "Vau!", "Ma teadsin, et suudad seda!", "Tubli, jätkakem"]

# Programm loeb failidest juhendid Kaspari programmilõigu jaoks (loe_failist funtksioon failis "funktsioonid.py")

programmi_tutvustus = loe_failist('programmi_tutvustus.txt')
tutvustus = loe_failist('tutvustus.txt')
koostisosad = loe_failist('koostisosad.txt')
tükeldamine = loe_failist('tükeldamine.txt')
potti = loe_failist('potti.txt')
keema = loe_failist('keema.txt')
keemiseks = loe_failist('keemiseks.txt')
äädikas = loe_failist('äädikas.txt')
pärast_keetmist = loe_failist('pärast_keetmist.txt')
kuumuta_purke = loe_failist('kuumuta_purke.txt')
pärast_kuumutamist = loe_failist('pärast_kuumutamist.txt')
lõpp = loe_failist('lõpp.txt')

# Muutujad, mida kasutatakse Kaspari edenemisribade puhul.

aeg1 = 3600
aeg2 = 600

# Esimene aken, mis annab kasutajal võimaluse valida retsepti või laboriprotokolli vahel.

akna_kujundus = [[sg.Text("Käehoidja", text_color='white', font=('Helvetica', 15))],
                 [sg.Text(programmi_tutvustus, font=('Helvetica', 11))],
[sg.Submit("Letšo valmistamise juhend"), sg.Submit("Western blot protokoll")]]

aken_1 = sg.Window('Käehoidja', akna_kujundus, size=(340,250))

while lehtede_indeksid[1] == True:
    sündmus, väärtused = aken_1.read()
    if sündmus == sg.WIN_CLOSED:
        lehtede_indeksid[1] = False
        aken_1.close()
    if sündmus == "Western blot protokoll":
        lehtede_indeksid[1] = False
        aken_1.close()
        
        # Western blot protokolli akna kujunduse loomine
        
        akna_kujundus = [[sg.Text("Sisukord", text_color='white', font=('Helvetica', 18))],
        [sg.Button("1. Sissejuhatus", font=('Helvetica', 11))],
        [sg.Button("2. Lahutava geeli valmistamine", font=('Helvetica', 11))],
        [sg.Button("3. Kontsentreeriva geeli valmistamine", font=('Helvetica', 11))],
        [sg.Button("4. Geeli jooksutamine",font=('Helvetica', 11))],
        [sg.Button("5. Valkude membraanile kandmine", font=('Helvetica', 11))],
        [sg.Button("6. Primaarsete antikehadega inkubeerimine", font=('Helvetica', 11))],
        [sg.Button("7. Sekundaarsete antikehadega inkubeerimine", font=('Helvetica', 11))],
        [sg.Button("8. Visualiseerimine", font=('Helvetica', 11))]]
        
# Western blot protokolli 1. akna avamine        
        
        aken_2 = sg.Window('Retseptid ja labori protokollid', akna_kujundus, size=(400,325))
        
        while lehtede_indeksid[2] == True:
            
# Kasutaja sisendi lugemine            
            
            sündmus, väärtused = aken_2.read() 
            if sündmus == sg.WIN_CLOSED:
                lehtede_indeksid[2] = False
                aken_2.close()
                
#Kui kasutaja vajutab vastavale nuppule, siis muudetakse lehekülje indeksi väärtus tõeseks, mis võimaldab minna sellese tsüklisse, kus leht asub.                
                
            if sündmus == "1. Sissejuhatus": 
                lehtede_indeksid[3] = True 
                aken_2.close()
            if sündmus == "2. Lahutava geeli valmistamine":
                lehtede_indeksid[4] = True
                aken_2.close()
            if sündmus == "3. Kontsentreeriva geeli valmistamine":
                lehtede_indeksid[5] = True
                aken_2.close()
            if sündmus == "4. Geeli jooksutamine":
                lehtede_indeksid[6] = True
                aken_2.close()
            if sündmus == "5. Valkude membraanile kandmine":
                lehtede_indeksid[7] = True
                aken_2.close()
            if sündmus == "6. Primaarsete antikehadega inkubeerimine":
                lehtede_indeksid[8] = True
                aken_2.close()
            if sündmus == "7. Sekundaarsete antikehadega inkubeerimine":
                lehtede_indeksid[9] = True
                aken_2.close()
            if sündmus == "8. Visualiseerimine":
                lehtede_indeksid[10] = True
                aken_2.close()
            
        akna_kujundus = [[sg.Text("Western blot", text_color='white', font=('Helvetica', 15))],
                         [sg.Text("Tervist! See programm juhatab sind läbi ühest valgubioloogia enim kasutust leiduvast meetodist Western blot. \n"
                                  "Meetodiga on võimalik tuvastada proovist sind huvitava valgu olemasolu ja hinnata selle molekulaarmassi ning kontsetratsiooni.\n", font=('Helvetica', 11))],
                         [sg.Text("Kas oled valmis meetodiga alustama?", font=('Helvetica', 11), key = "tekst_1"), sg.Button("Jah", key = "nupp_1", visible = True), sg.Button("Ei", key = "nupp_2", visible = True)],
                         [sg.Text(key = "kiitus_1", font=('Helvetica', 11))],
                         [sg.Text("Esimese asjana on vaja sul vaja otsida geeli valamiseks vajalikud osad, milleks on: \n"
                                  "\n"
                                  "1. Eesmine ja tagumine klaas \n"
                                  "2. Tihend \n"
                                  "3. Hambad \n"
                                  "4. Klaaside hoidja \n"
                                  "5. Klaasihoidja hoidja :)", visible = False, key = "tekst_2", font=('Helvetica', 11))],
                          [sg.Text("Kas oled leidnud asjad", key = "tekst_3", visible = False, font=('Helvetica', 11)), sg.Button("Leidsin", key = "nupp_3", visible = False), sg.Button("Ei leidnud", key = "nupp_4", visible = False)],
                          [sg.Text(key = "kiitus_2", font=('Helvetica', 11))],
                          [sg.Text("Nüüd pane need omavahel kokku. Lõpptulemus on nähtav nuppust avanevalt jooniselt.", key = "tekst_4", visible = False, font=('Helvetica', 11)),sg.Button("", image_data = luup, button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key = "nupp_5", visible = False)],
                          [sg.Button("->")]]
        aken_3 = sg.Window('Western-blot', akna_kujundus, size=(850,420))
        while lehtede_indeksid[3] == True:
            sündmus, väärtused = aken_3.read()
            if sündmus == sg.WIN_CLOSED:
                lehtede_indeksid[3] = False
                break
            
            if sündmus == "nupp_2":
                
# Kui kasutaja vajutab "nupp_2" peale (programmis nupp "Ei"), siis kuvab kasutajale alloleva sõne.
                
                aken_3["kiitus_1"].Update("Aga nüüd?")
                
# Kui kasutaja vajutab "nupp_1" peale (programmis nupp "Jah"), siis läheb programm edasi ja kuvab kasutajale kiituse.
            
            if sündmus == "nupp_1": 
                aken_3["kiitus_1"].Update(random.choice(kiitused))
                aken_3["tekst_1"].Update(visible = False)
                aken_3["nupp_1"].Update(visible = False)
                aken_3["nupp_2"].Update(visible = False)
                aken_3["tekst_2"].Update(visible = True)
                aken_3["tekst_3"].Update(visible = True)
                aken_3["nupp_3"].Update(visible = True)
                aken_3["nupp_4"].Update(visible = True)
            if sündmus == "nupp_4":
                aken_3["kiitus_2"].Update("Aga nüüd?")
            if sündmus == "nupp_3":
                aken_3["kiitus_2"].Update(random.choice(kiitused))
                aken_3["tekst_3"].Update(visible = False)
                aken_3["nupp_3"].Update(visible = False)
                aken_3["nupp_4"].Update(visible = False)
                aken_3["tekst_4"].Update(visible = True )
                aken_3["nupp_5"].Update(visible = True)
            if sündmus == "nupp_5":
                geeliraam()
            
# "->" nuppu vajutamisel muudetakse praeguse lehekülje indeks vääraks (ei luba uuesti tsüklisse minna) ja järgmise lehekülje indeksi tõeseks (lubab edasi minna).
            
            if sündmus == "->":   
                lehtede_indeksid[3] = False
                lehtede_indeksid[4] = True
                aken_3.close()
                
        akna_kujundus = [[sg.Text("Lahutava geeli valmistamine ja valamine", text_color='white', font=('Helvetica', 15))],
                         [sg.Text("Western blot kasutab polüakrüülamiid geeli, mis koosneb kontsentreerivast ja lahutavast osast. ",font=('Helvetica', 11))],
                         [sg.Text("Esmalt valame lahutava osa, milles toimub valkude omavaheline lahutamine elektriväljas, kusjuures suurema molekulaarmassiga valgud liiguvad geelis aeglasemalt.\n"
                                  "Tüüpiliselt kulub seda ühe geeli valmistamiseks umbes 5 ml.\n \n"
                                  "Reagentide koguste saamiseks sisesta geelide arv ja nende %.", font=('Helvetica', 11))],
                         [sg.Text("Geeli protsent: ", font=('Helvetica', 11)), sg.InputCombo((6,8,10,12,15), size=(2,1), key = "sisend_1")],
                         [sg.Text("Geelide arv: ",font=('Helvetica', 11)), sg.InputCombo((1,2,3,4,5,6),key = "sisend_2")],
                         [sg.Submit("Arvuta",font=('Helvetica', 11))],
                         [sg.Text(key="tekst_1",font=('Helvetica', 11))],
                         [sg.Text(key = "MQ",font=('Helvetica', 11))],
                         [sg.Text(key = "Akrüülamiid",font=('Helvetica',11))],
                         [sg.Text(key = "Tris",font=('Helvetica', 11))],
                         [sg.Text(key = "SDS",font=('Helvetica', 11))],
                         [sg.Text(key = "APS",font=('Helvetica', 11))],
                         [sg.Text(key = "Temed",font=('Helvetica', 11))],
                         [sg.Text("Kõik vajalik olemas?", visible = False, key = "tekst_2",font=('Helvetica', 11)), sg.Button("Jah", visible = False, key = "nupp_1"), sg.Button("Ei", visible = False, key = "nupp_2")],
                         [sg.Text(key = "kiitus_1", font=('Helvetica', 11))],
                         [sg.Text("Kui oled veendunud, et kõik asjad on olemas, siis võid need kokku segada. NB! Viimasena lisa alati TEMED, kuna see alustab polümerisatsiooni reaktsiooni.\n"
                                  "Kindlasti vortexi ka segu läbi!", visible=False, key = "tekst_3",font=('Helvetica', 11))],
                         [sg.Text("Kõik kokku segatud?", visible=False, key = "tekst_4", font=('Helvetica', 11)), sg.Button("Jah", visible = False, key = "nupp_3"), sg.Button("Ei", visible = False, key = "nupp_4")],
                         [sg.Text(key = "kiitus_2", font=('Helvetica', 11))],
                         [sg.Text("Järgnevalt pipeteeri geel kiiresti 1 ml kaupa geeliraami \n \n"
                                  "Kui see tehtud siis pipeteeri geeli peale MQ vett, kuniks mullid on kadunud.", visible=False, key = "tekst_5",font=('Helvetica', 11))],
                         [sg.Button("Valatud?", visible = False)],
                         [sg.Text("Nüüd tuleb oodata c. 45 min - selleks võid kasutada programmi stopperit.", visible = False, key = "tekst_6", font=('Helvetica', 11))],
                         [sg.Button("Stopper", visible=False), sg.Button("->")]]
        aken_4 = sg.Window('Lahutava geeli valmistamine ja valamine', akna_kujundus, size=(1100,750))
        while lehtede_indeksid[4] == True:
            sündmus, väärtused = aken_4.read()
            if sündmus == sg.WIN_CLOSED or sündmus == 'Sulge':
                lehtede_indeksid[4] = False
                break
            if sündmus == "Arvuta":
                
# Kui kasutaja sisestab täisarvulised väärtused, siis kuvab programm funktsiooni running_gel arvutatud väärtused.                
                
                try:                     
                    tabel_1 = running_gel(int(väärtused["sisend_2"]),int(väärtused["sisend_1"]))
                    aken_4["tekst_1"].update("Lahutava geeli jaoks on vaja:")
                    aken_4["MQ"].update(f"- {round(tabel_1[0],4)} ml MilliQ-d.")
                    aken_4["Akrüülamiid"].update(f"- {round(tabel_1[1],4)} ml 30% Bis-akrüülamiidi.")
                    aken_4["Tris"].update(f"- {round(tabel_1[2],4)} ml 1 M Tris-Cl-i (pH 6.8).")
                    aken_4["SDS"].update(f"- {round(tabel_1[3],4)} ml SDS-i.")
                    aken_4["APS"].update(f"- {round(tabel_1[4],4)} ml 10% ammooniaakpersulfaati.")
                    aken_4["Temed"].update(f"- {round(tabel_1[5],4)} ml TEMED-it.")
                    aken_4["tekst_2"].Update(visible = True)
                    aken_4["nupp_1"].Update(visible = True)
                    aken_4["nupp_2"].Update(visible = True)
                except:
                    continue
            if sündmus == "nupp_2":
                aken_3["kiitus_1"].Update("Aga nüüd?")
            if sündmus == "nupp_1":
                aken_4["kiitus_1"].Update(random.choice(kiitused))
                aken_4["tekst_2"].Update(visible = False)
                aken_4["tekst_3"].Update(visible = True)
                aken_4["tekst_4"].Update(visible = True)
                aken_4["nupp_1"].Update(visible = False)
                aken_4["nupp_2"].Update(visible = False)
                aken_4["nupp_3"].Update(visible = True)
                aken_4["nupp_4"].Update(visible = True)
            if sündmus == "nupp_4":
                aken_4["kiitus_2"].Update("Aga nüüd?")
            if sündmus == "nupp_3":
                aken_4["kiitus_2"].Update(random.choice(kiitused))
                aken_4["nupp_3"].Update(visible = False)
                aken_4["nupp_4"].Update(visible = False)
                aken_4["tekst_4"].Update(visible = False)
                aken_4["tekst_5"].Update(visible = True)
                aken_4["Valatud?"].Update(visible = True)
            if sündmus == "Valatud?":
                aken_4["Valatud?"].Update(visible = False)
                aken_4["tekst_6"].Update(visible = True)
                aken_4["Stopper"].Update(visible = True)
                
# Stopperi nuppu vajutamisel avab funktsiooni stopper                
                
            if sündmus == "Stopper": 
                stopperi_aken(2700)
            if sündmus == "->":
                lehtede_indeksid[4] = False
                lehtede_indeksid[5] = True
                aken_4.close()
                
        akna_kujundus = [[sg.Text("Kontsentreeriv geel", text_color='white', font=('Helvetica', 15))],
                         [sg.Text("Peale lahutava geeli tardumist vala ära MQ. Seejärel saad segada kokku kontsentreeriva geeli, milles toimub valkude koondumine.\n"
                                  "See tagab selle, et enne lahutavasse geeli minekul on kõigil valkudel ühine stardipunkt, mis võimaldab hinnata valkude molekulaarmassi.\n\n"
                                  "Tüüpilselt kulub seda ühe geeli kohta 1 ml, kuid igaks juhuks valmistatakse tavaliselt seda 2 ml.\n"
                                  "Koguste saamiseks sisesta palun geelide arv",font=('Helvetica', 11))], 
                         [sg.Text("Geelide arv: ",font=('Helvetica', 11)), sg.InputCombo((1,2,3,4,5), size=(2,1), key = "sisend_1"),sg.Submit("Arvuta")],
                         [sg.Text(key="tekst_1",font=('Helvetica', 11))],
                         [sg.Text(key = "MQ",font=('Helvetica', 11))],
                         [sg.Text(key = "Akrüülamiid",font=('Helvetica',11))],
                         [sg.Text(key = "Tris",font=('Helvetica', 11))],
                         [sg.Text(key = "SDS",font=('Helvetica', 11))],
                         [sg.Text(key = "APS",font=('Helvetica', 11))],
                         [sg.Text(key = "Temed",font=('Helvetica', 11))],
                         [sg.Text("Kõik vajalik olemas?", visible = False, font=('Helvetica', 11), key = "tekst_2"), sg.Button("Jah", visible = False, key = "nupp_1"), sg.Button("Ei", visible = False, key = "nupp_2")],
                         [sg.Text(key = "kiitus_1", font=('Helvetica', 11))],
                         [sg.Text("Kui oled veendunud, et kõik asjad on olemas, siis võid need kokku segada. NB! Viimasena lisa alati TEMED, kuna see alustab polümerisatsiooni reaktsiooni.\n"
                                  "Kindlasti vortexi ka segu läbi!", visible=False, key = "tekst_3",font=('Helvetica', 11))],
                         [sg.Text("Kõik kokku segatud?", visible=False, key = "tekst_4", font=('Helvetica', 11)), sg.Button("Jah", visible = False, key = "nupp_3"), sg.Button("Ei", visible = False, key = "nupp_4")], 
                         [sg.Text(key = "kiitus_2",font=('Helvetica', 11))],
                         [sg.Text("Pipeteeri geel kiiresti 1 ml kaupa geeliraami."
                                  " Kui see tehtud siis lisa ettevaatlikult hambad.", visible=False, key = "tekst_5",font=('Helvetica', 11))],
                         [sg.Button("Valatud?", visible = False, key = "nupp_5")], 
                         [sg.Text("Nüüd tuleb oodata jälle c. 45 min. Selleks võid taaskord kasutada stopperit.", visible = False, key = "tekst_6",font=('Helvetica', 11))],
                         [sg.Button("Stopper", visible=False), sg.Button("->")]]
        aken_5 = sg.Window('Kontsentreeriv geel', akna_kujundus, size=(1050,650))
        while lehtede_indeksid[5] == True:
            sündmus, väärtused = aken_5.read()
            if sündmus == sg.WIN_CLOSED:
                lehtede_indeksid[5] = False
                break
            if sündmus == "Arvuta":
                tabel_1 = stacking_gel(int(väärtused["sisend_1"]))
                aken_5["tekst_1"].update("Kontsentreeriva geeli jaoks on vaja:")
                aken_5["MQ"].update(f"- {round(tabel_1[0],4)} ml MilliQ-d.")
                aken_5["Akrüülamiid"].update(f"- {round(tabel_1[1],4)} ml 30% Bis-akrüülamiidi.")
                aken_5["Tris"].update(f"- {round(tabel_1[2],4)} ml 1 M Tris-Cl-i (pH 6.8).")
                aken_5["SDS"].update(f"- {round(tabel_1[3],4)} ml SDS-i.")
                aken_5["APS"].update(f"- {round(tabel_1[4],4)} ml 10% ammooniaakpersulfaati.")
                aken_5["Temed"].update(f"- {round(tabel_1[5],4)} ml TEMED-it.")
                aken_5["tekst_2"].Update(visible = True)
                aken_5["nupp_1"].Update(visible = True)
                aken_5["nupp_2"].Update(visible = True)
            if sündmus == "nupp_2":
                aken_5["kiitus_1"].Update("Aga nüüd?")
            if sündmus == "nupp_1":
                aken_5["nupp_1"].Update(visible = False)
                aken_5["nupp_2"].Update(visible = False)
                aken_5["kiitus_1"].Update(random.choice(kiitused))
                aken_5["tekst_2"].Update(visible = False)
                aken_5["tekst_3"].Update(visible = True)
                aken_5["tekst_4"].Update(visible = True)
                aken_5["nupp_3"].Update(visible = True)
                aken_5["nupp_4"].Update(visible = True)
            if sündmus == "nupp_4":
                aken_5["kiitus_2"].Update("Aga nüüd?")
            if sündmus == "nupp_3":
                aken_5["nupp_3"].Update(visible = False)
                aken_5["nupp_4"].Update(visible = False)
                aken_5["kiitus_2"].Update(random.choice(kiitused))
                aken_5["tekst_4"].Update(visible = False)
                aken_5["nupp_5"].Update(visible = True)
                aken_5["tekst_5"].Update(visible = True)
            if sündmus == "nupp_5":
                aken_5["nupp_5"].Update(visible = False)
                aken_5["tekst_6"].Update(visible = True)
                aken_5["Stopper"].Update(visible = True)
            if sündmus == "Stopper":
                stopperi_aken(2700)
            if sündmus == "->":
                lehtede_indeksid[5] = False
                lehtede_indeksid[6] = True
                aken_5.close()
        akna_kujundus = [[sg.Text("Proovide laadimine ja jooksutamine", text_color='white', font=('Helvetica', 15))],
                 [sg.Text("Nüüd on siis aeg geeli elektriväljas jooksutada, et valgud molekulaarmassi alusel üksteisest lahutada. \n"
                          "Enne proovide laadimist pead ka veenduma, et proovid on selleks ka vastvalt töödeldud (vt nuppust avanevat joonist).", font=('Helvetica', 11)), sg.Button("", image_data = luup, button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key = "joonis_1")],
                          [sg.Text("Proovid töödeldud?", font=('Helvetica', 11), key = "tekst_1"), sg.Button("Jah", key = "nupp_1"), sg.Button("Ei", key = "nupp_2")],
                          [sg.Text(key = "kiitus_1",font=('Helvetica', 11))],
                          [sg.Text("Nüüd paneme masina kokku ja lisame geeli. Nüüd lisa masinasse SDS-i seni, kuni see on katnud kogu geeli.", font=('Helvetica', 11), visible=False, key = "tekst_1")],
                          [sg.Text("Seejärel saad hakkata laadima proove. NB! Lisa ka pikkusmarker.", font=('Helvetica', 11), visible=False, key = "tekst_2")],
                          [sg.Text("Proovid laetud?", visible=False, font=('Helvetica', 11), key = "tekst_3"), sg.Button("Jah", key = "nupp_3", visible = False), sg.Button("Ei", key = "nupp_4", visible = False)],
                          [sg.Text(key = "kiitus_2",font=('Helvetica', 11))],
                          [sg.Text("Peale proovide laadimist jooksuta geeli 150 V juures 45 min (arvestame, et tegemist on c. 50 kDa valguga). Võid selleks kasutada stopperit.", font=('Helvetica', 11), visible=False, key = "tekst_4")],
                          [sg.Button("Stopper", visible=False), sg.Button("->")]]
        aken_6 = sg.Window('Retseptid ja labori protokollid', akna_kujundus, size=(1000,300))
        while lehtede_indeksid[6] == True:
            sündmus, väärtused = aken_6()
            if sündmus == sg.WIN_CLOSED:
                lehtede_indeksid[6] = False
                break
            if sündmus == "joonis_1":
                proovide_ettevalmistamine()
            if sündmus == "nupp_2":
               aken_6["kiitus_1"].Update("Aga nüüd?")
            if sündmus == "nupp_1":
                aken_6["kiitus_1"].Update(random.choice(kiitused))
                aken_6["tekst_1"].Update(visible = False)
                aken_6["nupp_1"].Update(visible = False)
                aken_6["nupp_2"].Update(visible = False)
                aken_6["tekst_2"].Update(visible = True)
                aken_6["tekst_3"].Update(visible = True)
                aken_6["nupp_3"].Update(visible = True)
                aken_6["nupp_4"].Update(visible = True)
            if sündmus == "nupp_4":
               aken_6["kiitus_2"].Update("Aga nüüd?")
            if sündmus == "nupp_3":
               aken_6["kiitus_2"].Update(random.choice(kiitused))
               aken_6["tekst_3"].Update(visible = False)
               aken_6["nupp_3"].Update(visible = False)
               aken_6["nupp_4"].Update(visible = False)
               aken_6["tekst_4"].Update(visible = True)
               aken_6["Stopper"].Update(visible = True)
            if sündmus == "Stopper":
                stopperi_aken(2700)
            if sündmus == "->":
                lehtede_indeksid[6] = False
                lehtede_indeksid[7] = True
                aken_6.close()
        akna_kujundus = [[sg.Text("Proovide ülekanne membraanile", text_color='white', font=('Helvetica', 15))],
        [sg.Text("Kuna valgud diffundeeruvad geelist kergesti välja tuleb need edasiseks analüüsiks kanda üle kas nitrotselluloos või PVDF membraanile\n"
                 "Selleks kasutama ülekandemasinat, mis elektrivoolu toimel kannab valgud geelist membraanile\n"
                 "Ülekandeks on vaja otsida välja 6 Whatmani paberit, membraan, ülekandepuhver ja metanool. Samuti on vaja ka valmistatud geeli.", font=('Helvetica', 11))],
        [sg.Text("Kas kõik on asjad leitud?", key = "tekst_1", font=('Helvetica', 11)), sg.Button("Jah", key = "nupp_1"), sg.Button("Ei", key="nupp_2")],
        [sg.Text(key = "kiitus_1", font=('Helvetica', 11))],
        [sg.Text("Kui kõik asjad on leitud, siis saad alustada ülekandega alljärgneva juhise abil. Lisaks on võimalik vaadata paigutust ka nuppust avanevast joonisest.",font=('Helvetica', 11), visible=False, key = "tekst_2"), sg.Button("", image_data = luup, button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key = "joonis_1", visible = False)],
        [sg.Text("- Kasta 3 Whatmani paberit ülekandepuhvrisse (veendu, et oleks märgunud) ning aseta masinasse.\n"
         "- Kasta membraan metanooli ja alles seejärel ülekandepuhvrisse ning aseta Whatmani paberite peale. NB! Tee seda pintsettidega.\n"
         "- Võta ettevaatlikult geel oma vormist välja, lõika kontsetreeriva geeli osa maha ja aseta ülejäänud geel kogu ulatuses membraanile.\n"
         "- Lisa 3 viimast ülekandepuhvrisse kastetud Whatmani paberit.\n"
         "- Rulli mullid välja ja pane masin käima 45 min (15 V peaks piisama). \n", font=('Helvetica', 11),visible = False, key = "tekst_3")],
        [sg.Button("Stopper", visible=False), sg.Button("->")]]                                                                             
        aken_7 = sg.Window('Kontsentreeriv geel', akna_kujundus, size=(1020,345))
        while lehtede_indeksid[7] == True:
            sündmus, väärtused = aken_7.read()
            if sündmus == sg.WIN_CLOSED:
                lehtede_indeksid[7] = False
                break
            if sündmus == "nupp_2":
                aken_7["kiitus_1"].Update("Aga nüüd?")
            if sündmus == "nupp_1":
                aken_7["tekst_1"].Update(visible = False)
                aken_7["kiitus_1"].Update(random.choice(kiitused))
                aken_7["nupp_1"].Update(visible = False)
                aken_7["nupp_2"].Update(visible = False)
                aken_7["tekst_2"].Update(visible = True)
                aken_7["tekst_3"].Update(visible = True)
                aken_7["Stopper"].Update(visible = True)
                aken_7["joonis_1"].Update(visible = True)
            if sündmus == "joonis_1":
                ülekanne()
            if sündmus == "Stopper":
                stopperi_aken(2700)
            if sündmus == "->":
                lehtede_indeksid[7] = False
                lehtede_indeksid[8] = True
                aken_7.close()
        akna_kujundus = [[sg.Text("Primaarsete antikehadega inkubeerimine", text_color='white', font=('Helvetica', 15))],
                         [sg.Text("Selleks, et valke membraanil visualiseerida tuleb kõigepealt membraani inkubeerida meid huvitava valguga seonduvate antikehadega. \n"
                                  "Tavaliselt tehakse seda üleöö 4°C juures.", font=('Helvetica', 11))],
                         [sg.Text("Kõigepealt aga võta membraan masinast välja, kuid ära lase sellel ära kuivada.", font=('Helvetica', 11))],
                         [sg.Text("Valmista 15ml antikehade lahust 5% lõssi lahuses 50ml tuubi.", font=('Helvetica', 11)), sg.Text("Mis antikehade kontsetratsiooni kasutad?", font=('Helvetica', 11)), sg.InputCombo(("1/2500", "1/5000", "1/10000", "1/15000"), key = "sisend_1", size=(6,10)), sg.Button("Arvuta")],
                         [sg.Text(key = "tekst_1",font=('Helvetica', 11))],
                         [sg.Text("Lisa membraan tuubi ja lase selle loksutil inkubeerida üleöö 4°C juures (alati võid kauem).", key = "tekst_2", visible = False, font=('Helvetica', 11)), sg.Button("Valmis", visible=False )],
                         [sg.Text("Üleliigsete antikehade mahapesemiseks peseme membraani vähemalt 3x10 min pesulahuses. Selleks avaneb allolevast 'pesu' nuppust stopper.", visible=False , key = "tekst_3",font=('Helvetica', 11))],
                         [sg.Button("1. Pesu", key = "pesemine", visible=False), sg.Button("->")]]        
        aken_8 = sg.Window('Primaarsete antikehadega inkubeerimine', akna_kujundus, size=(1000,270))
        
# Muutuja "n" märgib ära mitu pesu on juba olnud (muutujat suurendatakse peale igat pesu +1 võrra).        
        
        n = 0 
        while lehtede_indeksid[8] == True:
            sündmus, väärtused = aken_8.read()
            if sündmus == sg.WIN_CLOSED:
                lehtede_indeksid[8] = False
                break
            if sündmus == "Arvuta":
                
# Teeb jagatise lugejaks ja nimetajaks, mida kasutakse allolevas arvutuses.                
                
                try:
                    arvud = väärtused["sisend_1"].split("/") 
                    aken_8["tekst_1"].Update(f"Lisa {round(int(arvud[0])/int(arvud[1])*15000,2)} μl antikeha 15 ml 5% lõssile.")
                    aken_8["tekst_2"].Update(visible = True)
                    aken_8["Valmis"].Update(visible = True)
                except:
                    continue
            if sündmus == "Valmis":
                aken_8["tekst_3"].Update(visible = True)
                aken_8["pesemine"].Update(visible = True)
            if sündmus == "pesemine":
                stopperi_aken(600)
                n+=1
                aken_8["pesemine"].Update(f"{n+1}. pesu")
            if n == 3:
                aken_8["->"].Update(visible = True)
            if sündmus == "->":
                lehtede_indeksid[8] = False
                lehtede_indeksid[9] = True
                aken_8.close()
        akna_kujundus = [[sg.Text("Sekundaarsete antikehadega inkubeerimine", text_color='white', font=('Helvetica', 15))],
             [sg.Text("Peale pesu seome primaarsete antikehadega sekundaarsed antikehad, mis on vajalikud valkude tuvastamiseks membraanil.\n"
                      "Valgu tuvastavamiseks on antikeha külge kovalentselt seotud näiteks fluorofoor või reportermolekul.", font=('Helvetica', 11))],
             [sg.Text("Siin kasutame reporterina mädarõika peroksüdaasiga (HRP) konjugeeritud antikehi, mis katalüüsivad kolorimeetrilist reaktsiooni (vt nuppust joonist).", font=('Helvetica', 11)), sg.Button("", image_data = luup, button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key = "joonis_1")],
             [sg.Text("Sekundaarsete antikehadega inkubeerime membraani toatemperatuuril 1 tund.",font=('Helvetica', 11))],
             [sg.Text("Valmista 10 ml antikehade lahust 2.5% lõssi lahuses. Mis antikehade kontsetratsiooni kasutad?",font=('Helvetica', 11)), sg.InputCombo(("1/2500", "1/5000", "1/10000", "1/15000"), key = "sisend_1", size=(6,10)), sg.Button("Arvuta")],
             [sg.Text(key = "tekst_1",font=('Helvetica', 11))],
             [sg.Text("Lisa membraan alusesse ja lase sellel loksutil inkubeerida toatemperatuuril 1 tund.", key = "tekst_2", visible = False,font=('Helvetica', 11)), sg.Button("Lisasin!", visible=False )],
             [sg.Text("Üleliigsete antikehade mahapesemiseks peseme membraani vähemalt 3x10 min pesulahuses.", visible=False , key = "tekst_3",font=('Helvetica', 11))],
             [sg.Button("1. Pesu", key = "pesemine", visible=False), sg.Button("->")]]      
        aken_9 = sg.Window('Sekundaarsete antikehadega inkubeerimine', akna_kujundus, size=(1100,305))
        n = 0
        while lehtede_indeksid[9] == True:
            sündmus, väärtused = aken_9.read()
            if sündmus == sg.WIN_CLOSED:
                lehtede_indeksid[9] = False
                break
            if sündmus == "joonis_1":
                antikeha()
            if sündmus == "Arvuta":
                try:
                    arvud = väärtused["sisend_1"].split("/")
                    aken_9["tekst_1"].Update(f"Lisa {round(int(arvud[0])/int(arvud[1])*10000,2)} μl antikeha 10 ml 2.5% lõssile ja vala väiksesse alusesse.")
                    aken_9["tekst_2"].Update(visible = True)
                    aken_9["Lisasin!"].Update(visible = True)
                except:
                    continue
            if sündmus == "Lisasin!":
                stopperi_aken(3600)
                aken_9["tekst_3"].Update(visible = True)
                aken_9["pesemine"].Update(visible = True)
            if sündmus == "pesemine":
                stopperi_aken(600) 
                n+=1
                aken_9["pesemine"].Update(f"{n+1}. pesu")
            if sündmus == "->":
                lehtede_indeksid[9] = False
                lehtede_indeksid[10] = True
                aken_9.close()
        akna_kujundus = [[sg.Text("Visualiseerimine", text_color='white', font=('Helvetica', 15))],
        [sg.Text("Peale pesu on meil võimalik valke visualiseerida, kasutades substraadina TMB lahust.\n" 
              "TMB muutub HRP juuresolekul siniseks ja teeb nii valkude asukoha membraanil nähtavaks\n\n"
              "Värvusreaktsiooni algatamiseks pipeteeri umbes 1 ml TMD-d ühtlaselt membraani peale ja jälgi siniste vöötide tekkimist membraanil.",font=('Helvetica', 11))],
        [sg.Text("Kui vöödid on piisavalt tugevad peata reaktsioon pestes MQ veega TMB membraanilt maha.\n", font=('Helvetica', 11))],
        [sg.Text("Nüüd ongi valmis. Kuidas välja tuli? Nuppust avaneb pikkusmarkeri (Pageruler 10-80 kDa) vöötide molekulaarmasside joonis.",font=('Helvetica', 11)), sg.Button("", image_data = luup, button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key = "joonis_1")],
        [sg.Cancel("Lõpetaks nüüd äkki ära?",font=('Helvetica', 11))]]
        aken_10 = sg.Window('Visualiseerimine', akna_kujundus, size=(900,250))
        while lehtede_indeksid[10] == True:
            sündmus, väärtused = aken_10.read()
            if sündmus == sg.WIN_CLOSED:
                lehtede_indeksid[10] = False
                break
            if sündmus == "joonis_1":
                pikkusmarker()
            if sündmus == "Lõpetaks nüüd äkki ära?":
                lehtede_indeksid[10] == False
                aken_10.close()
                              
# Sisenemine Letšo valmistamise aknasse
# Aken kuvab juhised ja kontrollib kasutaja valmisolekut. Kui kasutaja on valmis, uuendatakse akent uute juhistega.
# Positiivse vastuse puhul läheb programm uude tsüklisse. Negatiivse puhul jääb see kasutajat pinnima.                              
                              
    if sündmus == "Letšo valmistamise juhend":
        lehtede_indeksid[1] = False
        aken_1.close()
        
# Kujunduses juhend (muutub igal sammul), nupud, 2 edenemisriba (algselt peidetud) ja vastuseriba.
        
        paigutus = [[sg.Text('Letšo valmistamise juhend', font=('Comic Sans MS', 14))],
                    [sg.Text(tutvustus, key='samm')],
                    [sg.Text('', key='riba1', visible=False)],
                    [sg.ProgressBar(aeg1, orientation='h', size=(100,20), border_width=4, key='edenemisriba', bar_color=("Red", "Yellow"), visible=False)],
                    [sg.ProgressBar(aeg2, orientation='h', size=(100,20), border_width=4, key='edenemisriba2', bar_color=("Red", "Yellow"), visible=False)],
                    [sg.Button('Jah', key='Jah'), sg.Button('Ei', key='Ei')],
                    [sg.Text('', key='vastus')]]
        aken_1.close()
        aken2 = sg.Window('Letšo valmistamise juhend', paigutus, size=(650, 400))
        while True:
            sündmus, väärtused = aken2.read()
            if sündmus == sg.WIN_CLOSED:
                break
            if sündmus == 'Ei':
                aken2['vastus'].update('Aga nüüd?')
            if sündmus == 'Jah':
                aken2['vastus'].update(visible=False)
                aken2['samm'].update(koostisosad)
                while True:
                    sündmus, väärtused = aken2.read()
                    if sündmus == sg.WIN_CLOSED:
                        break
                    if sündmus == 'Ei':
                        aken2['vastus'].update('Aga nüüd?', visible=True)
                    if sündmus == 'Jah':
                        aken2['vastus'].update(visible=False)
                        aken2['samm'].update(tükeldamine)
                        while True:
                            sündmus, väärtused = aken2.read()
                            if sündmus == sg.WIN_CLOSED:
                                break
                            if sündmus == 'Ei':
                                aken2['vastus'].update('Aga nüüd?', visible=True)
                            if sündmus == 'Jah':
                                aken2['vastus'].update(visible=False)
                                aken2['samm'].update(potti)
                                while True:
                                    sündmus, väärtused = aken2.read()
                                    if sündmus == sg.WIN_CLOSED:
                                        break
                                    if sündmus == 'Ei':
                                        aken2['vastus'].update('Aga nüüd?', visible=True)
                                    if sündmus == 'Jah':
                                        aken2['vastus'].update(visible=False)
                                        aken2['samm'].update(keema)
                                        while True:
                                            sündmus, väärtused = aken2.read()
                                            if sündmus == sg.WIN_CLOSED:
                                                break
                                            if sündmus == 'Ei':
                                                aken2['vastus'].update('Aga nüüd?', visible=True)
                                                
# Siit alates ilmub programmi edenemisriba. See kulgeb esialgu kuni 5/6  ette antud ajast.
# Pärast 5/6 möödumist programm piiksub ja annab märku, et peab lisama äädika. Samal ajal kulgeb riba lõpuni.
# Kuni edenemisriba edeneb, kaotame nupud "Jah/Ei" - pole sisendit vaja.
                                            
                                            if sündmus == 'Jah':
                                                aken2['vastus'].update(visible=False)
                                                aken2['samm'].update(keemiseks)
                                                aken2['edenemisriba'].update(visible=True)
                                                aken2['Jah'].update(visible=False)
                                                aken2['Ei'].update(visible=False)
                                                for i in range(aeg1*5//6+1):
                                                    sündmus, väärtused = aken2.read(1000)
                                                    if sündmus == sg.WIN_CLOSED:
                                                        break
                                                    aken2['edenemisriba'].update(i+1)
                                                    if i == aeg1*5/6:
                                                        winsound.Beep(1000, 500)
                                                        winsound.Beep(1000, 500)
                                                        winsound.Beep(2000, 1000)
                                                        aken2['samm'].update(äädikas)
                                                        for j in range(aeg1//6+1):
                                                            m = i+j+1
                                                            aken2['Jah'].update(visible=True)
                                                            aken2['Ei'].update(visible=True)
                                                            sündmus, väärtused = aken2.read(1000)
                                                            aken2['edenemisriba'].update(m)
                                                            if sündmus == sg.WIN_CLOSED:
                                                                break
                                                            if sündmus == 'Ei':
                                                                aken2['vastus'].update('Aga nüüd?', visible=True)
                                                            if sündmus == 'Jah':
                                                                aken2['vastus'].update('Väga hea! Ootame nüüd lõpuni.', visible=True)
                                                            if m == aeg1:
                                                                winsound.Beep(2000, 500)
                                                                winsound.Beep(2000, 500)
                                                                winsound.Beep(1000, 1000)
                                                                aken2['vastus'].update(visible=False)
                                                                break
                                                            
# Kaotame edenemisriba. Programm kulgeb vanamoodi, kuni tuleb mõõta järgmist ajavahemikku (purkide kuumutamine). 
                                                            
                                                while True:
                                                    aken2['edenemisriba'].update( visible=False)
                                                    aken2['samm'].update(pärast_keetmist)
                                                    sündmus, väärtused = aken2.read()
                                                    if sündmus == sg.WIN_CLOSED:
                                                        break
                                                    if sündmus == 'Ei':
                                                        aken2['vastus'].update('Aga nüüd?', visible=True)
                                                    if sündmus == 'Jah':
                                                        aken2['vastus'].update(visible=False)
                                                        aken2['samm'].update(kuumuta_purke)
                                                        while True:
                                                            sündmus, väärtused = aken2.read()
                                                            if sündmus == sg.WIN_CLOSED:
                                                                break
                                                            if sündmus == 'Ei':
                                                                aken2['vastus'].update('Aga nüüd?', visible=True)
                                                                
# Teine edenemisriba, mis mõõdab purkide kuumutamise aega. 1 kontroll pärast seda ja seejärel lõputekst.
                                                                
                                                            if sündmus == 'Jah':
                                                                aken2['vastus'].update(visible=False)
                                                                aken2['edenemisriba2'].update(visible=True)
                                                                aken2['Jah'].update(visible=False)
                                                                aken2['Ei'].update(visible=False)
                                                                for i in range(aeg2+1):
                                                                    sündmus, väärtused = aken2.read(1000)
                                                                    if sündmus == sg.WIN_CLOSED:
                                                                        break
                                                                    aken2['edenemisriba2'].update(i+1)
                                                                    if i == aeg2:
                                                                        winsound.Beep(2000, 500)
                                                                        winsound.Beep(2000, 500)
                                                                        winsound.Beep(1000, 1000)
                                                                        aken2['vastus'].update(visible=False)
                                                                        break
                                                                while True:
                                                                    aken2['samm'].update(pärast_kuumutamist)
                                                                    aken2['Jah'].update(visible=True)
                                                                    aken2['Ei'].update(visible=True)
                                                                    aken2['edenemisriba2'].update(visible=False)
                                                                    sündmus, väärtused = aken2.read()
                                                                    if sündmus == sg.WIN_CLOSED:
                                                                        break
                                                                    if sündmus == 'Ei':
                                                                        aken2['vastus'].update('Aga nüüd?', visible=True)
                                                                    if sündmus == 'Jah':
                                                                        aken2['vastus'].update(visible=False)
                                                                        aken2['samm'].update(lõpp)
                                                                        aken2['Jah'].update(visible=False)
                                                                        aken2['Ei'].update(visible=False)
                                                                        break
        aken2.close()