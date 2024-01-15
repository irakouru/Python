import random

class CoinFlipping:
    @staticmethod
    def toss_coin():
        result = random.randint(0, 1)
        return result

number_of_throws = int(input("Give the number of tosses: "))
number_of_heads = 0
number_of_tails = 0

for i in range(number_of_throws):
    print(f"Toss number {i + 1}:")   
    coin_flip = CoinFlipping.toss_coin()
    print(f"The coin landed on: {coin_flip}")
    
    if coin_flip == 0:
        #print("The coin landed on: tail")
        number_of_tails += 1
    else:
        #print("The coin landed on: head")
        number_of_heads += 1

print(f"\nThe number of heads: {number_of_heads}\nThe number of tails: {number_of_tails}")

