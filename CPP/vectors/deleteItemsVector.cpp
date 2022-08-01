// To add items one at a time to the end of a vector, you use the .push_back() method.

#include<iostream>
#include<vector>
using namespace std;

int main() {
    vector<string> names;

    names.push_back("Marshmello");
    names.push_back("Ed Sheeran");
    names.push_back("Shawn mendes");

    //check the size
    cout<<names.size()<<endl;  //outputs 3
    
    names.pop_back(); //remove the last element

    cout<<names.size()<<endl; // outputs 2


}