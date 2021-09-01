#this file is the bridge between trigger and event.
say Zombie started
execute store result score zombiecount logic run execute if entity @e[type=minecraft:zombie]
execute unless score zombiecount logic matches 30.. run summon zombie ~ ~200 ~ {CustomName:'{"text":"fred","color":"gray"}',ArmorItems:[{},{},{},{id:"minecraft:zombie_head",Count:1b}]}
execute unless score zombiecount logic matches 30.. run summon zombie ~ ~200 ~ {CustomName:'{"text":"fred","color":"gray"}',ArmorItems:[{},{},{},{id:"minecraft:zombie_head",Count:1b}]}
execute unless score zombiecount logic matches 30.. run summon zombie ~ ~200 ~ {CustomName:'{"text":"fred","color":"gray"}',ArmorItems:[{},{},{},{id:"minecraft:zombie_head",Count:1b}]}
execute unless score zombiecount logic matches 30.. run summon zombie ~ ~200 ~ {CustomName:'{"text":"fred","color":"gray"}',ArmorItems:[{},{},{},{id:"minecraft:zombie_head",Count:1b}]}
execute unless score zombiecount logic matches 30.. run summon zombie ~ ~200 ~ {CustomName:'{"text":"fred","color":"gray"}',ArmorItems:[{},{},{},{id:"minecraft:zombie_head",Count:1b}]}
execute unless score zombiecount logic matches 30.. run summon zombie ~ ~200 ~ {CustomName:'{"text":"fred","color":"gray"}',ArmorItems:[{},{},{},{id:"minecraft:zombie_head",Count:1b}]}
execute positioned ~ ~200 ~ run spreadplayers ~ ~ 1 20 true @e[type=minecraft:zombie,distance=0..50]
schedule function mcbut:zombieap/minute2 45s