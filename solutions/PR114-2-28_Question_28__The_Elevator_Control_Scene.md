# PR114-2-28: Question 28: The Elevator Control Scene

## 題目敘述
在一棟教學大樓中，有多位人員會搭乘電梯。你需要用程式描述 Person、Elevator 與 Building 之間的互動。
Person 代表一位搭乘者，至少應包含名字以及目前所在樓層。 Elevator 代表一台電梯，至少應包含目前樓層、最大容量以及目前乘客數。 Building 代表整棟建築，負責接收操作並協調人員與電梯的互動。
規則如下。MOVE f 表示電梯移動到樓層 f。ENTER name floor 表示一位目前在 floor 的人想進入電梯，只有當電梯也在同一樓層、此人目前不在電梯內、而且電梯尚未滿載時才成功。若該人第一次出現，視為其目前就在輸入指定的樓層。EXIT name floor 表示該人想在 floor 樓離開電梯，只有當此人目前在電梯內且電梯也在 floor 時才成功。
你必須使用物件導向方式作答，並以類別描述 Person、Elevator 與 Building。請讓 Building 透過成員函式統一管理這個場景。不得只用單純變數硬寫。
In a teaching building, many people use an elevator. You need to describe the interaction among Person, Elevator, and Building.
A Person represents one passenger and should at least contain a name and the current floor of that person. An Elevator represents one elevator and should at least contain the current floor, maximum capacity, and number of passengers. A Building represents the whole building, receives operations, and coordinates the interaction between people and the elevator.
The rules are as follows. MOVE f moves the elevator to floor f. ENTER name floor means a person currently on floor wants to enter the elevator. It succeeds only when the elevator is also on that floor, the person is not already inside the elevator, and the elevator is not full. If a person appears for the first time, assume that the person is currently on the floor given in the input. EXIT name floor means that person wants to leave the elevator on that floor. It succeeds only if the person is currently inside the elevator and the elevator is also on that floor.
You must solve this problem using object-oriented programming and classes for Person, Elevator, and Building. Let Building manage the whole scene through member functions. Do not write the whole logic using only simple variables.
1 ≤ C ≤ 20，1 ≤ Q ≤ 200，1 ≤ floor ≤ 100。
1 ≤ C ≤ 20, 1 ≤ Q ≤ 200, 1 ≤ floor ≤ 100.

## 輸入說明
第一行輸入兩個整數 C 與 Q，代表電梯容量與操作次數。
接著 Q 行，每行為 MOVE f、ENTER name floor、EXIT name floor 或 STATUS。
The first line contains two integers C and Q, the capacity of the elevator and the number of operations.
The next Q lines each contain one of the following operations: MOVE f, ENTER name floor, EXIT name floor, or STATUS.

## 輸出說明
對每個操作輸出一行。
MOVE 輸出「Elevator moved to f」。
ENTER 成功輸出「name entered」，否則輸出「name cannot enter」。
EXIT 成功輸出「name exited」，否則輸出「name cannot exit」。
STATUS 輸出「Floor: F, Passengers: P」。
Output one line for each operation.
For MOVE, output "Elevator moved to f".
If ENTER succeeds, output "name entered". Otherwise output "name cannot enter".
If EXIT succeeds, output "name exited". Otherwise output "name cannot exit".
For STATUS, output "Floor: F, Passengers: P".

---

## 範例測試
### 範例輸入 1
```text
2 8
STATUS
ENTER Amy 1
MOVE 3
STATUS
EXIT Amy 3
STATUS
MOVE 1
STATUS
```
### 範例輸出 1
```text
Floor: 1, Passengers: 0
Amy entered
Elevator moved to 3
Floor: 3, Passengers: 1
Amy exited
Floor: 3, Passengers: 0
Elevator moved to 1
Floor: 1, Passengers: 0
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Person
{
private:
    string name;
    int floor;
    bool inElevator;

public:
    Person(string n, int f)
    {
        name = n;
        floor = f;
        inElevator = 0;
    }
    void Enter()
    {
        inElevator = 1;
    }
    void Exit()
    {
        inElevator = 0;
    }
    string getName()
    {
        return name;
    }
    int &getFloor()
    {
        return floor;
    }
    bool isInElevator()
    {
        return inElevator;
    }
};

class Elevator
{
private:
    int nowFloor;
    int maxElevators;
    int peopleCount;

public:
    Elevator(int m) : maxElevators(m), nowFloor(1), peopleCount(0) {}
    int getNowFloor()
    {
        return nowFloor;
    }
    int getPeopleCount()
    {
        return peopleCount;
    }
    void PeopleEnter(Person *p, int floor)
    {
        if (p->isInElevator() || peopleCount == maxElevators || nowFloor != floor || p->getFloor() != floor)
        {
            cout << p->getName() << " cannot enter" << endl;
            return;
        }
        peopleCount++;
        p->Enter();
        cout << p->getName() << " entered" << endl;
    }
    void PeopleExit(Person *p, int floor)
    {
        if (!p->isInElevator() || nowFloor != floor)
        {
            cout << p->getName() << " cannot exit" << endl;
            return;
        }
        peopleCount--;
        p->Exit();
        p->getFloor() = floor;
        cout << p->getName() << " exited" << endl;
    }
    void Move(int floor)
    {
        nowFloor = floor;
        cout << "Elevator moved to " << floor << endl;
    }
};

class Building
{
private:
    Elevator elevator;
    int peopleCount = 0;
    Person *people[200];

public:
    Building(int m) : elevator(m) {}
    void display()
    {
        cout << "Floor: " << elevator.getNowFloor() << ", Passengers: " << elevator.getPeopleCount() << endl;
    }
    void PeopleEnter(string name, int floor)
    {
        if (!isInBul(name))
        {
            people[peopleCount] = new Person(name, floor);
            peopleCount++;
        }
        elevator.PeopleEnter(getPeople(name), floor);
    }
    void PeopleExit(string name, int floor)
    {
        elevator.PeopleExit(getPeople(name), floor);
    }
    void Move(int floor)
    {
        elevator.Move(floor);
    }
    bool isInBul(string name)
    {
        for (int i = 0; i < peopleCount; i++)
        {
            if (people[i]->getName() == name)
            {
                return true;
            }
        }
        return false;
    }
    Person *getPeople(string name)
    {
        for (int i = 0; i < peopleCount; i++)
        {
            if (people[i]->getName() == name)
                return people[i];
        }
        return nullptr;
    }
};

int main()
{
    int C, Q;
    string input;
    cin >> C >> Q;
    Building building(C);
    while (Q--)
    {
        string input;
        cin >> input;
        if (input == "STATUS")
        {
            building.display();
        }
        else if (input == "ENTER")
        {
            string name;
            int floor;
            cin >> name >> floor;
            building.PeopleEnter(name, floor);
        }
        else if (input == "EXIT")
        {
            string name;
            int floor;
            cin >> name >> floor;
            building.PeopleExit(name, floor);
        }
        else
        {
            int floor;
            cin >> floor;
            building.Move(floor);
        }
    }
    return 0;
}
```
