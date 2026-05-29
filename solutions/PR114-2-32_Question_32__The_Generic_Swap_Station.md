# PR114-2-32: Question 32: The Generic Swap Station

## 題目敘述
In this problem, you are asked to design a generic utility in C++ that can swap two values of the same type. The goal is not only to print the correct output, but also to practice the idea of function templates. Instead of writing separate functions for int, double, and char, you should define one function template that can work with different data types.
The input begins with a type code and then gives two values of that type. Your program should read the type code, create values of the corresponding type, call your function template, and output the values after the swap is completed.
The type code will be one of the following:
I represents int
D represents double
C represents char
When the type is double, the output must be printed with exactly two digits after the decimal point.
本題要你在 C++ 中設計一個可重複使用的交換工具，用來交換兩個相同型別的值。這題的重點不只是把答案印出來，而是要練習 function template 的概念。你不應該分別為 int、double、char 各寫一個交換函式，而是應該設計一個可以處理多種型別的函式模板。
輸入會先給你一個型別代號，再給兩個同型別的值。你的程式應根據型別代號建立對應型別的資料，呼叫你設計的函式模板完成交換，最後輸出交換後的結果。
型別代號只會是下列三種：
I 代表 int
D 代表 double
C 代表 char
當型別為 double 時，輸出必須固定為小數點後兩位。

## 輸入說明
The first line contains a type code.
The second line contains two values of that type.
The type code is one of I, D, or C.
第一行輸入一個型別代號。
第二行輸入兩個該型別的值。
型別代號只會是 I、D、C 之一。

## 輸出說明
Output the two values after swapping them.
If the type is double, print both values with exactly two digits after the decimal point.
輸出交換後的兩個值。
若型別為 double，兩個值都必須固定輸出到小數點後兩位。

---

## 範例測試
### 範例輸入 1
```text
D
3.5 7.25

```
### 範例輸出 1
```text
7.25 3.50

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

template <typename T>
void change(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
    return;
}

int main()
{
    char type;
    cin >> type;
    if (type == 'I')
    {
        int a, b;
        cin >> a >> b;
        change(a, b);
        cout << a << " " << b << endl;
    }
    else if (type == 'D')
    {
        double a, b;
        cin >> a >> b;
        change(a, b);
        cout << fixed << setprecision(2) << a << " " << b << endl;
    }
    else if (type == 'C')
    {
        char a, b;
        cin >> a >> b;
        change(a, b);
        cout << a << " " << b << endl;
    }
}
```
