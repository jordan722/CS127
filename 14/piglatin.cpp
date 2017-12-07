#include <iostream>
#include <string>
#include <algorithm>

using std::cout;
using std::endl;

bool vowel(char x){
  if (x == 'a' || x=='e' || x=='i' || x=='o' || x=='u'){
    return true;
  }
  return false;
}

std::string piglatin(std::string s){
  int l = s.length();
  for(int i = 0; i < l; ++i){
    s[i] = tolower(s[i]);
  }
  if(vowel(s[0])){
    return s + "ay";
  }
  else{
    return s.substr(1,l) + s[0] + "ay";
  }
}

int main(){
  cout << piglatin("hello") << endl;
  cout << piglatin("alphabet") << endl;
}
