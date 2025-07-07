def chatbot_response(msg):
    if "sad" in msg or "depressed" in msg:
        return "I'm here for you. Try taking a deep breath. Want to try a breathing exercise?"
    elif "lonely" in msg:
        return "You're not alone. Would you like to talk to a counselor?"
    else:
        return "Tell me more about how you're feeling."

# Test
while True:
    inp = input("You: ")
    if inp.lower() == "exit":
        break
    print("Bot:", chatbot_response(inp))
