# 走到 Laszlo 旁邊並聽取他的秘密數字。
hero.moveXY(30, 13)
las = hero.findNearestFriend().getSecret()

# 向 Laszlo 的數字中加7就能得到 Erzsebet的號碼
# 走到 Erzsebet 旁邊並說出她的魔法數字。
erz = las + 7
hero.moveXY(17, 26)
hero.say(erz)

# 將 Erzsebet 的數字除以 4 得到 Simoyi 的數字。
# 走到 Simonyi 旁邊並說出他的數字。
sim = erz / 4
hero.moveXY(30, 39)
hero.say(sim)

# 將 Simonyi 的數字乘以 Laszlo 的數字得到 Agata 的數字。
# 走到 Agata 旁邊並說出她的數字。
aga = sim * las
hero.moveXY(43, 26)
hero.say(aga)
