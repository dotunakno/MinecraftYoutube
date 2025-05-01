from mcrcon import MCRcon

def send_command(command):
    host = "localhost"
    port = 42352
    password = "KroBellVler3469ThisPasswordIsTooHeavyToBreak"

    with MCRcon(host, password, port) as mcr :
        resp = mcr.command("say Hello from Python!")
        return mcr.command(command)
    
def summon_zombie_at(player_name):
    command = f"execute at {player_name} run summon minecraft:zombie"
    return send_command(command)

def summon_creeper(player_name):
    command = f"execute at {player_name} run summon minecraft:creeper"
    return send_command(command)

def summon_TNT(player_name):
    command = f"execute at {player_name} run summon tnt"
    return send_command(command)

def FlyTroll(player_name):
    command = f"tp {player_name} ~ ~{50} ~"
    return send_command(command)

def give_effect(player_name, effect, duration, amplifier = 1):
    command = f"effect give {player_name} minecraft:{effect} {duration} {amplifier}"
    return send_command(command)

def teleport_Dimension(player_name, dimension, x = 0, y = 100, z = 0):
    command = f"execute in minecraft:{dimension} run tp {player_name} {x} {y} {z}"
    return send_command(command)

def kill_all_mobs():
    return send_command("kill @e[type=!player]")