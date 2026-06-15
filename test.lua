
local position = {
    x = 0,
    y = 0,
}

function update()
    position.y = position.y + 1
    position.x = position.x + 1
end

function draw()
    spr("test.jpg", position.x, position.y)
end
