senten_input=input("Enter the sentence:")
em_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "Python": "🐍",
    "AI": "🤖",
    "fire": "🔥",
    "cool": "😎",
    "coffee": "☕",
    "food": "🍕",
    "music": "🎵",
    "car": "🚗",
    "laugh": "😂",
    "money": "💰",
    "computer": "💻",
    "phone": "📱",
    "sun": "☀️",
    "moon": "🌙",
    "star": "⭐",
    "cat": "🐱",
    "dog": "🐶"
}
mod_senten=[]
for i in senten_input.split():
    if i in em_dict:
        i=em_dict[i]
        mod_senten.append(i)
    else:
        mod_senten.append(i)

for i in mod_senten:
    print(i,end=' ')


