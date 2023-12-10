@namespace
class SpriteKind:
    rangeBuy = SpriteKind.create()
def destroy_shop_items():
    sprites.destroy_all_sprites_of_kind(SpriteKind.rangeBuy)
def buy_projectile_upgrade():
    global projectile_speed
    projectile_speed += 0 - 900

def on_hit_wall(sprite2, location):
    if tiles.tile_is(tiles.location_of_sprite(sprite2),
        sprites.vehicle.road_turn3):
        sprite2.vy = 0
        sprite2.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite2),
        sprites.vehicle.road_intersection1):
        sprite2.vy = 0
        sprite2.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite2),
        sprites.vehicle.road_intersection4):
        sprite2.vy = enemySpeed
        sprite2.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite2),
        sprites.vehicle.road_turn4):
        sprite2.vy = 0
        sprite2.vx = 0 - enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite2),
        sprites.vehicle.road_intersection2):
        sprite2.vy = enemySpeed
        sprite2.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite2),
        assets.tile("""
            myTile5
        """)):
        sprite2.vy = 0 - enemySpeed
        sprite2.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite2),
        sprites.vehicle.road_intersection3):
        sprite2.vy = 0
        sprite2.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite2),
        sprites.vehicle.road_turn2):
        sprite2.vy = enemySpeed
        sprite2.vx = 0
    else:
        sprites.destroy(sprite2, effects.blizzard, 500)
        info.change_life_by(-1)
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

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
            projectile_speed)
        projectile.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
        music.play(music.melody_playable(music.pew_pew),
            music.PlaybackMode.UNTIL_DONE)
        
        def on_after():
            global canShoot
            canShoot = True
        timer.after(shootCooldown, on_after)
        
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def goShop():
    global rangeBuy2
    tiles.set_current_tilemap(tilemap("""
        level8
    """))
    tiles.place_on_tile(cursor, tiles.get_tile_location(7, 10))
    game.splash("Selecciona una ventaja para comprar")
    pause(1000)
    rangeBuy2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 3 3 3 3 3 . . . . . . 
                    . . . . . 3 3 3 3 3 . . . . . . 
                    . . . . . 3 3 3 3 3 . . . . . . 
                    . . . . . 3 3 3 3 3 . . . . . . 
                    . . . 3 3 3 3 3 3 3 . . . . . . 
                    . . . 3 3 3 3 3 3 3 3 3 3 . . . 
                    . . . 3 3 3 3 3 3 3 3 3 3 . . . 
                    . . . 3 3 3 3 3 3 3 3 3 3 . . . 
                    . . . 3 3 3 3 3 3 3 3 3 3 . . . 
                    . . . 3 3 3 3 3 3 3 3 3 3 . . . 
                    . . . . 3 3 3 3 3 3 3 3 3 . . . 
                    . . . . . 3 3 3 3 3 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.rangeBuy)
    tiles.place_on_tile(rangeBuy2, tiles.get_tile_location(4, 3))

