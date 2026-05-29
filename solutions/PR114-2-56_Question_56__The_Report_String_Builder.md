# PR114-2-56: Question 56: The Report String Builder

## 題目敘述
在訊息產生系統中，程式需要先把一段報告內容組裝成字串，再一次輸出。這題的目的，是讓你練習使用 ostringstream，把不同型別的資料依照指定格式串接成一段完整的字串。
你必須讀入一位學生的姓名、一門課程名稱，以及分數。接著請使用字串資料流建立一段報告字串，最後再輸出這個字串。
In a message generation system, the program first builds a report as a string and then prints it at once. The purpose of this problem is to practice using ostringstream to combine values of different types into one formatted string.
You must read a student's name, a course name, and a score. Then build a report string using a string output stream, and finally print that string.

## 輸入說明
輸入三行：
第一行是學生姓名 name
第二行是課程名稱 course
第三行是整數分數 score
The input contains three lines:
The first line is the student name
The second line is the course name
The third line is the integer score

## 輸出說明
輸出一行：
[Report] name got score points in course.
請依照格式完整輸出。
Output one line:
[Report] name got score points in course.
Print the line exactly in the required format.

---

## 範例測試
### 範例輸入 1
```text
Alice
Programming I
95
```
### 範例輸出 1
```text
[Report] Alice got 95 points in Programming I.
```

### 範例輸入 2
```text
Bob
Calculus
88
```
### 範例輸出 2
```text
[Report] Bob got 88 points in Calculus.
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
    string name, course, score;
    getline(cin, name);
    getline(cin, course);
    getline(cin, score);
    ostringstream os;
    os << "[Report] " << name << " got " << score << " points in " << course << "." << endl;
    cout << os.str();
    return 0;
}
```
