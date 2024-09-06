# start
# if else
score: int = int(input("enter your test score: "))

if (0 <= score <= 40):
    print("try harder next time...")
elif (41 <= score <= 60):
    print("your getting there,need some more work")
elif (61 <= score <= 80):
    print("pretty good")
elif (81 <= score <= 95):
    print("awesome!")
elif (96 <= score <= 100):
    print("excellent!!! You're a Star!")
else:
    print("illegal grade")

# match case
score: int = int(input("enter your test score: "))
match score:
    case score if 0 <= score <= 40:
        print("try harder next time...")
    case score if 41 <= score <= 60:
        print("your getting there,need some more work")
    case score if 61 <= score <= 80:
        print("pretty good")
    case score if 81 <= score <= 95:
        print("awesome!")
    case score if 96 <= score <= 100:
        print("excellent!!! You're a Star!")
    case _:
        print("illegal grade")
