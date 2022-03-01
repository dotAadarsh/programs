// A simple C program for traversal of a linked list

#include<stdio.h>
#include<stdlib.h>

struct Node {
int data;
struct Node* next;
};

void printList(struct Node* n) {
  while(n!=NULL){
    printf("%d\n", n->data);
    n= n->next;
  }
}

int main() {
  struct Node* head = NULL;
  struct Node* first = NULL;
  struct Node* second = NULL;

  head = (struct Node*) malloc(sizeof(struct Node));
  first = (struct Node*) malloc(sizeof(struct Node));
  second = (struct Node*) malloc(sizeof(struct Node));

  head -> data = 0;
  head -> next = first;

  first -> data = 1;
  first -> next = second;

  second -> data = 2;
  second -> next = NULL;

  printList(head);

  return 0;
  
 }