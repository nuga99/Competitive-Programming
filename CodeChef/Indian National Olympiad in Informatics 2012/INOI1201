Problem Code : INOI1201 

From : CodeChef

#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>

using namespace std;

struct data{
  
  int a,b,c;
  int sum;
  
};

bool comp(data a1, data b1){
    return a1.sum>b1.sum; // Compare the sum of a and b (Fastest Way to check)
}


int main(){
  
  int TestCase,i,j,k,l,m,n;
  int save, flag;
  bool ii;
  
  int a,b,c; //Donut
  vector<data> v(200000); // data = local;
  
  cin>>TestCase;
  for(i=0;i<TestCase;i++){
    
    cin>>v[i].a>>v[i].b>>v[i].c;
    
    v[i].sum = v[i].b + v[i].c; // Jumlah sementara dihitung untuk pemain kedua dan ketiga
  }
  
  sort(v.begin(),v.end(),comp); //Sorting cout<<v[i].b pertama minimum << v[i].c pertama minimum
  
  int jawab = v[0].sum+v[0].a;
  int jawab_sebelum =v[0].a;    //cout<< v[0].a (player 1)
  
  for(i=1;i<TestCase;i++){
    
    jawab = max(jawab, jawab_sebelum+v[i].a+v[i].sum);
    jawab_sebelum+=v[i].a; // Nambah setelahnya
  }
  cout<<jawab;
}
