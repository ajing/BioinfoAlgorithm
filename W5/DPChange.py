'''
    Dynamic programming calculate MinNumCoins
'''

def DPChange(money, coins):
    min_num_coins = dict()
    min_num_coins[0] = 0
    for m in range(1, money + 1):
        min_num_coins[m] = float("inf")
        for i in coins:
            if m >= i:
                if min_num_coins[m - i] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - i] + 1
    return min_num_coins[money]

if __name__ == "__main__":
    infile = "tmp"
    infile  = "/home/ajing/Downloads/dataset_71_8.txt"
    money, coins = [x.strip().split(",") for x in open(infile)]
    money = int(money[0])
    coins = [int(x) for x in coins]
    print DPChange(money, coins)
