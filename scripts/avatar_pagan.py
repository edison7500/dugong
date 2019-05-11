import pagan

# Acquire an arbitrary string.
inpt = 'jiaxin'

# Use pagan to generate the avatar object based on that input.
# Optional: You can choose which hash function should be used.
# The functions are available as constants.
# Default: MD5.
img = pagan.Avatar(inpt, pagan.SHA512)

# img.show()

outpath = '/tmp'
filename = inpt
img.save(outpath, filename)



