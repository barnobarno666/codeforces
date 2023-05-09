

#include <bits/stdc++.h>
 
using namespace std;
long long num_gen(int n,int j,int zero_count){
long long sux=0;
    int k=1;
    for(int i=n;i>0;i--){
        sux=5*pow(10,i)+sux;
       // k=n;
    }
    sux=sux/10;
    while (k<=zero_count)
    {
         k=k+1;
        sux=sux*10;
       
        
    }
    return sux ;
    
}

int main(){

int n,zero_count=0;
cin >> n;
int a[n];
int bara[n];
for(int i=0;i<n;i++){
    bara[i]=0 ;
}
//cout << bara[8] <<endl;
for(int i=0;i<n;i++){
    cin >> a[i];
}
//sort(a,a+n);
//reverse(begin(a), end(a));
//cout << a[n-1] <<endl ; 
int summ=0, k=0;
for(int i=0;i<n;i++){
    if(a[i]==0){
        zero_count++;
    }
}
//cout << zero_count << "ff" ;
for(int i=0;i<n;i++){
summ=summ +a[i];
k=i;
if(summ %9 ==0 &summ!=0 ){
    if(zero_count!=0){bara[i]=k;}
    if(zero_count==0){bara[i]=k+1;}
  //  cout << k <<endl;
}
//cout << bara[3]  <<endl;

}
sort(bara,bara+n);
//cout << bara[n-1];
if(bara[n-1]!=0){
    int f=bara[n-1];
   
    cout << num_gen(f,n,zero_count) ;

    
}
else{
    for(int i=0;i<n;i++){
        if(a[i]==0){
            cout << 0;
            return 0;
        }
    }
cout << -1 ;
}/**/
//if bara[max]!=0

}
