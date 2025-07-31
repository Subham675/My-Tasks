#include<iostream>
using namespace std;
class ABC {
protected:
    int a, b, c;

    int add(int x, int y, int z) {
        return (x + y + z);
    }

public:
    void input() {
        cout << "\nEnter the value for a: ";
        cin >> a;
        cout << "Enter the value for b: ";
        cin >> b;
        cout << "Enter the value for c: ";
        cin >> c;
    }

    void output() {
        cout << "\nA = " << a;
        cout << "\nB = " << b;
        cout << "\nC = " << c;
        cout << "\nSum of a, b, c = " << add(a, b, c);
    }
};
class DEF : public ABC {
    int d, e, f;

    int sum(int x, int y, int z) {
        return (x + y + z + add(a, b, c));
    }

public:
    void in() {
        input();
        cout << "Enter the value for d: ";
        cin >> d;
        cout << "Enter the value for e: ";
        cin >> e;
        cout << "Enter the value for f: ";
        cin >> f;
    }

    void out() {
        output();
        cout << "\nD = " << d;
        cout << "\nE = " << e;
        cout << "\nF = " << f;
        cout << "\nTotal Sum (a+b+c+d+e+f) = " << sum(d, e, f);
    }
};
int main() {
    DEF x;
    x.in();
    x.out();
    return 0;
}
