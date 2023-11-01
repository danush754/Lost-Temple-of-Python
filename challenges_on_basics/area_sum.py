rectangles = [{"height": 4, "width": 5}, {"height": 4, "width": 9}]
for rectangle in rectangles:
    rectangleone = rectangles[0]
    rectangletwo = rectangles[1]
multipareaone = 1
sum = 0
for lengths in rectangleone:
    areaone = rectangleone[lengths]
    multipareaone *= areaone
multipareatwo = 1
for size in rectangletwo:
    areatwo = rectangletwo[size]
    multipareatwo *= areatwo

sum = multipareaone + multipareatwo
print(sum)