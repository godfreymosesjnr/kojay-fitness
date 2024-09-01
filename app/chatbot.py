def get_response(user_input):
    # Normalize user input to lower case
    user_input = user_input.lower()

    # Basic greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today? If you have any questions regarding fitness or health, feel free to ask!"

    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input:
        return "Thank you for chatting with me! Remember, consistency is key to achieving your health goals. Have a great day!"

    # Inquiries about fitness or health
    elif "fitness" in user_input or "exercise" in user_input:
        return "Staying active is crucial for your health. What specific fitness goals are you looking to achieve? I can provide personalized tips!"

    elif "diet" in user_input or "nutrition" in user_input:
        return "A balanced diet is essential for overall well-being. Are you looking for advice on meal planning or specific dietary needs?"

    elif "motivation" in user_input:
        return "Remember, every small step counts towards your goals! Stay positive and keep pushing yourself. You've got this!"

    # General information requests
    elif "help" in user_input or "support" in user_input:
        return "I'm here to help! Please let me know what you need assistance with, and I'll do my best to provide the information you seek."

    # Unknown input
    else:
        return "I appreciate your input! However, I'm not equipped to answer that at the moment. Please ask me about fitness, nutrition, or motivation!"
