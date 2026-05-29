# PR114-2-38: Question 38: The Generic Point Adder

## 題目敘述
This problem asks you to build a generic addition tool in C++. The purpose is to show that a function template may look very general, but it still depends on the existence of suitable operators for the type being used.
You should write a function template that adds two values and returns the result. However, the type used in this problem is not int or double. It is a Point2D object that stores two integer coordinates x and y.
To make a generic add function work with Point2D, you must overload the + operator for the Point2D class. Once this is done, your template function can treat Point2D objects in the same style as built-in values.
Your task is to read two points, compute their sum, and output the resulting point.
本題要你在 C++ 中建立一個泛型加法工具。這題的目的，是讓你看到 template 看起來很通用，但它其實仍然依賴某些運算子是否已經為該型別定義完成。
你應該撰寫一個函式模板，用來把兩個值相加並回傳結果。但這裡的型別不是 int 或 double，而是一個 Point2D 物件，裡面儲存整數座標 x 與 y。
若要讓泛型加法函式能處理 Point2D，你就必須為 Point2D 類別多載 + 運算子。當這件事情完成後，你的模板函式就可以像處理內建型別一樣處理 Point2D 物件。
你的任務是讀入兩個點，求出它們的和，並輸出結果點。
You should solve this problem using object-oriented programming. Define a Point2D class, encapsulate its coordinates, and overload operator+ so that a function template can be used to add two Point2D objects.
你應該以物件導向方式完成本題。請定義 Point2D 類別、妥善封裝座標，並多載 operator+，讓函式模板可以用來相加兩個 Point2D 物件。

## 輸入說明
The input contains one line with four integers: x1 y1 x2 y2.
They represent two points (x1, y1) and (x2, y2).
輸入只有一行，包含四個整數 x1 y1 x2 y2。
它們分別代表兩個點 (x1, y1) 與 (x2, y2)。

## 輸出說明
Output the resulting point in the format (x, y).
請輸出結果點，格式為 (x, y)。

---

## 範例測試
### 範例輸入 1
```text
1 2 3 4

```
### 範例輸出 1
```text
(4, 6)

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

using namespace std;

class StudentRecord
{
public:
    int x, y;
    StudentRecord(int X, int Y) : x(X), y(Y)
    {
    }
    StudentRecord operator+(StudentRecord p)
    {
        return StudentRecord(x + p.x, y + p.y);
    }
    void display()
    {
        cout << '(' << x << ", " << y << ')';
    }
};

template <typename T>
T add(T &a, T &b)
{
    return a + b;
}

int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    StudentRecord num1(a, b), num2(c, d);
    StudentRecord ans = add(num1, num2);
    ans.display();
}
```
