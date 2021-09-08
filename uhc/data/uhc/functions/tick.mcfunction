function uhc:border/border_helper
execute as @a[tag=moderator] store result score @s PosX run data get entity @s Pos[0] 1
execute as @a[tag=moderator] store result score @s PosY run data get entity @s Pos[1] 1
execute as @a[tag=moderator] store result score @s PosZ run data get entity @s Pos[2] 1