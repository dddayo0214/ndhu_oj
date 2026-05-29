# PR114-2-36: Question 36: The Generic Array Sum

## 題目敘述
In this problem, you need to design a function template that computes the sum of all elements in an array. The goal is to practice writing one reusable function template that can process arrays of different numeric types.
The input gives a type code, an integer n, and then n values of the same type. Your program should read the array, call your function template, and output the sum of all elements.
The type code will be one of the following:
I represents int
D represents double
Your function template should be able to work correctly for both types. When the type is double, print the result with exactly two digits after the decimal point.
本題要你設計一個 function template，用來計算陣列中所有元素的總和。這題的目的是讓你練習如何用同一個模板函式，去處理不同數值型別的陣列資料。
輸入會給你一個型別代號、一個整數 n，以及接下來 n 個相同型別的值。你的程式應讀入這些資料，呼叫你設計的函式模板，並輸出所有元素的總和。
型別代號只會是下列兩種：
I 代表 int
D 代表 double
你的模板函式必須能同時正確處理這兩種型別。當型別為 double 時，輸出必須固定為小數點後兩位。

## 輸入說明
The first line contains a type code and an integer n.
The second line contains n values of that type.
The type code is one of I or D.
第一行輸入一個型別代號與一個整數 n。
第二行輸入 n 個該型別的值。
型別代號只會是 I、D 之一。

## 輸出說明
Output the sum of the array elements.
If the type is double, print the result with exactly two digits after the decimal point.
輸出陣列所有元素的總和。
若型別為 double，結果必須固定輸出到小數點後兩位。

---

## 範例測試
### 範例輸入 1
```text
D
4
1.5 2.25 3.0 4.25

```
### 範例輸出 1
```text
11.00

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

template <typename T>
class Obj
{
private:
    vector<T> v;

public:
    Obj(vector<T> V) : v(V) {}
    T sum()
    {
        T sum = 0;
        for (auto &i : v)
        {
            sum += i;
        }
        return sum;
    }
};

int main()
{
    char type;
    cin >> type;
    if (type == 'I')
    {
        int n;
        cin >> n;
        vector<int> v(n);
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }
        Obj<int> obj(v);
        cout << obj.sum();
    }
    else if (type == 'D')
    {
        int n;
        cin >> n;
        vector<double> v(n);
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }
        Obj<double> obj(v);
        cout << fixed << setprecision(2) << obj.sum();
    }
    else if (type == 'C')
    {
        int n;
        cin >> n;
        vector<char> v(n);
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }
        Obj<char> obj(v);
        cout << obj.sum();
    }
}
```
