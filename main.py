# Variables
newEnemy2: Sprite = None
coolDownBuy2: Sprite = None
playerSpeedBuy2: Sprite = None
proyectileSpeedBuy2: Sprite = None
projectile: Sprite = None
gemerated_enemys_in_level = 0
completed_enemies = 0
generated_enemys = 0
cursor: Sprite = None
enemySpeed = 0
shootCooldown = 0
canShoot = False
playerSpeed = 0
enemy_count = 0
level = 0
playerInShop = False
projectile_speed = 0



@namespace
class SpriteKind:
    proyectileSpeedBuy = SpriteKind.create()
    playerSpeedBuy = SpriteKind.create()
    coolDownBuy = SpriteKind.create()

# Comprueba si el nivel esta completado correctamente y pasa al siguiente nivel
def checkLevelCompleted():
    global level, enemySpeed, canShoot, enemy_count, gemerated_enemys_in_level, playerInShop
    if generated_enemys == completed_enemies + info.score():
        level += 1
        enemySpeed += 5
        canShoot = False
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
            music.play(music.melody_playable(music.magic_wand),
                music.PlaybackMode.UNTIL_DONE)
            game.show_long_text("Next leve: " + ("" + str(level)), DialogLayout.FULL)
            goShop()

# Comprueba si el jugador esta en la tienda y si es asi comprueba si esta en la mejora de velocidad
def on_on_overlap(sprite, otherSprite):
    global playerInShop, canShoot
    game.show_long_text("Esta mejora aumenta la velocidad del proyectil. Quieres comprarla?",
        DialogLayout.BOTTOM)
    story.show_player_choices("Si", "No")
    if story.check_last_answer("Si"):
        music.play(music.melody_playable(music.ba_ding),
            music.PlaybackMode.UNTIL_DONE)
        tiles.load_map(tiles.create_map(tilemap("""
            level0
        """)))
        playerInShop = False
        canShoot = True
        destroy_shop_items()
        buy_projectile_upgrade()
    pause(1000)
sprites.on_overlap(SpriteKind.player,
    SpriteKind.proyectileSpeedBuy,
    on_on_overlap)

# Elimina los objetos de mejora de la tienda
def destroy_shop_items():
    sprites.destroy_all_sprites_of_kind(SpriteKind.proyectileSpeedBuy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.playerSpeedBuy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.coolDownBuy)

# Comprueba si el jugador esta en la tienda y si es asi comprueba si esta en la mejora de culdown del disparo
def on_on_overlap2(sprite2, otherSprite2):
    global playerInShop, canShoot
    game.show_long_text("Esta mejora disminuye el coolDown del disparo Quieres comprarla?",
        DialogLayout.BOTTOM)
    story.show_player_choices("Si", "No")
    if story.check_last_answer("Si"):
        music.play(music.melody_playable(music.ba_ding),
            music.PlaybackMode.UNTIL_DONE)
        tiles.load_map(tiles.create_map(tilemap("""
            level0
        """)))
        playerInShop = False
        canShoot = True
        destroy_shop_items()
        buy_coolDown_upgrage()
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.coolDownBuy, on_on_overlap2)


# Compra la mejora de velocidad del proyectil
def buy_projectile_upgrade():
    global projectile_speed
    projectile_speed += 0 - 20


# Comprueba si el jugador esta en la tienda y si es asi comprueba si esta en la mejora de velocidad del jugador
def on_on_overlap3(sprite3, otherSprite3):
    global playerInShop, canShoot
    game.show_long_text("Esta mejora aumenta la velocidad del jugador. Quieres comprarla?",
        DialogLayout.BOTTOM)
    story.show_player_choices("Si", "No")
    if story.check_last_answer("Si"):
        music.play(music.melody_playable(music.ba_ding),
            music.PlaybackMode.UNTIL_DONE)
        tiles.load_map(tiles.create_map(tilemap("""
            level0
        """)))
        playerInShop = False
        canShoot = True
        destroy_shop_items()
        buy_player_upgrade()
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.playerSpeedBuy, on_on_overlap3)

