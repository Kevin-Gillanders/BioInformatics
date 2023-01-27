#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    fstream newfile;
    newfile.open("5.txt", ios::in); //open a file to perform read operation using file object
    int c,g,dnaLen = 0;
    if (newfile.is_open()){   //checking whether the file is open
        string dnaStringLbl;
        string dnaString;
        string read;
        while(getline(newfile, read))
        { //read data from file object and put it into string.
            if(read[0] == '>')
            {
                if(dnaStringLbl.empty())
                {
                    dnaStringLbl = read.substr(1, read.length());
                }
                c, g, dnaLen = 0;
                dnaString = "";
                cout << dnaStringLbl << endl;
            }
            else
            {
                dnaString = dnaString;
            }
        }
        newfile.close(); //close the file object.
    }
  return 0;
} 