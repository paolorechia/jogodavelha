#Makefile de exemplo (Manual GNU Make)
CFLAGS = -g -Wall

objects = main.o tree.o

main: $(objects)
	gcc -o grafo $(objects) 

main.o : main.c
	gcc -c main.c $(CFLAGS)

tree.o : tree.c
	gcc -c tree.c $(CFLAGS)
	

clean :
	rm grafo $(objects)