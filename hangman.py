def hangman():
    words=["Hi","Hot","Dowl","Giant","Cactus","Fortune","Crashout","wonderful","University"]
    play_or_not= input("Do you want to play hangman?")
    if(play_or_not=="yes"):
        word_count= int (input("How many letters you want choose from 2-10 cuh?"))
        selected_word=""
        for word in words:
            if(word_count==len(word)):
                selected_word = word
        guess_word=[]
        for i in range(len(selected_word)):
            guess_word.append("_")
        print(guess_word)
        while((word_count + 5) > 0):
            guess_letter = input("Whats you guessing?")
            word_count = word_count-1
            for i in range(len(selected_word)):
                if (selected_word[i] == guess_letter):
                    guess_word[i] = guess_letter
                    print(guess_word)
hangman()