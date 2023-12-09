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
    else:
        sprite.vy = enemySpeed
        sprite.vx = 0
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

newEnemy: Sprite = None
enemySpeed = 0
tiles.load_map(tiles.create_map(tilemap("""
    level0
""")))
enemySpeed = 20
effects.star_field.start_screen_effect()
cursor = sprites.create(img("""
        . . . . . . . . . . b 5 b . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 d 1 f 5 d 4 c . . 
            . . . . b 5 5 1 f f d d 4 4 4 b 
            . . . . b 5 5 d f b 4 4 4 4 b . 
            . . . b d 5 5 5 5 4 4 4 4 b . . 
            . . b d d 5 5 5 5 5 5 5 5 b . . 
            . b d d d d 5 5 5 5 5 5 5 5 b . 
            b d d d b b b 5 5 5 5 5 5 5 b . 
            c d d b 5 5 d c 5 5 5 5 5 5 b . 
            c b b d 5 d c d 5 5 5 5 5 5 b . 
            . b 5 5 b c d d 5 5 5 5 5 d b . 
            b b c c c d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player)
cursor.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
cursor.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
cursor.z = 10000
controller.move_sprite(cursor, 50, 50)
scene.camera_follow_sprite(cursor)

def on_update_interval():
    global newEnemy
    newEnemy = sprites.create(img("""
            . . . . b b b b . . . . . . . . 
                    . . . b 3 3 3 3 b b b b . . . . 
                    . . b b 3 3 3 3 3 1 1 b b c c . 
                    . . b 1 1 3 3 3 3 3 1 1 3 3 c c 
                    . . b 1 1 3 3 3 3 3 3 3 3 3 b c 
                    . . c 3 3 3 3 3 3 3 c c c b b f 
                    . c 3 3 3 3 3 b b b b c c c b f 
                    c 3 3 3 3 b b d d d d d c c b f 
                    c 3 3 c b d d d d d d c d c c . 
                    f 3 c c c d d c d d d c d b c . 
                    f b c c c d d d c d d d d d f . 
                    f b c c c d d d d d b b b d f . 
                    f f b b c b d d d d d d d c . . 
                    . f f f f b c c d d d d f f . . 
                    . . f b d d b c c f f b b f f . 
                    . . f d d d b . . f f b b b f .
        """),
        SpriteKind.enemy)
    tiles.place_on_random_tile(newEnemy, assets.tile("""
        myTile0
    """))
    newEnemy.vy = enemySpeed
game.on_update_interval(2000, on_update_interval)
