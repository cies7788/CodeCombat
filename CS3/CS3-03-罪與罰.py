while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        enemyPos = enemy.pos.x + " " + enemy.pos.y
        hero.say("敵人的位置在： " + enemyPos)

    gem = hero.findNearestItem()
    if gem:
        gemPos = gem.pos.x + " " + gem.pos.y
        hero.say("position of gem: " + gemPos)
