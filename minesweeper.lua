
local grid = {}

for x = 1, 10 do
    local row = {}
    for y = 1,10 do
        row[y] = {
            x = x,
            y = y,
            value = "tile.png"
        }
    end
    grid[x] = row
end

function doGrid(callback)
    for x = 1, 10 do
        for y = 1, 10 do
            callback(x, y, grid[x][y])
        end
    end
end

function draw()
    doGrid(function(x, y, cell)
        spr(cell.value, cell.x * 25, cell.y * 25)
    end)
end

function update(dt)
    
end