# Length of Last Word

## Overview

This Python script defines a class `Solution` with a method `lengthOfLastWord` that computes the length of the last word in a given string. It splits the string by spaces and returns the length of the last non-empty word.

## Usage

1. **Clone the Repository:**

   git clone https://github.com/your_username/length_of_last_word.git
   
Navigate to the Directory:
----------------------------
cd length_of_last_word

Run the Script:
---------------------------
python main.py

Example Output:
------------------------
words: ['', 'Hi', 'world', '', 'again', '', '', '']

words only: ['Hi', 'world', 'again']

last word: again

5

length: 5

Code Explanation
------------------------------
Method: lengthOfLastWord

Input:
s (str): The input string.

Output:
------------------------------
(int): The length of the last word.

Steps:
------------------------------------
The string "s" is split into a list of words using the split method with a space as the separator.
It prints the list of words for debugging purposes.
An empty list "words_only" is initialized to store non-empty words.
A "for"-loop iterates over the list words, and non-empty words are appended to the " words_only " list.
The list of non-empty words is printed for debugging purposes.
The last word from the " words_only list " is identified.
The last word is printed for debugging purposes.
The length of the last word is printed and returned.

Dependencies
--------------------------
This script does not have any external dependencies.

Notes
------------------------------
Ensure you replace " Hi world again " with any other string to test different cases.

License
--------------------------
This project is licensed under the MIT License - see the LICENSE file for details.




