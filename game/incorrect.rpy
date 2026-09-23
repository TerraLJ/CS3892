#To prevent looping to these by mistake, I'm separating them to here
label incorrect_room:
    show patient_confused
    if habitat == "forest":
        patient "I think I need somewhere with more trees and not too much moisture, if that makes sense."
    elif habitat == "savannah":
        patient "Hm... I think I need somewhere warm and drier, you know?"
    elif habitat == "arctic":
        patient "It's not cold enough for me there."
    elif habitat == "jungle":
        patient "Um... can you look for somewhere with more humidity and many trees?"
    else:
        patient "This doesn't feel right..."

    jump which_room

label incorrect_treatment:
    #add more options to give more hints for specific conditions
    show patient_confused
    if medicine == "cough medicine":
        patient "I think something to soothe my throat would help..."
    elif medicine == "bandages":
        patient "Can you cover my wound for me?"
    elif medicine == "allergy medicine":
        patient "Maybe... can I have something that would help with my allergies?"
    elif medicine == "toothpicks":
        patient "I don't think that would help me clean my mouth..."
    else:
        patient "This doesn't feel right..."

    jump medicine_time