# PR114-2-62: Question 62: Mini Java-Style GC Simulator

## 題目敘述
在 Java 這類語言中，程式建立出來的物件通常由執行環境自動管理。當某些物件已經無法再從程式手上的入口參考找到時，這些物件就不再有機會被使用，系統可以把它們清除，這個過程叫做垃圾回收，簡稱 GC。 在這組題目中，我們不實作真正的 JVM，而是用一個非常簡化的小型物件世界來理解 GC 的核心想法。
本題是整組題目的完整模擬器。你需要整合前面所有功能：建立物件、設定 next、設定或清除 root、查詢物件是否存在、執行 GC，並輸出目前整個物件空間的狀態。
這個簡化模型並不等於真正的 Java 虛擬機器，但它已經包含了 GC 最重要的核心觀念：系統保存了所有已建立的物件；root 是系統直接持有的入口；從 root 可達的物件仍然存活；不可達的物件可被回收。
In languages such as Java, objects created by a program are usually managed automatically by the runtime. When some objects can no longer be found from the references that the program still directly holds, those objects are no longer usable and may be removed. This process is called garbage collection, or GC. In this problem set, you will not implement a real JVM. Instead, you will use a very small simplified object world to understand the core idea of GC.
This problem is the full simulator of the whole problem set. You need to combine all previous features: create objects, set next, set or clear the root, check whether an object exists, run GC, and print the current state of the whole object space.
This simplified model is not a real Java Virtual Machine, but it already contains the most important GC ideas: the system stores all created objects, the root is the direct entry held by the system, objects reachable from the root remain alive, and unreachable objects may be collected.

## 輸入說明
第一行輸入整數 Q。指令可能為：NEW id、SETNEXT a b、CLEARNEXT a、SETROOT id、CLEARROOT、CHECK id、GC、STATUS。
The first line contains integer Q. Commands are one of: NEW id, SETNEXT a b, CLEARNEXT a, SETROOT id, CLEARROOT, CHECK id, GC, STATUS.

## 輸出說明
STATUS 時，第一行輸出目前所有存在的物件與其 next 狀態，格式為 Objects: id->next, id->next, ...，物件依 id 遞增排列；若沒有任何物件，輸出 Objects: none。第二行輸出 Root: x 或 Root: none。
For STATUS, print the current existing objects and their next states in the format Objects: id->next, id->next, ..., sorted by increasing id. If there is no object, print Objects: none. On the second line, print Root: x or Root: none.

---

## 範例測試
### 範例輸入 1
```text
7
NEW 1
NEW 2
SETNEXT 1 2
SETROOT 1
STATUS
GC
STATUS

```
### 範例輸出 1
```text
Created object 1
Created object 2
Object 1 now points to 2
Root now points to 1
Objects: 1->2, 2->none
Root: 1
Collected: none
Objects: 1->2, 2->none
Root: 1

```

### 範例輸入 2
```text
4
NEW 5
CHECK 5
CHECK 7
STATUS

```
### 範例輸出 2
```text
Created object 5
Object 5 exists
Object 7 not found
Objects: 5->none
Root: none

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
    void ClearNext(int a)
    {
        if (mp.count(a))
        {
            mp[a]->ClearNext();
            cout << "Object " << a << " now points to none" << endl;
        }
        else
        {
            cout << "Invalid operation" << endl;
        }
    }
    void Count() const
    {
        cout << "Object count: " << mp.size() << endl;
    }
    map<int, int> Collect(map<int, int> m)
    {
        map<int, int> mm;
        for (auto it = mp.begin(); it != mp.end();)
        {
            if (!m.count(it->first))
            {
                mm[it->first] = 1;
                delete it->second;
                it = mp.erase(it);
            }
            else
            {
                it++;
            }
        }
        return mm;
    }
    void CollectAll()
    {
        cout << "Collected:";
        for (auto &i : mp)
        {
            cout << " " << i.first;
        }
        cout << endl;
        mp.clear();
    }
    void Check(int id)
    {
        if (mp.count(id))
        {
            cout << "Object " << id << " exists" << endl;
        }
        else
        {
            cout << "Object " << id << " not found" << endl;
        }
    }
    int GetSize()
    {
        return mp.size();
    }
    void Status()
    {
        if (!mp.size())
        {
            cout << "Objects: none" << endl;
            return;
        }
        cout << "Objects: ";
        for (auto it = mp.begin(); it != mp.end(); it++)
        {
            auto next = it->second->GetNext();
            if (it == mp.begin())
            {
                if (next == nullptr)
                {
                    cout << it->first << "->none";
                }
                else
                {
                    cout << it->first << "->" << next->GetId();
                }
            }
            else
            {
                if (next == nullptr)
                {
                    cout << ", " << it->first << "->none";
                }
                else
                {
                    cout << ", " << it->first << "->" << next->GetId();
                }
            }
        }
        cout << endl;
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
    void Gc()
    {
        map<int, int> m;
        if (target != nullptr)
        {
            m[target->GetId()] = 1;
            Obj *next = target->GetNext();
            while (next != nullptr && next != target)
            {
                m[next->GetId()] = 1;
                next = next->GetNext();
            }
            if (m.size() == OM->GetSize())
            {
                cout << "Collected: none" << endl;
                return;
            }
            m = OM->Collect(m);
            cout << "Collected:";
            for (auto &i : m)
            {
                cout << " " << i.first;
            }
            cout << endl;
        }
        else
        {
            OM->CollectAll();
        }
    }
    void GetRoot()
    {
        if (target != nullptr)
            cout << "Root: " << target->GetId() << endl;
        else
            cout << "Root: none" << endl;
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
        else if (type == "CLEARNEXT")
        {
            int a;
            cin >> a;
            OM.ClearNext(a);
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
        else if (type == "CHECK")
        {
            int id;
            cin >> id;
            OM.Check(id);
        }
        else if (type == "GC")
        {
            root.Gc();
        }
        else if (type == "STATUS")
        {
            OM.Status();
            root.GetRoot();
        }
    }
}
```
