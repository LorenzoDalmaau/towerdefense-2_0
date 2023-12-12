namespace SpriteKind {
    export const proyectileSpeedBuy = SpriteKind.create()
    export const playerSpeedBuy = SpriteKind.create()
    export const coolDownBuy = SpriteKind.create()
}
function checkLevelCompleted () {
    if (generated_enemys == completed_enemies + info.score()) {
        level += 1
        enemySpeed += 5
        canShoot = false
        enemy_count = 10 * level
        gemerated_enemys_in_level = 0
        if (level == 6) {
            game.setGameOverEffect(true, effects.confetti)
            game.gameOver(true)
        } else {
            playerInShop = true
            game.setDialogFrame(img`
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
                `)
            game.showLongText("LEVEL COMPLETED!!", DialogLayout.Full)
            game.showLongText("Next leve: " + ("" + level), DialogLayout.Full)
            goShop()
        }
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.proyectileSpeedBuy, function (sprite, otherSprite) {
    game.showLongText("Esta mejora aumenta la velocidad del proyectil. Quieres comprarla?", DialogLayout.Bottom)
    story.showPlayerChoices("Si", "No")
    if (story.checkLastAnswer("Si")) {
        tiles.loadMap(tiles.createMap(tilemap`level0`))
        playerInShop = false
        canShoot = true
        destroy_shop_items()
        buy_projectile_upgrade()
    }
    pause(1000)
})
function destroy_shop_items () {
    sprites.destroyAllSpritesOfKind(SpriteKind.proyectileSpeedBuy)
    sprites.destroyAllSpritesOfKind(SpriteKind.playerSpeedBuy)
    sprites.destroyAllSpritesOfKind(SpriteKind.coolDownBuy)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.coolDownBuy, function (sprite, otherSprite) {
    game.showLongText("Esta mejora disminuye el coolDown del disparo Quieres comprarla?", DialogLayout.Bottom)
    story.showPlayerChoices("Si", "No")
    if (story.checkLastAnswer("Si")) {
        tiles.loadMap(tiles.createMap(tilemap`level0`))
        playerInShop = false
        canShoot = true
        destroy_shop_items()
        buy_coolDown_upgrage()
    }
    pause(1000)
})
function buy_projectile_upgrade () {
    projectile_speed += 0 - 20
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.playerSpeedBuy, function (sprite, otherSprite) {
    game.showLongText("Esta mejora aumenta la velocidad del jugador. Quieres comprarla?", DialogLayout.Bottom)
    story.showPlayerChoices("Si", "No")
    if (story.checkLastAnswer("Si")) {
        tiles.loadMap(tiles.createMap(tilemap`level0`))
        playerInShop = false
        canShoot = true
        destroy_shop_items()
        buy_player_upgrade()
    }
    pause(1000)
})
scene.onHitWall(SpriteKind.Enemy, function (sprite2, location) {
    if (tiles.tileIs(tiles.locationOfSprite(sprite2), sprites.vehicle.roadTurn3)) {
        sprite2.vy = 0
        sprite2.vx = enemySpeed
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite2), sprites.vehicle.roadIntersection1)) {
        sprite2.vy = 0
        sprite2.vx = enemySpeed
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite2), sprites.vehicle.roadIntersection4)) {
        sprite2.vy = enemySpeed
        sprite2.vx = 0
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite2), sprites.vehicle.roadTurn4)) {
        sprite2.vy = 0
        sprite2.vx = 0 - enemySpeed
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite2), sprites.vehicle.roadIntersection2)) {
        sprite2.vy = enemySpeed
        sprite2.vx = 0
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite2), assets.tile`myTile2`)) {
        sprite2.vy = 0 - enemySpeed
        sprite2.vx = 0
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite2), sprites.vehicle.roadIntersection3)) {
        sprite2.vy = 0
        sprite2.vx = enemySpeed
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite2), sprites.vehicle.roadTurn2)) {
        sprite2.vy = enemySpeed
        sprite2.vx = 0
    } else {
        sprites.destroy(sprite2, effects.blizzard, 500)
        completed_enemies += 1
        info.changeLifeBy(-1)
        checkLevelCompleted()
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (canShoot) {
        canShoot = false
        projectile = sprites.createProjectileFromSprite(img`
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
            `, cursor, 0, projectile_speed)
        animation.runImageAnimation(
        projectile,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
        projectile.setFlag(SpriteFlag.GhostThroughWalls, true)
        music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
        timer.after(shootCooldown, function () {
            if (!(playerInShop)) {
                canShoot = true
            }
        })
    }
})
function goShop () {
    tiles.setCurrentTilemap(tilemap`level8`)
    tiles.placeOnTile(cursor, tiles.getTileLocation(7, 15))
    game.splash("Selecciona una ventaja para comprar")
    pause(1000)
    proyectileSpeedBuy = sprites.create(img`
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
        `, SpriteKind.proyectileSpeedBuy)
    tiles.placeOnTile(proyectileSpeedBuy, tiles.getTileLocation(6, 9))
    playerSpeedBuy = sprites.create(img`
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
        `, SpriteKind.playerSpeedBuy)
    tiles.placeOnTile(playerSpeedBuy, tiles.getTileLocation(8, 9))
    coolDownBuy = sprites.create(img`
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
        `, SpriteKind.coolDownBuy)
    tiles.placeOnTile(coolDownBuy, tiles.getTileLocation(10, 9))
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite22, otherSprite2) {
    sprites.destroy(projectile, effects.fire, 500)
    sprites.destroy(otherSprite2, effects.disintegrate, 500)
    info.changeScoreBy(1)
    checkLevelCompleted()
})
function buy_player_upgrade () {
    playerSpeed += playerSpeed + 10
    controller.moveSprite(cursor, playerSpeed, playerSpeed)
}
function buy_coolDown_upgrage () {
    shootCooldown += 0 - 250
}
function initialMenu () {
    tiles.loadMap(tiles.createMap(tilemap`level12`))
    story.showPlayerChoices("PLAY", "HELP")
    if (story.checkLastAnswer("HELP")) {
        game.setDialogFrame(img`
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
            `)
        game.showLongText("El juego consta de varios niveles. \\n Cada nivel tiene varios enemigos que recorren un camino", DialogLayout.Full)
        game.showLongText("Tienes 3 vidas, si el enemigo llega al final del recorrido sin ser eliminado pierdes una vida \\n Si pierdes las tres seras eliminado", DialogLayout.Full)
        game.showLongText("Si eliminas a todos los enemigos de un nivel pasaras al siguiente nivel.", DialogLayout.Full)
        game.showLongText("Entre niveles podras acceder a una tienda en la que podras elegir una mejora para tu estadisticas", DialogLayout.Full)
        game.showLongText("Estas preparado?", DialogLayout.Full)
        initialMenu()
    }
}
let newEnemy2: Sprite = null
let coolDownBuy: Sprite = null
let playerSpeedBuy: Sprite = null
let proyectileSpeedBuy: Sprite = null
let projectile: Sprite = null
let gemerated_enemys_in_level = 0
let completed_enemies = 0
let generated_enemys = 0
let cursor: Sprite = null
let enemySpeed = 0
let shootCooldown = 0
let canShoot = false
let playerSpeed = 0
let enemy_count = 0
let level = 0
let playerInShop = false
let projectile_speed = 0
initialMenu()
let newEnemy = null
projectile_speed = -20
playerInShop = false
level = 1
enemy_count = 10 * level
playerSpeed = 50
info.setLife(3)
info.setScore(0)
canShoot = true
shootCooldown = 2000
tiles.loadMap(tiles.createMap(tilemap`level0`))
enemySpeed = 20
effects.starField.startScreenEffect()
cursor = sprites.create(img`
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
    `, SpriteKind.Player)
