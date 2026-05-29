# PR114-2-11: Question 11: The Pair Exchange Desk

## 題目敘述
請建立一個類別來保存兩個整數，並建立一個物件讀入資料。你必須使用 reference 參數設計交換成員函式，將兩個數值交換後輸出。
本題的重點不是只得到正確答案，而是練習以物件導向方式把資料與操作封裝在同一個類別中。
Create a class to store two integers, and create an object to read the input. You must use a member function with reference parameters to swap the two values, then output the result.
This problem is not only about getting the correct output. It is meant to help you practice organizing data and behavior together in an object-oriented way.

## 輸入說明
輸入一行，包含兩個整數 a b。
The input contains one line with two integers a b.

## 輸出說明
輸出交換後的兩個整數，中間以一個空白隔開。
Output the two integers after swapping, separated by one space.

---

## 範例測試
### 範例輸入 1
```text
10 25
```
### 範例輸出 1
```text
25 10
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Obj
{
private:
    int a;
    int b;

public:
    Obj(int a, int b) : a(a), b(b) {}
    void Myswap(int &x, int &y)
    {
        int temp = x;
        x = y;
        y = temp;
    }
    int &getA() { return a; }
    int &getB() { return b; }
};

int main()
{
    int a, b;
    cin >> a >> b;
    Obj obj(a, b);
    obj.Myswap(a, b);
    cout << a << " " << b << endl;
    return 0;
}
```
