

local instances = {}

function Instance(pos, image, size)
    local instanceCount = #instances
    local self = {
        pos = pos,
        image = image,
        size = size,
        vel = {},
    }
    instances[instanceCount + 1] = self
    return instances[instanceCount + 1]
end

local zac = Instance({100, 250}, "zac.jpg", {70, 70})

local pipeTimer = 0

function UpdateVel(dt)
    for _, instance in pairs(instances) do
        if instance.vel[1] == nil then
            instance.vel[1] = 0
        end
        if instance.vel[2] == nil then
            instance.vel[2] = 0
        end
        instance.pos[1] = instance.pos[1] + instance.vel[1] * dt
        instance.pos[2] = instance.pos[2] + instance.vel[2] * dt
    end
end

function update(dt)

    pipeTimer = pipeTimer + dt

    if pipeTimer > 2 then
        local pipe = Instance({600, 20}, "zac.jpg", {60, 500})
        pipe.vel = {-200, 0}
        pipeTimer = 0
    end

    UpdateVel(dt)
end

function draw()
    for _, instance in pairs(instances) do
        spr(instance.image, instance.pos[1], instance.pos[2], instance.size[1], instance.size[2])
    end
end
