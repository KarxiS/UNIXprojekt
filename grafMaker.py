import textwrap

import matplotlib.pyplot as plt
import randomcolor as randomcolor

import stranka


class grafMaker:

    def __init__(self, predmet):
        self.strankyObj = predmet;
        self.x = (predmet[0].znamky)

    def pridajDoYArrayu(self, yArray):
        self.yArray.append(yArray)

    def resetujPredmety(self):
        self.strankyObj=[]

    def vytvorGraf(self):
        arrayPercent=[]
        # Data
        plt.figure(figsize=(20, 10))
        plt.clf()

        for predmet in self.strankyObj:
            color = randomcolor.RandomColor().generate(format_='hex')

            # Plot the line
            menoPredmetu = predmet.getMeno();
            plt.plot(self.x,predmet.getPercenta(), label = menoPredmetu, color=color[0])

            #statistika
            menoPredmetuKey = menoPredmetu
            skupina = (predmet,predmet.getPriemerPercent())
            if(predmet.getPriemerPercent()!=0) :
                arrayPercent.append(skupina)





        # Add a title and axis labels
        plt.title('Predmety')
        plt.xlabel('znamky')
        plt.ylabel('percenta')
        plt.legend()
        stringConstructor = ""
        arrayPercentZoradeneHorsie = sorted(arrayPercent, key=lambda x: x[0].getPriemerPercent())[:7]
        arrayPercentZoradeneLepsie = sorted(arrayPercent, key=lambda x: x[0].getPriemerPercent(),reverse=True)[:7]
        stringConstructor+="-----Najlepsie predmety----------- \n"
        for predmet in arrayPercentZoradeneHorsie:
            print(predmet[0].getMeno()+str(round(predmet[0].getPriemerPercent(),2)))
            menoPredmetu = predmet[0].getMeno()[:13];

            stringConstructor+= menoPredmetu.ljust(15)+"  priemer: "+str(round(predmet[0].getPriemerPercent(),2))+" /6\n"
        stringConstructor += "-----Najhorsie predmety----- \n"
        for predmet in arrayPercentZoradeneLepsie:
            print(predmet[0].getMeno() + str(round(predmet[0].getPriemerPercent(), 2)))
            menoPredmetu = predmet[0].getMeno()[:13]

            stringConstructor += menoPredmetu.ljust(15) +"  priemer: "+ str(round(predmet[0].getPriemerPercent(), 2)) + " /6\n"

        # Show the plot

        plt.show(block=False)
        return stringConstructor