# Esta función se encarga de mover a los enemigos por el camino
def on_hit_wall(sprite22, location):
    global completed_enemies
    if tiles.tile_is(tiles.location_of_sprite(sprite22),
        sprites.vehicle.road_turn3):
        sprite22.vy = 0
        sprite22.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite22),
        sprites.vehicle.road_intersection1):
        sprite22.vy = 0
        sprite22.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite22),
        sprites.vehicle.road_intersection4):
        sprite22.vy = enemySpeed
        sprite22.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite22),
        sprites.vehicle.road_turn4):
        sprite22.vy = 0
        sprite22.vx = 0 - enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite22),
        sprites.vehicle.road_intersection2):
        sprite22.vy = enemySpeed
        sprite22.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite22),
        assets.tile("""
            myTile2
        """)):
        sprite22.vy = 0 - enemySpeed
        sprite22.vx = 0
    elif tiles.tile_is(tiles.location_of_sprite(sprite22),
        sprites.vehicle.road_intersection3):
        sprite22.vy = 0
        sprite22.vx = enemySpeed
    elif tiles.tile_is(tiles.location_of_sprite(sprite22),
        sprites.vehicle.road_turn2):
        sprite22.vy = enemySpeed
        sprite22.vx = 0
    else:
        sprites.destroy(sprite22, effects.blizzard, 500)
        completed_enemies += 1
        info.change_life_by(-1)
        music.play(music.melody_playable(music.small_crash),
            music.PlaybackMode.UNTIL_DONE)
        checkLevelCompleted()
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

# Dispara un proyectil al pulsar el botton A
def on_a_pressed():
    global canShoot, projectile
    if canShoot:
        canShoot = False
        
        # Sprite proyectil
        projectile = sprites.create_projectile_from_sprite(img("""
                . . 2 2 2 2 . .
                            . 4 4 5 5 4 4 .
                            . 4 5 1 5 5 4 .
                            2 4 5 1 5 5 4 2
                            2 4 4 5 5 4 4 2
                            . 2 5 5 4 4 2 2
                            . 2 4 4 4 2 2 .
                            . 2 2 2 2 . 2 .
                            . 2 . 2 . . 2 .
                            . 2 . . . . 2 .
                            . . . . 5 . 2 .
                            . . 5 . 2 . . .
                            . 2 . . . . . .
                            . . . 2 . . . .
                            . . . 2 . . . .
                            . . . . . . . .
            """),
            cursor,
            0,
            projectile_speed)
        animation.run_image_animation(projectile,
            [img("""
                    . . 2 2 2 2 . .
                                . 4 4 5 5 4 4 .
                                . 4 5 1 1 5 4 .
                                2 4 5 1 1 1 4 2
                                2 4 4 5 5 5 4 2
                                . 2 5 1 5 4 2 2
                                . 2 4 5 4 2 2 .
                                . 2 2 2 2 . 2 .
                                . 2 . 2 . . 2 .
                                . 2 . . . . 2 .
                                . . . . 5 . 2 .
                                . . 5 . 2 . . .
                                . 2 . . . . . .
                                . . . 2 . . . .
                                . . . 2 . . . .
                                . . . . . . . .
                """),
                img("""
                    . . 2 2 2 2 . .
                                . 4 4 4 4 4 4 .
                                . 4 5 1 1 4 4 .
                                2 4 5 1 5 4 4 2
                                2 4 4 5 5 5 4 2
                                . 2 5 5 5 5 2 2
                                . 2 4 5 4 2 2 .
                                5 . 2 2 2 . . .
                                2 . . 2 . . . .
                                2 . . . . . 2 .
                                . . . 2 . 2 5 .
                                . . . 2 . . . .
                                . 2 . . . . 5 .
                                . 5 . . . . 2 .
                                . 2 . . . . 2 .
                                . . . . . . . .
                """),
                img("""
                    . . 2 2 2 2 . .
                                . 4 4 5 5 4 4 .
                                . 4 5 1 5 5 4 .
                                2 4 5 1 1 5 4 2
                                2 4 5 1 5 5 4 2
                                . 2 5 5 4 4 2 .
                                . 2 4 4 4 2 . .
                                . 2 2 2 2 . . 2
                                . 2 . 2 . . . 2
                                . . . . . 2 . 2
                                5 . . . . 2 . .
                                2 . . . . 2 . .
                                . . . . . . . .
                                . . 5 . . . . .
                                . . 2 . . . . .
                                . . . . . . . .
                """),
                img("""
                    . . 2 2 2 2 . .
                                . 4 4 5 4 5 4 .
                                . 4 5 1 1 5 4 .
                                2 4 5 1 5 5 4 2
                                2 4 4 5 5 4 4 2
                                . 2 4 5 4 4 2 2
                                . 2 5 4 4 2 2 .
                                . 2 2 2 2 . 2 .
                                . 2 . 2 . . . .
                                . 5 . . . 5 . .
                                . . . . . 2 . 2
                                2 . . . . . 2 5
                                5 . . . . . . .
                                . . . 2 . . 5 .
                                . . . 2 . . 2 .
                                . . . . . . 2 .
                """)],
            100,
            True)
        
        
        # Sprite proyectil
        projectile.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
        music.play(music.melody_playable(music.pew_pew),
            music.PlaybackMode.UNTIL_DONE)
        
        def on_after():
            global canShoot
            if not (playerInShop):
                canShoot = True
        timer.after(shootCooldown, on_after)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# Esta función se encarga de llevar al jugador a la tienda
