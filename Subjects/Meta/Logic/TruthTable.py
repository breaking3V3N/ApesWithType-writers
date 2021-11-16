OPERATIONS = {
    #unary operators
    '~': (lambda x: not x),

    #binary operators
    '\/': (lambda x,y: x or y),

    "/\\": (lambda x,y: x and y),

    #Implication; if...then
    #If P then Q is logically equivalent to not p or q
    "=>": (lambda x,y: not x or y),


    #Bi-Implication; if and only if
    #need to rephrase. Use the above
    "<==>":(lambda x,y: (x and y) )
}