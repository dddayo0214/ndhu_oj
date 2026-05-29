# PR114-2-54: Question 54: The Registration Desk Form

## 題目敘述
在學生註冊櫃台中，工作人員會先輸入學號，再輸入學生的完整姓名與完整系所名稱。由於姓名與系所都可能包含空白，本題的重點是讓你練習同時使用 operator>> 與 getline，並理解標準輸入資料流中換行符號對讀取的影響。
你必須先讀入一個整數學號，接著讀入兩整行文字，分別代表學生姓名與系所名稱，最後依照指定格式輸出三行結果。
At a student registration desk, the staff enters the student ID first, then the student's full name and the full department name. Since the name and the department may contain spaces, the purpose of this problem is to practice using both operator>> and getline, and to understand how newline characters affect standard input streams.
You must first read one integer ID, then read two full lines representing the student's name and the department name, and finally output three lines in the required format.

## 輸入說明
輸入共三行：
第一行是一個整數 id
第二行是一整行學生姓名 name
第三行是一整行系所名稱 department
The input contains three lines:
The first line is an integer id
The second line is the full student name
The third line is the full department name

## 輸出說明
輸出三行：
ID: id
Name: name
Department: department
請保持格式完全一致。
Output three lines:
ID: id
Name: name
Department: department
Keep the format exactly the same.

---

## 範例測試
### 範例輸入 1
```text
12345
Alice Chen
Department of Computer Science
```
### 範例輸出 1
```text
ID: 12345
Name: Alice Chen
Department: Department of Computer Science
```

### 範例輸入 2
```text
10001
Bob Lee
Department of Applied Mathematics
```
### 範例輸出 2
```text
ID: 10001
Name: Bob Lee
Department: Department of Applied Mathematics
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    string id, name, de;
    cin >> id;
    cin.get();
    getline(cin, name);
    getline(cin, de);
    cout << "ID: " << id << endl;
    cout << "Name: " << name << endl;
    cout << "Department: " << de << endl;
    return 0;
}
```
