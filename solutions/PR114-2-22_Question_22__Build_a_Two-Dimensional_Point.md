# PR114-2-22: Question 22: Build a Two-Dimensional Point

## 題目敘述
現在請你把一維分量的想法延伸到平面座標。請設計一個類別 Point2D，用來表示二維平面上的一個點。類別中至少要保存 x 與 y 兩個整數座標，並提供建構子與成員函式。
你必須使用物件導向方式作答，建立 Point2D 類別與物件來處理資料。請不要只用兩個一般整數變數完成輸出。
輸入一個點的座標 x 與 y 後，請建立一個 Point2D 物件。接著輸出此點的座標表示法，格式固定為 (x, y)。
另外，請再輸出此點到原點 (0, 0) 的平方距離。平方距離定義為 x^2 + y^2。本題只要求平方距離，不需要開根號。
請輸出兩行。第一行輸出點的座標字串，第二行輸出平方距離。
Now extend the idea of a one-dimensional component to a coordinate on a plane. Design a class Point2D to represent a point in a two-dimensional plane. The class should store two integer coordinates x and y and provide constructors and member functions.
You must solve this problem in an object-oriented way by creating the Point2D class and an object. Do not solve it using only two ordinary integer variables.
After reading x and y, create a Point2D object. Then output the point in the exact format (x, y).
Also output the squared distance from this point to the origin (0, 0). The squared distance is defined as x^2 + y^2. You only need the squared distance, not the real distance.
Output two lines. The first line is the coordinate string of the point, and the second line is the squared distance.

## 輸入說明
輸入一行，包含兩個整數 x 與 y。
The input contains one line with two integers x and y.

## 輸出說明
輸出兩行。
第一行輸出點座標，格式為 (x, y)。
第二行輸出此點到原點的平方距離。
Output two lines.
The first line is the point in the format (x, y).
The second line is the squared distance from the point to the origin.

---

## 範例測試
### 範例輸入 1
```text
3 4
```
### 範例輸出 1
```text
(3, 4)
25
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Point2D
{
private:
    int x, y;

public:
    Point2D(int X, int Y) : x(X), y(Y) {}
    void getValue()
    {
        cout << '(' << x << ", " << y << ')' << endl;
    }
    void getDistance()
    {
        cout << x * x + y * y << endl;
    }
};

int main()
{
    int x, y;
    cin >> x >> y;
    Point2D obj1(x, y);
    obj1.getValue();
    obj1.getDistance();
    return 0;
}
```