cursor.setFlag(SpriteFlag.GhostThroughWalls, true)
cursor.setFlag(SpriteFlag.StayInScreen, true)
cursor.z = 10000
controller.moveSprite(cursor, playerSpeed, playerSpeed)
scene.cameraFollowSprite(cursor)
game.onUpdateInterval(1000, function () {
    if (gemerated_enemys_in_level < enemy_count && playerInShop == false) {
        newEnemy2 = sprites.create(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        newEnemy2,
        [img`
            . . . . b b b b . . . . . . . . 
            . . . b 3 3 3 3 b b b b . . . . 
            . . b b 3 3 3 3 3 1 1 b b c c . 
            . . b 1 1 3 3 3 3 3 1 1 3 b c c 
            . . b 1 1 3 3 3 3 3 3 3 3 3 b c 
            . . c 3 3 3 3 3 b c c c c b b f 
            . c 3 3 3 3 b b d d d c c c b f 
            c b 3 3 b b d d d d d d b c b f 
            c 3 3 c b d d d d d d c d b c . 
            f 3 c c c d d c d d d c d d c . 
            f b c c c d d d c d d d d d f . 
            f b c c c f f b d d b b b d f . 
            f f b b f b d d b d d d d c . . 
            . f f f f d d b b d d d c . . . 
            . . . . b b b b f b b f f . . . 
            . . . . . . . f f b b b f . . . 
            `,img`
            . . . . . . . . . . . . . . . . 
            . . . . b b b b . . . . . . . . 
            . . . b 3 3 3 3 b b b b . . . . 
            . . b b 3 3 3 3 3 1 1 b b c c . 
            . . b 1 1 3 3 3 3 1 1 1 3 c c c 
            . . b 1 1 3 3 3 3 3 3 3 3 3 b c 
            . . c 1 1 3 3 b b c c c c b b f 
            . c c 3 3 b b d d d d b c c b f 
            c b 3 3 b b d d d d d d d c b f 
            c 3 3 b b d d d d d d c d d c . 
            f 3 3 c b d d c d d d c d d c . 
            f b c c c d d d c d d d d d f . 
            f b c c c d d f f b b b b d f . 
            f f b b c c f b d d b d d c . . 
            . f f f c c f d d b b d c . . . 
            . . . . . . b b b b f c . . . . 
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
        tiles.placeOnRandomTile(newEnemy2, assets.tile`myTile0`)
        newEnemy2.vy = enemySpeed
        generated_enemys += 1
        gemerated_enemys_in_level += 1
    }
})
