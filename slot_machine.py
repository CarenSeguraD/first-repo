import random

symbols = ['🍒', '7️⃣']
result = random.choices(symbols, k=3)
print(" | ".join(result))

if result == ['7️⃣', '7️⃣', '7️⃣']:
    print("Jackpot! 💰")
else:
    print("Try again! 🍀")
