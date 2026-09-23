# The script of the game goes in this file.


label start:
    #Patient generation is done separately to clean up code :)
    jump generate_patient

    label patient_entry:

        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.

        scene office with fade

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
                        scene habitat_sprite with fade
                        show patient_happy
                        patient "This is perfect, thank you!"

                "Savannah!":
                    if habitat != "savannah":
                        jump incorrect_room

                    else:
                        scene habitat_sprite with fade
                        show patient_happy
                        patient "Oh yeah! I like it here."

                "Arctic!":
                    if habitat != "arctic":
                        jump incorrect_room

                    else:
                        scene habitat_sprite with fade
                        show patient_happy
                        patient "It's so chilly here, just how I like it!"

                "Jungle!":
                    if habitat != "jungle":
                        jump incorrect_room

                    else:
                        scene habitat_sprite with fade
                        show patient_happy
                        patient "Perfect! This is what I needed!"

        show patient_neutral
        "Now, what seems to be the problem?"

        patient "Well, I seem to have a [illness]."

        label illness_diagnosis:
            show patient_neutral
            menu:
                "Hm... does [patient.name] have a treatable condition?"

                "Yes!":
                    if actualCondition != True:
                        show patient_confused
                        patient "Are you sure?"
                        jump illness_diagnosis

                    else:
                        show patient_happy
                        patient "Oh! That's good news!"

                "No!":
                    if actualCondition != False:
                        show patient_confused
                        patient "Really? That doesn't sound right."
                        jump illness_diagnosis

                    else:
                        show patient_happy
                        patient "Huh. Weird. Okay, thanks for telling me!"
                        scene black with dissolve
                        $ patient_index = -1
                        jump generate_patient

        show patient_neutral
        patient "If what I have can be cured, can you help?"

        label medicine_time:
            show patient_neutral

            label answer_generator:
                default answer_list = ["", "", "", "", ""]
                default has_correct = False
                default i = 0
                while (i < 5):
                    label random_medicine:
                        $ medicine_index = renpy.random.randint(0, len(medicine_list) - 1)

                    if (answer_list.count(medicine_list [medicine_index]) > 0):
                        jump random_medicine

                    $ answer_list [i] = medicine_list [medicine_index]
                    if (medicine_list [medicine_index] == medicine):
                        $has_correct = True

                    $i = i + 1

            if has_correct != True:
                #reloop for a set that has the right answer as an option
                jump answer_generator

            menu:
                "Which treatment best fits [patient.name]'s problem?"

                "What about [answer_list [0]]?":
                    if answer_list [0] != medicine:
                        jump incorrect_treatment

                    else:
                        show patient_happy
                        patient "Yay! Thank you!"

                "Let's try [answer_list [1]]!":
                    if answer_list [1] != medicine:
                        jump incorrect_treatment

                    else:
                        show patient_happy
                        patient "Yay! Thank you!"

                "I think we should use [answer_list [2]]!":
                    if answer_list [2] != medicine:
                        jump incorrect_treatment

                    else:
                        show patient_happy
                        patient "Yay! Thank you!"

                "Oh, [answer_list [3]]! That's the answer!":
                    if answer_list [3] != medicine:
                        jump incorrect_treatment

                    else:
                        show patient_happy
                        patient "Yay! Thank you!"

                "I think [answer_list [4]] will help you!":
                    if answer_list [4] != medicine:
                        jump incorrect_treatment

                    else:
                        show patient_happy
                        patient "Yay! Thank you!"

            $ patient_index = -1
            scene black with dissolve
            jump generate_patient
                

    # This ends the game.

    return
