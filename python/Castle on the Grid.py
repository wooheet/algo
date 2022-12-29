def minimumMoves(grid, startX, startY, goalX, goalY):
    start = (startX, startY)
    goal = [goalX, goalY]
    x_index = [i for i, x in enumerate(grid) if x == '.X.']
    print(x_index)
    print()

    # while True:
    #     if startX[0] < goalX[0]:
    #         if x_index[0] != goalX[0]
    #         startX[0]

# ...
# .X.
# ...


grid = ['...', '.X.', '...']
# grid = ['.X.', '.X.', '...']
minimumMoves(grid, 0,0,1,2)
# minimumMoves(grid, 0,0,1,0)
