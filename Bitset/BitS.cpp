#include <bits/stdc++.h>
using namespace std;

signed main() {
    bitset<4> b("0000");
    b |= (b<<1);
    cout << b[0] << "\n";
    b[0] = 1; // Set bit 0;
    b.set(1); // Set bit 1 equals to 1
    b.reset(1); // Reset bit 1 back to 0;
    b.flip(1); // flip bit 1
    b.set(); // set all bits to 1
    cout << b.count() << "\n"; // Count the 1s;
    b.reset(); // reset all bits to 0
    b.any(); // check if there's any bit 1 left?
    b.all(); // Are all bits 1?
    b.none(); // Are all bits 0?
    cout << b[0] << "\n"; // Access bit
    return 0;
}