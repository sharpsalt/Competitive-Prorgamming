#include<bits/stdc++.h>

using namespace std;

unsigned long long xor128(){
  static unsigned long long x=123456789,y=362436069,z=521288629,w=88675123;
  unsigned long long t;
  t=(x^(x<<11));x=y;y=z;z=w; return( w=(w^(w>>19))^(t^(t>>8)) );
}

long long mod=1000000007;
long long base=31;

long long calcHash(string &s){
  long long h=0;
  for(auto &nx : s){
    h*=base; h%=mod;
    h+=(nx-'a'); h%=mod;
  }
  return h;
}

string randGenStr(){
  long long len=20;
  string res;
  for(long long i=0;i<len;i++){
    res.push_back('a'+xor128()%26);
  }
  return res;
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  map<long long,string> mp;
  while(1){
    string cs=randGenStr();
    long long ch=calcHash(cs);
    if(mp.find(ch)==mp.end()){
      mp[ch]=cs;
    }
    else if(mp[ch]!=cs){
      cout << mp[ch] << "\n";
      cout << cs << "\n";
      break;
    }
  }
  return 0;
}
