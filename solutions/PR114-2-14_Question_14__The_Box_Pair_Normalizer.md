# PR114-2-14: Question 14: The Box Pair Normalizer

## 題目敘述
請建立一個類別來保存一對整數 a 和 b，並建立物件以維護資料。你必須使用 reference 參數讓成員函式能直接調整兩個值，再輸出處理後的結果。
該類別有一公開成員函式，可以透過給定之整數 k 來修正 a 和 b 的值。其修正方法為「將 b 之中的 k 份移至 a 中保存」
本題重點是練習 class、object 與 reference 的基本配合。
Create a class to store a pair of integers a and b, and create an object to maintain the data. You must use reference parameters so a member function can directly adjust the two values, then output the processed result.
The class should provide a public method, which can adjust values of a and b by a given integer k. The adjust function will move k amounts from b to a.
The main goal is to practice the basic combination of class, object, and reference.

## 輸入說明
輸入一行，包含三個整數 a b k。
The input contains one line with three integers a b k.

## 輸出說明
輸出更新後的 a 與 b，中間以一個空白隔開。
Output the updated values of a and b, separated by one space.

---

## 範例測試
### 範例輸入 1
```text
4 9 2
```
### 範例輸出 1
```text
6 7
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Obj
{
private:
    int a, b, k;

public:
    Obj(int a, int b, int k) : a(a), b(b), k(k) {}
    int &getA() { return a; }
    int &getB() { return b; }
    void setA()
    {
        operA(a, k);
    }
    void operA(int &a, int &k)
    {
        a += k;
    }
    void setB()
    {
        operB(b, k);
    }
    void operB(int &b, int &k)
    {
        b -= k;
    }
};

int main()
{
    int a, b, k;
    cin >> a >> b >> k;
    Obj obj(a, b, k);
    obj.setA();
    obj.setB();
    cout << obj.getA() << " " << obj.getB() << endl;
    return 0;
}
```
