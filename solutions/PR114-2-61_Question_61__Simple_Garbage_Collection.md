# PR114-2-61: Question 61: Simple Garbage Collection

## 題目敘述
在 Java 這類語言中，程式建立出來的物件通常由執行環境自動管理。當某些物件已經無法再從程式手上的入口參考找到時，這些物件就不再有機會被使用，系統可以把它們清除，這個過程叫做垃圾回收，簡稱 GC。 在這組題目中，我們不實作真正的 JVM，而是用一個非常簡化的小型物件世界來理解 GC 的核心想法。
本題正式進入簡化版垃圾回收。當你執行 GC 時，系統應先找出所有從 root 可達的物件，然後把其餘不可達的物件全部回收。所謂回收，就是把這些物件從管理者保存的物件容器中刪除。
本題的 GC 採用最簡化的想法：可達的保留，不可達的刪除。你不需要處理真正 JVM 的細節，只要正確完成這個簡化模型即可。
In languages such as Java, objects created by a program are usually managed automatically by the runtime. When some objects can no longer be found from the references that the program still directly holds, those objects are no longer usable and may be removed. This process is called garbage collection, or GC. In this problem set, you will not implement a real JVM. Instead, you will use a very small simplified object world to understand the core idea of GC.
This problem enters simplified garbage collection. When you run GC, the system should first find all objects reachable from the root, and then collect every unreachable object. Here, collect simply means removing those objects from the manager's object container.
The GC in this problem uses the most simplified idea: keep reachable objects and delete unreachable objects. You do not need to deal with real JVM details. You only need to complete this simplified model correctly.

## 輸入說明
第一行輸入整數 Q。指令可能為：NEW id、SETNEXT a b、SETROOT id、CLEARROOT、GC、COUNT。
The first line contains integer Q. Commands are one of: NEW id, SETNEXT a b, SETROOT id, CLEARROOT, GC, COUNT.

## 輸出說明
GC 指令需輸出 Collected: 後接本次被回收的物件 id，並以遞增順序輸出。若沒有物件被回收，輸出 Collected: none。COUNT 指令輸出目前容器中仍存在的物件數量。
For the GC command, output Collected: followed by the ids collected in this run, in increasing order. If no object is collected, output Collected: none. The COUNT command outputs how many objects still remain in the container.

---

## 範例測試
### 範例輸入 1
```text
7
NEW 1
NEW 2
NEW 3
SETNEXT 1 2
SETROOT 1
GC
COUNT

```
### 範例輸出 1
```text
Created object 1
Created object 2
Created object 3
Object 1 now points to 2
Root now points to 1
Collected: 3
Object count: 2

```

### 範例輸入 2
```text
5
NEW 5
NEW 6
SETROOT 5
GC
COUNT

```
### 範例輸出 2
```text
Created object 5
Created object 6
Root now points to 5
Collected: 6
Object count: 1

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
    int GetSize()
    {
        return mp.size();
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
        else if (type == "COUNT")
        {
            OM.Count();
        }
        else if (type == "GC")
        {
            root.Gc();
        }
    }
}
```
