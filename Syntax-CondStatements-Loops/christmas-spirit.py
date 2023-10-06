decoration_quantity = int(input())
days_to_christmas = int(input())

#Decoration	Price/Piece	Points/Shopping
#Ornament Set	       2$	       5
#Tree Skirt	           5$	       3
#Tree Garland	       3$	       10
#Tree Lights	       15$	       17

total_cost = 0
spirit = 0

ornament_set_cost = 2 
tree_skirt_cost = 5 
tree_garland_cost = 3 
tree_lights_cost = 15 

ornament_set_sp = 5 
tree_skirt_sp = 3 
tree_garland_sp = 10 
tree_lights_sp = 17 

for curent_day in range(1, days_to_christmas + 1):
    if curent_day % 11 == 0:
        decoration_quantity += 2
    #Positive events
    if curent_day % 2 == 0:
        total_cost += ornament_set_cost * decoration_quantity
        spirit += ornament_set_sp 
    if curent_day % 3 == 0:
        total_cost += (tree_skirt_cost + tree_garland_cost) * decoration_quantity
        spirit += (tree_skirt_sp + tree_garland_sp)
    if curent_day % 5 == 0: 
        total_cost += tree_lights_cost * decoration_quantity
        spirit += tree_lights_sp
        if curent_day % 3 == 0:
            spirit += 30
    #Negative events
    if curent_day % 10 == 0: 
        spirit -= 20
        total_cost += tree_skirt_cost + tree_garland_cost + tree_lights_cost
        if curent_day == days_to_christmas:
            spirit -= 30


print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")