# PR114-2-02: Question 2: The Secret Rectangle

## 題目敘述
長方形有兩個重要資料：寬度與高度。請你想像建立一個**Rectangle**類別，並用它來計算面積。
這一題的重點是練習：有些資料可以放在**private**，再透過公開的方法取得結果。
輸入長方形的寬與高後，請輸出它的面積。
A rectangle has two important values: width and height. Imagine building a**Rectangle**class and use it to calculate the area.
The main idea is to practice that some data can be stored as**private**members and accessed through public methods.
Given the width and height, output the area of the rectangle.

## 輸入說明
輸入一行，包含兩個整數**w h**，代表長方形的寬與高。
The input contains one line with two integers**w h**, representing the width and height.

## 輸出說明
輸出一行：**Area: X**，其中**X**為面積。
Output one line:**Area: X**, where**X**is the area.

---

## 範例測試
### 範例輸入 1
```text
4 5
```
### 範例輸出 1
```text
Area: 20
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

class Rectangle
{
private:
    int w;
    int h;

public:
    Rectangle(int a, int b) : w(a), h(b) {}
    int getArea()
    {
        return w * h;
    }
};

int main()
{
    int a, b;
    std::cin >> a >> b;
    Rectangle rect(a, b);
    std::cout << "Area: " << rect.getArea() << std::endl;
    return 0;
}
```
