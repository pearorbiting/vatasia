# Dead Center (Peak)
```
After struggling with crew, AI, controls, ruses, and conscience, Esme has set the craft's path. Paintball of Fate,
moderated, modulated. Redirect.

Note: the realism and non-reductiveness of storyworld elements contrasts The Crunch!
```
#   < Ersatz Birthday (Trigger)

# call singular_peak from _call_singular_peak
# call slingshot_peak from _call_slingshot_peak
# call boldlygo_peak from _call_boldlygo_peak

label which_merger_event:
    went = "singular"  # a little defaultitude
    match went:
        case "singular":
            call singular_peak
        case "boldly":
            call boldlygo_peak
        cast "slingshot":
            call slingshot_peak

label singular_peak:
    return
label slingshot_peak:
    return
label boldlygo_peak:
    return