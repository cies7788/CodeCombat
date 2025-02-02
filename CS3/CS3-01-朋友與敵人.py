while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("去戰鬥, " + friend.id + "!")
    # 尋找最近的敵人，然後告訴他們"Go Away"。
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.say("Go Away, " + enemy.id)
