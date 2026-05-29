# PR114-2-31: Question 31: The Campus Delivery Scene with Polymorphism

## 題目敘述
在一座智慧校園中，物流中心每天都需要把包裹配送到不同的地點。為了讓整個配送流程更容易管理，校方希望使用物件導向的方式來描述場景中的各種角色與它們之間的互動。
在這個場景中，配送員會攜帶包裹，從目前所在的位置出發，透過不同的運輸方式將包裹送往指定目的地。不同配送員可能使用不同的運輸方式，例如自行車或自動配送機器人。雖然這些運輸方式都能讓配送員移動，但它們在移動成本的計算上並不相同，因此你需要一套清楚的類別設計來描述人物、位置、包裹、配送員、運輸方式，以及配送過程中的互動。
你必須使用 C++ 的物件導向方式完成這題，並在設計中體現以下概念：類別與物件、封裝、繼承、運算子多載、多型與虛擬函數。你不能只用一般變數與一般函式硬做出結果。
在概念上，你的程式至少應包含下列角色：
1. Location：表示校園中的座標位置，包含整數 x 與 y。
2. Package：表示包裹，包含包裹編號、重量，以及目的地位置。
3. Person：表示一般人物，至少包含姓名。
4. Courier：Courier 必須繼承自 Person，表示配送員。每位配送員有自己的目前位置、運輸方式，以及目前是否攜帶包裹。
5. Transport：Transport 應作為運輸方式的基底類別，並至少提供一個 virtual 成員函式。
6. BikeTransport 與 RobotTransport：兩者皆繼承自 Transport，並覆寫至少一個虛擬函式，以展現多型。你的程式必須透過基底類別指標或基底類別參考來呼叫被覆寫的函式。
你還必須在程式中設計並實際使用至少兩種運算子多載。建議使用 Location 的 operator+ 與 operator==，也可以自行設計其他合理的多載。除此之外，本題另提供 LIGHTER 指令，用來比較兩個包裹的重量；若你願意，也可以將 Package 的比較設計成運算子多載的一部分。
場景規則如下：
(1) 一開始會建立若干位配送員，每位配送員都有姓名、初始位置，以及一種運輸方式。運輸方式只會是 BIKE 或 ROBOT。
(2) 接著會建立若干個包裹。每個包裹有唯一的編號、重量，以及目的地位置。
(3) 每位配送員同一時間最多只能攜帶一個包裹。
(4) 每個包裹在成功配送後，不會再次被分配。
(5) 當系統收到 ASSIGN 指令時，表示要把指定包裹分配給指定配送員。若該配送員目前已攜帶包裹，則這次分配失敗。若該包裹已被其他配送員攜帶，也視為分配失敗。
(6) 當系統收到 MOVE 指令時，表示指定配送員要移動一段位移量 (dx, dy)。兩種運輸方式在 MOVE 指令中都會依照輸入的位移量直接更新位置，也就是新位置等於舊位置加上 (dx, dy)。
(7) 當系統收到 COST 指令時，表示查詢某位配送員若執行指定位移 (dx, dy)，其移動成本是多少。BikeTransport 的成本為 |dx| + |dy|，RobotTransport 的成本為 2 × (|dx| + |dy|)。
(8) 當系統收到 DELIVER 指令時，指定配送員會嘗試配送自己目前攜帶的包裹。若配送員目前沒有包裹，則配送失敗；若配送員目前位置與包裹目的地位置相同，則配送成功；否則配送失敗。
(9) 當系統收到 STATUS 指令時，請輸出該配送員目前的位置、運輸方式，以及是否攜帶包裹。
(10) 當系統收到 LIGHTER 指令時，請比較兩個包裹的重量，輸出較輕的包裹編號；若重量相同，輸出 Equal weight。
In a smart campus, the logistics center needs to deliver packages to different locations every day. To manage the whole process more clearly, the school wants the scene to be described using object-oriented programming.
In this scene, couriers carry packages, start from their current locations, and use different transport methods to deliver packages to target destinations. Different couriers may use different transport methods, such as bicycles or delivery robots. Although all transport methods can move a courier, they do not calculate movement cost in the same way. Therefore, you need a clear class design to describe people, locations, packages, couriers, transport methods, and the interactions during delivery.
You must solve this problem using object-oriented programming in C++, and your design must demonstrate the following concepts: class and object, encapsulation, inheritance, operator overloading, polymorphism, and virtual functions. You may not simply force the output with ordinary variables and ordinary functions only.
Conceptually, your program should include at least the following roles:
1. Location: represents a coordinate in the campus, with integer x and y.
2. Package: represents a package, including its ID, weight, and destination.
3. Person: represents a general person and should at least contain a name.
4. Courier: Courier must inherit from Person and represents a delivery worker. Each courier has a current location, a transport method, and information about whether the courier is carrying a package.
5. Transport: Transport should serve as the base class of transport methods and must provide at least one virtual member function.
6. BikeTransport and RobotTransport: both inherit from Transport and override at least one virtual function to demonstrate polymorphism. Your program must call the overridden function through a base-class pointer or base-class reference.
You must also design and actually use at least two overloaded operators in your program. Suggested choices are operator+ and operator== for Location. In addition, this problem provides the LIGHTER command to compare package weights. If you want, you may also design package comparison as part of your operator overloading.
The rules of the scene are as follows:
(1) Initially, several couriers are created. Each courier has a name, an initial location, and one transport type. The transport type is either BIKE or ROBOT.
(2) Then several packages are created. Each package has a unique ID, a weight, and a destination.
(3) At any time, each courier can carry at most one package.
(4) Once a package has been successfully delivered, it will never be assigned again.
(5) When the system receives an ASSIGN command, the specified package is assigned to the specified courier. If the courier is already carrying a package, the assignment fails. If the package is already being carried by another courier, the assignment also fails.
(6) When the system receives a MOVE command, the specified courier moves by a displacement (dx, dy). For the MOVE command, both transport types update the position directly according to the given displacement, meaning the new position is the old position plus (dx, dy).
(7) When the system receives a COST command, it asks for the movement cost if a given courier performs displacement (dx, dy). The cost rule is |dx| + |dy| for BikeTransport, and 2 × (|dx| + |dy|) for RobotTransport.
(8) When the system receives a DELIVER command, the specified courier attempts to deliver the package currently being carried. If the courier has no package, the delivery fails. If the courier’s current location is the same as the package destination, the delivery succeeds. Otherwise, the delivery fails.
(9) When the system receives a STATUS command, output the courier’s current position, transport type, and current package status.
(10) When the system receives a LIGHTER command, compare the weights of two packages. Output the ID of the lighter package. If the two packages have the same weight, output Equal weight.

