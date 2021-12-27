execute if score borderTimer BorderTimer matches 36000 run function uhc:border/start_border_shrink
execute if score borderTimer BorderTimer matches 144000 run function uhc:border/border_segment_one
execute if score borderTimer BorderTimer matches 147600 run function uhc:border/border_segment_two
execute if score borderTimer BorderTimer matches 151200 run function uhc:border/border_segment_three
execute if score borderTimer BorderTimer matches 154800 run function uhc:border/border_segment_four
scoreboard players add borderTimer BorderTimer 1
