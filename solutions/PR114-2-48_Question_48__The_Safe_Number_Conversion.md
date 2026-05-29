# PR114-2-48: Question 48: The Safe Number Conversion

## 題目敘述
In this problem, you will practice the most basic and safest use of static_cast in C++. You are given three values: an integer, a floating-point number, and a character. Your task is to perform three explicit conversions and print the results.
You must use static_cast in your program to complete the conversions. The purpose of this problem is to help you understand that static_cast is commonly used when the source type and target type are already known at compile time. It does not perform runtime type checking, but it makes the programmer's intention clear.
The three required conversions are listed below. First, convert the given floating-point number into an integer. Second, convert the given integer into a double. Third, convert the given character into its ASCII integer code.
When converting from double to int, the fractional part will be discarded. When printing the converted double value, print it with exactly two digits after the decimal point.
本題要你練習 C++ 中 static_cast 最基本也最直觀的使用方式。輸入會提供三個值：一個整數、一個浮點數，以及一個字元。你的任務是完成三個明確的型別轉換，並依指定格式輸出結果。
你的程式必須使用 static_cast 來完成這些轉換。這題的目的，是讓你理解 static_cast 常用在編譯期就已知來源型別與目標型別的情況。它不會進行執行期型別檢查，但可以讓程式的轉型意圖更清楚。
本題要求的三個轉換如下：第一，將輸入的浮點數轉成整數。第二，將輸入的整數轉成 double。第三，將輸入的字元轉成其 ASCII 整數代碼。
從 double 轉成 int 時，小數部分會被直接捨去。輸出轉換後的 double 時，必須固定顯示到小數點後兩位。

## 輸入說明
The input contains one line with three values: an integer a, a double b, and a character c.
輸入只有一行，包含三個值：整數 a、浮點數 b、以及字元 c。

## 輸出說明
Print three lines in the following format:
From double to int: X
From int to double: Y
ASCII of char: Z
The value Y must be printed with exactly two digits after the decimal point.
請輸出三行，格式如下：
From double to int: X
From int to double: Y
ASCII of char: Z
其中 Y 必須固定輸出到小數點後兩位。

---

## 範例測試
### 範例輸入 1
```text
7 3.9 A

```
### 範例輸出 1
```text
From double to int: 3
From int to double: 7.00
ASCII of char: 65

```

### 範例輸入 2
```text
-2 -8.75 z

```
### 範例輸出 2
```text
From double to int: -8
From int to double: -2.00
ASCII of char: 122

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int x;
    double y;
    char z;
    cin >> x >> y >> z;
    cout << "From double to int: " << static_cast<int>(y) << endl;
    cout << fixed << setprecision(2) << "From int to double: " << static_cast<double>(x) << endl;
    cout << "ASCII of char: " << static_cast<int>(z) << endl;
}
```
