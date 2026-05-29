# PR114-2-55: Question 55: The Integer Line Parser

## 題目敘述
在簡易資料分析系統中，所有整數都先被收集成一整行字串，之後再交給程式逐一解析。這題的重點，是讓你學會如何使用 istringstream 從一整行文字中依序讀出多個數值。
你會得到一整行，裡面包含若干個以空白分隔的整數。你必須使用字串資料流將這些整數逐一讀出，並輸出它們的個數與總和。
In a simple data analysis system, all integers are first collected into one whole line of text, and then the program parses them one by one. The purpose of this problem is to help you learn how to use istringstream to extract multiple values from a line.
You will be given one entire line containing several integers separated by spaces. Use a string stream to read them one by one, then output the count of numbers and their total sum.

## 輸入說明
輸入只有一行，包含若干個以空白分隔的整數。整數個數至少為 1。
The input contains only one line with several integers separated by spaces. There is at least one integer.

## 輸出說明
輸出兩行：
Count: X
Sum: Y
其中：
X 為該行整數個數
Y 為該行整數總和
Output two lines:
Count: X
Sum: Y
where:
X is the number of integers in the line
Y is the sum of those integers

---

## 範例測試
### 範例輸入 1
```text
1 2 3 4 5
```
### 範例輸出 1
```text
Count: 5
Sum: 15
```

### 範例輸入 2
```text
10 -2 7
```
### 範例輸出 2
```text
Count: 3
Sum: 15
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>

using namespace std;

int main()
{
    string n;
    getline(cin, n);
    istringstream is(n);
    int x;
    int sum = 0, counter = 0;
    while (is >> x)
    {
        counter++;
        sum += x;
    }
    cout << "Count: " << counter << endl;
    cout << "Sum: " << sum << endl;
    return 0;
}
```
