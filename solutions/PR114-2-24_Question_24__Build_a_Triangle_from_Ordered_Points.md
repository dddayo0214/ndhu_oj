# PR114-2-24: Question 24: Build a Triangle from Ordered Points

## 題目敘述
現在請你進一步把多個點組合成形狀。請設計一個基底類別 Shape，以及一個衍生類別 Triangle，並以物件導向方式完成本題。
Triangle 物件必須由三個 Point2D 物件依照給定順序組成，也就是第一個點、第二個點、第三個點都有明確位置。
你必須在 Triangle 類別中提供成員函式，判斷這三個點是否能形成非退化三角形。若三點共線，則視為無法形成有效三角形。
若可以形成有效三角形，請輸出 YES，並在下一行輸出其周長。若不行，請輸出 NO，並在下一行輸出 0.00。
你必須使用 Shape、Triangle、Point2D 等類別與物件來完成題目，不可只在 main 中直接寫公式與流程。
Now combine multiple points into a shape. Design a base class Shape and a derived class Triangle, and solve this problem in an object-oriented way.
A Triangle object must be built from three Point2D objects in the given order. That means the first point, second point, and third point all have specific roles.
In the Triangle class, provide member functions to determine whether these three points can form a non-degenerate triangle. If the three points are collinear, then the triangle is invalid.
If the triangle is valid, output YES and then output its perimeter on the next line. Otherwise output NO and then output 0.00 on the next line.
You must use classes such as Shape, Triangle, and Point2D to solve this problem. Do not put the whole logic directly in main.

## 輸入說明
輸入一行，包含六個整數 x1 y1 x2 y2 x3 y3，依序代表三個點的座標。
The input contains one line with six integers x1 y1 x2 y2 x3 y3 representing three points in order.

## 輸出說明
輸出兩行。
第一行輸出 YES 或 NO，表示是否能形成有效三角形。
第二行輸出周長，固定到小數點後兩位；若無效則輸出 0.00。
Output two lines.
The first line is YES or NO indicating whether a valid triangle can be formed.
The second line is the perimeter rounded to two decimal places; output 0.00 if invalid.

---

## 範例測試
### 範例輸入 1
```text
0 0 3 0 0 4
```
### 範例輸出 1
```text
YES
12.00
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
    double getDistance(Point2D &obj)
    {
        return sqrt((x - obj.x) * (x - obj.x) + (y - obj.y) * (y - obj.y));
    }
};

class Triangle : public Shape
{
private:
    Point2D a, b, c;

public:
    Triangle(int x1, int y1, int x2, int y2, int x3, int y3) : a(x1, y1), b(x2, y2), c(x3, y3) {}
    void getPerimeter()
    {
        cout << fixed << setprecision(2) << a.getDistance(b) + b.getDistance(c) + c.getDistance(a) << endl;
    }
    void isTriangle()
    {
        if ((a.getDistance(b) + b.getDistance(c) > a.getDistance(c)) && (a.getDistance(c) + c.getDistance(b) > a.getDistance(b)) && (b.getDistance(a) + a.getDistance(c) > b.getDistance(c)))
        {
            cout << "YES" << endl;
            getPerimeter();
        }
        else
        {
            cout << "NO" << endl;
            cout << "0.00" << endl;
        }
    }
};

int main()
{
    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    Triangle obj(x1, y1, x2, y2, x3, y3);
    obj.isTriangle();
    return 0;
}
```
