# PR114-2-53: Question 53: The Score Report Output

## 題目敘述
在成績報表系統中，老師會輸入三次小考成績與一次實驗成績，系統必須立即輸出總分與平均分數。這題的重點是讓你熟悉使用 cin 讀取多個不同型別的資料，並用 cout 搭配格式控制輸出結果。
你必須讀入三個整數與一個浮點數，計算總和與平均值。平均值請固定輸出到小數點後兩位。
This score-report task asks you to read three quiz scores and one lab score, then immediately print the total and the average. The goal of this problem is to help you practice reading multiple values of different types with cin, and formatting output with cout.
You must read three integers and one floating-point value, compute the total and the average, and print the average with exactly two digits after the decimal point.

## 輸入說明
輸入一行，包含四個數值：
q1 q2 q3 lab
其中：
q1, q2, q3 為整數
lab 為浮點數
The input contains one line with four values:
q1 q2 q3 lab
where:
q1, q2, q3 are integers
lab is a floating-point number

## 輸出說明
輸出兩行：
Total: X
Average: Y
其中：
X 為四個分數的總和
Y 為四個分數的平均值，固定輸出到小數點後兩位
Output two lines:
Total: X
Average: Y
where:
X is the total of the four scores
Y is the average of the four scores, printed with exactly two digits after the decimal point

---

## 範例測試
### 範例輸入 1
```text
80 90 85 92.5
```
### 範例輸出 1
```text
Total: 347.50
Average: 86.88
```

### 範例輸入 2
```text
100 95 88 76.0
```
### 範例輸出 2
```text
Total: 359.00
Average: 89.75
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int q1, q2, q3;
    double lab;
    cin >> q1 >> q2 >> q3 >> lab;
    cout << fixed << setprecision(2) << "Total: " << (q1 + q2 + q3 + lab) << endl;
    cout << fixed << setprecision(2) << "Average: " << (q1 + q2 + q3 + lab) / 4 << endl;
    return 0;
}
```
