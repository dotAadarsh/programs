/* Strings are useful for holding all types of long input. If you want the user to input his or her name, you must use a string. Using scanf() to input a string works, but it will terminate the string after it reads the first space, and moreover, because scanf doesn't know how big the array is, it can lead to "buffer overflows" when the user inputs a string that is longer than the size of the string (which acts as an input "buffer").

There are several approaches to handling this problem, but probably the simplest and safest is to use the fgets function, which is declared in stdio.h.*/


#include<stdio.h>

int main (int argc, char *argv[]) {
  char string[256];
  printf("enter the string: ");
  
  fgets(string,256,stdin);
  
  printf("You have entered %s", string);

/*The one thing to watch out for when using fgets is that it will include the newline character ('\n') when it reads input unless there isn't room in the string to store it. This means that you may need to manually remove the input. One way to do this would be to search the string for a newline and then replace it with the null terminator. */
  
  for(int i=0;i<256;i++) {
    if(string[i]=='\n') {
      string[i] = '\0';  
      break;
    }
  }


  
  getchar();
  return 0;

}