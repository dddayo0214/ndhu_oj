# PR114-2-58: Question 58: Object Creation and Next Reference

## 題目敘述
在 Java 這類語言中，程式建立出來的物件通常由執行環境自動管理。當某些物件已經無法再從程式手上的入口參考找到時，這些物件就不再有機會被使用，系統可以把它們清除，這個過程叫做垃圾回收，簡稱 GC。 在這組題目中，我們不實作真正的 JVM，而是用一個非常簡化的小型物件世界來理解 GC 的核心想法。
本題是整組題目的第一步。先不要考慮 root，也不要執行 GC。你只需要建立一個 ObjectManager，用來保存所有已建立的物件。每個物件只有兩個狀態：自己的編號 id，以及 next 參考。next 表示這個物件目前指向哪一個下一個物件；若沒有指向任何物件，則 next 為 none。
你必須使用 C++ 的物件導向方式完成本題。建議至少設計一個表示單一物件的類別，以及一個保存所有物件的管理者類別。所有 NEW、SETNEXT、CLEARNEXT、SHOW、COUNT 指令都應由管理者負責處理。
In languages such as Java, objects created by a program are usually managed automatically by the runtime. When some objects can no longer be found from the references that the program still directly holds, those objects are no longer usable and may be removed. This process is called garbage collection, or GC. In this problem set, you will not implement a real JVM. Instead, you will use a very small simplified object world to understand the core idea of GC.
This is the first step of the whole problem set. Do not consider roots yet, and do not run GC yet. You only need to build an ObjectManager that stores every created object. Each object has only two states: its own id and one next reference. The next reference means which object this object currently points to. If it points to nothing, then next is none.
You must solve this problem using object-oriented programming in C++. It is recommended that you design at least one class for a single object and one manager class that stores all objects. All commands NEW, SETNEXT, CLEARNEXT, SHOW, and COUNT should be handled by the manager.

## 輸入說明
第一行輸入一個整數 Q，表示操作數量。接下來 Q 行，每行是一個指令。指令可能為：NEW id、SETNEXT a b、CLEARNEXT a、SHOW id、COUNT。
The first line contains an integer Q, the number of operations. The next Q lines each contain one command. A command is one of: NEW id, SETNEXT a b, CLEARNEXT a, SHOW id, COUNT.

## 輸出說明
對每個指令輸出一行結果。若操作成功，依照題目格式輸出對應訊息。若 SETNEXT 或 CLEARNEXT 的目標物件不存在，輸出 Invalid operation。SHOW 不存在的物件時，輸出 Object [id] not found。
Output one line for each command. If an operation succeeds, print the corresponding message in the required format. If SETNEXT or CLEARNEXT refers to a missing object, print Invalid operation. If SHOW refers to a missing object, print Object [id] not found.

---

## 範例測試
### 範例輸入 1
```text
5
NEW 1
NEW 2
SETNEXT 1 2
SHOW 1
COUNT

```
### 範例輸出 1
```text
Created object 1
Created object 2
Object 1 now points to 2
Object 1: next = 2
Object count: 2

```

### 範例輸入 2
```text
5
NEW 5
SHOW 5
CLEARNEXT 5
SHOW 5
COUNT

```
### 範例輸出 2
```text
Created object 5
Object 5: next = none
Object 5 now points to none
Object 5: next = none
Object count: 1

```

### 範例輸入 3
```text
4
NEW 3
NEW 3
SHOW 7
COUNT

```
### 範例輸出 3
```text
Created object 3
Object 3 already exists
Object 7 not found
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
    void Count()
    {
        cout << "Object count: " << mp.size() << endl;
    }
    ~ObjectManager()
    {
        for (auto &i : mp)
        {
            delete i.second;
        }
    }
};

int main()
{
    int n;
    cin >> n;
    ObjectManager OM;
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
        else if (type == "SHOW")
        {
            int id;
            cin >> id;
            OM.Show(id);
        }
        else if (type == "COUNT")
        {
            OM.Count();
        }
    }
}
```
