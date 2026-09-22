# The script of the game goes in this file.

init python:
    import random

#Add more names and species as you like, as long as you follow the
#array conventions + each species being paired with its own habitat
define name_list = ["Bob", "Jessica", "Maria", "Shadow"]
#use "none" in habitat to mark as nonliving please and thank you :)
define species_list = ["hedgehog", "cheetah", "rock", "polar bear", "parrot"]
define habitat_list = ["forest", "savannah", "none", "arctic", "jungle"]

#generic stuff
default patient_index = -1
default species = ""
default habitat = ""
default name_index = 0
default patient = Character(name = "placeholder", color = "#ffffff")

label start:
    #these automatically account for different list sizes so do NOT change
    label generate_patient:
        if (patient_index == -1):
            $ patient_index = renpy.random.randint(0, len (species_list) - 1)
            $ species = species_list [patient_index]
            $ habitat = habitat_list [patient_index]
            $ name_index = renpy.random.randint(0, len (name_list) - 1)
            $ patient = Character(name = name_list [name_index], color = "#ffffff")

        jump patient_entry

    label patient_entry:

        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.

        scene bg room

        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.

        show patient_neutral

        # These display lines of dialogue.

        patient "Hello! I would like to get checked in, please."

        "Time to fill out the paperwork!"
        
        label living_or_not:
            menu:
                "First, is the patient a living animal?"

                "Yes!":
                    if habitat == "none":
                        #Add different flavor text here later
                        show patient_confused
                        patient "Hm... that doesn't feel right..."
                        jump living_or_not

                    else:
                        show patient_happy
                        patient "Yep, that's right!"

                "No!":
                    if habitat != "none":
                        #Add different flavor text here later
                        show patient_confused
                        patient "Hm... I'm not sure that's the case..."
                        jump living_or_not

                    else:
                        show patient_happy
                        patient "Oh yeah! I'm not an animal. Silly me."
                        $ patient_index = -1
                        jump generate_patient

        label which_room:
            show patient_neutral
            menu:
                "Next, which habitat would best fit our patient?"

                "Forest!":
                    if habitat != "forest":
                        jump incorrect_room

                    else:
                        show patient_happy
                        patient "This is perfect, thank you!"

                "Savannah!":
                    if habitat != "savannah":
                        jump incorrect_room

                    else:
                        show patient_happy
                        patient "Oh yeah! I like it here."

                "Arctic!":
                    if habitat != "arctic":
                        jump incorrect_room

                    else:
                        show patient_happy
                        patient "It's so chilly here, just how I like it!"

                "Jungle!":
                    if habitat != "jungle":
                        jump incorrect_room

                    else:
                        show patient_happy
                        patient "Perfect! This is what I needed!"

    # This ends the game.

    return
