def solvelist( list , position , N ):   # so we will first check the instructores and all their signed up classes.
    # give us the list of all the positions that we have explored
    # N a block cell
    if position == ( N - 1 , N - 1 ):
        return [ ( N - 1 , N - 1 ) ]
    x , y = position


    if x + 1 < N and list[x+1][y] == 1:   # so if x + 1 is less than N and the list ==1
        a = solvelist( list , ( x + 1 , y ) , N )       # make a equals to the solvelist
        if a != None:
            return [ (x , y ) ] + a


    if y + 1 < N and list[x][y+1] == 1:
        b = solvelist( list , (x , y + 1) , N )
        if  b != None:
            return [ ( x , y ) ] + b

#section a ,section b , section c , section d , section e
#sec a = section a


      #sec a --sec b -- sec c -- sec d -- sec e
list = [[ 1 ,   0 ,      1,      0 ,       0],
        [ 1 ,   1 ,      0,      1 ,       0],
        [ 0 ,   1 ,      0,      1 ,       0],
        [ 0 ,   1 ,      0,      0 ,       0],
        [ 1 ,   1 ,      1,      1 ,       1]
        ]
for i in [i for i,x in enumerate(list) if x == 0]:
    print(i)
# it will give me whenever there's a 1 , its position.

print (solvelist(list,(0,0),5))
