init python:
    import random

    #class for all the illnesses
    class Species():
        # constructor
        def __init__(self, species, habitat):
            self.species = species
            self.habitat = habitat

    #class for all the illnesses
    class Illnesses():
        # constructor
        def __init__(self, species, actualCondition, condition, medicine):
            self.species = species
            self.actualCondition = actualCondition
            self.condition = condition
            self.medicine = medicine

#Add more names and species as you like, as long as you follow the
#array conventions + each species being paired with its own habitat
#AND ALSO ADD AN APPROPRIATE IMAGE SET TO THE IMAGES FOLDER THANKS
define name_list = ["Bob", "Jessica", "Maria", "Shadow"]

#use "none" in habitat to mark as nonliving please and thank you :)
# list of species
define species_list = [
    Species("hedgehog", "forest"),
    Species("cheetah", "savannah"),
    Species("rock", "none"),
    Species("polarbear", "arctic"),
    Species("parrot", "jungle")
    ]

# list of illnesses; generic means it can impact any animal
# condition should be a singular word that can be madlibbed into "I think I have a [condition]"
# true means it's a real condition
# false means it's fake/shouldn't happen
# medicine should be in the form of "we can fix it with some [medicine]"
define illness_list = [
    Illnesses ("generic", True, "cough", "cough medicine"),
    Illnesses ("generic", True, "scrape", "bandages"),
    Illnesses ("generic", True, "itchy nose", "allergy medicine"),
    Illnesses ("generic", False, "clown nose", "none"),
    Illnesses ("hedgehog", True, "loose quill", "TBD"),
    Illnesses ("cheetah", True, "piece of food stuck in my teeth", "toothpicks"),
    Illnesses ("polarbear", True, "something", "TBD"),
    Illnesses ("parrot", True, "injured wing", "TBD")
    ]

#Patient generation
default patient_index = -1
default species = ""
default habitat = ""
default name_index = 0
default patient = Character(name = "placeholder", color = "#ffffff")
default illness_species = "generic"
default illness = ""
default actualCondition = True
default medicine = ""

#these automatically account for different list sizes so do NOT change
label generate_patient:
    if (patient_index == -1):
        $ patient_index = renpy.random.randint(0, len(species_list) - 1)
        $ species = species_list [patient_index].species
        $ habitat = species_list [patient_index].habitat
        $ name_index = renpy.random.randint(0, len (name_list) - 1)
        $ patient = Character(name = name_list [name_index], color = "#ffffff")

        $ illness_index = renpy.random.randint(0, len(illness_list) - 1)
        $ illness_species = illness_list[illness_index].species
        $ illness = illness_list[illness_index].condition
        $ actualCondition = illness_list[illness_index].actualCondition
        $ medicine = illness_list[illness_index].medicine

    jump patient_entry