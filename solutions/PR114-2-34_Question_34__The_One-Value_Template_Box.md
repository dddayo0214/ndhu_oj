# PR114-2-34: Question 34: The One-Value Template Box

## 題目敘述
In this problem, you are asked to design a class template that stores one value. The purpose is to practice how a single class template can describe objects of different data types without rewriting the whole class again and again.
The input begins with a type code and then gives one value. According to the type code, your program should create an object from your class template, store the value inside the object, and then output the stored value through a member function.
The type code will be one of the following:
I represents int
D represents double
C represents char
S represents string
This problem is intended to help you distinguish between ordinary classes and class templates. When the type is double, the output must be printed with exactly two digits after the decimal point.
本題要你設計一個 class template，用來儲存一個值。這題的目的，是讓你練習如何使用同一個模板類別來描述不同型別的物件，而不是每換一種型別就重寫一次整個類別。
輸入會先給你一個型別代號，再給一個值。你的程式應根據型別代號建立對應型別的模板物件，把資料存進物件中，再透過成員函式取出並輸出該值。
型別代號只會是下列四種：
I 代表 int
D 代表 double
C 代表 char
S 代表 string
這題的重點是讓你分辨一般類別與模板類別的差異。當型別為 double 時，輸出必須固定為小數點後兩位。

## 輸入說明
The first line contains a type code.
The second line contains one value of that type.
The type code is one of I, D, C, or S.
第一行輸入一個型別代號。
第二行輸入一個該型別的值。
型別代號只會是 I、D、C、S 之一。

## 輸出說明
Output the value stored in the template object.
If the type is double, print the result with exactly two digits after the decimal point.
輸出模板物件中儲存的值。
若型別為 double，結果必須固定輸出到小數點後兩位。

---

## 範例測試
### 範例輸入 1
```text
S
HelloTemplate

```
### 範例輸出 1
```text
HelloTemplate

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
    T data;

public:
    Obj(T D) : data(D) {}
    T getData()
    {
        return data;
    }
};

int main()
{
    char type;
    cin >> type;
    if (type == 'I')
    {
        int data;
        cin >> data;
        Obj obj(data);
        cout << obj.getData();
    }
    else if (type == 'D')
    {
        double data;
        cin >> data;
        Obj obj(data);
        cout << fixed << setprecision(2) << obj.getData();
    }
    else if (type == 'C')
    {
        char data;
        cin >> data;
        Obj obj(data);
        cout << obj.getData();
    }
    else if (type == 'S')
    {
        string data;
        cin >> data;
        Obj obj(data);
        cout << obj.getData();
    }
}
```
