//First we’re including another header file called stdio.h. This tells thecompiler that you’re going to use the standard Input/Output functions. Oneof those is printf

#include<stdio.h>
int main()
{
	int songs = 10;
  int artists = 5;
	printf("Total number of songs: %d\n", songs);
  printf("Total number of artists: %d\n", artists);
	return 0;
}
