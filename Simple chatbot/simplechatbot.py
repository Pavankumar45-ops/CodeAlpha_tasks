def simple_chatbot():
    print("chatbot: Hi I'm a simple bot.(type 'bye' to exit)")

    while True:
        user_input=input("YOU:").lower()
        if "hello" in user_input or "Hi" in user_input:
            print("chatbot: Hi there!")
        elif "how are you" in user_input:
            print("chatbot:I'm fine,thanks for asking!")
        elif "your name" in user_input:
            print("chatbot:I am the Codealpha Task bot.")
        elif "bye" in user_input:
            print("chatbot:Goodbye! Have a great day.")
        else:
            print("chatbot: I'm not sure how to answer that yet.")

simple_chatbot()