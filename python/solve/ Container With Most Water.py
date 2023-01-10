def maxArea(height):
    max_area = 0
    distance = 0 # distance 가장 길고

    # height 끼리 뺏을때 가장 작은 수 기준으로

    for i, h in enumerate(height):

        for j in range(len(height)-1, 0, -1):
            distance = (len(height) - i) - 1
            min_h = min(h, height[j])

            print(min_h * distance)




    # for i, h in enumerate(height):
    #     distance = (len(height) - i) - 1
    #     # min_h = min(h, height[-(i+1)])
    #     min_h = min(h, distance)
    #     max_area = min_h * distance
    #
    #
    #
    #     print(h, distance, height[-(i+1)])
    #     print(max_area)


    return 0


height = [1,8,6,2,5,4,8,3,7]
maxArea(height)