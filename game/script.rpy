# The script of the game goes in this file.


label start:
    #Patient generation is done separately to clean up code :)
    jump generate_patient

    label patient_entry:

        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.

        scene office

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
                        scene habitat_sprite
                        show patient_happy
                        patient "This is perfect, thank you!"

                "Savannah!":
                    if habitat != "savannah":
                        jump incorrect_room

                    else:
                        scene habitat_sprite
                        show patient_happy
                        patient "Oh yeah! I like it here."

                "Arctic!":
                    if habitat != "arctic":
                        jump incorrect_room

                    else:
                        scene habitat_sprite
                        show patient_happy
                        patient "It's so chilly here, just how I like it!"

                "Jungle!":
                    if habitat != "jungle":
                        jump incorrect_room

                    else:
                        scene habitat_sprite
                        show patient_happy
                        patient "Perfect! This is what I needed!"

        "Now, what seems to be the problem?"

        show patient_confused
        patient "Well, I seem to have a [illness]."

        show patient_neutral

        label illness_diagnosis:
            show patient_neutral
            menu:
                "Hm... is that a normal symptom for [patient.name] to be experiencing?"

                "Yes!":
                    if actualCondition != True:
                        show patient_confused
                        patient "Are you sure?"
                        jump illness_diagnosis

                    else:
                        scene habitat_sprite
                        show patient_happy
                        patient "Oh! That's good news!"

                "No!":
                    if actualCondition != False:
                        show patient_confused
                        patient "Really? That doesn't sound right."
                        jump illness_diagnosis

                    else:
                        scene habitat_sprite
                        show patient_happy
                        patient "Huh. Weird. Okay, thanks for telling me!"
                        $ patient_index = -1
                        jump generate_patient

    # This ends the game.

    return
