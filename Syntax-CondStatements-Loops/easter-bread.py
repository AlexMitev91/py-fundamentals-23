budget = float(input())
kg_of_flour = float(input())

pack_of_eggs = 0.75 * kg_of_flour
liter_of_milk = 1.25 * kg_of_flour

colored_eggs = 0
breads_made = 0
while True: 
    budget -= (kg_of_flour + pack_of_eggs + (liter_of_milk / 4))
    if budget < 0:
        budget += (kg_of_flour + pack_of_eggs + (liter_of_milk / 4))
        break
    breads_made += 1
    colored_eggs += 3
    if breads_made % 3 == 0:
        colored_eggs -= (breads_made - 2)
print(f"You made {breads_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

