# PR114-2-59: Question 59: Root Reference Manager

## 題目敘述
在 Java 這類語言中，程式建立出來的物件通常由執行環境自動管理。當某些物件已經無法再從程式手上的入口參考找到時，這些物件就不再有機會被使用，系統可以把它們清除，這個過程叫做垃圾回收，簡稱 GC。 在這組題目中，我們不實作真正的 JVM，而是用一個非常簡化的小型物件世界來理解 GC 的核心想法。
在 GC 的概念中，root 可以理解為程式目前仍直接持有的入口參考。只要系統還握有某個 root，之後就可能從這個入口一路找到更多物件。本題在前一題的基礎上，加入一個單一 root。這個 root 不是一般物件，而是管理者額外保存的一個直接入口。
你需要支援設定 root、清除 root，以及查詢 root 目前指向哪一個物件。本題仍然不要求你找 reachable objects，也不要求你執行 GC；目標只是先理解 root 是什麼。
In languages such as Java, objects created by a program are usually managed automatically by the runtime. When some objects can no longer be found from the references that the program still directly holds, those objects are no longer usable and may be removed. This process is called garbage collection, or GC. In this problem set, you will not implement a real JVM. Instead, you will use a very small simplified object world to understand the core idea of GC.
In GC, a root can be understood as an entry reference that the program still directly holds. As long as the system still owns a root, it may continue to reach more objects from that entry. Based on Problem 1, this problem adds a single root. This root is not a normal object. It is an extra direct entry stored by the manager.
You need to support setting the root, clearing the root, and checking which object the root currently points to. This problem still does not ask you to find reachable objects or run GC. The goal is only to understand what a root is.

## 輸入說明
第一行輸入一個整數 Q。指令可能為：NEW id、SETNEXT a b、SETROOT id、CLEARROOT、SHOWROOT、SHOW id。
The first line contains an integer Q. Commands are one of: NEW id, SETNEXT a b, SETROOT id, CLEARROOT, SHOWROOT, SHOW id.

## 輸出說明
對每個指令輸出一行結果。若 SETROOT 指向不存在的物件，輸出 Invalid operation。SHOWROOT 時，若目前沒有 root，輸出 Root: none。
Output one line for each command. If SETROOT refers to a missing object, print Invalid operation. For SHOWROOT, if there is currently no root, print Root: none.

---

## 範例測試
### 範例輸入 1
```text
5
NEW 1
SETROOT 1
SHOWROOT
CLEARROOT
SHOWROOT

```
### 範例輸出 1
```text
Created object 1
Root now points to 1
Root: 1
Root cleared
Root: none

```

### 範例輸入 2
```text
6
NEW 2
NEW 3
SETNEXT 2 3
SETROOT 2
SHOW 2
SHOWROOT

```
### 範例輸出 2
```text
Created object 2
Created object 3
Object 2 now points to 3
Root now points to 2
Object 2: next = 3
Root: 2

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
    void Show(int id)
    {
        if (mp.count(id))
        {
            if (mp[id]->GetNext() == nullptr)
            {
                cout << "Object " << id << ": next = none" << endl;
            }
            else
            {
                cout << "Object " << id << ": next = " << mp[id]->GetNext()->GetId() << endl;
            }
        }
        else
        {
            cout << "Object " << id << " not found" << endl;
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
    void ShowRoot()
    {
        if (target == nullptr)
        {
            cout << "Root: none" << endl;
        }
        else
        {
            cout << "Root: " << target->GetId() << endl;
        }
    }
    void ClearRoot()
    {
        target = nullptr;
        cout << "Root cleared" << endl;
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
        else if (type == "SHOWROOT")
        {
            root.ShowRoot();
        }
        else if (type == "SHOW")
        {
            int id;
            cin >> id;
            OM.Show(id);
        }
    }
}
```
