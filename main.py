import os
import sys
import sqlite3
import movies_path


def get_watched_movies():
	cursor = conn.execute("SELECT name FROM movies")
	return [row[0] for row in cursor]


def scan(path, folder, all_movies):
	for movie in os.listdir(path):
		if os.path.isdir(os.path.join(path, movie)):
			scan(os.path.join(path, movie), movie, all_movies)
		else:
			if len(folder) > 0:
				all_movies.append('{0}->{1}'.format(folder, movie))
			else:
				all_movies.append('{}'.format(movie))


def get_all_movies():
	all_movies = []
	for path in movies_path.paths:
		scan(path, '', all_movies)
	return all_movies


def get_not_watched_movies():
	all_movies_list = get_all_movies()
	watched_movies_list = get_watched_movies()
	return [movie for movie in all_movies_list if movie not in watched_movies_list]


def not_watched_movies():
	movies = sorted(get_not_watched_movies())
	print("List of not watched movies:\n")
	for i in range(len(movies)):
		print('{0}. {1}'.format(i+1, movies[i]))


def watched_movies():
	movies = sorted(get_watched_movies())
	print("List of watched movies:\n")
	for i in range(len(movies)):
		print('{0}. {1}'.format(i+1, movies[i]))


def add_movie():
	movie = input('Name of the movie with extension: ')
	cursor = conn.execute("SELECT name FROM movies WHERE name = ?", (movie, ))
	if len([row[0] for row in cursor]) == 0:
		conn.execute("INSERT INTO movies (name) VALUES (?)", (movie, ))
		conn.commit()
	print("\nMovie {} added successfully.".format(movie))


def remove_movie():
	movie = input('Name of the movie with extension: ')
	conn.execute("DELETE FROM movies WHERE name = ?", (movie, ))
	conn.commit()
	print("\nMovie {} removed successfully.".format(movie))


def update_movie():
	curr = input('Current name of the movie with extension: ')
	new = input('New name of the movie with extension: ')
	conn.execute("UPDATE movies SET name = ? WHERE name = ?", (new, curr))
	conn.commit()
	print("\n{} updated to {} successfully.".format(curr, new))


def clear_invalid_watched_movies():
	all_movies_list = get_all_movies()
	for movie in get_watched_movies():
		if movie not in all_movies_list:
			conn.execute("DELETE FROM movies WHERE name = ?", (movie, ))
	conn.commit()
	print("\nInvalid watched movies deleted successfully.")


conn = sqlite3.connect('watched_movies.db')
while True:
	os.system('cls')
	print(" ------\n| MENU |\n ------\n")
	print('1. List of not watched movies')
	print('2. List of watched movies')
	print('3. Add a movie in list of watched movies')
	print('4. Remove a movie from list of watched movies')
	print('5. Update name of movie in list of watched movies')
	print('6. Clear all the invalid watched movies')
	print('7. Exit')
	opt = int(input("\nEnter your opt: "))

	os.system('cls')
	print()
	if opt == 1:
		not_watched_movies()
	elif opt == 2:
		watched_movies()
	elif opt == 3:
		add_movie()
	elif opt == 4:
		remove_movie()
	elif opt == 5:
		update_movie()
	elif opt == 6:
		clear_invalid_watched_movies()
	elif opt == 7:
		sys.exit()
	else:
		continue
	input("\n\nPress any key to continue.")
conn.close()
