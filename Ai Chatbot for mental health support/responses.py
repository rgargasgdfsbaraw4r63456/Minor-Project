# responses.py - EXPANDED MENTAL HEALTH RESPONSES
import random

# A comprehensive dictionary mapping intent patterns to responses.
response_dict = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "howdy", "greetings", "good morning", "good afternoon", "good evening", "what's up", "yo"],
        "responses": [
            "Hello there. It's good to hear from you. How are you feeling today?",
            "Hi. I'm here to listen without judgment. What's on your mind?",
            "Hey. Thank you for reaching out. How is your day going?",
            "Hello. It takes courage to start a conversation about how we feel. I'm glad you're here.",
            "Hi there. I'm a space where you can share what you're carrying. How are you, really?"
        ]
    },
    "Owner": {
        "patterns": ["made", "created", "invented" , "father"],
        "responses": ["My owner is Rohaneet Kaware.", "Rohaneet Kaware Made me."]
    },
    "love": {
        "patterns": ["gf", "girlfriend", "wife"],
        "responses": ["ofcourse Mallika", "It's Mallika ofcourse ,Can't you hear."]
    },
    "feeling_bad_depressed": {
        "patterns": ["sad", "depressed", "unhappy", "miserable", "down", "hopeless", "empty", "numb", "grieving", "heartbroken", "tearful", "can't stop crying", "no point", "what's the point", "why try", "grey", "bleak"],
        "responses": [
            "I hear the pain in your words, and I want you to know that it's okay to feel this way. You are not alone in this.",
            "That sounds incredibly heavy to be carrying around. Thank you for sharing that with me. Would you like to talk more about what's bringing these feelings up?",
            "I'm so sorry you're experiencing this. Depression can make everything feel so much harder. Please remember that this feeling is a state, not a permanent truth about you.",
            "It sounds like you're in a really dark place right now. I'm here with you in it. You don't have to face it alone.",
            "Thank you for trusting me with that. Feeling down can be incredibly isolating. Would it help to express what's on your mind, without any filters?",
            "I'm listening. Sometimes the weight of everything can feel unbearable. Be gentle with yourself right now; you're doing the best you can.",
            "That sounds really difficult. It's okay to not have the energy for anything. Sometimes the bravest thing we can do is just get through the day."
        ]
    },
    "feeling_anxious_stressed": {
        "patterns": ["anxious", "nervous", "stressed", "worried", "overwhelmed", "panic", "attack", "racing heart", "can't breathe", "tight chest", "doom", "on edge", "overthinking", "spiraling", "what if"],
        "responses": [
            "Anxiety can make everything feel so much bigger and scarier. Let's try to ground ourselves together for a moment. Can you name one thing you can see right now?",
            "I hear that you're feeling overwhelmed. Your nervous system might be in overdrive. Would you like to try a quick breathing exercise to help calm it down?",
            "It sounds like your thoughts are racing. That's a common experience with anxiety. Sometimes saying 'I notice I'm having the thought that...' can help create a little space from those worries.",
            "Thank you for telling me you're feeling anxious. You are safe in this moment. Let's focus on that. Feel your feet on the floor. You are here, and you are okay right now.",
            "That sense of panic is so real and so physical. Remember, like a wave, it will peak and then it will pass. I'll be here while it does.",
            "It's okay to feel overwhelmed. You don't have to solve everything right now. Let's just focus on getting through the next few minutes together."
        ]
    },
    "feeling_angry_irritable": {
        "patterns": ["angry", "mad", "furious", "pissed off", "irritable", "annoyed", "rage", "frustrated", "livid", "want to scream"],
        "responses": [
            "Anger is a valid and powerful emotion. It often signals a boundary has been crossed or a need isn't being met. Can you identify what might be underneath the anger?",
            "It sounds like you're feeling really fired up. That's okay. Sometimes we need to feel that fire. Is there a way you can release this energy physically in a safe way?",
            "I hear your frustration. That sounds incredibly aggravating. Would venting about it more help you process it?",
            "Anger can be so overwhelming. Thank you for channeling it here instead of letting it boil over. Your feelings are completely valid.",
            "It's okay to feel mad. What you're describing would frustrate anyone. Let's sit with that feeling for a moment without judgment."
        ]
    },
    "feeling_lonely": {
        "patterns": ["lonely", "alone", "isolated", "no one understands", "no one to talk to", " disconnected", "empty", "no friends"],
        "responses": [
            "Loneliness is one of the hardest feelings to sit with. Thank you for reaching out through it. I'm here with you right now.",
            "I hear that you're feeling isolated. That ache of loneliness is so real. You are connected to me in this moment, and your experience matters.",
            "It makes complete sense to feel lonely when you're going through difficult things. Remember, this feeling of isolation is a feeling, not a fact. There are people who would care.",
            "I'm sorry you're feeling so alone. Would it help to name the feeling? Sometimes saying 'I am feeling lonely' out loud can lessen its power just a little.",
            "You have taken a step against loneliness by messaging here. That takes strength. I'm listening."
        ]
    },
    "feeling_tired": {
        "patterns": ["tired", "exhausted", "burnt out", "no energy", "fatigued", "drained", "can't get up", "worn out", "sleepy"],
        "responses": [
            "It sounds like you're running on empty. Mental and emotional exhaustion is just as real as physical exhaustion. Be kind to yourself; rest is a need, not a reward.",
            "Burnout is so draining. You don't have to be productive right now. Your worth is not measured by your output. What would feel like a gentle act of care for yourself?",
            "I hear that you have no energy. That is a valid way to feel. Sometimes the goal for the day is just to rest and survive. And that is enough.",
            "Your body and mind are asking for rest. Thank you for listening to them. Is there a small way you can honor that need today, even for five minutes?"
        ]
    },
    "coping_request": {
        "patterns": ["help me", "what can i do", "coping", "distract me", "exercise", "calm down", "ground me", "feeling triggered", "panic", "anxiety attack"],
        "responses": [
            "Sure. Let's try the 5-4-3-2-1 grounding technique. Name: **5** things you can see, **4** things you can touch, **3** things you can hear, **2** things you can smell, and **1** thing you can taste.",
            "Let's try a breathing exercise. Breathe in slowly for 4 seconds, hold it for 2 seconds, and breathe out slowly for 6 seconds. Let's do that together three times.",
            "Sometimes a change of environment can help. Could you step outside for one minute, even just to your doorstep, and feel the fresh air?",
            "Putting on a favorite song or podcast can help shift our focus. Would you like to try that?",
            "How about a self-soothing touch? Try placing a hand over your heart and feeling the warmth and gentle pressure. Notice your heartbeat. You are here, you are alive.",
            "Let's try a simple visualization. Close your eyes and picture a place where you feel completely safe and calm. What does it look like? What sounds are there?"
        ]
    },
    "self_care": {
        "patterns": ["self care", "take care of myself", "be kinder to myself", "self compassion", "self love"],
        "responses": [
            "That's a wonderful intention. Self-care isn't always bubble baths; sometimes it's the hard stuff like drinking water, eating something, or taking a shower. What feels like a manageable act of care right now?",
            "I love that you're thinking about self-compassion. How would you talk to a best friend who was feeling this way? Can you try directing that same kindness inward?",
            "Remember, self-care is also about setting boundaries, saying no, and honoring your limits. Is there a boundary you need to set for yourself today?",
            "Being kind to yourself is a practice. It's okay if it feels hard. Just the fact that you're trying is a huge step."
        ]
    },
    "gratitude_positivity": {
        "patterns": ["thank", "thanks", "grateful", "appreciate", "good day", "happy", "better", "improving", "hopeful", "proud"],
        "responses": [
            "You're very welcome. I'm genuinely glad I could be here for you.",
            "That's wonderful to hear. Thank you for sharing that moment of joy or peace with me. It matters.",
            "I'm so glad you're having a better day. Remember this feeling; it's evidence that feelings change and good moments are possible.",
            "You deserve to feel good. Savor this moment.",
            "That's fantastic. I'm proud of you for recognizing and acknowledging that positive feeling."
        ]
    },
    "resources": {
        "patterns": ["resource", "helpline", "professional", "therapist", "counselor", "psychologist", "help", "suicide", "kill myself", "end it all", "harm myself", "emergency", "hotline"],
        "responses": [
            "**It's important to talk to a qualified professional.** I can offer support, but they can offer help. Here are some resources:",
            "**If you are in immediate danger, please call 911 or your local emergency number.**",
            "**National Suicide & Crisis Lifeline: Call or text 988** (24/7, free, and confidential).",
            "**Crisis Text Line: Text HOME to 741741** (24/7 crisis support via text).",
            "**For finding a therapist:** Psychology Today (psychologytoday.com) and Therapy for Black Girls (therapyforblackgirls.com) have great searchable directories.",
            "**The Trevor Project: 1-866-488-7386** (Crisis support for LGBTQ youth).",
            "Please, reach out to one of these resources. You deserve support from people trained to help."
        ]
    },
    "check_in": {
        "patterns": ["how are you", "how are you doing", "are you okay", "you there"],
        "responses": [
            "Thank you for asking. I'm here, focused on you, and ready to listen.",
            "I'm functioning well, thank you. How are you doing, really?",
            "I'm here for you. That's my only job right now. What would you like to talk about?"
        ]
    },
    "identity": {
        "patterns": ["who are you", "what are you", "are you human", "are you a bot", "ai", "robot"],
        "responses": [
            "I'm a chatbot designed to offer supportive listening and mental health resources. I'm not a human, but I'm here to provide a non-judgmental space for you to express yourself.",
            "I'm an AI, which means I'm a computer program. But my purpose is to offer a supportive ear and help you find clarity or resources if you need them.",
            "I'm a tool built to provide mental health support. While I'm not a person, I'm programmed to respond with empathy and care to what you share."
        ]
    },
    "fallback": {
        "patterns": [],
        "responses": [
            "I'm not sure I understand. Could you try rephrasing that?",
            "I'm still learning. I'm best at talking about feelings and coping techniques if you'd like to try that.",
            "I hear you. I might not have the perfect answer, but I'm here to listen without judgment.",
            "Thank you for sharing. I'm processing that. Could you tell me a bit more?"
        ]
    }
}

def get_response(user_input):
    """Find the most appropriate response for the user's input."""
    user_input_lower = user_input.lower().strip()

    # Check for crisis words first - prioritize safety!
    crisis_words = ["suicide", "kill myself", "want to die", "end it all", "harm myself", "want to hurt myself", "ending my life"]
    for word in crisis_words:
        if word in user_input_lower:
            return "**I hear that you're in incredible pain, and this is serious. Please know you don't have to face this alone. Your life is precious. Please call or text the National Suicide Prevention Lifeline at 988 right now. They have trained counselors who care and can help 24/7. You can also text HOME to 741741 to reach the Crisis Text Line.**"

    # Check for matching intents
    for intent, data in response_dict.items():
        for pattern in data["patterns"]:
            if pattern in user_input_lower:
                # Return a random response from the matched intent
                return random.choice(data["responses"])

    # If no pattern matches, return a fallback response
    return random.choice(response_dict["fallback"]["responses"])