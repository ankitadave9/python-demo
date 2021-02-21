from enemy import Enemy, Troll, Vampyre


ugly_troll = Troll("pug")
print("ugly_troll- {}".format(ugly_troll))

another_troll = Troll("ur")
print(another_troll)
another_troll.take_damage(18)
print(another_troll)

brother = Troll("urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

Vamp = Vampyre("vlad")
print(Vamp)
Vamp.take_damage(5)
print(Vamp)

print("*" * 40)
another_troll.take_damage(30)
print(another_troll)

# while Vamp.alive:
#     Vamp.take_damage(1)

Vamp._lives = 0
Vamp._hit_points = 1
print(Vamp)


