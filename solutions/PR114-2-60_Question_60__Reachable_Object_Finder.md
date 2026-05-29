# PR114-2-60: Question 60: Reachable Object Finder

## 題目敘述
在 Java 這類語言中，程式建立出來的物件通常由執行環境自動管理。當某些物件已經無法再從程式手上的入口參考找到時，這些物件就不再有機會被使用，系統可以把它們清除，這個過程叫做垃圾回收，簡稱 GC。 在這組題目中，我們不實作真正的 JVM，而是用一個非常簡化的小型物件世界來理解 GC 的核心想法。
現在你已經有物件、next 參考，以及單一 root。本題要做的是找出哪些物件仍然可達。所謂可達，指的是從 root 開始，順著 next 一路走，能夠抵達的所有物件。這些物件代表系統目前仍然可能使用到，因此可以視為存活物件。
本題不要求你刪除任何物件，只需要正確列出可達物件即可。若目前沒有 root，或 root 沒有指向任何存在中的物件，則沒有任何物件是可達的。
In languages such as Java, objects created by a program are usually managed automatically by the runtime. When some objects can no longer be found from the references that the program still directly holds, those objects are no longer usable and may be removed. This process is called garbage collection, or GC. In this problem set, you will not implement a real JVM. Instead, you will use a very small simplified object world to understand the core idea of GC.
Now you already have objects, next references, and one root. In this problem, you need to find which objects are still reachable. Reachable means all objects that can be reached by starting from the root and repeatedly following next. Such objects are still potentially usable by the system, so they may be considered alive.
This problem does not ask you to delete anything yet. You only need to list the reachable objects correctly. If there is currently no root, or the root does not point to any existing object, then no object is reachable.

## 輸入說明
第一行輸入整數 Q。指令可能為：NEW id、SETNEXT a b、SETROOT id、CLEARROOT、REACHABLE。
The first line contains integer Q. Commands are one of: NEW id, SETNEXT a b, SETROOT id, CLEARROOT, REACHABLE.

## 輸出說明
每個指令輸出一行結果。REACHABLE 指令要輸出 Reachable: 後接所有可達物件的 id，順序依照實際從 root 沿著 next 走訪的順序。若沒有可達物件，輸出 Reachable: none。
Print one line for each command. For the REACHABLE command, output Reachable: followed by all reachable object ids in the order actually visited by following next from the root. If no object is reachable, output Reachable: none.

---

## 範例測試
### 範例輸入 1
```text
7
NEW 1
NEW 2
NEW 3
SETNEXT 1 2
SETNEXT 2 3
SETROOT 1
REACHABLE

```
### 範例輸出 1
```text
Created object 1
Created object 2
Created object 3
Object 1 now points to 2
Object 2 now points to 3
Root now points to 1
Reachable: 1 2 3

```

### 範例輸入 2
```text
6
NEW 5
NEW 6
SETROOT 6
REACHABLE
CLEARROOT
REACHABLE

```
### 範例輸出 2
```text
Created object 5
Created object 6
Root now points to 6
Reachable: 6
Root cleared
Reachable: none

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>
#include <map>

using namespace std;

class Obj
{
private:
    int id;
    Obj *next;

public:
    Obj(int i) : id(i), next(nullptr) {}
    void SetNext(Obj *n)
    {
        next = n;
    }
    void ClearNext()
    {
        next = nullptr;
    }
    Obj *GetNext() const
    {
        return next;
    }
    int GetId() const
    {
        return id;
    }
};

class ObjectManager
{
private:
    map<int, Obj *> mp;

public:
    void New(int id)
    {
        if (!mp.count(id))
        {
            mp[id] = new Obj(id);
            cout << "Created object " << id << endl;
        }
        else
        {
            cout << "Object " << id << " already exists" << endl;
        }
    }
    void SetNext(int a, int b)
    {
        if (mp.count(a) && mp.count(b))
        {
            mp[a]->SetNext(mp[b]);
            cout << "Object " << a << " now points to " << b << endl;
        }
        else
        {
            cout << "Invalid operation" << endl;
        }
    }
    Obj *GetTarget(int id)
    {
        if (mp.count(id))
            return mp[id];
        else
            return nullptr;
    }
    ~ObjectManager()
    {
        for (auto &i : mp)
        {
            delete i.second;
        }
    }
};

class Root
{
private:
    ObjectManager *OM;
    Obj *target;

public:
    Root(ObjectManager *om) : OM(om), target(nullptr) {}
    void SetRoot(int id)
    {
        auto i = OM->GetTarget(id);
        if (i == nullptr)
        {
            cout << "Invalid operation" << endl;
        }
        else
        {
            target = i;
            cout << "Root now points to " << id << endl;
        }
    }
    void ClearRoot()
    {
        target = nullptr;
        cout << "Root cleared" << endl;
    }
    void Reachable()
    {

        if (target == nullptr)
        {
            cout << "Reachable: none" << endl;
        }
        else
        {
            cout << "Reachable: " << target->GetId();
            Obj *next = target->GetNext();
            while (next != nullptr && next != target)
            {
                cout << " " << next->GetId();
                next = next->GetNext();
            }
            cout << endl;
        }
    }
};

int main()
{
    int n;
    cin >> n;
    ObjectManager OM;
    Root root(&OM);
    while (n--)
    {
        string type;
        cin >> type;
        if (type == "NEW")
        {
            int id;
            cin >> id;
            OM.New(id);
        }
        else if (type == "SETNEXT")
        {
            int a, b;
            cin >> a >> b;
            OM.SetNext(a, b);
        }
        else if (type == "CLEARROOT")
        {
            root.ClearRoot();
        }
        else if (type == "SETROOT")
        {
            int id;
            cin >> id;
            root.SetRoot(id);
        }
        else if (type == "REACHABLE")
        {
            root.Reachable();
        }
    }
}
```
