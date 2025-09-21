import random
common_english_words = [
    "people", "before", "number", "school", "family", "because", "through", "during", "should", "better",
    "called", "around", "others", "course", "within", "system", "public", "policy", "society", "office",
    "market", "figure", "project", "process", "service", "member", "however", "problem", "picture", "another",
    "meeting", "company", "college", "product", "program", "support", "example", "country", "history", "subject",
    "present", "produce", "measure", "pattern", "manager", "between", "include", "message", "control", "against",
    "article", "perform", "provide", "feature", "decision", "research", "security", "financial", "benefit", "officework",
    "official", "position", "available", "increase", "knowledge", "language", "material", "pressure", "probably", "relative",
    "building", "including", "consumer", "education", "effective", "activity", "specific", "possible", "original", "practice",
    "property", "strategy", "important", "interest", "question", "quality", "processes", "structure", "behavior", "economy",
    "situation", "political", "medicine", "industry", "distance", "planning", "solution", "computer", "community", "standard",
    "hospital", "technical", "technology", "capacity", "analysis", "approach", "resource", "reference", "conference", "creative",
    "customer", "development", "management", "organize", "training", "proposal", "practice", "consumer", "creativework", "interface",
    "activity", "originality", "literature", "collection", "function", "identity", "identityed", "together", "available", "objective",
    "mortgage", "situation", "structure", "building", "candidate", "describe", "difficult", "direction", "discovery", "distance",
    "politics", "personal", "financial", "involved", "involve", "including", "increasing", "instance", "institute", "internet",
    "inspired", "inspiredly", "resourceful", "recognize", "recently", "regional", "securitys", "suitable", "sentence", "selection",
    "sensitive", "standard", "strategy", "strength", "structure", "stopping", "strongly", "suddenly", "suitable", "telephone",
    "television", "training", "transfer", "transport", "treatment", "together", "ultimate", "umbrella", "unified", "unusual",
    "valuable", "variable", "variation", "variety", "vertical", "veterans", "vehicle", "versions", "violence", "visibility",
    "visible", "visiting", "waiting", "walking", "warning", "website", "welfare", "western", "wherever", "whenever",
    "whether", "whilst", "working", "workplace", "workforce", "writing", "written", "yesterday", "youngest", "yourself",
    "baseline", "boundary", "breaking", "building", "business", "capacitys", "carefuly", "careless", "celebrate", "cemetery",
    "challenge", "challengeable", "champion", "character", "chemical", "children", "circular", "citizen", "civilian", "clarity",
    "classroom", "classical", "clinical", "closure", "clothing", "coalition", "collapse", "collect", "college", "combine",
    "comfortable", "command", "comment", "commercial", "committee", "commodity", "community", "companion", "companys", "comparable",
    "compare", "compete", "complete", "complex", "complaint", "component", "composed", "compound", "composedly", "comprehensive",
    "computerized", "concerning", "conclude", "concrete", "condition", "conference", "confidence", "confirmed", "conflict", "congress",
    "connect", "conscience", "conscious", "consensus", "consequence", "consider", "consistent", "constant", "constructed", "consumer",
    "contact", "container", "content", "contest", "context", "continue", "contract", "contrast", "contribute", "control",
    "convenient", "convention", "conversion", "convert", "convince", "cooking", "copyright", "corporate", "correct", "correspond"
]
stages = [r"""
  +----+
  |    |
  |   (o_o)
  |   /(█)\ 
  |    / \
  |
=======""", r"""
  +----+
  |    |
  |   (o_o)
  |   /(█)\ 
  |    / 
  |
=======""", r"""
  +----+
  |    |
  |   (o_o)
  |   /(█)\ 
  |     
  |
=======""", r"""
  +----+
  |    |
  |   (o_o)
  |   /(█)  
  |     
  |
=======""", r"""
  +----+
  |    |
  |   (o_o)
  |    (█)  
  |     
  |
=======""", r"""
  +----+
  |    |
  |   (o_o)
  |     
  |     
  |
=======""", r"""
  +----+
  |    |
  |     
  |     
  |     
  |
======="""] 
logo = r"""
 _   _                           
| | | | __ _ _ __   __ _  ___    
| |_| |/ _` | '_ \ / _` |/ _ \   
|  _  | (_| | | | | (_| |  __/   
|_| |_|\__,_|_| |_|\__, |\___|   
                   |___/         
     HANGMAN GAME
"""
print(logo)
lives = 6
chosen_word = random.choice(common_english_words)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"{lives}/6 LIVES LEFT")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word")

        if lives == 0:
            game_over = True
            print(f"It Was {chosen_word}YOU LOSE")

    if "_" not in display:
        game_over = True
        print("YOU WIN")
    print(stages[lives])
