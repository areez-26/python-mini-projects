import random

subjects = [
    "Aishwarya Rai",
    "Shubhman Gill",
    "A group of cats",
    "President of India",
    "Nirmala Sitharaman",
    "A Bangalore Software Engineer",
    "A Delhi Chaiwala"
]

actions = [
    "launches",
    "eats Jalebi",
    "goes by walk",
    "declares war",
    "secretly builds robot",
    "dances with",
    "argues about"
]

Places_or_things = [
    "At Tajmahal",
    "A plate of biryani",
    "During IPL match",
    "Inside college library",
    "Dubai Marina",
    "At Burj Khalifa",
    "On a wedding stage"

]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    Places_or_thing = random.choice(Places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {Places_or_thing}"
    print("\n",headline)

    user_input = input("\nDo you want another headline (Yes/No)?").strip().lower()
    if user_input == "no":
        break
    
print("\n Thanks for using the Fake News Headline Generator!")
        