## 輸入說明
第一行輸入兩個整數 C 與 P，分別表示配送員數量與包裹數量。
接下來 C 行，每行輸入：name type x y
其中 name 為配送員姓名，type 為運輸方式，只可能是 BIKE 或 ROBOT，x 與 y 為初始位置座標。
接下來 P 行，每行輸入：id weight dx dy
其中 id 為包裹編號，weight 為包裹重量，(dx, dy) 為包裹目的地位置。
接著輸入一個整數 Q，表示操作數量。
接下來 Q 行，每行為以下指令之一：
ASSIGN courierName packageId
MOVE courierName dx dy
COST courierName dx dy
DELIVER courierName
STATUS courierName
LIGHTER packageId1 packageId2
題目保證所有輸入格式皆正確，且出現在指令中的配送員名稱與包裹編號皆存在。
The first line contains two integers C and P, the number of couriers and the number of packages.
The next C lines each contain: name type x y
Here, name is the courier name, type is the transport type and is either BIKE or ROBOT, and x and y are the initial coordinates.
The next P lines each contain: id weight dx dy
Here, id is the package ID, weight is the package weight, and (dx, dy) is the destination location of the package.
Then an integer Q is given, the number of operations.
The following Q lines each contain one of the following commands:
ASSIGN courierName packageId
MOVE courierName dx dy
COST courierName dx dy
DELIVER courierName
STATUS courierName
LIGHTER packageId1 packageId2
It is guaranteed that all input formats are valid, and every referenced courier name and package ID exists.

