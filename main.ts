namespace SpriteKind {
    export const rangeBuy = SpriteKind.create()
}
function destroy_shop_items () {
    sprites.destroyAllSpritesOfKind(SpriteKind.rangeBuy)
}
function buy_projectile_upgrade () {
    projectile_speed += 0 - 20
}
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
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite2), assets.tile`myTile5`)) {
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
        info.changeLifeBy(-1)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (canShoot) {
        canShoot = false
        projectile = sprites.createProjectileFromSprite(img`
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
            `, cursor, 0, projectile_speed)
        projectile.setFlag(SpriteFlag.GhostThroughWalls, true)
        music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
        timer.after(shootCooldown, function () {
            canShoot = true
        })
    }
})
function goShop () {
    tiles.setCurrentTilemap(tilemap`level8`)
    tiles.placeOnTile(cursor, tiles.getTileLocation(7, 10))
    game.splash("Selecciona una ventaja para comprar")
    pause(1000)
    rangeBuy2 = sprites.create(img`
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
        `, SpriteKind.rangeBuy)
    tiles.placeOnTile(rangeBuy2, tiles.getTileLocation(4, 3))
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite22, otherSprite2) {
    sprites.destroy(projectile, effects.fire, 500)
    sprites.destroy(otherSprite2, effects.disintegrate, 500)
    info.changeScoreBy(1)
    if (info.score() == generated_enemys) {
        level += 1
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
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.rangeBuy, function (sprite, otherSprite) {
    game.showLongText("Esta mejora aumenta la velocidad del proyectil. Quieres comprarla?", DialogLayout.Bottom)
    story.showPlayerChoices("Si", "No")
    if (story.checkLastAnswer("Si")) {
        tiles.loadMap(tiles.createMap(tilemap`level0`))
        playerInShop = false
        destroy_shop_items()
        buy_projectile_upgrade()
    }
    pause(1000)
})
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
let gemerated_enemys_in_level = 0
let generated_enemys = 0
let rangeBuy2: Sprite = null
let projectile: Sprite = null
let cursor: Sprite = null
let enemySpeed = 0
let shootCooldown = 0
let canShoot = false
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
controller.moveSprite(cursor, 100, 100)
scene.cameraFollowSprite(cursor)
game.onUpdateInterval(1000, function () {
    if (gemerated_enemys_in_level < enemy_count && playerInShop == false) {
        newEnemy2 = sprites.create(img`
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
            `, SpriteKind.Enemy)
        tiles.placeOnRandomTile(newEnemy2, assets.tile`myTile0`)
        newEnemy2.vy = enemySpeed
        generated_enemys += 1
        gemerated_enemys_in_level += 1
    }
})
