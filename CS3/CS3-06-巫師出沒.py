# 移動到 Zsofia 的身邊，從他那得到秘密號碼
hero.moveXY(18, 20)
zso = hero.findNearestFriend().getSecret()

# 將 Zsofia 的數字除以 4 得到 Mihaly 的數字。
# 移動到 Mihaly 旁邊並且告訴她魔幻數字(計算後的數字)
mih = zso / 4
hero.moveXY(30, 15)
hero.say(mih)

# 把 Mihaly 的號碼除以 5 來得到 Beata 的號碼
# 移動到 Beata 旁邊並且告訴她魔幻數字(計算後的數字)
bea = mih / 5
hero.moveXY(42, 20)
hero.say(bea)

# 將 Mihaly 的數字減去 Beata 的數字得到 Sandor 的數字。
# 移動到 Sandor 旁邊並且告訴她魔幻數字(計算後的數字)
san = mih - bea
hero.moveXY(38, 37)
hero.say(san)