def goShop():
    global proyectileSpeedBuy2, playerSpeedBuy2, coolDownBuy2
    tiles.set_current_tilemap(tilemap("""
        level8
    """))
    tiles.place_on_tile(cursor, tiles.get_tile_location(7, 15))
    game.splash("Selecciona una ventaja para comprar")
    pause(1000)
    
    
    proyectileSpeedBuy2 = sprites.create(img("""
            ........................7..
                    ........................7..
                    ......................77777
                    .fffff...fffff...fffff..7..
                    f17777f.f17777f.f17777f.7..
                    .f17777f.f17777f.f17777f...
                    ..f17777f.f17777f.f17777f..
                    ...f17777f.f17777f.f17777f.
                    ....f17777f.f17777f.f17777f
                    ...f17777f.f17777f.f17777f.
                    ..f17777f.f17777f.f17777f..
                    .f17777f.f17777f.f17777f...
                    f17777f.f17777f.f17777f....
                    .fffff...fffff...fffff.....
        """),
        SpriteKind.proyectileSpeedBuy)
    tiles.place_on_tile(proyectileSpeedBuy2, tiles.get_tile_location(6, 9))
    
    
    playerSpeedBuy2 = sprites.create(img("""
            .............................
                    .fff....................7fff.
                    .f99ff.................f799f.
                    .f9999ff.............f77777f.
                    .f999999ff.........ff999799f.
                    .ff9999999f.......f9999979ff.
                    ff9fff99999f.....f99999fff9ff
                    f99999999999f...f99999999999f
                    f99999999999f...f99999999999f
                    .f99999fff999f.f999fff99999f.
                    ..ff99f999f99f.f99f999f99ff..
                    .f999f9999f99f.f99f9999f999f.
                    ..f99f999f999f.f999f999f99f..
                    ...fff999999f...f999999fff...
                    ......f9999f.....f9999f......
                    .......ffff.......ffff.......
        """),
        SpriteKind.playerSpeedBuy)
    
    tiles.place_on_tile(playerSpeedBuy2, tiles.get_tile_location(8, 9))
    
    coolDownBuy2 = sprites.create(img("""
            .......fff.......
                    ......fcccf.7....
                    ......ffcff.7....
                    ....ffcccc77777..
                    ...fcccccccc7f...
                    ..fccc11f11c7cf..
                    .fccc1112111cccf.
                    .fcc111121111ccf.
                    fccc111121111cccf
                    fcc11111211111ccf
                    fccf111122211fccf
                    fcc11111111111ccf
                    fccc111111111cccf
                    .fcc111111111ccf.
                    .fccc1111111cccf.
                    ..fcccc1f1ccccf..
                    ...fcccccccccf...
                    ....ffcccccff....
                    ......fffff......
        """),
        SpriteKind.coolDownBuy)
    
    tiles.place_on_tile(coolDownBuy2, tiles.get_tile_location(10, 9))

