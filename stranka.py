from bs4 import BeautifulSoup
from unidecode import unidecode
from statistics import mean
import re
class stranka:

    # poslem, tu spracujem cez BS
    def __init__(self, stranka):
        self.stranka = BeautifulSoup(stranka, 'html.parser')
        self.nazov = '';
        self.pocetZiakov =0;
        self.znamky = []
        self.percenta = []
        self.priemerZnamok = 0;
        self.pocetZiakovFX = 0
    def getPocetZiakovFX(self):
        return self.pocetZiakovFX;
    def getMeno(self):
        return self.nazov;
    def getPriemerPercent(self):
        return self.priemerZnamok;
    def getPocetZiakov(self):
        return self.pocetZiakov;
    def getPercenta(self):
        return self.percenta;
    def spracuj(self):
        nazovPredmetu = self.stranka.find('table', {'id': 'id-tabulka-inf-list-predmetu'})
        ratac = 0;
        for td in nazovPredmetu.find_all('td'):
            text = td.text.strip()
            if(ratac==2):
                break;
            if 'Názov predmetu' in text:
                text = text.replace('Názov predmetu: ', '')
                text = unidecode(text)
                self.nazov = text;
                ratac += 1


            if 'Hodnotenie predmetov' in text:
                pctZiakov = re.search(r'\d+', text)
                if pctZiakov:

                    self.pocetZiakov =  int(pctZiakov.group())
                else:
                    self.pocetZiakov = 0;
                ratac+=1





        znamky = []
        tabulkaSoZnamkami = self.stranka.find('table', {'class': 'ilstat'})
        for td in tabulkaSoZnamkami.find_all('td'):
            text = td.text.strip()

            if '%' in text:
                percent = float(text.rstrip('%'))
                self.percenta.append(percent)
            else:
                self.znamky.append(text)
        print(self.znamky)
        print(self.percenta)


        #rataniePriemeruZnamok
        vysledok = (1*self.percenta[0]+2*self.percenta[1]+3*self.percenta[2]+4*self.percenta[3]+5*self.percenta[4]+6*self.percenta[5])/100
        self.priemerZnamok=vysledok;
        # pocetZiakovFX, trojclenka
        try:
            trojclenka = (self.pocetZiakov * self.percenta[5]) / 100
        except ZeroDivisionError:
            trojclenka = 0;
        self.pocetZiakovFX = trojclenka;



