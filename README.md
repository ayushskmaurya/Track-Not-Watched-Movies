# Track-Not-Watched-Movies
Simple Python CLI program to track those movies which are not watched yet.

* With the help of this CLI user can track movies which he/she have seen and not seen which are present in the same folder.
* User can get the list of the movies that he/she have seen and not seen yet.

### Main File:
`main.py`

### Instructions:
1. Add the path of the all folders which you want to be tracked in `movies_path.py` file. For ex.:
	```
	paths = [
		'D:\Movies',
		'D:\Series'
	]
	```

2. Execute `create.py` to create database & table:
	```
	python create.py
	```
