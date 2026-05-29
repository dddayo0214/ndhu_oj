# PR114-2-16: Question 16: The Student Badge Summary

## 題目敘述
請設計一個基底類別與一個衍生類別，並建立衍生類別物件完成資料輸入與輸出。你必須使用基礎繼承語法，讓衍生類別能延伸基底類別的資料與功能。
本題重點是練習 inheritance 的基本結構與物件導向程式設計。
Design a base class and a derived class, then create a derived-class object to complete the input and output. You must use basic inheritance syntax so the derived class can extend the data and behavior of the base class.
The main goal is to practice the basic structure of inheritance and object-oriented programming.

## 輸入說明
輸入一行，包含兩個不含空白的字串：name id。
The input contains one line with two strings without spaces: name id.

## 輸出說明
輸出兩行：
Name: name
ID: id
Output exactly two lines:
Name: name
ID: id

---

## 範例測試
### 範例輸入 1
```text
Alice B12345678
```
### 範例輸出 1
```text
Name: Alice
ID: B12345678
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Father
{
protected:
    string name;

public:
    string &getName() { return name; }
};

class Child : public Father
{
protected:
    string id;

public:
    string &getId() { return id; }
};

int main()
{
    string name, id;
    cin >> name >> id;
    Child child;
    child.getName() = name;
    child.getId() = id;
    cout << "Name: " << child.getName() << endl;
    cout << "ID: " << child.getId() << endl;
    return 0;
}
```
