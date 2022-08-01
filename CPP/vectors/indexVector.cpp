// vectors are containers of sequential items, so this means that each individual item can be accessed by its index.

#include<iostream>
#include<vector>
using namespace std;

int main() {
    vector<string> names;

    names[0] = "Shankar";
    names[1] = "Sanjay";
    names[2] = "Vineeth";

    // To access an element and output each individual item, you mention the name of the vector and the position of the desired element in square brackets.
    cout<<names[0]<<endl;
    cout<<names[1]<<endl;
    cout<<names[2]<<endl;
}