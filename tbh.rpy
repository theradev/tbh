# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    $ gratitude = 0
    $ growth = 0
    $ dreams = 0
    $ self_discovery = 0
    $ self_love_healing = 0
    $ fears_doubt = 0
    $ relationships = 0
    $ fun_more = 0


    menu:
        "Select a topic."
        "Gratitude":
            $ var = "gratitude"
            jump evaluate_category_choice
        "Growth":
            $ var = "growth"
            jump evaluate_category_choice
        "Dreams and Goals":
            $ var = "dreams"
            jump evaluate_category_choice
        "Self Discovery":
            $ var = "self_discovery"
            jump evaluate_category_choice
        "Self Love & Healing":
            $ var = "self_love_healing"
            jump evaluate_category_choice
        "Fears and Doubts":
            $ var = "fears_doubt"
            jump evaluate_category_choice
        "Relationships":
            $ var = "relationships"
            jump evaluate_category_choice
        "Fun and More":
            $ var = "fun_more"
            jump evaluate_category_choice
        "Exit program":
            return

label evaluate_category_choice:
    python:
        import random
        if var == "gratitude":
            n = random.randint(1, 6)
        elif var == "growth":
            n = random.randint(1, 15)
        elif var == "dreams":
            n = random.randint(1, 15)
        elif var == "self_discovery":
            n = random.randint(1, 16)
        elif var == "self_love_healing":
            n = random.randint(1, 15)
        elif var == "fears_doubt":
            n = random.randint(1, 11)
        elif var == "relationships":
            n = random.randint(1, 17)
        elif var == "fun_more":
            n = random.randint(1, 25)

        renpy.jump(var + "_" + str(n))

# Gratitude
label gratitude_1:
    "What are five things you've achieved in your life that you're proud of?"
    jump start

label gratitude_2:
    "Love comes in many forms. Where do you see love in your life?"
    jump start

label gratitude_3:
    "What's your favorite place in the world? What do you love about this place?"
    jump start

label gratitude_4:
    "What in your life do you have now that you used to dream about having in the past?"
    jump start

label gratitude_5:
    "What are five things you're grateful for that you can see from where you're sitting now?"
    jump start

label gratitude_6:
    "What's something you tend to take for granted? How can you start showing gratitude instead?"
    jump start

# Growth
label growth_1:
    "What are the life lessons that you've had to learn over and over again?"
    jump start

label growth_2:
    "What skills or knowledge do you have now that you didn't have before?"
    jump start

label growth_3:
    "What do you tend to not take responsibility for? How can you take more responsibility in this area?"
    jump start

label growth_4:
    "What are the excuses you make for not doing the things you say you want to do? Why do you make these excuses?"
    jump start

label growth_5:
    "What failures in your life can you see as detours instead? What did you learn and gain from these detours?"
    jump start

label growth_6:
    "What is a mistake you've made recently? What lessons have you learned from that mistake?"
    jump start

label growth_7:
    "What was a life lesson that you had to learn the hard way?"
    jump start

label growth_8:
    "What was a perspective shift you've experienced that had the greatest impact on your life?"
    jump start

label growth_9:
    "What was the biggest challenge that you've ever faced in your life? How were you able to overcome it?"
    jump start

label growth_10:
    "When was the last time you felt like giving up? What motivated you to keep going?"
    jump start

label growth_11:
    "Where do you feel shame or guilt in your life? Why do you feel ashamed or guilty about this?"
    jump start

label growth_12:
    "What are some lies you tell yourself? What is false about those lies?"
    jump start

label growth_13:
    "How has your life evolved over the past three months?"
    jump start

label growth_14:
    "What is the biggest risk you've ever taken?"
    jump start

label growth_15:
    "What is one thing you can change today that would make the greatest impact on your future?"
    jump start

# Dreams and Goals
label dreams_1:
    "What does it mean for you to live a successful and meaningful life?"
    jump start

label dreams_2:
    "What is a dream oracle that is so big, you'd be amazed at yourself for achieving it?"
    jump start

label dreams_3:
    "What would you say to your future self who has achieved all of their dreams?"
    jump start

label dreams_4:
    "Where is your ideal place to live? What does your dream home and community look like?"
    jump start

label dreams_5:
    "What is something you would do (big or small), if you knew you could not fail?"
    jump start

label dreams_6:
    "If you didn't have to work and money wasn't an issue, how would you spend your days?"
    jump start

label dreams_7:
    "How would you live your life if you stopped caring about what others thought of you?"
    jump start

label dreams_8:
    "What are the characteristics of your dream life? Which ones are nonnegotiable?"
    jump start

label dreams_9:
    "What's one habit that has been helping you, and one habit that has been hurting you?"
    jump start

label dreams_10:
    "Every career has its downsides. What are the downsides of your dream career that you're willing to deal with?"
    jump start

