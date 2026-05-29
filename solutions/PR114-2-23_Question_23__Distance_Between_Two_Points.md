# PR114-2-23: Question 23: Distance Between Two Points

## 題目敘述
請設計一個類別 Point2D，用來表示平面上的點，並以物件導向方式完成本題。你必須建立兩個 Point2D 物件，分別代表兩個點。
本題的重點是讓物件與物件互動。請在 Point2D 類別中設計一個成員函式，用來計算目前這個點到另一個 Point2D 物件的歐氏距離。
給定兩個點 A(x1, y1) 與 B(x2, y2)，它們的距離公式為 sqrt((x1 - x2)^2 + (y1 - y2)^2)。
請輸出兩點之間的距離，並且固定輸出到小數點後兩位。
你必須使用類別、物件與成員函式完成本題，不可只在 main 中直接套公式計算後輸出。
Design a class Point2D to represent a point on the plane and solve this problem in an object-oriented way. You must create two Point2D objects to represent two points.
The main idea of this problem is object-to-object interaction. In the Point2D class, design a member function that computes the Euclidean distance from the current point to another Point2D object.
Given two points A(x1, y1) and B(x2, y2), their distance is sqrt((x1 - x2)^2 + (y1 - y2)^2).
Output the distance between the two points with exactly two digits after the decimal point.
You must use classes, objects, and member functions to solve this problem. Do not compute the formula directly only in main.

## 輸入說明
輸入一行，包含四個整數 x1 y1 x2 y2，依序代表兩個點的座標。
The input contains one line with four integers x1 y1 x2 y2 representing the coordinates of two points.

## 輸出說明
輸出一行，表示兩點間的距離，固定到小數點後兩位。
Output one line containing the distance between the two points, rounded to exactly two decimal places.

---

## 範例測試
### 範例輸入 1
```text
0 0 3 4
```
### 範例輸出 1
```text
5.00
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

class Point2D
{
private:
    int x, y;

public:
    Point2D(int X, int Y) : x(X), y(Y) {}
    void getDistance(Point2D &obj)
    {
        cout << fixed << setprecision(2) << sqrt((x - obj.x) * (x - obj.x) + (y - obj.y) * (y - obj.y)) << endl;
    }
};

int main()
{
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    Point2D obj1(x1, y1), obj2(x2, y2);
    obj1.getDistance(obj2);
    return 0;
}
```
