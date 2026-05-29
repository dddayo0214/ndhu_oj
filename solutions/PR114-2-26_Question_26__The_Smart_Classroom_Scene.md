# PR114-2-26: Question 26: The Smart Classroom Scene

## 題目敘述
在一間智慧教室中，有三種重要物件：Student、Light 與 Classroom。
Student 代表一位學生，至少需要有名字以及是否在教室內的狀態。Light 代表教室燈，燈只有 ON 與 OFF 兩種狀態。Classroom 代表教室本身，負責管理目前有哪些學生在教室內，並依照教室內的人數控制燈的狀態。
規則如下：一開始教室是空的，燈為 OFF。當第一位學生進入教室時，燈會自動變成 ON。當最後一位學生離開教室時，燈會自動變回 OFF。如果同一位學生重複 ENTER，狀態不改變；如果本來不在教室內卻執行 LEAVE，也不改變狀態。
你必須使用物件導向方式作答。請至少以類別描述 Student、Light 與 Classroom，並讓 Classroom 透過成員函式處理 ENTER、LEAVE 與 STATUS 操作。不得只用零散變數與一般函式硬寫整個流程。
In a smart classroom, there are three important objects: Student, Light, and Classroom.
A Student represents one student and should at least store the student's name and whether the student is inside the classroom. A Light represents the classroom light, which has only two states: ON and OFF. A Classroom represents the classroom itself. It manages which students are currently inside and controls the light according to the number of students in the room.
The rules are as follows. Initially, the classroom is empty and the light is OFF. When the first student enters, the light turns ON automatically. When the last student leaves, the light turns OFF automatically. If the same student performs ENTER again, nothing changes. If a student who is not inside performs LEAVE, nothing changes.
You must solve this problem using object-oriented programming. At minimum, use classes to describe Student, Light, and Classroom, and let Classroom handle ENTER, LEAVE, and STATUS through member functions. Do not write the whole solution using only scattered variables and ordinary functions.
1 ≤ Q ≤ 100。不同學生姓名數量不超過 100。
1 ≤ Q ≤ 100. The number of distinct student names does not exceed 100.

## 輸入說明
第一行輸入一個整數 Q，表示操作次數。
接下來 Q 行，每行為下列三種操作之一：ENTER name、LEAVE name、STATUS。
name 只包含英文字母，且不含空白。
The first line contains an integer Q, the number of operations.
The next Q lines each contain one of the following operations: ENTER name, LEAVE name, or STATUS.
The name contains only English letters and no spaces.

## 輸出說明
對每個操作輸出一行。
ENTER 成功輸出「name entered」，重複進入輸出「name already inside」。
LEAVE 成功輸出「name left」，若該學生不在教室內則輸出「name not inside」。
STATUS 輸出「Students: X, Light: Y」，其中 Y 為 ON 或 OFF。
Output one line for each operation.
If ENTER succeeds, output "name entered". If the student is already inside, output "name already inside".
If LEAVE succeeds, output "name left". If the student is not inside, output "name not inside".
For STATUS, output "Students: X, Light: Y", where Y is either ON or OFF.

---

## 範例測試
### 範例輸入 1
```text
8
STATUS
ENTER Alice
STATUS
ENTER Bob
LEAVE Alice
STATUS
LEAVE Bob
STATUS
```
### 範例輸出 1
```text
Students: 0, Light: OFF
Alice entered
Students: 1, Light: ON
Bob entered
Alice left
Students: 1, Light: ON
Bob left
Students: 0, Light: OFF
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Student
{
private:
    string name;

public:
    Student(string Name) : name(Name) {}
    string getName()
    {
        return name;
    }
};

class Light
{
private:
    bool status = 0;

public:
    void toggle()
    {
        status = !status;
    }
    bool getStatus()
    {
        return status;
    }
};

class Classroom
{
private:
    Student *students[200];
    int studentCount = 0;
    Light light;

public:
    void display()
    {
        cout << "Students: " << studentCount << ", Light: " << (light.getStatus() ? "ON" : "OFF") << endl;
    }
    void insertStudent(string name)
    {
        students[studentCount] = new Student(name);
        studentCount++;
        if (studentCount == 1)
        {
            light.toggle();
        }
    }
    bool isInClass(string name)
    {
        for (int i = 0; i < studentCount; i++)
        {
            if (students[i]->getName() == name)
            {
                return true;
            }
        }
        return false;
    }
    void removeStudent(string name)
    {
        for (int i = 0; i < studentCount; i++)
        {
            if (students[i]->getName() == name)
            {
                for (int j = i; j < studentCount - 1; j++)
                {
                    students[j] = students[j + 1];
                }
                studentCount--;
                if (studentCount == 0)
                {
                    light.toggle();
                }
                break;
            }
        }
    }
};

int main()
{
    int n;
    string input;
    Classroom cls;
    cin >> n;
    while (n--)
    {
        cin >> input;
        if (input == "STATUS")
        {
            cls.display();
        }
        else if (input == "ENTER")
        {
            string name;
            cin >> name;
            if (!cls.isInClass(name))
            {
                cls.insertStudent(name);
                cout << name << " entered" << endl;
            }
            else
            {
                cout << name << " already inside" << endl;
            }
        }
        else
        {
            string name;
            cin >> name;
            if (cls.isInClass(name))
            {
                cls.removeStudent(name);
                cout << name << " left" << endl;
            }
            else
            {
                cout << name << " not inside" << endl;
            }
        }
    }
    return 0;
}
```
