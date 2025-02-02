potionsOnTheWall = 10
numToTakeDown = 1
while True:
    hero.say(potionsOnTheWall + " potions of health on the wall!")
    # 唱出下一句：
    hero.say(potionsOnTheWall + "potions of health!")
    # 唱出下一句：
    hero.say("Take " + numToTakeDown + " down, pass it around!")
    potionsOnTheWall -= numToTakeDown
    # 唱出最後一句：
    hero.say(potionsOnTheWall + "potions of health on the wall.")
