all: EstPalindrome TriSelection Syracuse graph
EstPalindrome: EstPalindrome.c
	gcc -Wall -g EstPalindrome.c -o EstPalindrome
TriSelection: TriSelection.c
	gcc -Wall -g TriSelection.c -o TriSelection
Syracuse: Syracuse.c 
	gcc -Wall -g Syracuse.c -o Syracuse

graph: script.gp
	./Syracuse
	gnuplot -persistent script.gp


