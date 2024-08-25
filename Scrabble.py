#Dictionaries -- Scrabble -- Cyb3r_Fr0g -- 8/24/24

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combine lists into dictionary
letter_to_points = {}
for key, value in zip(letters, points):
  letter_to_points[key] = value

#Add the forgoten blank tile
letter_to_points[" "] = 0

#Scoring function
def score_word(word):
  point_total = 0
  for letter in word:
    point_total = point_total + (letter_to_points.get(letter.upper(), 0))
  return point_total

brownie_points = score_word("Brownie")
print(brownie_points)

#Score a Game

player_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "Prof Reader": ["zap", "coma", "period"]}

players_to_points = {}

#Final player score calculation.
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  players_to_points[player] = player_points
print(players_to_points)


