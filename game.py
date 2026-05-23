import random
import time

score = 0
lives = 3

print("🎮 Welcome to Math Quiz Game!")
print("❤️ Lives:", lives)

start_time = time.time()

for i in range(5):

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        answer = num1 + num2

    elif operation == "-":
        answer = num1 - num2

    else:
        answer = num1 * num2

    user = int(input(f"\n{num1} {operation} {num2} = "))

    if user == answer:
        print("🔊 Ding! Correct ✅")
        score += 1

    else:
        print("🔊 Buzz! Wrong ❌")
        print("Correct answer was:", answer)

        lives -= 1
        print("❤️ Lives left:", lives)

        if lives == 0:
            print("💀 Game Over!")
            break

end_time = time.time()

total_time = round(end_time - start_time, 2)

print("\n🎯 Final Score:", score, "/ 5")
print("⏱️ Time Taken:", total_time, "seconds")

if score == 5:
    print("🏆 Amazing! Perfect Score!")

elif score >= 3:
    print("😄 Good Job!")

else:
    print("💪 Keep Practicing!")