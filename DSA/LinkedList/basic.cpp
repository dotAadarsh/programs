#include<bits/stdc++.h>
using namespace std;

class Node {
    public: 
    int data;
    Node* next;
};

int main() {
    Node* head;
    Node* one = NULL;
    Node* two = NULL;
    Node* three = NULL;

    // allocate 3 nodes in the heap
    one = new Node();
    two = new Node();
    three = new Node();

    // Assign data values
    one -> data = 1;
    two -> data = 2;
    three -> data = 3;

    // Connect nodes
    one -> next = two;
    two -> next = three;
    three -> next = NULL;

    // print the linked list values
    head = one;
    while(head!=NULL) {
        cout<<head->data;
        head = head->next;
    }

    return 0;
}