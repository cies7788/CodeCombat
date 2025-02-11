# 您將獲得一定數量的金幣、銀幣和銅幣。
# 將每個數學運算的結果保存到變量中，並在每一步說出結果。
wizard = hero.findNearestFriend()
goldCoins = wizard.goldCoins
silverCoins = wizard.silverCoins
bronzeCoins = wizard.bronzeCoins

# 將金幣和銀幣的數目相加，然後說出結果。
gs = (goldCoins+silverCoins)
hero.say(gs)

# 用前一個結果減去銅幣的數量，然後說出新的結果。
gs = gs - bronzeCoins
hero.say(gs)

# 將前一個結果除以3，然後說出新的結果。
gs = gs / 3
hero.say(gs)

# 將前一個結果乘以2，然後說出新的結果。
gs = gs * 2
hero.say(gs)
