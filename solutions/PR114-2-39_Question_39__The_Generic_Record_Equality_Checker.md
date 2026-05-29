# PR114-2-39: Question 39: The Generic Record Equality Checker

## 題目敘述
This problem focuses on another common situation in generic programming: checking whether two values are the same. A function template for equality may look simple, but once the type becomes a user-defined class, the program still needs a suitable equality operator.
In this problem, the data type is a StudentRecord object. Each record contains a student name and a score. Two records are considered equal only when both the name and the score are the same.
You should design a function template that checks whether two values are equal. To make it work with StudentRecord, you must overload the == operator for the StudentRecord class.
Your task is to read two student records and output Equal if they are the same, or Not Equal otherwise.
本題聚焦在 generic programming 中另一個常見情境：判斷兩個值是否相同。用 template 寫一個相等性檢查函式看起來很簡單，但一旦型別變成自訂類別，程式仍然需要該型別具備對應的相等運算。
在本題中，資料型別是一個 StudentRecord 物件。每筆紀錄包含學生姓名與分數。只有當姓名與分數都相同時，兩筆紀錄才算相等。
你應該設計一個函式模板，用來判斷兩個值是否相等。若要讓它能處理 StudentRecord，你就必須為 StudentRecord 類別多載 == 運算子。
你的任務是讀入兩筆學生紀錄，若它們相同則輸出 Equal，否則輸出 Not Equal。
You should solve this problem using object-oriented programming. Define a StudentRecord class, encapsulate its data, and overload operator== so that your template function can compare two StudentRecord objects correctly.
你應該以物件導向方式完成本題。請定義 StudentRecord 類別、妥善封裝資料，並多載 operator==，讓函式模板可以正確比較兩個 StudentRecord 物件。

## 輸入說明
The input contains two lines.
Each line contains a name and an integer score.
輸入共有兩行。
每行包含一個姓名與一個整數分數。

## 輸出說明
If the two student records are equal, output Equal.
Otherwise, output Not Equal.
若兩筆學生紀錄相同，輸出 Equal。
否則輸出 Not Equal。

---

## 範例測試
### 範例輸入 1
```text
Alice 90
Alice 90

```
### 範例輸出 1
```text
Equal

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

using namespace std;

class StudentRecord
{
public:
    string name;
    int score;
    StudentRecord(string n, int s) : name(n), score(s)
    {
    }
    bool operator==(StudentRecord s)
    {
        return (s.name == name && s.score == score);
    }
};

template <typename T>
bool equal(T &a, T &b)
{
    return a == b;
}

int main()
{
    string name;
    int score;
    cin >> name >> score;
    StudentRecord s1(name, score);
    cin >> name >> score;
    StudentRecord s2(name, score);
    if (equal(s1, s2))
    {
        cout << "Equal";
    }
    else
    {
        cout << "Not Equal";
    }
}
```
