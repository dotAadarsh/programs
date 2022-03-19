#include<stdio.h>
#include<stdlib.h>

struct node {
int data;
struct node *link;
};

void add_at_end(struct node *head, int data) {
  struct node *ptr, *temp;
  ptr = head;
  temp = (struct node *)malloc(sizeof(struct node));

  temp->data = data;
  temp->link=NULL;

  while(ptr->link!=NULL) {
    ptr=ptr->link;
  }
  ptr->link = temp;
}

int main() {
  
  struct node *head = malloc(sizeof(struct node));
  head->data = 45;
  head->link = NULL;

  struct node *ptr = malloc(sizeof(struct node));
  ptr->data = 55;
  ptr->link = NULL;
  head->link= ptr;

add_at_end(head,67);

  while(ptr!=NULL) {
    printf("%d ", ptr->data);
    ptr = ptr->link;
  }

  
  return 0;
}