while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("Friend " + friend.id)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.say("Enemy " + enemy.id)
