# 移動到'Eszter'並從她那裡得到神秘數字。
hero.moveXY(16, 32)
esz = hero.findNearestFriend().getSecret()

# 乘以3，減去2，得到'Tamas'的數字。
# 記住使用括號來確保計算順序正確。
# 移到'Tamas'並說出他的魔法數字。
tam = (esz * 3) - 2
hero.moveXY(24, 28)
hero.say(tam)

# 然後繼續 減去1然後乘4得到'Zsofi'的數字
# 移到'Zsofi'並說出她的魔法數字。
zso = (tam - 1)*4
hero.moveXY(32, 24)
hero.say(zso)

# 先將'Tamas'和'Zsofi'的數字相加，然後除以2得到'Istvan'的數字。
# 移到'Istvan'並說出他的魔法數字。
ist = (tam + zso)/2
hero.moveXY(40, 20)
hero.say(ist)

# 先將'Tamas'和'Zsofi'的數字相加，然後用'Zsofi'的數字減去'Istvan'的數字，再將兩個結果相乘得到'Csilla'的數字。
# 移動到'Csilla'並說出她的魔法數字。
csi = (tam + zso) * (zso - ist)
hero.moveXY(48, 16)
hero.say(csi)
