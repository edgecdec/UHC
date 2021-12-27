# Spread players out
execute as @p run spreadplayers 0 0 100 500 false @a[tag=!admin]

# Give players iron tools
execute as @p run give @a[tag=!admin] iron_sword{Enchantments:[{id:efficiency,lvl:3},{id:unbreaking,lvl:3}]} 1
execute as @p run give @a[tag=!admin] iron_pickaxe{Enchantments:[{id:efficiency,lvl:3},{id:unbreaking,lvl:3}]} 1
execute as @p run give @a[tag=!admin] iron_axe{Enchantments:[{id:efficiency,lvl:3},{id:unbreaking,lvl:3}]} 1
execute as @p run give @a[tag=!admin] iron_shovel{Enchantments:[{id:efficiency,lvl:3},{id:unbreaking,lvl:3}]} 1

# Give players effects for first 20 mins
execute as @p run effect give @a[tag=!admin] minecraft:fire_resistance 1200 0 true
execute as @p run effect give @a[tag=!admin] minecraft:resistance 1200 2 true
execute as @p run effect give @a[tag=!admin] minecraft:regeneration 1200 0 true
