# -*- coding: utf-8 -*-

# My Quizz

# Questions require:
# Answers: number, text, a selection.

import random;

def et_movie():
	print "Who is the director from the film \"E.T. the Extra-Terrestrial\"?\n"
	print "(1) Quentin Tarantino\n"
	print "(2) Martin Scorsese\n"	
	print "(3) Spike Lee\n"
	print "(4) Steven Spielberg\n"
	print "(5) Steve Martin\n"
	
	et_director = input()
	if et_director == 4 :
		print "\nCorrect!"
	else :
		print "\nIncorrect..."
	
def ghost():
	print "Who is the couple in the film \"Ghost\"?\n"
	print "(1) Juliete Lewis and Woody Harrelson\n"
	print "(2) Demi Moore and Patrick Swayze\n"	
	print "(3) Kate Winslet and Leonardo DiCaprio\n"
	print "(4) Julia Roberts and Hugh Grant\n"
	print "(5) Meg Ryan and Tom Hanks\n"
	
	ghost_couple = input()
	if ghost_couple == 2 :
		print "\nCorrect!"
	else :
		print "\nIncorrect..."
		
def oscar_2012():
	print "Which film won best original screenplay in the 2012 Oscar?\n"
	print "(1) A Separation\n"
	print "(2) Bridesmaids\n"	
	print "(3) Margin Call\n"
	print "(4) Midnight in Paris\n"
	print "(5) The Artist\n"

	original_screenplay = input()
	
	if original_screenplay == 4 :
		print "\nCorrect!"
	else :
		print "\nIncorrect..."		
	
movie_questions = {
	1: et_movie,
	2: ghost,
	3: oscar_2012
}

def math_quiz():
 	print "You chose the Math Quiz.\n"
	print "How many \"Back to the Future\" were made? "
	
	number_of_moviews = input()
	
	if number_of_moviews == 3 :
		print "\nCorrect!"
	else :
		print "\nIncorrect...The correct number is 3"		
	
def movie_quiz():
	print "You chose the Movie Quiz.\n"
	random_movie = random.randint(1, 3)

	if random_movie in movie_questions:
		movie_questions[random_movie]()
	else :
	 print "Bye!!!"
	
def music_quiz()	:
	print "You chose the Music Quiz.\n"
	print "Which style of music do you prefer?"
	
	user_music_preference = raw_input()
	
	print "\nAh! Great! You like ", user_music_preference

options = {
	1 : math_quiz,
  2 : movie_quiz,
  3 : music_quiz,
}

print "*" * 90
print "\t\t\t\tHello! Welcome to the Quiz!"
print "*" * 90

print "We have:"
print "(1) MATH QUIZ:"
print "(2) MOVIE QUIZ:"
print "(3) MUSIC QUIZ:"
print "Which one do you want to take?"
print "Type \"q\" when you want to exit!"

user_option = input()
print user_option != "q"

while user_option != "q":

	if user_option in options:
		options[user_option]()
		print "We have:"
		print "(1) MATH QUIZ:"
		print "(2) MOVIE QUIZ:"
		print "(3) MUSIC QUIZ:"
		print "Which one do you want to take?"
		print "Type \"q\" when you want to exit!"
		user_option = input()
				
	else :
		print "Leaving the Quiz"
		user_option = 'q'
		
		



