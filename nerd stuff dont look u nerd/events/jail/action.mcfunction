fill ~-2 ~-1 ~-2 ~2 ~5 ~2 minecraft:iron_block hollow
fill ~-2 ~4 ~-2 ~2 ~4 ~2 minecraft:lava
fill ~-2 ~3 ~-2 ~2 ~3 ~2 minecraft:moving_piston
setblock ~ ~ ~-1 oak_sign[rotation=0]{Text2:'{"text":"rekt","color":"red","bold":true}'} replace
tellraw @s "You have been jailed."