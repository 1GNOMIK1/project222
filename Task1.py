import random
wizard1_name= input("Введите имя первого волшебника: ")
wizard2_name= input("Введите имя второго волшебника: ")
spells_wizards1 = int(input("Сколько заклинаний использовал первый волшебник?"))
spells_wizards2 = int(input("Сколько заклинаний использовал второй волшебник?"))
wizard1_points = random.randint(3,10) * spells_wizards1
wizard2_points = random.randint(3,10) * spells_wizards2
print(f"Очки {wizard1_name} после дуэли: {wizard1_points} ")
print(f"Очки {wizard2_name} после дуэли: {wizard2_points} ")
answer = ""
while not answer in ['yes', 'no']:
    answer = input("разгадал загадку?")
    if answer == 'yes':
        wizard1_points += random.randint(30,50)
    else:
        pass
answer = ""
while not answer in ['yes', 'no']:
    answer = input("разгадал загадку?")
    if answer == 'yes':
        wizard2_points += random.randint(30,50)
    else:
        pass

print(f"Очки {wizard1_name} после испытания на ловкость: {wizard1_points}")
print(f"Очки {wizard2_name} после испытания на ловкость: {wizard2_points}")

wizard1_bonus_points =0

total_wizard1_points = (wizard1_points + wizard1_bonus_points)
total_wizard2_points = (wizard2_points + wizard2_played_honestly+ wizard2_received_friends_support)


print(f"Общие баллы {wizard1_name}: {total_wizard1_points}")
print(f"Общие баллы {wizard2_name}: {total_wizard2_points}")

if total_wizard1_points > total_wizard2_points:
    print(f"Победил {}".format(wizard1_name))
elif total_wizard2_points > total_wizard1_points:
    print(f"Победил {}".format(wizard2_name))
else:
    print("Ничья!")


