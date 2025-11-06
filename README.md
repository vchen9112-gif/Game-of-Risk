# Cyber Risk Simulator (CyberJack-Roulette)

## 📖 Overview
Cyber Risk Simulator is a single-player Python game that combines blackjack-inspired mechanics with cybersecurity-themed challenges.  
Players aim to get a hand value as close to 21 as possible while facing random cybersecurity events, reinforcing concepts such as phishing, firewalls, and encryption in an interactive way.

## 🎮 How to Play

**Player:** Single-player against an automated dealer.  
**Objective:** Get as close to 21 as possible without exceeding it. Cybersecurity-themed events add an educational twist.

### Gameplay Overview
1. Both the player and dealer receive **two cards** from a shuffled 52-card deck at the start of each round.  
2. A **roulette wheel** introduces random cybersecurity events:  
   - **Phishing Alert:** Answer a cybersecurity question correctly to continue your turn.  
   - **Firewall Down:** Dealer receives an extra card.  
   - **Zero-Day Exploit:** Dealer’s hand becomes fully visible.  
   - **System Stable:** No event occurs.  
3. During your turn, choose to **Hit** (draw another card) or **Stand** (keep your current hand).  
4. Exceeding 21 results in an **automatic loss**.  
5. The dealer draws cards until reaching **at least 17**. Exceeding 21 causes the dealer to lose.  
6. Round outcome:  
   - Player wins if total is closer to 21 than dealer.  
   - Dealer wins if total is higher.  
   - Tie if scores are equal.  
7. Each round lasts one game, but you can **play indefinitely** until you choose to exit.

### How to Run
1. Ensure **Python 3** is installed.  
2. Open **Visual Studio Code** (or any Python IDE).  
3. Create a `.py` file and paste the code.  
4. Run the program:  
```bash
cyberjack_roulette .py

## 🧩 What I Learned
1. Implemented blackjack-inspired gameplay in Python
2. Integrated cybersecurity concepts into interactive events
3.Developed clean, functional, single-file Python code
4.Learned how to structure game logic and handle random events in Python

##🔮 Future Improvements
1.Dynamic Questions: Shuffle questions and answer choices to make gameplay more unpredictable and engaging.
2.Replay Feature: Allow players to continue playing without restarting the program, improving user experience.
3.GUI Interface (Optional): Create a graphical interface for a more interactive experience.
4.Expanded Cybersecurity Events: Add more types of challenges or scenarios to enhance the educational component.







