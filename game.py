import random
n = random.randint(1,50)
ans = None
while ans!=n:
	ans = int(input("guess the num between 1 t0 50: "))

	if ans == n:
		print("yes it is true")
		break
	else:
		print("better luck next time")
