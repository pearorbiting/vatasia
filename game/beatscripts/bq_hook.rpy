# Morning Office (Hook)
```
Intro in Esme's home office.

Farheit, her AI, banters with her and she decides whether to eat breakfast before sleeping.

- Plant crash seed (why worked all night)
- Plant paintball seed
- Boba tea
```
#   > Piled Outro (Updating Reversal)

label morning_office:
    "This is the introduction."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "The city murmurs."

    scene morning city with pixellate

    "Dawn whispers..."

    scene dawn forest with dissolve
        
    "...out of sight..."
    "...then closer, touching air and snow."

    scene morning desk with dissolve

    #show esme sleepy
    show esme at top with dissolve

    # These display lines of dialogue.

    e "(Sigh.) I thought it was midnight. Feels like last I checked, it was a summer afternoon."

    show esme at topleft with ease:
        alpha 0.2

    #show ferris silly at right
    show farheit cheerful at truecenter with moveinright

    f "Shall I make breakfast to end the day, Ms. Hyperbole?"

    menu:
        "anNOYing":
            #show esme# suspicious
            hide farheit
            show esme:
                alpha 1
            e "Don't ever call me Mizz again, FUZZ."
            f "Are you referring to the hair on the chin I don't have? I haven't shaved. Hope you don't enjoy the look."
            e "Did I say I was in a funny mood? This isn't even funny for a funny mood. Try again."
            f "Commencing light treading."
            e "Thank you for not being as annoying as a human."
        "whatevs":
            show esme# laughing
            e "Fucker, I'll take it."

    f "Omelette, half the yolk, onions and mushrooms?"

    menu:
        "yay":
            e "That's fine. It was maybe a tiny bit funny."
            f "I'll try to do better next time... if I remember."
            e "I rarely know if you're serious, Ferris."
        "nay":
            e "Skip it, please. I'm meeting for boba tea later. I'll get an appetizer... or three."


# # Hook/Trigger Segue - boba with Greta
#     choice about whether to call to confirm
#     call from bf... or his friend? passes phone? is that futuristic?
# call boba from _call_boba

#Boba with Friend
label boba:
    
    e "Should we branch out and meet at the carousel later?"
    g "Hell yes."
    h "Hell to the HELL to the yes. To the hell to the YESes??"