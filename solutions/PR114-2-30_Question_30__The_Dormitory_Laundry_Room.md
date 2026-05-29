# PR114-2-30: Question 30: The Dormitory Laundry Room

## 題目敘述
在學生宿舍的洗衣間中，有多台洗衣機，學生可以使用空閒機器進行洗衣。你需要用程式描述這個場景中的互動。
Student 代表一位學生，至少應包含姓名以及目前是否正在使用某台洗衣機。 Machine 代表一台洗衣機，至少應包含編號與是否被佔用。 LaundryRoom 代表整個洗衣間，負責管理所有機器與學生的使用狀態。
規則如下。START name id 表示學生 name 想開始使用編號 id 的洗衣機，只有當該機器存在、目前空閒且該學生尚未使用其他機器時才成功。FINISH name id 只有在該學生目前真的使用那台機器時才成功。STATUS 用來查詢目前忙碌與空閒的洗衣機數量。
你必須使用物件導向方式作答，並以 Student、Machine 與 LaundryRoom 類別描述此場景。請讓 LaundryRoom 作為主要的管理物件。不得只用零散變數硬寫。
In a dormitory laundry room, several washing machines are available, and students may use free machines to do laundry. You need to describe the interaction in this scene.
A Student represents one student and should at least include a name and whether the student is currently using a machine. A Machine represents one washing machine and should at least include an id and whether it is occupied. A LaundryRoom represents the whole room and manages all machines and all student usage states.
The rules are as follows. START name id means that student name wants to start using machine id. It succeeds only if the machine exists, is currently free, and the student is not already using another machine. FINISH name id succeeds only if the student is really using that machine. STATUS asks for the current numbers of busy and idle machines.
You must solve this problem using object-oriented programming and use Student, Machine, and LaundryRoom classes to describe the scene. Let LaundryRoom act as the main manager object. Do not write the whole solution using only scattered variables.
1 ≤ M ≤ 50，1 ≤ Q ≤ 200。學生姓名只包含英文字母與數字。
1 ≤ M ≤ 50, 1 ≤ Q ≤ 200. Student names contain only letters and digits.

## 輸入說明
第一行輸入兩個整數 M 與 Q，代表洗衣機台數與操作次數。
洗衣機編號固定為 1 到 M。
接著 Q 行，每行為 START name id、FINISH name id 或 STATUS。
The first line contains two integers M and Q, the number of washing machines and the number of operations.
Machine ids are fixed from 1 to M.
The next Q lines each contain START name id, FINISH name id, or STATUS.

## 輸出說明
對每個操作輸出一行。
START 成功輸出「name started machine id」，否則輸出「name cannot start」。
FINISH 成功輸出「name finished machine id」，否則輸出「name cannot finish」。
STATUS 輸出「Busy: X, Idle: Y」。
Output one line for each operation.
If START succeeds, output "name started machine id". Otherwise output "name cannot start".
If FINISH succeeds, output "name finished machine id". Otherwise output "name cannot finish".
For STATUS, output "Busy: X, Idle: Y".

---

## 範例測試
### 範例輸入 1
```text
3 8
STATUS
START Amy 1
START Bob 2
STATUS
FINISH Amy 1
START Amy 3
STATUS
FINISH Bob 2
```
### 範例輸出 1
```text
Busy: 0, Idle: 3
Amy started machine 1
Bob started machine 2
Busy: 2, Idle: 1
Amy finished machine 1
Amy started machine 3
Busy: 2, Idle: 1
Bob finished machine 2
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <map>
using namespace std;

class Machine
{
public:
    int isUsing;
    Machine() : isUsing(0) {}
};

class Student
{
public:
    string name;
    int isUsing;
    Student() : name(""), isUsing(0) {}
    Student(string n) : name(n), isUsing(0) {}
};

class LaundryRoom
{
private:
    map<int, Machine> machines;
    map<string, Student> students;
    int machineCount;
    int count;

public:
    LaundryRoom(int M) : machineCount(M), count(0)
    {
        for (int i = 1; i <= M; i++)
        {
            machines[i] = Machine();
        }
    }
    void status()
    {
        cout << "Busy: " << count << ", Idle: " << machineCount - count << endl;
    }
    void start(string name, int id)
    {
        if (students.find(name) == students.end())
        {
            students[name] = Student(name);
        }
        if (id <= machineCount && id > 0 && machines[id].isUsing == 0 && students[name].isUsing == 0)
        {
            machines[id].isUsing = 1;
            students[name].isUsing = id;
            count++;
            cout << name << " started machine " << id << endl;
        }
        else
        {
            cout << name << " cannot start" << endl;
        }
    }
    void finish(string name, int id)
    {
        if (students.find(name) == students.end())
        {
            students[name] = Student(name);
        }
        if (id <= machineCount && id > 0 && students[name].isUsing == id)
        {
            machines[id].isUsing = 0;
            students[name].isUsing = 0;
            count--;
            cout << name << " finished machine " << id << endl;
        }
        else
        {
            cout << name << " cannot finish" << endl;
        }
    }
};

int main()
{
    int M, Q;
    cin >> M >> Q;
    LaundryRoom lr(M);
    while (Q--)
    {
        string input;
        cin >> input;
        if (input == "START")
        {
            string name;
            int id;
            cin >> name >> id;
            lr.start(name, id);
        }
        else if (input == "FINISH")
        {
            string name;
            int id;
            cin >> name >> id;
            lr.finish(name, id);
        }
        else
        {
            lr.status();
        }
    }

    return 0;
}
```
