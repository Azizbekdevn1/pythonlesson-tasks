def coupleIs(numbers):
    couplelist = []
    for i in numbers:
        if i % 2 == 0:
            couplelist.append(i)

    return couplelist


# nums = [2, 3, 4, 5, 5, 678, 64, 43, 76, 98, -43]
# print(CoupleIs(nums))
