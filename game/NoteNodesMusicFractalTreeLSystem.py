# This builds a harmony tree for a particular piece of music, that allows for foldbacks among the branches.

# An interesting concept is that each dimension (prime) can be subdivided like the octaves using an ET scheme.
# And this can refer to the ET intervals.
# For example, if we want to subdivide the tritave, it's easy! What's a trivate based on? The P5. What's a P5 in ET?
# It's 7 semitones. Right. Good. Ok. So if we equally subdivide a tritave by 7, even if that tritave is purer or less
# pure than the ET P5, we'll get scale degrees very closely matching the familiar ones. This might sound like a piece
# of trivia, but it's neat and a jumping-off point for further elaboration. For example, we can split those 7 in 2
# (tritaves are bigger than octaves) for an ET chromatic scale of 14 degrees up to the P5 (3rd harmonic) that is an
# octave and a half above.
# This same trick - referring to the ET interval between two nodes and extrapolating - can be used for any prime or
# really any interval. We start with the ET distance and subdivide (or sometimes reduce).
# For an example of reducing, consider the 5th harmonic. This is M3. What's M3 in ET? It's 4 semitones, or 2 tones. So
# we can subdivide a pentatave (however it's tune, whether pure, Pythagorean, 12-ET, or some other approach) by 4 and
# get a very familiar or even identical set of degrees. Yet we could also subdivide by 2 (in this case basically whole
# tones would be the result), or by 8, or 12, or 16, etc.
# This should get more interesting when applied to harmonics 7, 11, 13, and beyond.
# Note also that uneven scale patterns can of course be used after we get the ET along that dimension, and these could
# echo (or not, or partially) the parent scale pattern (alternation or bigger and smaller spaces).

# There are 3 closely related entities:
# 1) an interval, like M3
# 2) an abstract note based on a root, like C# (with A as root)
# 3) a specific register for that note, comprising a specific frequency, like C#3 (with perhaps A3 as root)

# This notenode below is for 2), the abstract note. Instances of it together form a harmonic network
# that compliments the underlying theoretical lattice (the vector space).
# The prime exponent vector is for 1).
# And of course we can use a frequency on a particular note performance/instance/object for 3).

# I'm not exactly sure how to jump around to connect the branches/twigs (I reserve "leaves" for the timbre components).
# Maybe it would be useful to have a multidimensional lookup array / hash? of pointers back to the nodes in the tree,
# so that from any position, one can look at the vector, do simple arithmetic, and jump along any and several dimensions
# at once, landing on the correct node. Without a lookup, the tree would have to be fully connected with pointers,
# which I suppose is possible but could be tedious. A lookup array/tensor of pointers could simplify things.
# That would give every node an address in the vector space and a sort of "mailbox" along with it, if you will.

# If all the notes are put in a single linear array by (reduced/canonical) sharpness, the weights can then be used to do
# weighted random selection. I think you'd sum all the weights and that would be the integer you'd use, and you might
# want to use some sort of lookup to find the correct bin once you have the random number. I forget exactly how
# the binning is usually done for weighted random sampling, but it's standard and I've done it several times. You could
# of course use an array of (repeated as needed) pointers or ID values or whatever. Is that the simplest way, though?

class notenode:
    # references to notenodes in these directions, by multiplying once
    x3 = None
    x5 = None
    x7 = None
    x11 = None
    x13 = None

    # references to notenodes in these directions, by dividing once
    d3 = None
    d5 = None
    d7 = None
    d11 = None
    d13 = None

    # corresponding weights for multiplying, with 0 meaning never (reference above can be null) and 1 default for on
    wx3 = 0
    wx5 = 0
    wx7 = 0
    wx11 = 0
    wx13 = 0

    # corresponding weights for dividing, see above
    wd3 = 0
    wd5 = 0
    wd7 = 0
    wd11 = 0
    wd13 = 0

    # the weights can be interpreted as probabilities, amplitudes, layers allowed to go in (a stack counter)

    prime_position_vector_from_root = (0,0,0,0,0)
    prime_position_vector_from_previous_layer = (0,0,0,0,0)  # unsure this is useful; can always subtract vectors for comparison
    # could instead (if needed) use a "last" pointer to the preceding root, rather than a vector
    # there's also a version (for specific instances... maybe leave that for later or descended objects) with the 2 exp
    pointer_to_root = None
    pointer_to_parent = None

    reducedcompositemultiplier = 1 # this is the canonical value of this interval with respect to the root, no 2s in it
    # that's basically a universal conceptual address for that note... then it's adjusted by octave (or tritave, etc)
    # aka "integer_address"? or "composite_address"?
    layer_depth = 0 #  (this might be inferred in simple cases from the vector representation but not always?)

# array or linked list or vector or something with all the notes in a row
# can have one of these for each layer perhaps
# want a canonical top level layer for melody and also a kitchen sink also maybe intermediate layers
class topscale
class kitchenssinkscale

# I think two layers in covers most of Western music, so no need yet to go very deep

# should/could probably/possibly have a stack concept, or maybe that's the case for the actual frequency instances, so
# they remember how far into the tree they are? but that's tracked by layer_depth, hm

# there's a version of the above that then knows which exact octave (thanks to the power of 2) and frequency (thanks
# to the exact root frequency)

# I like the concept of a variant of Hz that rescales the frequency of the root to 1... was calling it A-urtz but there
# must be a better name
# Arz?
# Perz (after primes)?
# maybe the former is unreduced and the latter is reduced, no 2... hm, except then the former will be a fraction often
# don't want to be confusing, least of all with myself

# remember this is a tree, and remember foldbacks link the branches in surprising ways
# also, at a certain depth, can convert from new melodic/harmonic nodes to, beyond that, components of timbre
# also can somehow work rhythm ratios in as it's the same concept, maybe earlier, before the harmonic stuff?