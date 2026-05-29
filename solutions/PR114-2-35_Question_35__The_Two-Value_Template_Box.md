# PR114-2-35: Question 35: The Two-Value Template Box

## 題目敘述
This problem extends the previous idea and asks you to design a class template that stores two values of the same type. Your class should also provide a member function that returns the larger of the two stored values.
The input gives a type code followed by two values of the same type. Your program should create an object of the corresponding template type, store both values inside the object, and then output the larger value by calling a member function of that object.
The type code will be one of the following:
I represents int
D represents double
C represents char
This problem is meant to practice class templates together with member functions. The comparison logic should belong to the object itself rather than being written as a completely separate non-template solution. When the type is double, print the answer with exactly two digits after the decimal point.
本題延續前一題的概念，要你設計一個 class template，用來儲存兩個相同型別的值，並提供一個成員函式回傳其中較大的那一個。
輸入會給你一個型別代號以及兩個相同型別的值。你的程式應建立對應型別的模板物件，把這兩個值存進物件中，再透過該物件的成員函式輸出較大的值。
型別代號只會是下列三種：
I 代表 int
D 代表 double
C 代表 char
本題的重點是練習模板類別與成員函式的搭配，讓比較邏輯成為物件本身的一部分，而不是另外用一套和模板無關的做法硬寫。當型別為 double 時，輸出必須固定為小數點後兩位。

## 輸入說明
The first line contains a type code.
The second line contains two values of that type.
The type code is one of I, D, or C.
第一行輸入一個型別代號。
第二行輸入兩個該型別的值。
型別代號只會是 I、D、C 之一。

## 輸出說明
Output the larger value returned by the member function of the template object.
If the type is double, print the result with exactly two digits after the decimal point.
輸出模板物件成員函式所回傳的較大值。
若型別為 double，結果必須固定輸出到小數點後兩位。

---

## 範例測試
### 範例輸入 1
```text
C
m e

```
### 範例輸出 1
```text
m

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

template <typename T>
class Obj
{
private:
    T a, b;

public:
    Obj(T A, T B) : a(A), b(B) {}
    T cmp()
    {
        return (a > b ? a : b);
    }
};

int main()
{
    char type;
    cin >> type;
    if (type == 'I')
    {
        int a, b;
        cin >> a >> b;
        Obj<int> obj(a, b);
        cout << obj.cmp();
    }
    else if (type == 'D')
    {
        double a, b;
        cin >> a >> b;
        Obj<double> obj(a, b);
        cout << fixed << setprecision(2) << obj.cmp();
    }
    else if (type == 'C')
    {
        char a, b;
        cin >> a >> b;
        Obj<char> obj(a, b);
        cout << obj.cmp();
    }
}
```
