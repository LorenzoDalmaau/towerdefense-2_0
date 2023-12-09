scene.onHitWall(SpriteKind.Enemy, function (sprite, location) {
    if (tiles.tileIs(tiles.locationOfSprite(sprite), sprites.vehicle.roadTurn3)) {
        sprite.vy = 0
        sprite.vx = enemySpeed
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite), sprites.vehicle.roadIntersection1)) {
        sprite.vy = 0
        sprite.vx = enemySpeed
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite), sprites.vehicle.roadIntersection4)) {
        sprite.vy = enemySpeed
        sprite.vx = 0
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite), sprites.vehicle.roadTurn4)) {
        sprite.vy = 0
        sprite.vx = 0 - enemySpeed
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite), sprites.vehicle.roadIntersection2)) {
        sprite.vy = enemySpeed
        sprite.vx = 0
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite), assets.tile`myTile5`)) {
        sprite.vy = 0 - enemySpeed
        sprite.vx = 0
    } else if (tiles.tileIs(tiles.locationOfSprite(sprite), sprites.vehicle.roadIntersection3)) {
        sprite.vy = 0
        sprite.vx = enemySpeed
    } else {
        sprite.vy = enemySpeed
        sprite.vx = 0
    }
})
let newEnemy: Sprite = null
let enemySpeed = 0
tiles.loadMap(tiles.createMap(tilemap`level0`))
enemySpeed = 20
effects.starField.startScreenEffect()
let cursor = sprites.create(img`
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
    `, SpriteKind.Player)
cursor.setFlag(SpriteFlag.GhostThroughWalls, true)
cursor.setFlag(SpriteFlag.StayInScreen, true)
cursor.z = 10000
controller.moveSprite(cursor, 50, 50)
scene.cameraFollowSprite(cursor)
game.onUpdateInterval(2000, function () {
    newEnemy = sprites.create(img`
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
        `, SpriteKind.Enemy)
    tiles.placeOnRandomTile(newEnemy, assets.tile`myTile0`)
    newEnemy.vy = enemySpeed
})
