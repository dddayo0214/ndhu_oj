# PR114-2-33: Question 33: The Generic Maximum Checker

## 題目敘述
This problem asks you to design a generic comparison utility in C++. You should write one function template that returns the larger of two values with the same type. The purpose is to practice how one template function can be reused for different data types.
The input provides a type code followed by two values of the same type. Your program should read the values, call your function template, and output the larger one. You should not write separate functions for int, double, and char.
The type code will be one of the following:
I represents int
D represents double
C represents char
For char values, use the normal built-in comparison rule of characters. When the type is double, print the result with exactly two digits after the decimal point.
本題要你在 C++ 中設計一個泛型的比較工具。你必須撰寫一個 function template，用來回傳兩個相同型別值中較大的那一個。這題的重點是練習如何用同一個模板函式重複處理不同型別的資料。
輸入會先給你一個型別代號，再給兩個相同型別的值。你的程式應讀入這些資料，呼叫你設計的函式模板，並輸出較大的值。你不應該分別為 int、double、char 寫三個不同版本的函式。
型別代號只會是下列三種：
I 代表 int
D 代表 double
C 代表 char
對於 char，請使用字元本身的內建比較規則。當型別為 double 時，輸出必須固定為小數點後兩位。

## 輸入說明
The first line contains a type code.
The second line contains two values of that type.
The type code is one of I, D, or C.
第一行輸入一個型別代號。
第二行輸入兩個該型別的值。
型別代號只會是 I、D、C 之一。

## 輸出說明
Output the larger of the two values.
If the type is double, print the result with exactly two digits after the decimal point.
輸出兩個值中較大的那一個。
若型別為 double，結果必須固定輸出到小數點後兩位。

---

## 範例測試
### 範例輸入 1
```text
I
12 5

```
### 範例輸出 1
```text
12

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

template <typename T>
T cmp(T &a, T &b)
{
    return (a > b ? a : b);
}

int main()
{
    char type;
    cin >> type;
    if (type == 'I')
    {
        int a, b;
        cin >> a >> b;
        cout << cmp(a, b);
    }
    else if (type == 'D')
    {
        double a, b;
        cin >> a >> b;
        cout << fixed << setprecision(2) << cmp(a, b);
    }
    else if (type == 'C')
    {
        char a, b;
        cin >> a >> b;
        cout << cmp(a, b);
    }
}
```
