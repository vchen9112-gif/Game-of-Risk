# Used to randomize most of the features within the code
import random

# A format list used to set the value of the card 
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10,
    'A': 11  
}

# Create a deck of cards (52 cards total)
def create_deck():
    deck = [] # A list with nothing in it currently(used to store the value of the 52 cards)
    for card in card_values: #the values inside card_values are card(13)
        for _ in range(4):  # There is 4 suits of 13 of the same card we used double for loop(4)
            deck.append(card) # Adds the card one by one into the deck list 
    random.shuffle(deck) # .shuffle is used to randomize the list order 
    return deck

# Calculate total score that is in the hand of the user(both player and dealer)
# Act as the algorithm for the player and the dealer
def calculate_score(hand):
    total = 0   #
    aces = 0
    for card in hand:
        total += card_values[card]  # When drawn if the player/dealer receives A in their and the total
        if card == 'A':     # value of the score in hand is less than 21 then the aces is recorded and plus 1
            aces += 1
    # If total is over 21, turn Aces from 11 to 1
    while total > 21 and aces > 0:  #Conditional statement where both total score is above 21 and aces is greater than 0
        total -= 10
        aces -= 1
    return total

# Ask a cybersecurity question
def ask_question():
    questions = [
    {
        "question": "What does HTTPS stand for?",   # The question ask when a certain requirement is met
        "choices": [                                # The answer choices regarding the question
            ("HyperText Transfer Protocol Secure", True),   #Multiple choice question with only one correct answer
            ("High-Tech Transport Protocol Service", False),
            ("HyperText Transfer Private Session", False),
            ("Home Transfer Protocol Service", False)
        ]
    },
    {
        "question": "What is a firewall used for?",
        "choices": [
            ("Blocking unauthorized access", True),
            ("Speeding up internet", False),
            ("Encrypting data", False),
            ("Building websites", False)
        ]
    },
    {
        "question": "What is phishing?",
        "choices": [
            ("A method to trick people into giving info", True),
            ("A firewall configuration", False),
            ("A type of encryption", False),
            ("A security update", False)
        ]
    },
    {
        "question": "What is multi-factor authentication?",
        "choices": [
            ("Using more than one way to verify identity", True),
            ("Logging in with a username only", False),
            ("Changing passwords regularly", False),
            ("Encrypting passwords", False)
        ]
    },
    {
        "question": "Which of the following is a type of social engineering?",
        "choices": [
            ("Phishing", True),
            ("Malware", False),
            ("Firewall", False),
            ("Encryption", False)
        ]
    },
    {
        "question": "What does CIA stand for in cybersecurity?",
        "choices": [
            ("Confidentiality, Integrity, Availability", True),
            ("Cybersecurity Information Agency", False),
            ("Confidential Internet Access", False),
            ("Central Intelligence Access", False)
        ]
    },
    {
        "question": "What does a VPN do?",
        "choices": [
            ("Creates a secure connection over the internet", True),
            ("Deletes malicious files", False),
            ("Speeds up the internet", False),
            ("Blocks pop-ups", False)
        ]
    },
    {
        "question": "What is the purpose of penetration testing?",
        "choices": [
            ("Find security weaknesses in a system", True),
            ("Improve software speed", False),
            ("Train users on phishing", False),
            ("Install firewalls", False)
        ]
    },
    {
        "question": "What is the main purpose of endpoint protection software?",
        "choices": [
            ("Protect devices like laptops and phones from cyber threats", True),
            ("Create backup servers", False),
            ("Host websites", False),
            ("Detect hardware failure", False)
        ]
    },
    {
        "question": "What is the least privileged principle?",
        "choices": [
            ("Users should only have access to what they need", True),
            ("Admins can do anything", False),
            ("Only guests can view files", False),
            ("All users should be equal", False)
        ]
    },
    {
        "question": "What is the function of a Security Information and Event Management (SIEM) system?",
        "choices": [
            ("Monitor and analyze security alerts", True),
            ("Encrypt user passwords", False),
            ("Run automatic updates", False),
            ("Block advertisements", False)
        ]
    },
    {
        "question": "Which one is an example of a strong password?",
        "choices": [
            ("D3f!n3_S3cur3#2024", True),
            ("12345678", False),
            ("password", False),
            ("abcdefg", False)
        ]
    }
]
    # Randomize the questions being asked 
    q = random.choice(questions)
    print("\nCybersecurity Question:")
    print(q["question"]) # Prints the question that is randomized from the list and print them to the user
    # Shuffle the answer choices
    choices = q["choices"]  # the variable choices represents the answer choices corresponding with the question that has been randomize
    random.shuffle(choices) # As said before .shuffle reorganize the order of the strings of the answer choices in the list 
