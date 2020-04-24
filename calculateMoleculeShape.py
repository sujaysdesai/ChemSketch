#Determining the shape of the molecule

from elements import *

def inputSolver(inputMol):
    #convert string of formula into list of elements in that molecule
    molecule = []
    element = ""
    for char in inputMol:
        if char.isupper():
            if element != "":
                molecule.append(element)
            element = char
            if inputMol[-1] == char:
                molecule.append(element)
                element = ""
        elif char.islower():
            element = element + char
            if inputMol[-1] == char:
                molecule.append(element)
                element = ""
        elif char.isdigit():
            for i in range(int(char)):
                molecule.append(element)
            element = ""
        else: #if there is an invalid character
            return None #later check if None and then return error message
    #translate string of element to instance of element
    return translate(molecule)

def translate(molecule):
    #takes list of string of elements and returns
    #list of instances of elements
    new = []
    for atom in molecule:
        new.append(Element.names[atom])
    return new

class Molecule(object): 
    #each molecule is an instance of this class
    details = dict() #properties of molecular that will be showed
    isLegal = True

    def __init__(self,molecule):
        self.molecule = molecule #list of atoms in molecule
        self.center = self.getCenterAtom()

    def getCenterAtom(self):
        maxLoneElectrons = 0
        center = None
        #only molecules with more than 2 atoms have a center
        if len(self.molecule) > 2:
            for atom in self.molecule:
                bondingElectrons = atom.getBondingElectrons()
                if bondingElectrons > maxLoneElectrons:
                    maxLoneElectrons = bondingElectrons
                    center = atom
        Molecule.details["Center"] = str(center)
        return center

    def getBondNumber(self):
        numOfBonds = 0
        for atom in self.molecule:
            if atom != self.center:
                numOfBonds += atom.getBondingElectrons()
        loneElectronNum = self.center.valence - numOfBonds
        return (self.center,numOfBonds,loneElectronNum)

    def isLegalStructure(self):
        #no single atoms, only molecules
        if len(self.molecule) == 1:
            return False
        elif len(self.molecule) > 2:
            shape = self.getBondNumber()
            #can't have negative number of lone electrons or lone radicals
            if (shape[2] < 0) or (shape[2] % 2 == 1):
                return False
            #atoms with atomic number less than 10 must obey octet rule
            elif (shape[0].num <= 10) and (shape[1]*2+shape[2] > 8):
                return False
            #if hydrogen then can only form one bond
            elif (shape[0].num == 1) and (shape[1] > 1):
                return False
            else:
                return True

    def containsMultipleBonds(self):
        shape = self.getBondNumber()
        numOfBonds = shape[1]
        #if molecule forms more bonds than it has bonding electrons,
        #it must contain at least one double or triple bond
        if (numOfBonds > len(self.molecule) - 1):
            return True
        return False

    def containsDoubleBonds(self):
        if self.containsMultipleBonds == False:
            return None
        else:
            doubleBonds = dict()
            for atom in self.molecule:
                if atom != self.center:
                    #2 bonding electrons means 1 double bond
                    if atom.getBondingElectrons() == 2:
                        doubleBonds[atom] = True
                    else:
                        doubleBonds[atom] = False
            return doubleBonds

    def containsTripleBonds(self):
        if self.containsMultipleBonds == False:
            return None
        else:
            tripleBonds = dict()
            for atom in self.molecule:
                if atom != self.center:
                    #3 bonding electrons means 1 triple bond
                    if atom.getBondingElectrons() == 3:
                        tripleBonds[atom] = True
                    else:
                        tripleBonds[atom] = False
            return tripleBonds

    def getStericNumber(self):
        shape = self.getBondNumber()
        #steric number is number of atoms bonded to central atom
        #plus number of lone pairs on central atom
        num = (len(self.molecule) - 1) + shape[2]/2
        return num

    def getHybridization(self):
        #use steric number to determine molecular geometry
        if len(self.molecule) == 2:
            return "linear"
        else:
            num = self.getStericNumber()
            if num == 2:
                return "sp"
            elif num == 3:
                return "sp2"
            elif num == 4:
                return "sp3"
            elif num == 5:
                return "sp3d"
            elif num == 6:
                return "sp3d2"