"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card = str(card)
        
    if 'A' == card:
        card = 1
    elif card in 'QJK':
        card = 10
    else:
        card = int(card)
        
        
    
    return card   
    


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
            
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two
        

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    
    card_one = str(card_one)
    card_two = str(card_two)
    valor = value_of_card(card_one)
    valor2 = value_of_card(card_two)
    suma = valor + valor2
        
    if card_one == 'A' or card_two == 'A':
        return 1

        

    
    if suma + 11 > 21:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_one = str(card_one)
    card_two = str(card_two)
   
   
    if (card_one == 'A' and card_two in ['J','Q','K','10']) or \
       (card_two == 'A' and card_one in ['K','J','Q','10']):
        return True
    else:
        return False



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """    
    card_one = str(card_one)
    card_two = str(card_two)

    card_valor_1= value_of_card(card_one)
    card_valor_2= value_of_card(card_two)

    if (card_valor_1 == card_valor_2) or (card_one == card_two):
        return True
    else:
        return False
    
    

    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    ""    
    card_one = str(card_one)
    card_two = str(card_two)

    card_valor_1= value_of_card(card_one)
    card_valor_2= value_of_card(card_two)
    suma = card_valor_1 + card_valor_2
    if suma == 9 or suma == 10 or suma ==11 :
        return True
    else:
        return False
    
