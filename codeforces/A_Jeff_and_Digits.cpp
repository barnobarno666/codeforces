/*/so jevabe korbo, sobgula digit er sum divisible by 9 hol number ta divisble by 9 hobe, so 5 joto gula max pari nibo, then sum each type e brute force dia divide korbo
/**/



#include <bits/stdc++.h>
 
using namespace std;
long long num_gen(int n,int j){
    long long sux=0;
    int k;
    for(int i=n;i>0;i--){
        sux=5*pow(10,i)+sux;
        k=n;
    }
    sux=sux/10;
    while (k<=j)
    {
         k=k+1;
        sux=sux*10;
       
        
    }
    return sux/10 ;
    
}

int main(){
   int n;
    cin >> n;
    int ara[n];
    for(int i=0;i<n;i++){
        cin  >> ara[n];
}
std::vector <int>  bara;
bara.push_back(0) ;
sort(ara,ara+n);
int k=0, summ=0;
for(int i=0;i< n;i++ ){
    summ=summ+ara[i];
    k=i;
    if(summ % 9==0  ){
        bara.push_back(k);
        cout << k <<endl ;
    }

}

//std::sort(bara.begin(), bara.end(), greater<int>());
cout << bara[0] ; 
if(bara[0]==0  ){
    cout << 0; 
    return 0;

}


//cout << bara[0] << endl << num_gen(bara[0],n);
}