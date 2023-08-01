# Breakfast Afar (Resolved Image)
```
What does breakfast or another meal, or morning for that matter, look like on this new path?
```
#   < Town Intro (Image)

label served:
    went = "singular"  # a little defaultitude
    match went:
        case "singular":
            call singular_breakfast
        case "boldly":
            call boldlygo_breakfast
        cast "slingshot":
            call slingshot_breakfast

label singular_breakfast:
    return
label slingshot_breakfast:
    return
label boldlygo_breakfast:
    return