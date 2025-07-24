import os
def birthdayCakeCandles(candles):
    # Write your code here
    tallest = candles.count(max(candles))
    return tallest


if __name__ == '__main__':

    candles = [3 ,2, 1, 3]
    result = birthdayCakeCandles(candles)

    print(str(result) + '\n')


