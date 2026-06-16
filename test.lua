
local position = {
    x = 0,
    y = 0,
}
local speed = 150

function update(dt)
    if btn("right") then
        position.x = position.x + dt * speed
    end
    if btn("left") then
        position.x = position.x - dt * speed
    end
    if btn("down") then
        position.y = position.y - dt * speed
    end
    if btn("up") then
        position.y = position.y + dt * speed
    end
end

function draw()
    spr("test.jpg", position.x, position.y)
end
