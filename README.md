
# **CS50P - Final Project: FLASHCARD APPLICATION**

### Video Demo:  https://youtu.be/qTnxGJdUJfw
## **Description**
This was my final project for conclude the HarvardX [CS50’s Introduction to Programming with Python](https://www.harvardonline.harvard.edu/course/cs50s-introduction-programming-python) course.
This Flashcard Application wrote by Anna Zwolińska is a command-line tool designed to help users build and test their vocabulary. The application allows you to manage a dictionary of words and their definitions, offering functionality to add new entries, remove existing ones, and test your knowledge through a test. It can be adapted to the user's needs, this is why neither the source nor the target language has been indicated.

*Personally, I have stuggled with active use of French vocabulary, this is why I intended to use it with a French word and their French definition.*

## **Features**
- **Add Words**: Add new words or phrases along with their definitions to the dictionary file.
- **Remove Words**: Delete words and their definitions from the dictionary.
- **Test**: Test your knowledge with a customizable number of words. The application tracks your performance depending on which, you might unlock another option, which is:
- **Troublemaking Words Practice**: After a test, you can choose to re-test only the words you struggled with to improve your understanding and retention. You can re-take the test with the remaining words as long as you want or until you get a perfect score.

## **Dictionary file**
The application has its vocabulary source in the mydictionary.json file. JSON (JavaScript Object Notation) was chosen as the format for storing the dictionary data due to its simplicity and ease of use. Its structure is straightforward, allowing the dictionary to be stored as a collection of key-value pairs, where each word (key) is associated with its definition (value). The file has been created in advance but if it happens that it doesn't exist, the application with create a new empty file.

## **Usage & Commands**
Run the application from the command line. You can provide commands directly as arguments or enter them interactively when prompted. Follow the instructions displayed to perform actions such as:
- **`add`**: Adds a new word and its definition to the dictionary.
- **`rem`**: Removes a specified word and its definition from the dictionary.
- **`test`**: Initiates a quiz/test with a user-defined number of words.
- **`exitf`**: Exits the application.

## Main Files
- project.py
- README.md
- requirements.txt
- test_project.py

## Possible improvements
1) Saving Trouble Vocabulary: Implement a feature to save the words that users struggle with into a separate file. Add a new command in the menu that allows users to test themselves exclusively on these challenging words.
2) Error-Weighted Randomness: Introduce a system that adjusts the frequency of word occurrences based on previous mistakes, for instance:
    - if everything was ok - 10% chance of the next occurance | skip 90% * n (the number of words)
    - if the accuracy was above 50% - 40% chance of the next occurance
    - if the accuracy was below 50% - 60% chance of the next occurance
3) Language Selection: Provide an option to choose whether the words should be displayed in the source language, the target language, or a mix of both. This feature is more suitable for single words rather than full expressions.
4) Test on repeat 10/20/more words: If all 10/20/more words are correct add a nice image as a bonus to enhance the user experience.

## Acknowledgments
I’d like to express my gratitude to David Malan and the CS50 team for their engaging teaching style, captivating lectures and the problem sets that provided valuable hands-on experience.