def on_on_overlap(sprite22, otherSprite2):
    global level, enemy_count, gemerated_enemys_in_level, playerInShop
    sprites.destroy(projectile, effects.fire, 500)
    sprites.destroy(otherSprite2, effects.disintegrate, 500)
    info.change_score_by(1)
    if info.score() == generated_enemys:
        level += 1
        enemy_count = 10 * level
        gemerated_enemys_in_level = 0
        if level == 6:
            game.set_game_over_effect(True, effects.confetti)
            game.game_over(True)
        else:
            playerInShop = True
            game.set_dialog_frame(img("""
                ..................................................................
                                ............fff........fff.............fff..............ffff......
                                ...........fddbf......fbdbf...........fbdbf............fbddf......
                                ...........fddbbf.....fdddffff........fdddffff...fff..ffddbff.....
                                ...........fddddffffffbdddbddbffffffffbdddbddbffffddffddddddf.....
                                ...fff....fdddddfddddddddbbddddddddddddddbbddddddfdddddbccddf.....
                                .fffddf..fddffffddddddddddbbddddddddddddddbbdddddffbddbbddff......
                                .fdbddfffddfffdddfffffbdddbddbffffffffbdddbddbfffefddccbddf.......
                                .fdddcddddffeffffeeeeefbdbfddfeeeeeeeefbdbfddfeeeefffcddddf.......
                                .fbddcddddfeeeeeeeeeeeefffffffeeeeeeeeefffffffeeeeeeefdddddf......
                                ..ffdbbbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffddf.....
                                ...fddbcddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffddfff..
                                ....fddccffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffddddf.
                                ....fdddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddddf.
                                ...fddbdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdfddbbf.
                                ...fddfffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdfddbf..
                                ...ffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddfff...
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ...fbddbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ...fdddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ...fddbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbff..
                                ..ffbbbbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbdddddbf.
                                .fbddbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddf.
                                .fdddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbddbf.
                                .fbdddddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbbbbff..
                                ..ffbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbddf...
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddf...
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbddbf...
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ...fbddbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ...fdddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ...fddbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbff..
                                ..ffbbbbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbdddddbf.
                                .fbddbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddf.
                                .fdddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbddbf.
                                .fbdddddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbbbbff..
                                ..ffbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbddf...
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddf...
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbddbf...
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                                ...fffddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffff...
                                ..fbddfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddf...
                                .fbbddfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdbddf...
                                .fddddfffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddf....
                                .fddddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffccddf....
                                ..fffddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddcbddf...
                                .....fddfffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbbbdff..
                                ......fdddddfeeeeeeefffffffeeeeeeeeefffffffeeeeeeeeeeeefddddcddbf.
                                .......fddddcfffeeeefddfbdbfeeeeeeeefddfbdbfeeeeeffffeffddddcdddf.
                                .......fddbccddfefffbddbdddbffffffffbddbdddbfffffdddfffddfffddbdf.
                                ......ffddbbddbffdddddbbddddddddddddddbbddddddddddffffddf..fddfff.
                                .....fddccbdddddfddddddbbddddddddddddddbbddddddddfdddddf....fff...
                                .....fddddddffddffffbddbdddbffffffffbddbdddbffffffddddf...........
                                .....ffbddff..fff...ffffdddf........ffffdddf.....fbbddf...........
                                ......fddbf............fbdbf...........fbdbf......fbddf...........
                                ......ffff..............fff.............fff........fff............
                                ..................................................................
            """))
            game.show_long_text("LEVEL COMPLETED!!", DialogLayout.FULL)
            game.show_long_text("Next leve: " + ("" + str(level)), DialogLayout.FULL)
            goShop()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    global playerInShop
    game.show_long_text("Esta mejora aumenta la velocidad del proyectil. Quieres comprarla?",
        DialogLayout.BOTTOM)
    story.show_player_choices("Si", "No")
    if story.check_last_answer("Si"):
        tiles.load_map(tiles.create_map(tilemap("""
            level0
        """)))
        playerInShop = False
        destroy_shop_items()
        buy_projectile_upgrade()
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.rangeBuy, on_on_overlap2)

newEnemy2: Sprite = None
gemerated_enemys_in_level = 0
generated_enemys = 0
rangeBuy2: Sprite = None
projectile: Sprite = None
cursor: Sprite = None
enemySpeed = 0
shootCooldown = 0
canShoot = False
enemy_count = 0
level = 0
playerInShop = False
projectile_speed = 0
newEnemy = None
projectile_velocity = 0
projectile_speed = -20
playerInShop = False
level = 1
enemy_count = 10 * level
info.set_life(3)
info.set_score(0)
canShoot = True
shootCooldown = 2000
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
    global newEnemy2, generated_enemys, gemerated_enemys_in_level
    if gemerated_enemys_in_level < enemy_count and playerInShop == False:
        newEnemy2 = sprites.create(img("""
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
        tiles.place_on_random_tile(newEnemy2, assets.tile("""
            myTile0
        """))
        newEnemy2.vy = enemySpeed
        generated_enemys += 1
        gemerated_enemys_in_level += 1
game.on_update_interval(1000, on_update_interval)
