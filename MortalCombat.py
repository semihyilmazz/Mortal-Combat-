import random
print "----- First Hero -----"
first_name=raw_input("Please type your hero's name:")

print "----- Second Hero------"
while True:
    second_name = raw_input("Please type your hero's name:")
    if second_name == first_name:
        print second_name,"is taken please try another"
        continue
    else:
        break

coin = random.randint(1,2)

if coin == 1:
    print first_name,"starts first"
else:
    print second_name,"starts first"

first_heal = 100
second_heal= 100

def show_health():
    if coin ==1:
        print first_name,"[HP]:",first_heal,("|"*(first_heal/2)), "           ", second_name,"[HP]:",second_heal,("|"*(second_heal/2))
    else:
        print second_name,"[HP]:",second_heal,("|" * (second_heal / 2)), "           ", first_name,"[HP]:",first_heal,("|" * (first_heal / 2))

def attack1():
    global first_heal
    global second_heal
    global first_name
    global second_name
    print "--------",first_name,"attacks--------"
    while True:
        damage = input("Choose your attack magnitude between 1 and 50:")
        if damage > 50 or damage < 1:
            print "The attack magnitude must be between 1 and 50."

        else:
            no_miss = random.randint(1, 100)
            if 100 - damage > no_miss:
                second_heal = second_heal - damage
                print first_name, "hits", damage
                show_health()
                break
            else:
                print first_name, "missed the shot"
                show_health()
                break


def attack2():
    global first_heal
    global second_heal
    global first_name
    global second_name


    print "--------",second_name,"attacks--------"
    while True:
        damage = input("Choose your attack magnitude between 1 and 50:")
        if damage > 50 or damage < 1:
            print "The attack magnitude must be between 1 and 50."

        else:
            no_miss = random.randint(1, 100)
            if 100 - damage > no_miss:
                first_heal = first_heal - damage
                print second_name, "hits", damage
                show_health()
                break
            else:
                print second_name, "missed the shot"
                show_health()
                break


while first_heal> 0 and second_heal > 0:

    if coin == 1:  # if random number which is (1,100) is more than 50 then first player starts
        while True:
            attack1()  # and this loop goes on until one of the player's health less or equal to "0"
            if second_heal <= 0:
                print first_name,"won"
                break
            attack2()
            if first_heal<=0:
                print second_name,"won"
                break

    else:
        while True:
            attack2()
            if first_heal <= 0:
                print second_name,"won"
                break
            attack1()
            if second_heal <=0:
                print first_name,"won"
                break
