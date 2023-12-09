def on_a_pressed():
    global canShoot, projectile
    if canShoot:
        canShoot = False
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . 3 3 3 3 3 3 3 . . . . 
                            . . . . 3 3 1 1 1 1 1 3 3 . . . 
                            . . . . 2 1 1 1 1 1 1 1 2 . . . 
                            . . . . 2 2 1 1 1 1 1 2 2 . . . 
                            . . . 3 3 2 3 3 1 3 3 2 3 3 . . 
                            . . 3 3 . . 2 3 1 3 2 . . 3 3 . 
                            . . 1 . . . 2 3 1 3 2 . . . 1 . 
                            . . 1 3 . . . 3 1 3 . . . 3 1 . 
                            . . . 1 1 3 3 3 3 3 3 3 1 1 . . 
                            . . . . . 1 1 1 1 1 1 1 . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . . 2 . . . . . . . 
                            . . . . . . . . 2 . . . . . . .
            """),
            cursor,
            0,
            -100)
        projectile.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
        music.play(music.melody_playable(music.pew_pew),
            music.PlaybackMode.UNTIL_DONE)
        
        def on_after():
            global canShoot
            canShoot = True
        timer.after(shootCooldown, on_after)
        
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite):
    sprites.destroy(projectile, effects.fire, 500)
    sprites.destroy(otherSprite, effects.disintegrate, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_hit_wall(sprite, location):
    if tiles.tile_is(tiles.location_of_sprite(sprite), sprites.vehicle.road_turn3):
        sprite.vy = 0
        sprite.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite),
        sprites.vehicle.road_intersection1):
        sprite.vy = 0
        sprite.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite),
        sprites.vehicle.road_intersection4):
        sprite.vy = enemySpeed
        sprite.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite), sprites.vehicle.road_turn4):
        sprite.vy = 0
        sprite.vx = 0 - enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite),
        sprites.vehicle.road_intersection2):
        sprite.vy = enemySpeed
        sprite.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite),
        assets.tile("""
            myTile5
        """)):
        sprite.vy = 0 - enemySpeed
        sprite.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite),
        sprites.vehicle.road_intersection3):
        sprite.vy = 0
        sprite.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite), sprites.vehicle.road_turn2):
        sprite.vy = enemySpeed
        sprite.vx = 0
    else:
        sprites.destroy(sprite, effects.blizzard, 500)
        info.change_life_by(-1)
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

newEnemy: Sprite = None
projectile: Sprite = None
cursor: Sprite = None
enemySpeed = 0
shootCooldown = 0
canShoot = False
info.set_life(3)
info.set_score(0)
canShoot = True
shootCooldown = 1000
tiles.load_map(tiles.create_map(tilemap("""
    level0
""")))
enemySpeed = 20
effects.star_field.start_screen_effect()
cursor = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . f f . . . . . f f f . . . . . 
            f 1 1 f . . f f 1 1 1 f . . . . 
            f 1 1 1 f f 1 1 f 1 1 1 f . . . 
            f 1 1 1 1 1 f 1 1 1 1 1 f . . . 
            . f 1 1 1 1 1 1 1 1 f 1 1 f . . 
            . . f 1 1 1 1 1 f 1 1 f 1 f . . 
            . . f f 1 1 f 1 1 f 1 1 1 f . . 
            . . f 1 1 1 1 f 1 1 1 1 1 f f . 
            . . f 1 1 1 1 1 1 1 1 1 f 1 1 f 
            . . . f 1 1 1 1 1 1 1 1 1 1 1 f 
            . . . . f 1 1 1 1 1 f 1 1 1 f . 
            . . . . . f f f f f 1 1 1 f . . 
            . . . . . . . . f 1 1 1 f . . . 
            . . . . . . . . f 1 1 f . . . . 
            . . . . . . . . . f f . . . . .
    """),
    SpriteKind.player)
cursor.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
cursor.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
cursor.z = 10000
controller.move_sprite(cursor, 100, 100)
scene.camera_follow_sprite(cursor)

def on_update_interval():
    global newEnemy
    newEnemy = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . b b b b . . . . . . . . 
                    . . . b 3 3 3 3 b b b b . . . . 
                    . . b b 3 3 3 3 3 3 1 1 b c c . 
                    . . b 3 3 3 3 3 3 1 1 1 3 c c c 
                    . . b 1 1 3 3 3 3 3 3 3 3 3 b c 
                    . . c 1 1 3 3 3 b c c c c b b f 
                    . c c 3 3 3 b b d d d c c c b f 
                    c b 3 3 b b d d d d d d b c b f 
                    c 3 3 c b d d d d d d d d b c . 
                    f 3 c c c d d d d d d c c d c . 
                    f b c c c d d c c d d d d d f . 
                    f b c c c d d d d d b b b d f . 
                    f f b b c f f b d d d d d c . . 
                    . f f f f d d b b d d d b f . . 
                    . . . . f d d d b c c f f f . .
        """),
        SpriteKind.enemy)
    tiles.place_on_random_tile(newEnemy, assets.tile("""
        myTile0
    """))
    newEnemy.vy = enemySpeed
game.on_update_interval(2000, on_update_interval)
