# PR114-2-13: Question 13: The Score Correction Card

## 題目敘述
請建立一個類別來保存兩筆成績資料，並建立物件處理資料修正。你必須使用 reference 參數讓成員函式可以調整這兩個數值，最後依題意輸出結果。
本題要求你用物件導向方式完成，不建議只寫成一般函式與獨立變數。
Create a class to store two scores, and create an object to handle the correction process. You must use reference parameters so a member function can adjust these two values, then output the final result.
This problem should be solved in an object-oriented way instead of only using ordinary functions and standalone variables.

## 輸入說明
輸入一行，包含兩個整數 a b。
The input contains one line with two integers a b.

## 輸出說明
輸出排序後的兩個整數，中間以一個空白隔開。
Output the two integers in sorted order, separated by one space.

---

## 範例測試
### 範例輸入 1
```text
9 2
```
### 範例輸出 1
```text
2 9
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Obj
{
private:
    int x, k;

public:
    Obj(int a, int b) : x(a), k(b) {}
    int &getX() { return x; }
    int &getK() { return k; }
    void Sort()
    {
        Mysort(x, k);
    }
    void Mysort(int &x, int &k)
    {
        if (x < k)
        {
            return;
        }
        int temp = x;
        x = k;
        k = temp;
    }
};

int main()
{
    int x, k;
    cin >> x >> k;
    Obj obj(x, k);
    obj.Sort();
    cout << obj.getX() << " " << obj.getK() << endl;
    return 0;
}
```
