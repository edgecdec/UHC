execute if score borderTimer BorderTimer matches 0 run function uhc:border/start_border_shrink
execute if score borderTimer BorderTimer matches 12000 run function uhc:border/border_segment_one
execute if score borderTimer BorderTimer matches 14400 run function uhc:border/border_segment_two
execute if score borderTimer BorderTimer matches 16800 run function uhc:border/border_segment_three
execute if score borderTimer BorderTimer matches 19200 run function uhc:border/border_segment_four
scoreboard players add borderTimer BorderTimer 1
