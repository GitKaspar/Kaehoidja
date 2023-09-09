import PySimpleGUI as sg
import time
import winsound
from playsound import playsound

# Stopperi inspiratsioon: https://tinyurl.com/y93en6u3

def stopperi_aken(aeg, muusikapala = None, muusika_aeg=None, pealkiri = "Stopper"):
    stopperi_kujundus = [[sg.Text(pealkiri, text_color='black', font=('Helvetica', 20))],
                                                                [sg.Text(key = "taimer", font=('Helvetica', 20))],
                                                                [sg.ProgressBar(aeg, orientation='h', size=(100, 20), border_width=4, key="riba")],
                                                                [sg.Button("Aitab küll", key="Lõpp")]]
    st_aken = sg.Window("Stopper", stopperi_kujundus, size=(350,200))
    praegune_aeg = 0
    algusaeg = int(round(time.time() * 100))
    n = 0
    
    while True:
        sündmus, väärtused = st_aken.read(timeout=10)
        praegune_aeg = int(round(time.time() * 100)) - algusaeg
        st_aken["riba"].update(praegune_aeg // 100)
        st_aken['taimer'].update('{:02d}:{:02d}.{:02d}'.format((praegune_aeg // 100) // 60,
                                                                      (praegune_aeg // 100) % 60,
                                                                      praegune_aeg % 100))
        
# Funktsiooni päises võimalik anda muutujatele muusika_aeg ja muusikaaus väärtus, mis vastavalt märgivad, millal ja mida mängida.
        
        if praegune_aeg // 100 == muusika_aeg:
            muusika_aeg = 0 
            playsound(muusikapala,False)
        if praegune_aeg // 100 == aeg:
            break
        if sündmus == sg.WIN_CLOSED or sündmus == "Lõpp":
            st_aken.close()
            break
    while True:
        sündmus, väärtused = st_aken.read(timeout=5)
        if sündmus == sg.WIN_CLOSED or sündmus == "Lõpp":
            st_aken.close()
            break
        
# Aja lõppedes kaotab korduvalt progressiriba ära ja toob nähtavale, tehes samal ajal ka helimärguandeid.
        
        st_aken.Element("riba").update(visible=False)
        winsound.Beep(1000,500)
        winsound.Beep(1000,500)
        st_aken.Element("riba").update(visible=True)
        winsound.Beep(1000,500)
        winsound.Beep(1000,500)