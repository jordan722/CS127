#include <iostream>
using namespace std;

int lone_sum(int a, int b, int c){
  int sum = 0;
  if (a != b && a != c){
    sum += a;
  }
  if (b != a && b != c){
    sum += b;
  }
  if (c != a && c != b){
    sum += c;
  }
  return sum;
}

bool cigar_party(int cigars, bool is_weekend){
  if (is_weekend){
    if(cigars >= 40){
      return true;
    }
    return false;
  }
  if(cigars >= 40 && cigars <= 60){
    return true;
  }
  return false;
}

int caught_speeding(int speed, bool is_birthday){
  int low = 60;
  int high = 80;
  if(is_birthday){
    low += 5;
    high += 5;
  }
  if (speed <= low){
    return 0;
  }
  if (speed <= high){
    return 1;
  }
  return 2;
}


int main(){
  int sum;
  sum = lone_sum(3,6,3);
  cout << "The result is " << sum << "\n";
}
