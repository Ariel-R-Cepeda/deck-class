# Import statements go here
 import random
 import collections

card= collections.namedtuple('card',['rank','suit'])
#idk what to do with this information cuz almost all of my code has been written already

  ranks= ["2","3","4","5","6","7","8","9","10","Q","K","A","J"]
  suits= ["clubs","diamonds","hearts","spades"]
  all_cards= [None]
  r=0
  s=0
  counts=0
  for idfk in range(52):
     all_cards.extend(str(ranks[r] + suits[s]))
     r+=1
     counts+=1
     if counts == 13:
        r=0
        s+=1
        #AHH its the index is out of range and idk how to fix this, cuz I dont get why its out of range
        #ps, I coded this before reading the format you wanted this in, whoops, so much for that format
def __init__(self, ranks, suits):
    if self.ranks not in ranks:
      return ValueError
    if self.suits not in suits:
      return ValueError


  def __repr__(self):
    return all_cards
  def deal(self):
    choice_suit_ind=random.randint(0,12)
    choice_rank_ind=random.randint(0,3)
    choice_suit= suits[choice_suit_ind]
    choice_rank= ranks[choice_rank_ind]
    all_cards_ind= (choice_suit_ind + 1)*(choice_rank_ind + 1)-1
    del all_cards[all_cards_ind]
    return f'{choice_rank} of {choice_suit}'
    

    def __len__(self):
        return len(all_cards)

 
