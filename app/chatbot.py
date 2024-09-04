def get_response(user_input):
    # Normalize user input to lower case and remove leading/trailing spaces
    user_input = user_input.lower().strip()

    # Request to speak to a representative
    if "speak to a representative" in user_input or "speak to an agent" in user_input or \
       "talk to a representative" in user_input or "need help" in user_input:
        return ("I can help with that! Please provide your full name, phone number, date of birth, "
                "and the reason for wanting to speak to a representative. A representative will reach out to you shortly. "
                "However, please note that most of your queries can be answered here!")

    # Membership cancellation inquiries
    if "cancel membership" in user_input or "end membership" in user_input or \
       "want to leave" in user_input or "leaving" in user_input or \
       "stop my membership" in user_input or "unsubscribe" in user_input:
        return ("I understand you're looking to cancel your membership. We can offer you a one-time discount "
                "before you make that decision. Would you like more information?")

    # Basic greetings
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return ("Hello! How can I assist you today? If you have any questions regarding fitness, registration, "
                "or payments, feel free to ask! Don't forget to follow us on Instagram for tips and updates!")

    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return ("Thank you for chatting with me! Remember, consistency is key to achieving your health goals. "
                "Have a great day! And don't forget to follow us on Instagram for more tips!")

    # Inquiries about fitness or health
    elif "fitness" in user_input or "exercise" in user_input or "workout" in user_input:
        return ("Staying active is crucial for your health. What specific fitness goals are you looking to achieve? "
                "I can provide personalized tips or workout routines! Also, check out our Instagram for daily motivation!")

    elif "diet" in user_input or "nutrition" in user_input or "meal" in user_input:
        return ("A balanced diet is essential for overall well-being. Are you looking for advice on meal planning, "
                "specific dietary needs, or healthy recipes? Follow us on Instagram for nutritious meal ideas!")

    elif "motivation" in user_input or "inspiration" in user_input:
        return ("Remember, every small step counts towards your goals! Stay positive and keep pushing yourself. "
                "You've got this! Follow us on Instagram for daily motivation and inspiration!")

    # Registration inquiries
    elif "registration" in user_input or "sign up" in user_input or "register" in user_input or "enroll" in user_input:
        return ("To register, please visit our registration page or fill the online form or request a call. "
                "If you need help, let me know what specific issues you're facing!")

    # Payment confirmation inquiries
    elif "payment" in user_input or "confirmation" in user_input:
        return ("Please check your email for a payment confirmation. If you haven't received it or if there's an issue, "
                "please let me know!")

    # Subscription inquiries
    elif "subscription" in user_input or "plan" in user_input:
        return ("You can manage your subscription through your account settings. If you have issues, please describe them, "
                "and I'll do my best to help!")

    # Issues with assigned fitness program
    elif "issue" in user_input or "problem" in user_input or "assigned program" in user_input:
        return ("I'm sorry to hear you're having issues with your assigned fitness program. Could you please describe "
                "the problem you're facing? If it's not resolved, feel free to email support@kojayfitness.com for assistance.")

    # Specific fitness goals and programs
    elif ("chest" in user_input or "legs" in user_input or "arms" in user_input or "shoulders" in user_input or 
          "weight loss" in user_input or "lose weight" in user_input or "gain muscle" in user_input or 
          "glutes" in user_input or "ass" in user_input):
        return ("For specific training programs like building your chest, legs, arms, or for weight loss and muscle gain, "
                "please fill out the request form on our page to schedule a call with one of our trainers. "
                "They can provide personalized guidance to help you reach your goals!")

    # Common fitness queries
    elif "how to" in user_input:
        return ("I can help with that! What would you like to know how to do? Whether it's exercises, diets, or routines, just ask!")

    elif "best exercises" in user_input or "top workouts" in user_input:
        return ("The best exercises depend on your goals! For overall fitness, consider a mix of cardio, strength training, "
                "and flexibility exercises. What are your goals?")

    # Unknown input
    else:
        return ("I appreciate your input! However, I'm not equipped to answer that at the moment. Please ask me about "
                "fitness, nutrition, motivation, or any other health-related questions!")
