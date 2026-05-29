# PR114-2-46: Question 46: The Classroom Capacity Exception

## 題目敘述
一間教室的容量上限為 capacity，目前已有 current 位學生，現在又有 entering 位學生想進入。若 current + entering 不超過 capacity，輸出更新後的人數。否則，你必須定義並拋出一個自訂例外類別 ClassroomFullException，並讓它繼承 std::exception。其 what() 必須回傳固定字串 "Classroom capacity exceeded"。主程式必須接住此例外並輸出 what()。
A classroom has a maximum capacity of capacity. There are currently current students inside, and entering more students want to enter. If current + entering does not exceed capacity, output the updated number of students. Otherwise, you must define and throw a custom exception class ClassroomFullException that inherits from std::exception. Its what() must return the fixed string "Classroom capacity exceeded". The main program must catch the exception and output what().

## 輸入說明
輸入三個整數 capacity、current、entering。
The input contains three integers: capacity, current, and entering.

## 輸出說明
若能成功進入，輸出進入後的人數；否則輸出 Classroom capacity exceeded。
If entry is successful, output the new number of students; otherwise output Classroom capacity exceeded.

---

## 範例測試
### 範例輸入 1
```text
30 25 3
```
### 範例輸出 1
```text
28
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <vector>

using namespace std;

class ClassroomFullException : public exception
{
public:
    string msg;
    ClassroomFullException(string e) : msg(e) {}
    virtual string what()
    {
        return msg;
    }
};

int main()
{
    int n, m, o;
    cin >> n >> m >> o;
    try
    {
        if (m + o <= n)
        {
            cout << m + o << endl;
        }
        else
        {
            throw ClassroomFullException("Classroom capacity exceeded");
        }
    }
    catch (ClassroomFullException &e)
    {
        cout << e.what() << endl;
    }
    return 0;
}
```
