### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #needs double equals/==
      return True
    else #colon is missing from else
      return False
   

  dif highest_card(self, card1 card2):#should be def.#no comma between card 1 and card2 between brackets.
  if card1.value > card2.value:#indentation missing.
    return card #should be card1 or will return error.
  else:
    return card2
  


def cards_total(self, cards):#function isn't inside class CardGame. Needs to be indented.
  total #total isn't defined.
  for card in cards:
    total += card.value 
    return "You have a total of" + total #return shouldn't be idented. Should be inline with for. '+ total' is as an integer, should be concatenated to a string.
  
```
