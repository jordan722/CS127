#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;


std::string line(int l, std::string c){
  std::string s = "";
  for(int i = 0; i < l; i++){
    s += c;
  }
  return s;
}

std::string rect(int w, int h) {
  std::string s = "";
  for(int i = 0; i < h; ++i){
    for(int j=0; j < w; ++j){
      s += "*";
    }
    s += "\n";
  }
  return s;
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  std::string s = "";
  for(int i = 1; i <= h; ++i){
    for(int j=0; j < i; ++j){
      s += "*";
    }
    s += "\n";
  }
  return s;
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  std::string s = "";
  int length = 2*h-1;
  int filler = (length-1)/2;
  while (filler >= 0){
    std::string space;
    for(int i = 0; i < filler; ++i){
      space += " ";
    }
    s += space;
    for(int i = 0; i < length-filler*2;++i){
      s += "*";
    }
    s+= space;
    --filler;
    s += "\n";
  }
  return s;
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  std::string s = "";
  for(int i=0; i <= h; ++i){
    for(int j=0; j < h; ++j){
      if (j< h-i){
        s += " ";
      }
      else{
        s += "+";
      }
    }
    s += "\n";
  }
  return s;
}

int main(){
  string s=line(4,"hello");
  cout<<s<<endl;
  string r = rect(60,20);
  cout<<r<<endl;
  string t1 = tri1(4);
  cout<<t1<<endl;
  string t2 = tri2(10);
  cout<<t2<<endl;
  string t3 = tri3(5);
  cout<<t3<<endl;
}
