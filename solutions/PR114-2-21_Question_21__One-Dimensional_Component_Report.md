# PR114-2-21: Question 21: One-Dimensional Component Report

## 題目敘述
請設計一個類別 Component1D，用來表示數線上的一個一維分量。類別中至少要保存一個整數座標 value，並提供適當的建構方式與成員函式來完成本題要求。
你必須使用物件導向的方式作答，也就是建立 class 與 object 來處理資料。請不要只用一般變數直接計算後輸出結果。
輸入兩個整數 a 與 b，請分別建立兩個 Component1D 物件，代表數線上的兩個位置。接著計算從 a 移動到 b 的位移量，以及從 b 移動回 a 的位移量。
若以位移的觀點來看，從 a 到 b 的位移可表示為 b - a；從 b 到 a 的位移可表示為 a - b。
請輸出兩行。第一行輸出 fromAtoB，第二行輸出 fromBtoA。
Design a class named Component1D to represent a one-dimensional component on a number line. The class should store at least one integer coordinate value and provide suitable constructors and member functions to complete this problem.
You must solve this problem in an object-oriented way by creating classes and objects. Do not solve it using only ordinary variables and direct calculations.
Given two integers a and b, create two Component1D objects to represent two positions on the number line. Then compute the displacement from a to b and the displacement from b to a.
From the displacement point of view, the displacement from a to b is b - a, and the displacement from b to a is a - b.
Output two lines. The first line is fromAtoB, and the second line is fromBtoA.

## 輸入說明
輸入一行，包含兩個整數 a 與 b。
The input contains one line with two integers a and b.

## 輸出說明
輸出兩行。
第一行輸出從 a 到 b 的位移量。
第二行輸出從 b 到 a 的位移量。
Output two lines.
The first line is the displacement from a to b.
The second line is the displacement from b to a.

---

## 範例測試
### 範例輸入 1
```text
3 5
```
### 範例輸出 1
```text
2
-2
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Component1D
{
private:
    int value;

public:
    Component1D(int v) : value(v) {}
    int getValue() { return value; }
    void getDisplacement(Component1D &obj)
    {
        cout << obj.getValue() - value << endl;
    }
};

int main()
{
    int a, b;
    cin >> a >> b;
    Component1D obj1(a), obj2(b);
    obj1.getDisplacement(obj2);
    obj2.getDisplacement(obj1);
    return 0;
}
```