label dreams_11:
    "If you could become an expert in anything, what would it be?"
    jump start

label dreams_12:
    "What would you do if you only had one year left to live?"
    jump start

label dreams_13:
    "What are some dreams that you have buried and forgotten, that you once wanted to achieve?"
    jump start

label dreams_14:
    "On a scale from one to 10, how aligned do you feel to your dream life and why?"
    jump start

label dreams_15:
    "If you were famous, what would you want to be known for?"
    jump start

# Self Discovery
label self_discovery_1:
    "What are your most important values in life? Are you living in a way that prioritizes these values?"
    jump start

label self_discovery_2:
    "What moments or experiences make you feel the most alive?"
    jump start

label self_discovery_3:
    "What is the one message or lesson you would want to share with the world and why?"
    jump start

label self_discovery_4:
    "Do you usually listen to your head or your heart? What are examples of when you've done each?"
    jump start

label self_discovery_5:
    "What beliefs do you have that could be holding you back from living your best life?"
    jump start

label self_discovery_6:
    "What were you like as a child? What did you love to do?"
    jump start

label self_discovery_7:
    "What do you feel life has been trying to teach you lately? What are the signs that make you think this way?"
    jump start

label self_discovery_8:
    "Are there any emotions you've been hiding from yourself or others recently? Why?"
    jump start

label self_discovery_9:
    "What is your favorite childhood memory? Why is it your favorite?"
    jump start

label self_discovery_10:
    "As a child, what did you want to be when you grew up? Why were you interested in that path?"
    jump start

label self_discovery_11:
    "Flow is a mental state where you're fully immersed in an activity you enjoy, and you lose track of time. What activities put you into a flow state?"
    jump start

label self_discovery_12:
    "What's the biggest thing you've been procrastinating on lately? Why have you been resistant to working on it?"
    jump start

label self_discovery_13:
    "What is a unique strength or talent you have that you're proud of? How do you use it in your own life and for others? How did you discover it?"
    jump start

label self_discovery_14:
    "If you could relive your life, what would you have done differently?"
    jump start

label self_discovery_15:
    "What was your favorite feeling from the past month? What happened to spark that feeling?"
    jump start

label self_discovery_16:
    "Where do you find the most joy in your days?"
    jump start

# Self-Love & Healing
label self_love_healing_1:
    "Who do you tend to compare yourself to? Why?"
    jump start

label self_love_healing_2:
    "What are you too hard on yourself for? Where did this pressure come from?"
    jump start

label self_love_healing_3:
    "What types of experiences make you feel loved? How do you show yourself that kind of love?"
    jump start

label self_love_healing_4:
    "What's one belief, memory, or item in your life that you would like to let go of?"
    jump start

label self_love_healing_5:
    "In what ways can you start putting yourself first and doing what's best for you?"
    jump start

label self_love_healing_6:
    "What parts of your personality do you love? How can you show these parts of yourself more often?"
    jump start

label self_love_healing_7:
    "What was one of the most emotionally painful experiences in your life? How are you a better person after this experience?"
    jump start

label self_love_healing_8:
    "What's a part of yourself that you keep hidden from others? What would happen if you showed that part of yourself?"
    jump start

label self_love_healing_9:
    "When was the last time you cried? Have you healed from that experience?"
    jump start

label self_love_healing_10:
    "What was the best compliment you've ever received? Why was it so special?"
    jump start

label self_love_healing_11:
    "Think back to a time when you were in a period of struggle. What would you say to your past self?"
    jump start

label self_love_healing_12:
    "Describe an embarrassing moment in your life that has stuck with you."
    jump start

label self_love_healing_13:
    "What area of your life has been neglected the most? What is one thing that you can do to nurture that area?"
    jump start

label self_love_healing_14:
    "What does your self-care look like right now? What can you do to improve it?"
    jump start

label self_love_healing_15:
    "What is a pain in your life that you'd most like to heal?"
    jump start

# Fears and Doubt
label fears_doubt_1:
    "What are some fears you used to have? How were you able to overcome them?"
    jump start

label fears_doubt_2:
    "What are the fears that have been holding you back recently?"
    jump start

label fears_doubt_3:
    "When do you notice your sense of self-doubt or self-criticism the most? What are your triggers?"
    jump start

label fears_doubt_4:
    "In what areas of your life do you care about what people think about you? Why?"
    jump start

label fears_doubt_5:
    "If your worst fears were to come true, what would you do?"
    jump start

label fears_doubt_6:
    "When was the last time you stepped outside of your comfort zone? How did you feel afterwards?"
    jump start

label fears_doubt_7:
    "What advice might your future self give you about something difficult you're dealing with today?"
    jump start

label fears_doubt_8:
    "What's something you've always wanted to do but were too scared to? What thoughts have stopped you from moving forward?"
    jump start

