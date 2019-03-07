# Stone-paper-scissor
Game Development using Python
Python is a multipurpose language and one can do literally anything with it. Python can also be used for game development.Python has been used to create a Stone-Paper-Scissor game without using any external game libraries like PyGame and play against computer.

The module imported in this program is 'random' which provides access to functions that support many operations but here it is used to generate random numbers.


Rules: You and the computer both choose rock, paper or scissors. The winner is decided by these rules:

Stone blunts scissors
Paper covers rock
Scissors cut paper
where in the program the computer generates numbers from '1 to 3' randomly by using function 'random.randrange()' from limits 1 to 4.

1 denotes stone
2 denotes paper
3 denotes scissor

In this game the user is first asked for the number of times he/she wants to play the game. After a specific value is entered by the user, an array is created of length upto which user wants to play and by using function 'random.randrange(1,4)' the values 1,2 and 3 are made to enter in the array randomly.

After creation of the array the user is asked to make choices to play the game and stored in another array, and the values are checked correspondingly, wherein if the value entered by the user matches with the computer generated value then a message "It's a tie" is displayed and if choices by user and computer match any of the rules then result will be displayed. 


![screenshot 4](https://user-images.githubusercontent.com/40642572/53984850-2e2e2800-4140-11e9-8697-103562eccc05.png)
