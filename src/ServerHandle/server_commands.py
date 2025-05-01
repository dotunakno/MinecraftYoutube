from mcrcon import MCRcon

def send_command(command):
    host = "localhost"
    port = 42352
    password = "KroBellVler3469ThisPasswordIsTooHeavyToBreak"

    with MCRcon(host, password, port) as mcr :
        return mcr.command(command)


def summon(player_name, mob_name):
    command = f"execute at {player_name} run summon minecraft:{mob_name}"
    return send_command(command)


def summon_SilverFish(player_name):
    command = f"execute at {player_name} run summon minecraft:silverfish"
    return send_command(command)

def summon_zombie_at(player_name):
    command = f"execute at {player_name} run summon minecraft:zombie"
    return send_command(command)

def summon_SpecialZombie(player_name):
    command = (
        f'execute at {player_name} run summon zombie ~ ~ ~ '
        '{ArmorItems:['
        '{id:"minecraft:netherite_boots",Count:1b},'
        '{id:"minecraft:netherite_leggings",Count:1b},'
        '{id:"minecraft:netherite_chestplate",Count:1b},'
        '{id:"minecraft:netherite_helmet",Count:1b}],'
        'HandItems:[{id:"minecraft:netherite_sword",Count:1b},{}],'
        'ArmorDropChances:[0.0f,0.0f,0.0f,0.0f],'
        'HandDropChances:[0.0f,0.0f],'
        'IsBaby:1b}'
    )

    return send_command(command)

def summon_SpecialCreeper(player_name, radius = 30, TimeBomb = 40):
    command = (
        f'execute at {player_name} run summon minecraft:creeper ~ ~ ~ '
        f'{{powered:1b,ExplosionRadius:{radius},Fuse:{TimeBomb},'
        f'CustomName:\'{{"text":"KROOOOOOOO BELLLL"}}\'}}'
    )
    print("command : " , command)
    return send_command(command)

def summon_creeper(player_name):
    command = f"execute at {player_name} run summon minecraft:creeper"
    return send_command(command)

def summon_Guardian(player_name):
    command = f"execute at {player_name} run summon minecraft:guardian"
    return send_command(command)

def summon_TNT(player_name):
    command = f"execute at {player_name} run summon tnt"
    return send_command(command)

def summon_Box(player_name, x):
    outer_fill = f"execute at {player_name} run fill ~{x} ~{x} ~{x} ~-{x} ~-{x} ~-{x} dirt"
    send_command(outer_fill)
    inner_fill = f"execute at {player_name} run fill ~{x-1} ~{x-1} ~{x-1} ~-{x-1} ~-{x-1} ~-{x-1} air"
    return send_command(inner_fill)

def FlyTroll(player_name):
    command = f"tp {player_name} ~ ~{50} ~"
    return send_command(command)

def give_effect(player_name, effect, duration, amplifier = 1):
    command = f"effect give {player_name} minecraft:{effect} {duration} {amplifier}"
    return send_command(command)

def teleport_Dimension(player_name, dimension, x = 0, y = 100, z = 0):
    command = f"execute in minecraft:{dimension} run tp {player_name} {x} {y} {z}"
    return send_command(command)

def CreateHole(player_name, depth):
    command = f"execute at {player_name} run fill ~1 ~ ~1 ~-1 ~-{depth} ~-1 air"
    return send_command(command)

def summon_Water(player_name, x):
    command = f"execute at {player_name} run fill ~{x} ~-1 ~{x} ~-{x} ~-1 ~-{x} minecraft:water"
    return send_command(command)

def kill_all_mobs():
    return send_command("kill @e[type=!player]")


def FallTroll(player_name, depth):
    commands = []
    commands.append(
        f"execute at {player_name} run fill ~1 ~{depth+1} ~1 ~-1 ~-{depth+1} ~-1 air"
    )

    commands.append(
        f"execute at {player_name} run fill ~1 ~-{depth} ~1 ~-1 ~-{depth} ~-1 oak_wall_sign[facing=north]"
    )
    commands.append(
        f"execute at {player_name} run fill ~1 ~-{depth+2} ~1 ~-1 ~-{depth+2} ~-1 water"
    )
    commands.append(
        f"execute at {player_name} run fill ~1 ~-{depth-1} ~1 ~-1 ~-{depth-1} ~-1 lava"
    )

    commands.append(
        f"execute at {player_name} run fill ~1 ~{depth} ~1 ~-1 ~{depth} ~-1 anvil"
    )

    commands.append(
        f"give {player_name} minecraft:bucket"
    )
    commands.append(
        f"give {player_name} minecraft:dirt 64"
    )
    for cmd in commands:
        send_command(cmd)

def summon_GiantZombie(player_name):
    command = "say Summon kro bel successfully"
    send_command(command)
    command = f"execute at {player_name} run summon giant"
    return send_command(command)