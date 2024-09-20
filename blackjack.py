from art import logo
import os #os means operating system
import random

def calculate_user_score(user_random_cards):
    """Calculates the score of the user's hand"""
    #Convert 10, 11, 12, 13 to 10 for the user
    for i, card in enumerate(user_random_cards): # means for each card in the list user_random_cards, i is the index and card is the value
        if card in [10, 11, 12, 13]:
            user_random_cards[i]=10
                
    # Handle Ace(1) for the user
    if 1 in user_random_cards:
        if sum(user_random_cards)+10<=21: #the sum includes the value 1 so we need to add 10 to it equalling 11
            user_random_cards[user_random_cards.index(1)]=11 #replace 1 with 11
            
    user_score=sum(user_random_cards)
    return user_score

def calculate_computer_score(computer_random_cards):
    """Calculates the score of the computer's hand"""
    #Convert 10, 11, 12, 13 to 10 for the user
    for i, card in enumerate(computer_random_cards): # means for each card in the list user_random_cards, i is the index and card is the value
        if card in [10, 11, 12, 13]:
            computer_random_cards[i]=10
                
    # Handle Ace(1) for the user
    if 1 in computer_random_cards:
        if sum(computer_random_cards)+10<=21: #the sum includes the value 1 so we need to add 10 to it equalling 11
            computer_random_cards[computer_random_cards.index(1)]=11 #replace 1 with 11
            
    computer_score=sum(computer_random_cards)
    return computer_score

#3 Ask if want to hit or stand 'y/n'
def hit_or_stand(user_score, computer_score, cards, user_random_cards, computer_random_cards):
    """asks the user if they want to hit or stand"""
    while user_score<21:
        user_choice=input("Do you want to hit (y) or stand (n)? 'y/n' ")
        if user_choice=='y':
            user_random_card=random.choice(cards)
            user_random_cards.append(user_random_card)
            user_score=sum(user_random_cards)
            print(f"Your hand: {user_random_cards}")
            print(f"Your score: {user_score}")
            
            #print("Computer's turn")
            computer_random_card=random.choice(cards)
            computer_random_cards.append(computer_random_card)
            computer_score=sum(computer_random_cards)
            #print(f"Computer's first card: {computer_random_cards[0]}")
            #print(f"checking computer card values prior to comparison: {computer_random_cards}")
        
        print(f"Computer's hand: {computer_random_cards}")
        print(f"Computer's final score: {computer_score}")
        can_continue = compare_scores(user_score, computer_score)
        if can_continue:
            continue
        else:
            return [user_score, computer_score, user_random_cards, computer_random_cards]
    
def compare_scores(user_score, computer_score):
    """compares the scores of the user and computer"""
    if user_score>21 and computer_score>21:
        #print(f"user score is:{user_score}")
        #print(f"computer score is:{computer_score}")
        print("Both players bust! It's a tie! 🙃")
        return False
    elif user_score>21:
        #print(f"user score is:{user_score}")
        #print(f"computer score is:{computer_score}")
        print("You bust! You lose! 😭")
        return False
    elif computer_score>21:
        #print(f"user score is:{user_score}")    
        #print(f"computer score is:{computer_score}")
        print("Computer bust! You win!😃")
        return False
    elif user_score==computer_score:
        #print(f"user score is:{user_score}")
        #print(f"computer score is:{computer_score}")
        print("It's a tie! 🙃")
        return False
    elif user_score>computer_score:
        #print(f"user score is:{user_score}")
        #print(f"computer score is:{computer_score}")
        print("You win!😃")
        return False
    elif user_score<computer_score:
        #print(f"user score is:{user_score}")
        #print(f"computer score is:{computer_score}")
        print("Computer wins!😱")
        return False
    else:
        print("Comparing scores...")
        return True
        
def restart_game():
    """restarts the game"""
    restart=input("Do you want to play again? 'y/n' ")
    if restart=='y':
        print("restarting game...")
        play_game()
    else:
        print("Thanks for playing, bye bye!")

def play_game():
    print(logo)
    """starts the game"""
    #1 Get 2 cards and calculate total score
    cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    user_random_cards=random.sample(cards,2)
    print(f"Your cards: {user_random_cards}")

    computer_random_cards=random.sample(cards,2)
    #print(f"Computer's cards: {computer_random_cards}")
    #2 Get 2 cards from computer, only reveal the first card
    print(f"Computer's first card: {computer_random_cards[0]}")

    user_score=calculate_user_score(user_random_cards)
    print(f"Your score: {user_score}")

    computer_score=calculate_user_score(computer_random_cards)     
    #print(f"Computer's score: {computer_score}")
    
    if user_score==21 and computer_score!=21:
        print(f"You win!")
    else:
        hit_or_stand(user_score, computer_score, cards, user_random_cards, computer_random_cards)
        restart_game()

while input("Do you want to play a game of Blackjack? 'y/n' ")=='y':
    print("\n" * 20) 
    play_game()