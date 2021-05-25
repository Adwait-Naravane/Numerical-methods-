#include <iostream>
#include <cmath>
using namespace std;


double func(double x){
    return pow(x,3) - pow(x,2) + 2;
}

double derivFunc(double x, double h){
    return (func(x+h) - func(x-h))/(2*h);
}

void newtonraphson(double x){
    
    double k = func(x)/derivFunc(x, 0.001);
    while (abs(k) >= 0.001){
        k = func(x)/derivFunc(x,0.001);
        x = x - k;
    }
    cout << "Root is:" << x << endl; 
}

int main(){
    double x0 = -20;
    newtonraphson(x0);
    return 0;
}
