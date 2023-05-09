n=int(input())
f=[int(x) for x in input().split()]
x=[i for i in f]
y=sorted(x)
maxdif=abs(x[0]-x[-1])
#print(maxdif)
numdif=0
for i in range(len(f)):
    for j in range(i,len(f)):
        if y[j]-y[i]>maxdif:break
        if y[j]-y[i]==maxdif:
            numdif=numdif+1
print(maxdif,numdif)
#include <iostream>
#include <algorithm>
#include <vector>

# int main() {
#   int n;
#   std::cin >> n;

#   std::vector<int> f;
#   for (int i = 0; i < n; i++) {
#     int x;
#     std::cin >> x;
#     f.push_back(x);
#   }

#   std::vector<int> x = f;
#   std::sort(x.begin(), x.end());

#   int maxdif = std::abs(x[0] - x[x.size() - 1]);
#   int numdif = 0;
#   for (int i = 0; i < f.size(); i++) {
#     for (int j = i; j < f.size(); j++) {
#       if (x[j] - x[i] == maxdif) {
#         numdif++;
#       }
#     }
#   }
#   std::cout << maxdif << " " << numdif << std::endl;
#   return 0;
# }
