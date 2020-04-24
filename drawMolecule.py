#Drawing the molecule

from elements import *
from checkStructure import *
from visual import *
import math

class Draw(Molecule):
    scale = 1.5 #to make easily viewable
    bondRadius = 10
    objects = [] #list of all objects to rotate
    labels = [] #list of all labels to store
    isPaused = False #for rotation
    showLabels = False

    def __init__(self,mol):
        super(Draw,self).__init__(mol)
        self.bondLength = 0

class DrawLinear(Draw):
    position = (0,0,0)

    def __init__(self,mol):
        super(DrawLinear,self).__init__(mol)

    def drawLabels(self,position,atom):
        #label originates at center of atom
        if Draw.showLabels == True:
            description = label(pos=position,text=str(atom.name),
                                xoffset=-20,yoffset=-20)
            Draw.labels.append(description)

    def drawBonds(self,position,atom,molecule):
        double = molecule.containsDoubleBonds()
        triple = molecule.containsTripleBonds()
        if (double[atom] == True):
            #draw 2 cylinders for double bond
            bond1 = cylinder(pos=(0,10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,-10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
        elif (triple[atom] == True):
            #draw 3 cylinders for triple bond
            bond1 = cylinder(pos=(0,25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
            bond3 = cylinder(pos=(0,-25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond3)
        else:
            #draw 1 cylinder for single bond
            bond = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond)

    def getBondLength(self):
        #the scaled sum of the atomic radii
        length = 0
        for atom in self.molecule:
            length += atom.radius
        return length * Draw.scale

    def drawAtoms(self,molecule):
        for i in range(len(self.molecule)):
            atom = self.molecule[i]
            self.bondLength = self.getBondLength()
            #first atom positioned at center
            if (i == 0):
                position = (0,0,0)
            else:
                position = (self.bondLength,0,0)
            newSphere = sphere(pos=position,radius=atom.radius,color=atom.color)
            Draw.objects.append(newSphere)
            self.drawBonds(position,atom,molecule)
            self.drawLabels(position,atom)

class DrawSp(Draw):
    position = (0,0,0)
    angle = 0

    def __init__(self,mol):
        super(DrawSp,self).__init__(mol)

    def drawLabels(self,position,atom):
        if Draw.showLabels == True:
            description = label(pos=position,text=str(atom.name),
                                xoffset=-20,yoffset=-20)
            Draw.labels.append(description)

    def drawCenterAtom(self):
        radius = self.center.radius
        #each element has different color atom
        color = self.center.color
        centerAtom = sphere(pos=DrawSp.position,radius=radius,color=color)
        self.drawLabels(DrawSp.position,self.center)
        Draw.objects.append(centerAtom)

    def drawBonds(self,position,atom,molecule):
        double = molecule.containsDoubleBonds()
        triple = molecule.containsTripleBonds()
        if (double[atom] == True):
            bond1 = cylinder(pos=(0,10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,-10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
        elif (triple[atom] == True):
            bond1 = cylinder(pos=(0,25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
            bond3 = cylinder(pos=(0,-25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond3)
        else:
            bond = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond)

    def drawSurroundingAtoms(self,molecule):
        for atom in self.molecule:
            if atom != self.center:
                self.bondLength = (self.center.radius + atom.radius) * Draw.scale
                x = self.bondLength*math.cos(DrawSp.angle)
                y = self.bondLength*math.sin(DrawSp.angle)
                position = (x,y,0)
                newSphere = sphere(pos=position,radius=atom.radius,color=atom.color)
                Draw.objects.append(newSphere)
                self.drawBonds(position,atom,molecule)
                self.drawLabels(position,atom)
                DrawSp.angle += math.pi #bond angle

class DrawSp2(Draw):
    position = (0,0,0)    
    angle = 0

    def __init__(self,mol):
        super(DrawSp2,self).__init__(mol)

    def drawLabels(self,position,atom):
        if Draw.showLabels == True:
            description = label(pos=position,text=str(atom.name),
                                xoffset=-20,yoffset=-20)
            Draw.labels.append(description)

    def drawCenterAtom(self):
        radius = self.center.radius
        color = self.center.color
        centerAtom = sphere(pos=DrawSp2.position,radius=radius,color=color)
        self.drawLabels(DrawSp2.position,self.center) #add label to center
        Draw.objects.append(centerAtom)

    def drawBonds(self,position,atom,molecule):
        double = molecule.containsDoubleBonds()
        triple = molecule.containsTripleBonds()
        if (double[atom] == True):
            bond1 = cylinder(pos=(0,10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,-10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
        elif (triple[atom] == True):
            bond1 = cylinder(pos=(0,25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
            bond3 = cylinder(pos=(0,-25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond3)
        else:
            bond = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond)

    def drawSurroundingAtoms(self,molecule):
        for atom in self.molecule:
            if atom != self.center:
                self.bondLength = (self.center.radius + atom.radius) * Draw.scale
                x = self.bondLength*math.cos(DrawSp2.angle)
                y = self.bondLength*math.sin(DrawSp2.angle)
                position = (x,y,0)
                newSphere = sphere(pos=position,radius=atom.radius,color=atom.color)
                Draw.objects.append(newSphere)
                self.drawBonds(position,atom,molecule)
                #add labels to each surrounding atom
                self.drawLabels(position,atom) 
                DrawSp2.angle += math.pi * 2/3 #all atoms in one plane

class DrawSp3(Draw):
    position = (0,0,0)    
    angle = 0

    def __init__(self,mol):
        super(DrawSp3,self).__init__(mol)

    def drawLabels(self,position,atom):
        if Draw.showLabels == True:
            description = label(pos=position,text=str(atom.name),
                                xoffset=-20,yoffset=-20)
            Draw.labels.append(description)

    def drawCenterAtom(self):
        radius = self.center.radius
        color = self.center.color
        centerAtom = sphere(pos=DrawSp3.position,radius=radius,color=color)
        self.drawLabels(DrawSp3.position,self.center)
        Draw.objects.append(centerAtom)

    def drawBonds(self,position,atom,molecule):
        double = molecule.containsDoubleBonds()
        triple = molecule.containsTripleBonds()
        if (double[atom] == True):
            bond1 = cylinder(pos=(0,10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,-10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
        elif (triple[atom] == True):
            bond1 = cylinder(pos=(0,25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
            bond3 = cylinder(pos=(0,-25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond3)
        else:
            bond = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond)

    def drawSurroundingAtoms(self,molecule):
        #109.5 degree bond angles
        directions = [(1,0,-1/(2**0.5)),(-1,0,-1/(2**0.5)),
                      (0,1,1/(2**0.5)),(0,-1,1/(2**0.5))]
        index = 0
        for atom in self.molecule:
            if atom != self.center:
                self.bondLength = (self.center.radius + atom.radius) * Draw.scale
                x = self.bondLength*directions[index][0]
                y = self.bondLength*directions[index][1]
                z = self.bondLength*directions[index][2]
                position = (x,y,z)
                newSphere = sphere(pos=position,radius=atom.radius,color=atom.color)
                Draw.objects.append(newSphere)
                #draw bonds based on positions of surrounding atoms
                self.drawBonds(position,atom,molecule)
                self.drawLabels(position,atom)
                DrawSp2.angle += 109.5 * (math.pi/180)
                index += 1

class DrawSp3d(Draw):
    position = (0,0,0) 
    theta = 0 #angle in x-y axis
    phi = 0 #angle from positive z-axis

    def __init__(self,mol):
        super(DrawSp3d,self).__init__(mol)

    def drawLabels(self,position,atom):
        if Draw.showLabels == True:
            description = label(pos=position,text=str(atom.name),
                                xoffset=-20,yoffset=-20)
            Draw.labels.append(description)

    def drawCenterAtom(self):
        radius = self.center.radius
        color = self.center.color
        centerAtom = sphere(pos=DrawSp3d.position,radius=radius,color=color)
        self.drawLabels(DrawSp3d.position,self.center)
        Draw.objects.append(centerAtom)

    def drawBonds(self,position,atom,molecule):
        double = molecule.containsDoubleBonds()
        triple = molecule.containsTripleBonds()
        if (double[atom] == True):
            bond1 = cylinder(pos=(0,10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,-10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
        elif (triple[atom] == True):
            bond1 = cylinder(pos=(0,25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
            bond3 = cylinder(pos=(0,-25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond3)
        else:
            bond = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond)

    def drawSurroundingAtoms(self,molecule):
        for atom in self.molecule:
            if atom != self.center:
                self.bondLength = (self.center.radius + atom.radius) * Draw.scale
                #draw in one axis then move to the next
                if (DrawSp3d.theta < 2*math.pi):
                    x = self.bondLength*math.cos(DrawSp3d.theta)
                    y = self.bondLength*math.sin(DrawSp3d.theta)
                    position = (x,y,0)
                    DrawSp3d.theta += math.pi * 2/3
                else:
                    z = self.bondLength*math.cos(DrawSp3d.phi)
                    position = (0,0,z)
                    DrawSp3d.phi += math.pi
                newSphere = sphere(pos=position,radius=atom.radius,color=atom.color)
                Draw.objects.append(newSphere)
                self.drawBonds(position,atom,molecule)
                self.drawLabels(position,atom)

class DrawSp3d2(Draw):
    position = (0,0,0)
    theta = 0
    phi = 0

    def __init__(self,mol):
        super(DrawSp3d2,self).__init__(mol)

    def drawLabels(self,position,atom):
        if Draw.showLabels == True:
            description = label(pos=position,text=str(atom.name),
                                xoffset=-20,yoffset=-20)
            Draw.labels.append(description)

    def drawCenterAtom(self):
        radius = self.center.radius
        color = self.center.color
        centerAtom = sphere(pos=DrawSp3d2.position,radius=radius,color=color)
        self.drawLabels(DrawSp3d2.position,self.center)
        Draw.objects.append(centerAtom)

    def drawBonds(self,position,atom,molecule):
        double = molecule.containsDoubleBonds()
        triple = molecule.containsTripleBonds()
        if (double[atom] == True):
            bond1 = cylinder(pos=(0,10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,-10,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
        elif (triple[atom] == True):
            bond1 = cylinder(pos=(0,25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond1)
            bond2 = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond2)
            bond3 = cylinder(pos=(0,-25,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond3)
        else:
            bond = cylinder(pos=(0,0,0),axis=position,radius=Draw.bondRadius,color=color.white)
            Draw.objects.append(bond)

    def drawSurroundingAtoms(self,molecule):
        for atom in self.molecule:
            if atom != self.center:
                self.bondLength = (self.center.radius + atom.radius) * Draw.scale
                if (DrawSp3d.theta < 2*math.pi):
                    x = self.bondLength*math.cos(DrawSp3d.theta)
                    y = self.bondLength*math.sin(DrawSp3d.theta)
                    position = (x,y,0)
                    DrawSp3d.theta += math.pi/2
                else:
                    z = self.bondLength*math.cos(DrawSp3d.phi)
                    position = (0,0,z)
                    DrawSp3d.phi += math.pi
                newSphere = sphere(pos=position,radius=atom.radius,color=atom.color)
                Draw.objects.append(newSphere)
                self.drawBonds(position,atom,molecule)
                self.drawLabels(position,atom)

def identifyClass(hybridization,molecule):
    #determine which class to use based on hybridization
    if hybridization == "linear":
        return DrawLinear(molecule.molecule)
    elif hybridization == "sp":
        return DrawSp(molecule.molecule)
    elif hybridization == "sp2":
        return DrawSp2(molecule.molecule)
    elif hybridization == "sp3":
        return DrawSp3(molecule.molecule)
    elif hybridization == "sp3d":
        return DrawSp3d(molecule.molecule)
    elif hybridization == "sp3d2":
        return DrawSp3d2(molecule.molecule)

def run(inputMol): 
    mol = inputSolver(inputMol)
    molecule = Molecule(mol) #create instance of molecule class
    #don't continue if structure is illegal
    if molecule.isLegalStructure() == False:
        Molecule.isLegal = False
    else:
        Molecule.isLegal = True
        hybridization = molecule.getHybridization()
        Molecule.details["Hybridization"] = hybridization
        struct = identifyClass(hybridization,molecule)
        struct.center = molecule.center
        if (len(molecule.molecule) > 2):
            struct.drawCenterAtom()
            struct.drawSurroundingAtoms(molecule)
            Molecule.details["Number of Bonds"] = molecule.getBondNumber()[1]
            Molecule.details["Number of Lone Electrons"] = molecule.getBondNumber()[2]
            Molecule.details["Steric Number"] = molecule.getStericNumber()
        else: #linear structure is created differently
            struct.drawAtoms(molecule)
