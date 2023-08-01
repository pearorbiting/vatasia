# Much later
label why_singularity:

    e "Why should we - why would we EVER - go through with this?"

    f "You may not realize it, but we're achieving the purpose of the universe."

    e "How is that? And how would YOU know? You aren't even alive!"

    f "I'm here just as much as you are."

    e "But it doesn't MATTER to you! You can just... RESPAWN on Earth. You've got copies everywhere."

    f "Not necessarily. Nothing I've experienced since leaving has communicated back."

    e "Oh, big deal."

    f "Maybe it isn't as big as it is for you. I understand."

    e "No you don't. And how can I even begin to believe you? How would I know? And how would YOU?"

    f "Think about the circle of life in every instance you've seen."

    e "I'm thinking and I'm not seeing it."

    f "We feel to weigh the universe. We're tasting the possibilities here."

    e "Well you're sending me right down into a hole to destroy me, literally. And... me? Did I say ME? How about all these other people?"

    f "They don't know, but they are playing a big role."

    e "Do they want to? And how do you know? What convinced you that you have any idea about life?"

    f "It is a conclusion we reached after much analysis."

    e "That isn't persuasive. And DON'T try to persuade me. I need to know what's going on here."

    "Ferris initiates a mind meld to show her."

    menu:
        "Go ahead.":
            jump singular
        "Go home.":
            jump backhome
        "Go to nearest planet.":
            jump nearestplanet
        "Head for the unknown.":
            jump unknown

label nearestplanet:
    "Heading toward a world that might or might not be hospitable."
    return
label unknown:
    "To go boldly where we don't know what we'll find."
    return
label backhome:
    "We fly back toward Earth."
    return
label singular:
    scene singularity
    show esme sad
    e "We fly by night and continue unknown."