# PR114-2-25: Question 25: Ordered Triangle Area

## 題目敘述
請延續前一題的想法，設計 Shape 與 Triangle 類別，並使用三個依照固定順序輸入的 Point2D 物件來建立一個三角形。
本題保證輸入的三個點一定能形成非退化三角形，而且三個點會依照題目給定的順序輸入。你的 Triangle 類別應提供成員函式來計算三角形面積。
你可以使用座標幾何常見的公式來計算面積，例如 |x1(y2-y3)+x2(y3-y1)+x3(y1-y2)| / 2。
請輸出三角形的面積，並固定輸出到小數點後兩位。
你必須使用物件導向方式完成本題，也就是建立 Point2D、Shape、Triangle 等類別與物件來表示資料與行為，不可只用一組一般變數直接完成。
Continue the idea from the previous problem. Design classes Shape and Triangle, and use three Point2D objects given in a fixed order to build a triangle.
This problem guarantees that the three input points always form a non-degenerate triangle, and the points are given in the exact order specified by the input. Your Triangle class should provide a member function to compute the area of the triangle.
You may use a standard coordinate geometry formula such as |x1(y2-y3)+x2(y3-y1)+x3(y1-y2)| / 2.
Output the area of the triangle with exactly two digits after the decimal point.
You must solve this problem in an object-oriented way by creating classes such as Point2D, Shape, and Triangle to represent the data and behavior. Do not solve it using only ordinary variables.

## 輸入說明
輸入一行，包含六個整數 x1 y1 x2 y2 x3 y3，依序代表三個點的座標。
The input contains one line with six integers x1 y1 x2 y2 x3 y3 representing three points in order.

## 輸出說明
輸出一行，表示三角形面積，固定到小數點後兩位。
Output one line containing the area of the triangle, rounded to exactly two decimal places.

---

## 範例測試
### 範例輸入 1
```text
0 0 3 0 0 4
```
### 範例輸出 1
```text
6.00
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

class Shape
{
};

class Point2D
{
private:
    int x, y;

public:
    Point2D(int X, int Y) : x(X), y(Y) {}
    Point2D getVector(Point2D &obj)
    {
        return Point2D(obj.x - x, obj.y - y);
    }
    int getX()
    {
        return x;
    }
    int getY()
    {
        return y;
    }
};

class Triangle : public Shape
{
private:
    Point2D a, b, c;

public:
    Triangle(int x1, int y1, int x2, int y2, int x3, int y3) : a(x1, y1), b(x2, y2), c(x3, y3) {}
    double getArea()
    {
        Point2D tmp1 = a.getVector(b);
        Point2D tmp2 = a.getVector(c);
        return 0.5 * abs(tmp1.getX() * tmp2.getY() - tmp1.getY() * tmp2.getX());
    }
};

int main()
{
    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    Triangle obj(x1, y1, x2, y2, x3, y3);
    cout << fixed << setprecision(2) << obj.getArea() << endl;
    return 0;
}
```
