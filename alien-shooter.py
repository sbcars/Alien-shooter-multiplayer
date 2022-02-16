import pgzrun

alien = Actor("player1")
bullet = Actor("bullet1")
bullet1_state = "ready"

alien2 = Actor("player2")
alien2.pos = (750, 100)
bullet2 = Actor("bullet2")
bullet2.pos = alien2.pos
bullet2_state = "ready"

health1 = 3
health2 = 3

heart1 = Actor("life")
heart1.pos = (150, 50)
heart2 = Actor("life")
heart2.pos = (100, 50)
heart3 = Actor("life")
heart3.pos = (50, 50)
heart4 = Actor("life")
heart4.pos = (650, 50)
heart5 = Actor("life")
heart5.pos = (700, 50)
heart6 = Actor("life")
heart6.pos = (750, 50)

music.play("intro_action")

def update():
    global bullet1_state, bullet2_state, health1, health2
    screen.clear()
    screen.fill("green")
    alien.draw()
    alien2.draw()
    
    if health1 >= 1:
        heart3.draw()
        

    if health1 >= 2:
        heart2.draw()
        
    if health1 >= 3:
        heart1.draw()
        
    if health2 >= 1:
        heart4.draw()
        

    if health2 >= 2:
        heart5.draw()
        
    if health2 >= 3:
        heart6.draw()
        
    if bullet1_state == "ready":
        bullet.pos = alien.pos
        
    if bullet2_state == "ready":
        bullet2.pos = alien2.pos
    
    if keyboard.w:
        alien.y -= 5
        
    if keyboard.up:
        alien2.y -= 5
        
    if keyboard.s:
        alien.y += 5
        
    if keyboard.down:
        alien2.y += 5
        
    if keyboard.LSHIFT:
        bullet1_state = "shot"
        
    if keyboard.SPACE:
        bullet2_state = "shot"
        
    if bullet1_state == "shot":
        bullet.draw()
        bullet.x += 14
        
    if bullet2_state == "shot":
        bullet2.draw()
        bullet2.x -= 14
        
    if bullet.colliderect(alien2):
        bullet.pos = alien.pos
        bullet1_state = "ready"
        health2 -= 1
        
    if bullet2.colliderect(alien):
        bullet2.pos = alien2.pos
        bullet2_state = "ready"
        health1 -= 1
        
    if bullet.x >= 800:
        bullet1_state = "ready"
        
    if bullet2.x <= 0:
        bullet2_state = "ready"
    
    if health1 == 0:
        screen.draw.text("Game Over\nPlayer 2 Wins\nPress Right Shift", topleft = (200, 100), color=("red"), fontsize = 100, shadow = (1,1))
        alien.image = "player1 hurt"
        if keyboard.RSHIFT:
            health1 = 3
            health2 = 3
            alien.image = "player1"

    if health2 == 0:
        alien2.image = "player2 hurt"
        screen.draw.text("Game Over\nPlayer 1 Wins\nPress Right Shift", topleft = (200, 100), color=("red"), fontsize = 100, shadow = (1,1))
        if keyboard.RSHIFT:
            health1 = 3
            health2 = 3
            alien2.image = "player2"

    
pgzrun.go()
