# PR114-2-07: Question 7: The Rectangle Builder

## 題目敘述
請設計一個**Rectangle**類別，使用建構子接收長與寬，並提供方法計算面積。
雖然 Online Judge 只檢查輸出，但建議你真的用建構子來初始化物件。
Design a**Rectangle**class. Use a constructor to receive the width and height, and provide a method to compute the area.
Although the Online Judge only checks the output, you are encouraged to really initialize the object with a constructor.

## 輸入說明
輸入一行，包含兩個整數**width height**。
The input contains one line with two integers:**width height**.

## 輸出說明
輸出一行：**Area: area**
Output one line:**Area: area**

---

## 範例測試
### 範例輸入 1
```text
3 4
```
### 範例輸出 1
```text
Area: 12
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

using namespace std;

class Rectangle
{
private:
    int h, w;

public:
    Rectangle(int h, int w) : h(h), w(w) {};
    int getArea()
    {
        return h * w;
    }
};

int main()
{
    int h, w;
    cin >> h >> w;
    Rectangle rect(h, w);
    cout << "Area: " << rect.getArea() << endl;
    return 0;
}
```