# Destruye proyectil y enemigo al colisionar
def on_on_overlap4(sprite222, otherSprite22):
    sprites.destroy(projectile, effects.fire, 500)
    sprites.destroy(otherSprite22, effects.disintegrate, 500)
    info.change_score_by(1)
    checkLevelCompleted()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap4)

# Compra la mejora de velocidad del jugador
def buy_player_upgrade():
    global playerSpeed
    playerSpeed += playerSpeed + 10
    controller.move_sprite(cursor, playerSpeed, playerSpeed)

# Compra la mejora de culdown
def buy_coolDown_upgrage():
    global shootCooldown
    shootCooldown += 0 - 260

# Actualiza el juego y genera un enemigo si es necesario
def on_update_interval():
    global newEnemy2, generated_enemys, gemerated_enemys_in_level
    if gemerated_enemys_in_level < enemy_count and playerInShop == False:
        newEnemy2 = sprites.create(img("""
                . . . . . . . . . . . f f f . .
                            f f f . . . . . . . . c c f f f
                            c b b c f . . . c c . c c c f f
                            . c b b b f f c c 3 c c 3 c f f
                            . c c c b b f c b 3 c b 3 c f f
                            . c c b c b f c b b b b b b c f
                            . c b b c b b c b 1 b b b 1 c c
                            . c b c c c b b b b b b b b b c
                            . . c c c c c b b c 1 f f 1 b c
                            . . . c f b b b b f 1 f f 1 f c
                            . . . c f b b b b f f f f f f f
                            . . c c f b b b b f 2 2 2 2 f f
                            . . . . f c b b b 2 2 2 2 2 f .
                            . . . . . f c b b b 2 2 2 f . .
                            . . . . . . f f f f f f f . . .
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        tiles.place_on_random_tile(newEnemy2, assets.tile("""
            myTile0
        """))
        newEnemy2.vy = enemySpeed
        generated_enemys += 1
        gemerated_enemys_in_level += 1
game.on_update_interval(1000, on_update_interval)

# Llama al menú inicial
def initialMenu():
    tiles.load_map(tiles.create_map(tilemap("""
        level12
    """)))
    story.show_player_choices("PLAY", "HELP")
    if story.check_last_answer("HELP"):
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
        
        game.show_long_text("El juego consta de varios niveles. \\n Cada nivel tiene varios enemigos que recorren un camino",
            DialogLayout.FULL)
       
        game.show_long_text("Tienes 3 vidas, si el enemigo llega al final del recorrido sin ser eliminado pierdes una vida \\n Si pierdes las tres seras eliminado",
            DialogLayout.FULL)
        
        game.show_long_text("Si eliminas a todos los enemigos de un nivel pasaras al siguiente nivel.",
            DialogLayout.FULL)
       
        game.show_long_text("Entre niveles podras acceder a una tienda en la que podras elegir una mejora para tu estadisticas",
            DialogLayout.FULL)
       
        game.show_long_text("Estas preparado?", DialogLayout.FULL)
        initialMenu()



music.set_volume(20)
music.play(music.create_song(assets.song("""
        DISCOTEKA
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
music.set_volume(100)
initialMenu()
newEnemy = None
projectile_speed = -20
playerInShop = False
level = 1
enemy_count = 10 * level
playerSpeed = 50
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
controller.move_sprite(cursor, playerSpeed, playerSpeed)
scene.camera_follow_sprite(cursor)



