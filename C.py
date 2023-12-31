"""important constants"""

prune1 = [float("inf"), 32, 12, 4, 3, 3] #values for pruning your moves
prune2 = [float("inf"), float("inf"), 24, 8, 4, 3] #values for pruning opponent's moves

"""heuristic constants below"""

#positional evaluation for every position every piece can be on
poseval = [[],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, 0.5, -0.5, 1.0, 0.0, 0.0, -1.0, -0.5, 0.5, 0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, 1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, 3, 4, 4, 4, 4, 4, 4, 3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0, -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0, -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0, -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0, -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0, -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0, -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0, -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0], 
            [-2, -1, -1, -1, -1, -1, -1, -2, -1, 0.5, 0, 0, 0, 0, 0.5, -1,  -1, 1, 1, 1, 1, 1, 1, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1, -1, 0, 0.5, 1, 1, 0.5, 0, -1, -1, 0, 0, 0, 0, 0, 0, -1, -2, -1, -1, -1, -1, -1, -1, -2],
            [0, 0, 1, 3, 3, 1, 0, 0, -.5, 0, 0, 0, 0, 0, 0, -.5,-.5, 0, 0, 0, 0, 0, 0, -.5,-.5, 0, 0, 0, 0, 0, 0, -.5,-.5, 0, 0, 0, 0, 0, 0, -.5,-.5, 0, 0, 0, 0, 0, 0, -.5, .5, 1, 1, 1, 1, 1, 1, .5, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [-2, -1, -1, -.5, -.5, -1, -1, -2, -1, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1, -1, .5, .5, .5, .5, .5, 0.0, -1, 0, 0, 0.5, .5, .5, .5, 0.0, -.5, -.5, 0, .5, .5, .5, .5, 0, -.5, -1, 0, .5, .5, .5, .5, 0, -1, -1, 0, 0, 0, 0, 0, 0, -1, -2, -1, -1, -.5, -.5, -1, -1, -2],
            [6, 7, 4, 0, 0, 4, 7, 6, 2, 2, 0, 0, 0, 0, 2, 2, -1, -2, -2, -2, -2, -2, -2, -1,-2, -3, -3, -4, -4, -3, -3, -2, -3, -4, -4, -5, -5, -4, -4, -3,-3, -4, -4, -5, -5, -4, -4, -3,-3, -4, -4, -5, -5, -4, -4, -3,-3, -4, -4, -5, -5, -4, -4, -3]]
mateval = [0, 10, 30, 30, 50, 90, 200] #material evaluation for every piece

doubleP = -2 #(n^2-n)/2 how bad a doubled pawn and more is 
isolatedP = [-3.5, -1.5, 0] #how bad isolated pawns are, with both columns empty, then one column empty, then none
passedP = 3 #bonus for pawn being passed
passedpawncoef = 0.5 #how good it is for a pawn to be closer to promoting

castleval = 5 #how good it is to still be able to castle