# Show the answer choices with numbers
    for i in range(len(choices)): # choices: the str that represents the 4 answer choice to the question 
        print(str(i + 1) + ". " + choices[i][0]) # len (choices) equal 4 and range of 4 equals from 0 to 3: 0,1,2,3
# Then with each for loop it adds 1 to each i which gives 1,2,3,4 and print each answer choice with it's number and content
    # Ask for user input
    answer = input("Choose your choices(type the number): ")

    # Check if the answer is correct
    if answer.isdigit(): # Convert the input of the user back to len(uno reverse of the previous)
        index = int(answer) - 1
        if 0 <= index < len(choices):
            if choices[index][1]: # Check the content of the answer with the list 
                print("Correct! You earned a bonus.")
                return True
        else:
            print("Incorrect.")
            return False

# Spin the roulette wheel
def spin_roulette():
    outcomes = [
        "Firewall Down",       # Dealer gets one extra card
        "Phishing Alert",      # Player loses turn unless they answer correctly
        "System Stable",       # Nothing happens
        "Zero-Day Exploit"     # Dealer shows all cards
    ]
    result = random.choice(outcomes)    # Randomize the outcome of the roulette
    print("\nRoulette spin result:", result) # Prints the result of the randomize roulette 
    return result


# Main game function

def play_game():
    print("=== Welcome to CyberJack-Roulette ===")

    # Create and shuffle deck
    deck = create_deck()

    # Deal cards
    player_hand = [deck.pop(), deck.pop()]  # Save the value you have rolled in the deck list to player
    dealer_hand = [deck.pop(), deck.pop()]  # Save the value of the dealer in the deck list to dealer
# Both dealer and player's process start at the same time 
    # Spin the roulette
    event = spin_roulette()
    bonus = False

    if event == "Phishing Alert":
        bonus = ask_question()
        if not bonus:
            print("You lost your turn due to phishing!")
            return  # End game early

    if event == "Zero-Day Exploit":
        print("Dealer’s cards are visible:", dealer_hand)

    if event == "Firewall Down":
        dealer_hand.append(deck.pop())
        print("Dealer got an extra card due to firewall breach!")

    # Show player’s hand
    print("\nYour cards:", player_hand)

    # Player turn: Hit or Stand
    # Conditional statement for the respond of the player to either risk or save
    while True:
        player_score = calculate_score(player_hand)
        print("Your current score:", player_score)
        if player_score > 21:
            print("You lost!")
            return
        move = input("Do you want to Hit or Stand? ").lower()
        if move == "hit":
            player_hand.append(deck.pop())
            print("You drew:", player_hand[-1])
        elif move == "stand":
            break
        else:
            print("Please type 'hit' or 'stand'.")

    # Dealer turn
    while calculate_score(dealer_hand) < 17: # A conditional statement thar is used to update dealer deck and score when it doesn't exceed 17
        dealer_hand.append(deck.pop())

    # Final scores
    print("\nFinal Hands:")
    print("Your hand:", player_hand, "| Score:", calculate_score(player_hand)) #prints the card in your deck and the current score 
    print("Dealer hand:", dealer_hand, "| Score:", calculate_score(dealer_hand)) #prints the card in the dealer's deck and the current score 

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Decide winner
    if player_score > 21:
        print("You lost. Dealer wins.")
    elif dealer_score > 21:
        print("Dealer lost. You win!")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")


# Start the game

play_game()
# Reattempting the game without configuring the code again
while True:
    play_game()
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != True:
        print("Thanks for playing CyberJack-Roulette! Stay cyber safe!")
        break
