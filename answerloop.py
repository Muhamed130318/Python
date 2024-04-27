import random

dict = {
    "is TCP connection oriented?":"yes",
    "is 192.168.x.x private address?":"yes",
    "are MAC address useful outside of the local network?":"no",
    "can a l2 switch route?":"no"
}
i = 0


while i < 4:
    print(i)
    dictkey = random.choice(list(dict))
    print(dictkey)
    answer = input("Answer: ")

    if dict[dictkey] == answer:
        print("correct")
        i += 1
    else:
        print("incorrect")

print("You have escaped the loop!")