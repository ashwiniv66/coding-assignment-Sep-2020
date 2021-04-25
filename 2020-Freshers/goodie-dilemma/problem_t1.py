def getGoodies():
    goodiesDic = {}
    goodiesArr = []
    with open("./input.txt", "r") as fhandle:
        numPeople = None
        titleFlag = False
        for line in fhandle:
            tempList = line.split(":")
            if numPeople is None:
                numPeople = int(tempList[1])
                continue
            elif titleFlag is False:
                titleFlag = True
                continue

            goodiesDic.update({str(int(tempList[1])): tempList[0]})
            goodiesArr.append(int(tempList[1]))
    return (goodiesDic, goodiesArr, numPeople)


def getMinMax(goodiesList, numPeople):
    goodiesList.sort()
    differenceList = list(
        map(
            lambda idxOne: goodiesList[idxOne + numPeople - 1] - goodiesList[idxOne],
            range(len(goodiesList) - (numPeople)),
        )
    )
    minDifference = min(differenceList)
    idx = differenceList.index(minDifference)
    goodiesGiftedPrice = goodiesList[idx : idx + numPeople]
    return (minDifference, goodiesGiftedPrice)


def getGifted(priceList, goodiesDic):
    gifted = []
    priceStrList = list(map(lambda price: str(price), priceList))

    for price in priceStrList:
        gifted.append("{} : {}".format(goodiesDic[price], price))
    return gifted


def printOutput(goodiesGifted):
    with open("./output.txt", "w") as fhandle:
        for line in goodiesGifted:
            print(line)
            fhandle.write(line + "\n")
    return


if __name__ == "__main__":
    (goodiesDic, goodiesList, numberOfPeople) = getGoodies()
    (minDifference, goodiesGiftedPrice) = getMinMax(goodiesList, numberOfPeople)
    goodiesGifted = getGifted(goodiesGiftedPrice, goodiesDic)
    printOutput(goodiesGifted)