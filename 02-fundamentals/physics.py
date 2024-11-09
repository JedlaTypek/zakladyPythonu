'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''
import math

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení v m/s2
MOON_GRAVITY = 1.62 #? měsíční gravitace v m/s2
GRAVITIES = {
    "Merkur": 3.7,
    "Venuše": 8.87,
    "Země": 9.81,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uran": 8.69,
    "Neptun": 11.15
}
SPEED_OF_LIGHT = 299796 #? rychlost světla ve vakuu v km/s
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu v m/s

def padVeVakuu(h, g):
    """
    Funkce vrací délku pádu v sekundách a rychlost dopadu tělesa vše ve vakuu. Jako parametry zadej výšku tělesa od místa dopadu v metrech a tíhové zrychlení v místě pádu tělesa.

    Použití:
    cas, rychlost = padVeVakuu(vyska, tihove_zrychleni) nebo
    _,rychlost = padVeVakuu(vyska, tihove_zrychleni) pro získání pouze rychlosti a naopak
    """

    t = math.sqrt(2 * h / g)
    v = g * t
    return t, v

def vahaNaPlanete(hmotnost, g):
    """
    Funkce vrací váhu tělesa na planetě s tíhovým zrychlením g, které na zemi váží hmonost.
    """

    vaha = hmotnost / EARTH_GRAVITY * g
    return vaha

def vzdalenostBlesku(t):
    """
    Funkce vypočítá vzádelnost blesku od místa pozorování. Jako vstupní parametr zadejte časovou prodlevu mezi bleskem a hromem.
    """
    return t * SPEED_OF_SOUND

def jak_rychle_urazi_svetlo(s):
    """
    Funkce vypočítá, za kolik sekund světlu urazí zadanou vzálenost v metrech v parametru.
    """
    return s / 1000 / SPEED_OF_LIGHT


''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''