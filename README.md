# DC-Project-Poker
## How to use CSV file
### Title Headings
For collumns 1, 2 & 3 use 'Player', 'Card1' & 'Card2' Respectively
### Card inputs
Please use the following formats for Card inputs
suits = ['D', 'C', 'H', 'S']
values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#### Card examples
Ten of Clubs = TC
Two of Hearts = 2H
Ace of Spades = AS
### Code will fail if cards repeated in CSV and Community cards
Make sure that no card is repeated in the community cards or the cards dealt to players.
This is because those cards are removed from the 52 card deck.
If the same card is removed twice, the code will fail 