## 輸出說明
對每一個操作輸出一行結果。
1. ASSIGN courierName packageId
若成功分配，輸出 Assigned package packageId to courierName
若該配送員已有包裹，輸出 courierName is already carrying a package
若該包裹已由其他配送員攜帶，輸出 Package packageId is already assigned
若該包裹已完成配送，輸出 Package packageId has already been delivered
2. MOVE courierName dx dy
輸出 courierName moved to (x, y)，其中 (x, y) 為移動後的新位置。
3. COST courierName dx dy
輸出 Cost for courierName: v，其中 v 為計算出的移動成本。
4. DELIVER courierName
若沒有包裹，輸出 courierName has no package
若成功，輸出 courierName delivered package packageId
若失敗，輸出 courierName failed to deliver package packageId
5. STATUS courierName
若未攜帶包裹，輸出 courierName at (x, y), transport: type, carrying: none
若正在攜帶包裹，輸出 courierName at (x, y), transport: type, carrying: packageId
6. LIGHTER packageId1 packageId2
若第一個較輕，輸出 Lighter package: packageId1
若第二個較輕，輸出 Lighter package: packageId2
若重量相同，輸出 Equal weight
Output one line for each operation.
1. ASSIGN courierName packageId
If assignment succeeds, output Assigned package packageId to courierName
If the courier is already carrying a package, output courierName is already carrying a package
If the package is already carried by another courier, output Package packageId is already assigned
If the package has already been delivered, output Package packageId has already been delivered
2. MOVE courierName dx dy
Output courierName moved to (x, y), where (x, y) is the new position after moving.
3. COST courierName dx dy
Output Cost for courierName: v, where v is the movement cost.
4. DELIVER courierName
If the courier has no package, output courierName has no package
If delivery succeeds, output courierName delivered package packageId
If delivery fails, output courierName failed to deliver package packageId
5. STATUS courierName
If the courier is not carrying a package, output courierName at (x, y), transport: type, carrying: none
If the courier is carrying a package, output courierName at (x, y), transport: type, carrying: packageId
6. LIGHTER packageId1 packageId2
If the first package is lighter, output Lighter package: packageId1
If the second package is lighter, output Lighter package: packageId2
If the two packages have the same weight, output Equal weight

---

