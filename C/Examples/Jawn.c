/*#include<stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main() {
  int batsman;
  char scores[100];
  scanf("%d", &batsman);

  for(int i=0;i<batsman;i++){
    scanf("%s", &scores[i]);
  }

    for(int i=0;i<batsman;i++){
    printf("%s\n", &scores[i]);

  }*/

  


     
    /*int main(void) {
        char *str = "programmingarticles2test#5/-", *p = str;
        float arr[10];
        while (*p) {
            if (isdigit(*p)) {
                long val = strtol(p, &p, 10);
                printf("%ld\n", val);
            } else {
                p++;
            }
        }
        return 0;
    }*/



#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_STRINGS	10
#define STRING_LENGTH	50

int main()
{
	char strings[MAX_STRINGS][STRING_LENGTH];
	int loop,n;

  char *p = strings[MAX_STRINGS][STRING_LENGTH];

  
	printf("Enter total number of strings: ");
	scanf("%d",&n);
	
	for(loop=0; loop<n; loop++)
	{
		getchar();
		scanf("%[^\n]s",&strings[loop]);
	}

  int num[n];
  for(int i=0;i<n;i++) {
    if (isdigit(strings[i])) {
               long val = strtol(strings[i], &p, 16);
               num[i] = val;
  }

    }
	for(loop=0; loop<n; loop++)
	{
		
		printf("%d",num[loop]);
	}

	return 0;
}
