#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[]) {
  char string[100];
  printf("Enter the String: ");
  scanf("%s",string);

  int len = strlen(string);
  int freq[len];
  
  for(int i=0;i<strlen(string);i++)   {
    freq[i]=1;
    for(int j=i+1;j<strlen(string);j++){
      if(string[j] == string[i]){
        freq[i]++;
        string[j] = '\0';
      }
    }
  }
printf("The frequency fo character are: ");
  
  for(int i=0;i<len;i++){
    if(string[i]!= ' ' && string[i]!= '\0'){
      printf("%c - %d\n", string[i], freq[i]);
    }
  }
  
  return 0;
} 