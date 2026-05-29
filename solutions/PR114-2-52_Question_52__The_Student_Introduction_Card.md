# PR114-2-52: Question 52: The Student Introduction Card

## 題目敘述
在校園迎新系統中，每位新生都需要輸入自己的基本資料，系統再用標準輸出產生一段簡單的自我介紹。這題的目的，是讓你熟悉 C++ 的標準輸入資料流 cin 與標準輸出資料流 cout 的最基本用法。
你必須讀入一位學生的姓名、年齡與主修科系，然後依照指定格式輸出一行結果。
本題希望你使用 C++ 的標準輸入輸出資料流完成，不要使用其他不必要的技巧。請注意，姓名與科系都不包含空白。
In a campus orientation system, each new student enters basic information, and the system prints a short self-introduction using standard output. The purpose of this problem is to help you practice the most basic use of C++ standard input stream cin and standard output stream cout.
You must read one student's name, age, and major, then output exactly one line in the required format.
This problem is intended to be solved using C++ standard input and output streams. You do not need any complicated technique here. Note that the name and the major contain no spaces.

## 輸入說明
輸入一行，包含三個資料：
name age major
其中：
name 為學生姓名
age 為整數年齡
major 為主修科系名稱
The input contains one line with three items:
name age major
where:
name is the student's name
age is an integer age
major is the name of the major

## 輸出說明
輸出一行：
Student name is age years old and majors in major.
請依照格式輸出，包含標點符號與空白。
Output one line:
Student name is age years old and majors in major.
Follow the format exactly, including punctuation and spaces.

---

## 範例測試
### 範例輸入 1
```text
Alice 18 CS
```
### 範例輸出 1
```text
Student Alice is 18 years old and majors in CS.
```

### 範例輸入 2
```text
Bob 20 Math
```
### 範例輸出 2
```text
Student Bob is 20 years old and majors in Math.
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

using namespace std;

int main()
{
    string name, age, maj;
    cin >> name >> age >> maj;
    cout << "Student " << name << " is " << age << " years old and majors in " << maj << "." << endl;
    return 0;
}
```
