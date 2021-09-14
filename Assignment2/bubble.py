mylist = [12, 5, 13, 8, 9, 65]

def bubble(badList):
    length = len(badList) - 2
    unsorted = True

    while unsorted:
        for element in range(0,length):
            unsorted = False

            if badList[element] > badList[element + 1]:
                hold = badList[element + 1]
                badList[element + 1] = badList[element]
                badList[element] = hold
                print badList
                unsorted = True

    return badList

print bubble(mylist)