## 範例測試
### 範例輸入 1
```text
2 2
Amy BIKE 0 0
Ben ROBOT 1 1
PK1 4 2 1
PK2 6 3 3
10
STATUS Amy
ASSIGN Amy PK1
COST Amy 2 1
MOVE Amy 2 1
DELIVER Amy
ASSIGN Ben PK2
COST Ben 2 2
MOVE Ben 2 2
STATUS Ben
LIGHTER PK1 PK2
```
### 範例輸出 1
```text
Amy at (0, 0), transport: BIKE, carrying: none
Assigned package PK1 to Amy
Cost for Amy: 3
Amy moved to (2, 1)
Amy delivered package PK1
Assigned package PK2 to Ben
Cost for Ben: 8
Ben moved to (3, 3)
Ben at (3, 3), transport: ROBOT, carrying: PK2
Lighter package: PK1
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <map>
#include <string>
#include <memory>
using namespace std;

class Person
{
public:
    string name;
    Person(string N) : name(N) {}
};

class Location
{
public:
    int x;
    int y;
    Location(int X, int Y) : x(X), y(Y) {}
    Location operator+(Location n)
    {
        return Location(x + n.x, y + n.y);
    }
    bool operator==(Location n)
    {
        return (x == n.x && y == n.y);
    }
    bool operator!=(Location n)
    {
        return (x != n.x || y != n.y);
    }
};

class Package
{
private:
    string id;
    int weight;
    Location destination;
    string courierName;
    bool isDelivered;

public:
    Package(string I, int W, Location D) : id(I), weight(W), destination(D), courierName(""), isDelivered(0) {}
    string getCourierName()
    {
        return courierName;
    }
    Location getDestination()
    {
        return destination;
    }
    int getWeight()
    {
        return weight;
    }
    void deliver()
    {
        isDelivered = 1;
        courierName = "";
    }
    bool getIsDeliver()
    {
        return isDelivered;
    }
    void setCourier(string name)
    {
        courierName = name;
    }
};

class Courier : public Person
{
private:
    Location location;
    string carring;

public:
    string deliveryMethod;
    Courier(string N, Location L, string M) : Person(N), location(L), deliveryMethod(M), carring("") {}
    void assighPackage(string id)
    {
        carring = id;
    }
    string getPackage()
    {
        return carring;
    }
    Location getLocation()
    {
        return location;
    }
    void move(int x, int y)
    {
        location = Location(location.x + x, location.y + y);
    }
};

class Transport
{
public:
    virtual int getCost(int x, int y) = 0;
};

class BikeTransport : public Transport
{
public:
    int getCost(int x, int y)
    {
        return abs(x) + abs(y);
    }
};

class RobotTransport : public Transport
{
public:
    int getCost(int x, int y)
    {
        return 2 * (abs(x) + abs(y));
    }
};

class DeliverySystem
{
private:
    map<string, unique_ptr<Courier>> C;
    map<string, unique_ptr<Package>> P;
    BikeTransport B;
    RobotTransport R;

public:
    void newCourier(string name, string M, int x, int y)
    {
        C.emplace(name, make_unique<Courier>(name, Location(x, y), M));
    }
    void newPackage(string id, int w, int x, int y)
    {
        P.emplace(id, make_unique<Package>(id, w, Location(x, y)));
    }
    void Assigh(string name, string id)
    {
        if (C[name]->getPackage() != "")
        {
            cout << name << " is already carrying a package" << endl;
            return;
        }
        if (P[id]->getCourierName() != "")
        {
            cout << "Package " << id << " is already assigned" << endl;
            return;
        }
        if (P[id]->getIsDeliver())
        {
            cout << "Package " << id << " has already been delivered" << endl;
            return;
        }
        C[name]->assighPackage(id);
        P[id]->setCourier(name);
        cout << "Assigned package " << id << " to " << name << endl;
    }
    void Move(string name, int x, int y)
    {
        C[name]->move(x, y);
        cout << name << " moved to (" << C[name]->getLocation().x << ", " << C[name]->getLocation().y << ")" << endl;
    }
    void Cost(string name, int x, int y)
    {
        if (C[name]->deliveryMethod == "BIKE")
        {
            cout << "Cost for " << name << ": " << B.getCost(x, y) << endl;
        }
        else if (C[name]->deliveryMethod == "ROBOT")
        {
            cout << "Cost for " << name << ": " << R.getCost(x, y) << endl;
        }
    }
    void Deliver(string name)
    {
        if (C[name]->getPackage() == "")
        {
            cout << name << " has no package" << endl;
            return;
        }
        string id = C[name]->getPackage();
        if (P[id]->getDestination() != C[name]->getLocation())
        {
            cout << name << " failed to deliver package " << id << endl;
            return;
        }
        P[id]->deliver();
        C[name]->assighPackage("");
        cout << name << " delivered package " << id << endl;
    }
    void Status(string name)
    {
        if (C[name]->getPackage() == "")
        {
            cout << name << " at (" << C[name]->getLocation().x << ", " << C[name]->getLocation().y << "), transport: " << C[name]->deliveryMethod << ", carrying: none" << endl;
        }
        else
        {
            cout << name << " at (" << C[name]->getLocation().x << ", " << C[name]->getLocation().y << "), transport: " << C[name]->deliveryMethod << ", carrying: " << C[name]->getPackage() << endl;
        }
    }
    void Lighter(string p1, string p2)
    {
        if (P[p1]->getWeight() < P[p2]->getWeight())
        {
            cout << "Lighter package: " << p1 << endl;
        }
        else if (P[p1]->getWeight() > P[p2]->getWeight())
        {
            cout << "Lighter package: " << p2 << endl;
        }
        else
        {
            cout << "Equal weight" << endl;
        }
    }
};

int main()
{
    DeliverySystem D;
    int C, P, Q;
    cin >> C >> P;
    while (C--)
    {
        string name, type;
        int x, y;
        cin >> name >> type >> x >> y;
        D.newCourier(name, type, x, y);
    }
    while (P--)
    {
        string id;
        int w, x, y;
        cin >> id >> w >> x >> y;
        D.newPackage(id, w, x, y);
    }
    cin >> Q;
    while (Q--)
    {
        string input;
        cin >> input;
        if (input == "ASSIGN")
        {
            string name, id;
            cin >> name >> id;
            D.Assigh(name, id);
        }
        else if (input == "MOVE")
        {
            string name;
            int x, y;
            cin >> name >> x >> y;
            D.Move(name, x, y);
        }
        else if (input == "COST")
        {
            string name;
            int x, y;
            cin >> name >> x >> y;
            D.Cost(name, x, y);
        }
        else if (input == "DELIVER")
        {
            string name;
            cin >> name;
            D.Deliver(name);
        }
        else if (input == "STATUS")
        {

            string name;
            cin >> name;
            D.Status(name);
        }
        else if (input == "LIGHTER")
        {
            string p1, p2;
            cin >> p1 >> p2;
            D.Lighter(p1, p2);
        }
    }
    return 0;
}
```
