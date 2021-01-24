def maxDifference(px):
    diff = px[1] - px[0]
    minimum = px[0]

    for i in range(1, len(px)):
        if (px[i] - minimum) > diff:    diff = px[i] - minimum
        if px[i] < minimum: minimum = px[i]
    if diff <= 0:    return -1
    return diff

print(maxDifference([7,9,5,6,3,2]))