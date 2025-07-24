#function to count the tallest candles
def birthdayCakeCandles(candles):
    tallest = candles.count(max(candles))
    return tallest

#example to test the function
if __name__ == '__main__':

    candles = [3 ,2, 1, 3]
    result = birthdayCakeCandles(candles)

    print(str(result) + '\n')


