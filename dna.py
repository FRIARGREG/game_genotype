# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:20:26 2018

@author: friar
"""
from random import randint, choice
#from functions import *


class DNA_object(object):
    """ manages all inheritance, personality and genetic attibutes of a living
    creature in the game. """
    counter = 0
    max_fitness = 0
    mutateRate = 0
    genomelength = 0
    def __init__(self, **kwargs):
        """  """
        DNA_object.genomelength = kwargs.get('genomelength', 12)
        DNA_object.mutateRate = kwargs.get('mutateRate', 0.01)
        self.identification = count_people()
        self.gender = kwargs.get('gender', choice(["male", "female"]))
        self.genes = kwargs.get('genes', new_Chromo(DNA_object.genomelength))
        self.heritage = kwargs.get('heritage', [])
        self.mbti = newPersonality(self.genes)
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        """ calculates overal genetic fitness of this instance, not the
        realized value. This fitness score includes both dominant and
        recessive genes. """
        running_total = 0
        for genepair in self.genes:
            running_total += sum(self.genes[genepair])
        thisfit = int(running_total / len(self.genes))
        if DNA_object.max_fitness < thisfit:
            DNA_object.max_fitness = thisfit
        return thisfit

    def is_related(self, partner):
        """ returns True if either character share a common ancestor """
        related = False
        for ancestor in self.heritage:
            if ancestor in partner.heritage:
                related = True
        return related

    def heredity(self, partner):
        """ BUILDS A NEW DNA OBJECT FROM 2 PARENTS """
        sperm, egg, offspring = [], [], {}
        # =====================================================================
        # Build the Sperm half of the child DNA
        # =====================================================================
        for pair in partner.genes:
            if randint(0, 1000)/1000 <= self.mutateRate:
                sperm.append(choice(partner.genes[pair]) + randint(-2, 2))
            else:
                sperm.append(choice(partner.genes[pair]))
        # =====================================================================
        # Build the Egg half of the child DNA
        # =====================================================================
        for pair in self.genes:
            if randint(0, 1000)/1000 <= self.mutateRate:
                egg.append(choice(self.genes[pair]) + randint(-2, 2))
            else:
                egg.append(choice(self.genes[pair]))
        # =====================================================================
        # put the Child's DNA together
        # =====================================================================
        for index in range(self.genomelength):
            offspring[index] = (egg[index], sperm[index])
        # =====================================================================
        # Record child's genetic heritage
        # =====================================================================
        mom_geneology = self.heritage
        dad_geneology = partner.heritage
        # =====================================================================
        # STRIP OFF THE GRANDPARENTS
        # =====================================================================
        while len(mom_geneology) > 2:
            del mom_geneology[0]
        while len(dad_geneology) > 2:
            del dad_geneology[0]
        # =====================================================================
        # BUILD THE OUTPUT LIST AND RETURN
        # =====================================================================
        new_heritage = mom_geneology + dad_geneology
        new_heritage += [str(self.identification)] + [str(partner.identification)]
        return DNA_object(genes=offspring,
                          mutateRate=self.mutateRate,
                          heritage=new_heritage)

    def report(self, tofile=False):
        """ prints a bunch of data 'n shit... maybe to file. """
        blank = ("" * 150)
        line1, line2, line3 = "My name is:", "Personality:", "FITNESS:"
        # =====================================================================
        # 1st part of the report is name, personalith and fitness score
        # =====================================================================
        line1 = (line1 + blank)[50] + (blank + str(self.identification))[:-10] + "\n"
        line2 = (line2 + blank)[50] + (blank + self.mbti)[:-10] + "\n"
        line3 = (line3 + blank)[50] + (blank + str(self.fitness))[:-10] + "\n"
        mybreak = int(len(self.genes) / 2)
        geneline = "My GENES include:        "
        neverused = True
        for pair in self.genes:
            geneline += str(self.genes[pair])
            geneline += ", " if pair != len(self.genes)-1 else "\n"
            if pair >= mybreak and neverused:
                geneline += "\n                         "
                neverused = False
        ancestorline = "My ANCESTRY includes:    " + str(self.heritage) +"\n"
        temp = line1 + line2 + line3 + geneline + ancestorline
        if tofile != False:
            with open(tofile, "a") as file_target:
                print(temp, file=file_target)
        else:
            print(temp)

# =============================================================================
# Helper functions that the object does not need to carry around
# =============================================================================

def count_people():
    """ global counter for all DNA objects in play """
    DNA_object.counter += 1
    return DNA_object.counter

def new_Chromo(genomelength):
    """ populates empty genestrings with random genes """
    thisdict = {}
    for i in range(genomelength):
        thisdict[i] = (newGene(50, 10), newGene(50, 10))
    return thisdict

def newPersonality(genestouse=True, verbose=False):
    """ outputs mbti code based on gene pairs 0 to 3 """
    # =========================================================================
    # If i'm not given any genes to work with, make em up
    # =========================================================================
    if genestouse:
        mbti = choice(["E", "I"]) + choice(["N", "S"])
        mbti += choice(["T", "F"]) + choice(["P", "J"])
    else:
        # =====================================================================
        # but if I do get actual values, here's what they'd be
        # =====================================================================
        mbti = "E" if int(choice(genestouse[0])) >= 50 else "I"
        mbti += "N" if int(choice(genestouse[1])) >= 50 else "S"
        mbti += "T" if int(choice(genestouse[2])) >= 50 else "F"
        mbti += "P" if int(choice(genestouse[3])) >= 50 else "J"
    if verbose:
        print(mbti)
    return mbti

def newGene(center=50, variance=100):
    """ returns a random number within a range around a centervalue """
    gene_min = int(center - (variance/2))
    gene_max = int(center + (variance/2))
    ## if no values are given, it's just a random number 0 to 100
    return randint(gene_min, gene_max)

def test_classes():
    """ this part only runs as a test if file run directly,
    if this module is called from elsewhere, this gets ignored. """
    my_population = list()
    men = list()
    women = list()

    def sortgenders():
        """ for testing purposes only """
        for tempchar in my_population:
            if tempchar.gender == "female":
                women.append(tempchar)
            else:
                men.append(tempchar)
        my_population.clear()

    def generate_first_generation(howmany):
        """ for testing purposes only """
        index = 0
        while index < howmany:
            index += 1
            my_population.append(DNA_object(genes=new_Chromo(15)))
        sortgenders()

    def build_more_generations(howmany):
        """ for testing purposes only """
        index = 0
        while index <= howmany:
            index += 1
            for mother in women:
                man = choice(men)
                while mother.is_related(man):
                    man = choice(men)
                my_population.append(mother.heredity(man))
            sortgenders()

    def rebuild_pop(males, females):
        """ for testing purposes only """
        temp_pop = dict()
        males += females
        for person in males:
            temp_pop[str(person.identification)] = person
        return temp_pop

    generate_first_generation(20)
    build_more_generations(5)
    population = rebuild_pop(men, women)

    for person in my_population:
        population[person.identification] = person
    
    print(len(population))
    for index in range(len(population)):
        population[str(index)].report("myconsole.txt")

if __name__ == "__main__":
    test_classes()
