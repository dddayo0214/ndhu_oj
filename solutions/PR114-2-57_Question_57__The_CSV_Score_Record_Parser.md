# PR114-2-57: Question 57: The CSV Score Record Parser

## 題目敘述
在教務系統中，一筆成績資料可能先以單行字串形式儲存，例如：
name,midterm,final,bonus
程式需要先從這一行字串中拆出各欄位，再計算總成績並重新輸出整理後的報表。這題的重點，是讓你綜合使用字串資料流、getline 的分隔字元版本，以及格式化輸出。
你必須讀入一整行 CSV 風格的資料，欄位以逗號分隔。欄位依序為：
姓名、期中考分數、期末考分數、加分
請使用字串資料流解析這一行資料，計算總分與平均值，並依照指定格式輸出。平均值固定輸出到小數點後兩位。
In an academic system, one record may be stored as a single line of text in the following style:
name,midterm,final,bonus
The program must extract each field from the line, compute the final statistics, and print a formatted report. The purpose of this problem is to practice integrated use of string streams, getline with a custom delimiter, and formatted output.
You must read one line of CSV-style data separated by commas. The fields are:
name, midterm score, final score, and bonus
Use string streams to parse the line, compute the total and the average, and print the report in the required format. The average must be printed with exactly two digits after the decimal point.

## 輸入說明
輸入只有一行，格式如下：
name,midterm,final,bonus
其中：
name 是不含逗號的姓名字串
midterm, final, bonus 都是整數
The input contains one line in the following format:
name,midterm,final,bonus
where:
name is a string without commas
midterm, final, and bonus are integers

## 輸出說明
輸出三行：
Name: name
Total: X
Average: Y
其中：
X = midterm + final + bonus
Y = X / 3，固定輸出到小數點後兩位
Output three lines:
Name: name
Total: X
Average: Y
where:
X = midterm + final + bonus
Y = X / 3, printed with exactly two digits after the decimal point

---

## 範例測試
### 範例輸入 1
```text
Alice,80,90,5
```
### 範例輸出 1
```text
Name: Alice
Total: 175
Average: 58.33
```

### 範例輸入 2
```text
Bob,70,85,10
```
### 範例輸出 2
```text
Name: Bob
Total: 165
Average: 55.00
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
    string name, input;
    getline(cin, input);
    stringstream ss;
    ss << input;
    getline(ss, name, ',');
    int x = 0;
    while (getline(ss, input, ','))
    {
        x += stoi(input);
    }
    double y = x / 3.0;
    cout << "Name: " << name << endl;
    cout << "Total: " << x << endl;
    cout << fixed << setprecision(2) << "Average: " << y << endl;
    return 0;
}
```
