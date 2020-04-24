#Defining the elements that will be used in the ChemSketch program

#My method of storing the properties of each element. A potential future
#improvement would be to extract the data out of a CSV file to make it 
#more organized and less hardcoded.

class Element(object):
    names = dict()
    #store all properties of each element
    def __init__(self,name,num,mass,radius,valence,electro,color):
        self.name = name
        self.num = num
        self.mass = mass
        self.radius = radius
        self.valence = valence
        self.electronegativity = electro
        self.color = color #rgb value
        Element.names[self.name] = self 
        #string of name maps to instance of element

    def getAtomicNumber(self):
        return self.num

    def getAtomicRadius(self):
        return self.radius

    def getValenceElectronNumber(self):
        return self.valence

    def getBondingElectrons(self):
        if self.valence <= 4:
            return self.valence
        else:
            return 8 - self.valence

    def __repr__(self):
        return self.name

#create an instance for every element that is not radioactive 
#or a transition metal
H = Element("H",1,1.008,53,1,2.20,(1,0,0))
He = Element("He",2,4.003,31,2,0,(0,1,0))
Li = Element("Li",3,6.94,167,1,0.98,(0,0,1))
Be = Element("Be",4,9.012,112,2,1.57,(1,1,0))
B = Element("B",5,10.81,87,3,2.04,(1,0.5,0))
C = Element("C",6,12.011,67,4,2.55,(0,1,1))
N = Element("N",7,14.007,56,5,3.04,(1,0,1))
O = Element("O",8,15.999,48,6,3.44,(0.6,0.2,0.9))
F = Element("F",9,18.998,42,7,3.98,(0.9,0.6,0.2))
Ne = Element("Ne",10,20.180,38,8,0,(0.6,0.9,0.2))
Na = Element("Na",11,22.990,190,1,0.93,(0.9,0.2,0.6))
Mg = Element("Mg",12,24.305,145,2,1.31,(0.2,0.6,0.9))
Al = Element("Al",13,26.982,118,3,1.61,(0.2,0.9,0.6))
Si = Element("Si",14,28.085,111,4,1.90,(0.7,0.3,0.1))
P = Element("P",15,30.974,98,5,2.19,(0.7,0.1,0.3))
S = Element("S",16,32.06,88,6,2.58,(0.3,0.7,0.1))
Cl = Element("Cl",17,35.45,79,7,3.16,(0.3,0.1,0.7))
Ar = Element("Ar",18,39.948,71,8,0,(0.1,0.3,0.7))
K = Element("K",19,39.098,243,1,0.82,(0.1,0.7,0.3))
Ca = Element("Ca",20,40.078,194,2,1.00,(0.2,0.7,0.6))

Ga = Element("Ga",31,69.723,136,3,1.81,(0.3,0.6,0.5))
Ge = Element("Ge",32,72.63,125,4,2.01,(0.4,0.5,0.4))
As = Element("As",33,74.922,114,5,2.18,(0.5,0.4,0.2))
Se = Element("Se",34,78.971,103,6,2.55,(0.8,0.8,0.8))
Br = Element("Br",35,79.904,94,7,2.96,(0.7,0.7,0.7))
Kr = Element("Kr",36,83.798,88,8,3.00,(0.6,0.6,0.6))
Rb = Element("Rb",37,85.468,265,1,0.82,(0.5,0.5,0.5))
Sr = Element("Sr",38,87.62,219,2,0.95,(0.4,0.4,0.4))

In = Element("In",49,114.818,156,3,1.78,(0.2,0.3,0.5))
Sn = Element("Sn",50,118.710,145,4,1.96,(0.3,0.26,0.9))
Sb = Element("Sb",51,121.760,133,5,2.05,(0.2,0.4,0.6))
Te = Element("Te",52,127.60,123,6,2.1,(0.6,0.4,0.2))
I = Element("I",53,126.904,115,7,2.66,(0.9,0.6,0.3))
Xe = Element("Xe",54,131.293,108,8,2.6,(0.4,0.8,0.2))
Cs = Element("Cs",55,132.905,298,1,0.79,(0.2,0.8,0.4))
Ba = Element("Ba",56,137.327,253,2,0.89,(0.8,0.4,0.2))

Tl = Element("Tl",81,204.38,156,3,1.62,(0.7,0.3,0.1))
Pb = Element("Pb",82,207.2,154,4,2.33,(0.8,0.5,0.6))
Bi = Element("Bi",83,208.980,143,5,2.02,(0.5,0.1,0.2))