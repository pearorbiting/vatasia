# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Esme", color="#00FF00")
define f = Character("Farheit", color="FFAA66") #was Ferris
define g = Character("Ganymede")
define h = Character("Han")
define s = Character("Sis")
define u = Character("Golden Girl")
define w = Character("Wolf")
define c = Character("Critic")
define m = Character("Cult Henchperson")
define b = Character("Boss")
define a = Character("Coworker 1")
define aa = Character("Coworker 2")
define p = Character("Paintball Shooter")
define o = Character("Political Forces")
define bo = Character ("Boba Owner")
define n = Character ("News Anchor")
    '''
    Cast:
    Esme
    Hansel (codename)  #Han, was Hal, could be Hansel and Han for short
    Gretel (codename) #Ganymede, was Greta, could be Gani or Gany or Gan or Gaia or Gaa for short
    Sis (codename)
    Golden Girl (codename)
    Wolf (codename)
    Critic (codename) - villain ruse
    Cult Henchpeople (codename)
    Farheit

    Boss (codename)
    Co1 (codename)
    Co2 (codename)
    Shooter (codename)
    Politicians (codename)
    Political Forces (codename)
    Boba Owner (codename)
    Boba Waiter (codename)
    Boba Floor Manager (codename)
    Boba Bartend (codename)
    Boba Clientele (codename)
    Movie People (codename)
    Submarine People (codename)
    News Anchors (codename)
    Crystallized Dead People (codename)
        Do they have ghosts? Are they whispering from the future singular? I rather like that idea.
    Retrocausal 1 (codename)

    there might be 40 different faces
    '''

image esme:
    "char/cybergal.jpg"

image farheit cheerful:
    "char/farheit cheerful.jpg"
    zoom 0.4

image morning city:
    "bg/morning city.jpg"
    zoom 0.5

image morning desk:
    "bg/morning desk.jpg"
    zoom 4

image dawn forest:
    "bg/dawn forest.jpeg"
    zoom 1.25

# The game starts here.
label start:

    call town from _call_ar_image
    call morning_office from _call_bq_hook
    call birthday from _call_cp_trigger
    call work_herring from _call_do_consideration
    call bring_friend from _call_en_acceptance
    call transit from _call_fm_departure
    call wind from _call_gl_complications
    call shadowy from _call_hk_pinch
    call jealous from _call_ij_mirror
    call token from _call_ji_newleaf
    call vanishing from _call_kh_sabotage
    call doublebound from _call_lg_destitution
    call nexus_fool from _call_mf_choice
    call whirlpool from _call_ne_twists
    call carnival from _call_od_acceleration
    call which_merger_event from _call_pc_peak
    call piled from _call_qb_updating
    call served from _call_ra_resolved
    
    call why_singularity from _call_why_singularity
    call wake from _wake
    call approach_singularity from _call_approach_singularity

    '''
    Props:
    Box with Crystal
    '''

    # This ends the game.
    return