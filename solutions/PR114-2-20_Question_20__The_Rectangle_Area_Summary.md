# PR114-2-20: Question 20: The Rectangle Area Summary

## 題目敘述
請設計一個基底類別與一個衍生類別，並建立衍生類別物件完成資料輸入、計算與輸出。你必須使用 inheritance 的基本語法來表達類別之間的關係。
請用物件導向方式完成本題，不要只把它當成一般計算題。
Design a base class and a derived class, then create a derived-class object to complete the input, calculation, and output. You must use the basic syntax of inheritance to express the relationship between the classes.
Solve this problem in an object-oriented way instead of treating it as an ordinary calculation problem.

## 輸入說明
輸入一行，包含一個不含空白的字串 name 與兩個整數 w h。
The input contains one line with a string name and two integers w h.

## 輸出說明
輸出兩行：
Name: name
Area: w*h
Output exactly two lines:
Name: name
Area: w*h

---

## 範例測試
### 範例輸入 1
```text
Rect 4 7
```
### 範例輸出 1
```text
Name: Rect
Area: 28
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Shape
{
private:
    string name;

public:
    Shape(string name) : name(name) {}
    string getName() { return name; }
};

class Rectangle : public Shape
{
private:
    int w, h;

public:
    Rectangle(string name, int w, int h) : Shape(name), w(w), h(h) {}
    int getArea() { return w * h; }
};

int main()
{
    string name;
    int w, h;
    cin >> name >> w >> h;
    Rectangle obj(name, w, h);
    cout << "Name: " << obj.getName() << endl;
    cout << "Area: " << obj.getArea() << endl;
    return 0;
}
```