label fears_doubt_9:
    "What's the biggest thing you've been in denial about recently? What would it take to work through that denial?"
    jump start

label fears_doubt_10:
    "What do you feel is holding you back from feeling successful in your life? Is there a way you can push past that barrier?"
    jump start

label fears_doubt_11:
    "What emotion is the hardest for you to express? Why do you think that is?"
    jump start

# Relationships
label relationships_1:
    "What would you say now to someone who hurt you in the past?"
    jump start

label relationships_2:
    "Is there someone who holds a grudge against you? Is there a way you can help them heal?"
    jump start

label relationships_3:
    "What type of people do you want to surround yourself with?"
    jump start

label relationships_4:
    "How can you show the people in your life more love?"
    jump start

label relationships_5:
    "At the end of your life, how do you want to be remembered by the world?"
    jump start

label relationships_6:
    "What's your definition of an ideal friendship?"
    jump start

label relationships_7:
    "Who is someone in your life you haven't shown enough appreciation for? How can you show them your appreciation?"
    jump start

label relationships_8:
    "Who is someone in your life you'd like to become closer to? Why?"
    jump start

label relationships_9:
    "Is there someone in your life who you've grown apart from? Why did you grow apart? Would you like to reconnect? Why or why not?"
    jump start

label relationships_10:
    "Is there someone you've been trying to prove yourself to? Who do you seek approval from, and why?"
    jump start

label relationships_11:
    "What habits or traits in other people bother you? Why?"
    jump start

label relationships_12:
    "What habits or traits in other people do you love? Why?"
    jump start

label relationships_13:
    "What is one lesson you learned from your upbringing that you'd like to pass onto future generations? Why?"
    jump start

label relationships_14:
    "How do you think your family has influenced your relationships?"
    jump start

label relationships_15:
    "When was the last time you were happy for another person?"
    jump start

label relationships_16:
    "Is there someone from your past you've been unable to forgive or let go of?"
    jump start

label relationships_17:
    "When is the last time you stood up for yourself? How did that make you feel?"
    jump start

# Fun and More!
label fun_more_1:
    "What fictional character do you relate to most? What qualities do you see in them?"
    jump start

label fun_more_2:
    "Are there any scents that you associate with special memories or experiences?"
    "Sage reminds me of the part of the pandemic when I lived alone. In a way, my life resetted then."
    jump start

label fun_more_3:
    "Are there any foods or drinks that you associate with special memories or experiences?"
    "There was that time you made the maple turkey dumplings. It reminds me of when we used to go to the city to that spot next to the park."
    jump start

label fun_more_4:
    "If you could live out five other imaginary lives and be/do anything in the world, what would you be or do?"
    jump start

label fun_more_5:
    "What's one place you'd like to travel to in the next five years? What draws you to that place?"
    jump start

label fun_more_6:
    "What is the best advice you've ever received? How have you applied it to your own life?"
    "Wearing a helmet. In other words, having a contingency plan for when life goes left."
    jump start

label fun_more_7:
    "What is your favorite quote? What does it mean to you?"
    jump start

label fun_more_8:
    "What are your favorite song lyrics? Why?"
    jump start

label fun_more_9:
    "If you could relive one day of your life, which would it be and why?"
    jump start

label fun_more_10:
    "If you could relive one year of your life, which would it be and why?"
    jump start

label fun_more_11:
    "What memory never fails to make you laugh?"
    jump start

label fun_more_12:
    "If a crystal ball could show you any part of your future, what would you want to see and why?"
    jump start

label fun_more_13:
    "What is something you can do to make the world a better place?"
    jump start

label fun_more_14:
    "If you could have a conversation with one person in the world, who would it be and why? What would you want to talk about?"
    jump start

label fun_more_15:
    "What does a peaceful life look like to you? In contrast, what does a playful life look like to you?"
    jump start

label fun_more_16:
    "If you could go back in time one year and tell yourself one thing, what would you say?"
    jump start

label fun_more_17:
    "What's the worst advice you've ever received?"
    jump start

label fun_more_18:
    "What's your biggest pet peeve?"
    jump start

label fun_more_19:
    "If you could swap lives for a day with anyone in the world, who would it be and why?"
    jump start

label fun_more_20:
    "What's one book, movie, or TV show that you can reread/rewatch over and over again?"
    "Cryptonomicon."
    jump start

label fun_more_21:
    "If you could've picked your own name, what would it be and why?"
    jump start

label fun_more_22:
    "What book, movie, or TV show is your guilty pleasure and why?"
    jump start

label fun_more_23:
    "If you had to start your own business and have it be a guaranteed success, what kind of business would it be?"
    jump start

label fun_more_24:
    "What's the silliest fear you have?"
    jump start

label fun_more_25:
    "What is your earliest memory?"
    jump start





    # This ends the game.

    return
