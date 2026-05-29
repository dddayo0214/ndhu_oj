# PR114-2-29: Question 29: The Vending Machine Scene

## 題目敘述
在校園角落有一台自動販賣機。學生會投幣、購買商品，或要求退幣。你需要用程式描述這個場景中的互動。
Product 代表一種商品，至少應包含名稱、價格與庫存。 Customer 代表一位使用者，至少應包含名字與目前已投入販賣機的金額。 VendingMachine 代表整台機器，負責管理商品、接收投幣、處理購買與退幣。
規則如下。INSERT name amount 表示某位顧客投入 amount 元。BUY name product 只有在商品存在、庫存足夠且顧客餘額足夠時才成功，成功後扣除商品價格並使庫存減一。若商品不存在或庫存為 0，輸出 unavailable。若餘額不足，輸出 insufficient funds。REFUND name 會退還該顧客目前餘額，並將餘額清為 0。
你必須使用物件導向方式作答，請以類別與成員函式描述 Product、Customer 與 VendingMachine 的互動。不得只用一般變數模擬。
There is a vending machine in a corner of the campus. Students can insert money, buy products, or request a refund. You need to describe the interaction in this scene.
A Product represents one kind of item and should at least include a name, a price, and a stock count. A Customer represents one user and should at least include a name and the amount of money currently inserted. A VendingMachine represents the whole machine and manages products, accepts money, handles purchases, and returns refunds.
The rules are as follows. INSERT name amount means that a customer inserts amount units of money. BUY name product succeeds only when the product exists, has stock available, and the customer has enough balance. On success, the product price is deducted from the customer's balance and the stock decreases by one. If the product does not exist or has no stock, output unavailable. If the balance is not enough, output insufficient funds. REFUND name returns the customer's current balance and resets it to 0.
You must solve this problem using object-oriented programming. Use classes and member functions to describe the interaction among Product, Customer, and VendingMachine. Do not simulate the whole problem using only ordinary variables.
1 ≤ P ≤ 50，1 ≤ Q ≤ 200。價格、庫存與投入金額皆為正整數。
1 ≤ P ≤ 50, 1 ≤ Q ≤ 200. Prices, stocks, and inserted amounts are positive integers.

## 輸入說明
第一行輸入兩個整數 P 與 Q，代表商品種類數與操作次數。
接著 P 行，每行輸入 product price stock。
再接著 Q 行，每行為 INSERT name amount、BUY name product、REFUND name 或 STATUS。
The first line contains two integers P and Q, the number of product types and the number of operations.
The next P lines each contain product price stock.
The next Q lines are operations in one of the following forms: INSERT name amount, BUY name product, REFUND name, or STATUS.

## 輸出說明
對每個操作輸出一行。
INSERT 輸出「name balance X」。
BUY 成功輸出「name bought product」，商品不可買輸出「product unavailable」，餘額不足輸出「name insufficient funds」。
REFUND 輸出「name refund X」。
STATUS 輸出「Items with stock: X」。
Output one line for each operation.
For INSERT, output "name balance X".
If BUY succeeds, output "name bought product". If the product cannot be bought because it does not exist or is out of stock, output "product unavailable". If the balance is not enough, output "name insufficient funds".
For REFUND, output "name refund X".
For STATUS, output "Items with stock: X".

---

## 範例測試
### 範例輸入 1
```text
3 8
Tea 20 2
Soda 25 1
Water 10 3
STATUS
INSERT Amy 15
BUY Amy Tea
INSERT Amy 10
BUY Amy Tea
STATUS
REFUND Amy
STATUS
```
### 範例輸出 1
```text
Items with stock: 3
Amy balance 15
Amy insufficient funds
Amy balance 25
Amy bought Tea
Items with stock: 3
Amy refund 5
Items with stock: 3
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

using namespace std;

class Product
{
public:
    string name;
    int price;
    int stock;

    Product(string n, int p, int s) : name(n), price(p), stock(s) {}

    bool isAvailable()
    {
        return stock > 0;
    }

    void decreaseStock()
    {
        if (stock > 0)
            stock--;
    }
};

class Customer
{
public:
    string name;
    int balance;

    Customer(string n) : name(n), balance(0) {}

    void insertMoney(int amount)
    {
        balance += amount;
    }

    bool canAfford(int price)
    {
        return balance >= price;
    }

    void deduct(int price)
    {
        balance -= price;
    }

    int refund()
    {
        int temp = balance;
        balance = 0;
        return temp;
    }
};

class VendingMachine
{
private:
    Product *products[55];
    Customer *customers[255];
    int productCount = 0;
    int customerCount = 0;

public:
    void addProduct(string name, int price, int stock)
    {
        if (productCount < 55)
        {
            products[productCount++] = new Product(name, price, stock);
        }
    }

    Customer *getCustomer(string name)
    {
        for (int i = 0; i < customerCount; i++)
        {
            if (customers[i]->name == name)
                return customers[i];
        }
        Customer *newCust = new Customer(name);
        customers[customerCount++] = newCust;
        return newCust;
    }

    Product *getProduct(string name)
    {
        for (int i = 0; i < productCount; i++)
        {
            if (products[i]->name == name)
                return products[i];
        }
        return nullptr;
    }

    void insert(string name, int amount)
    {
        Customer *c = getCustomer(name);
        c->insertMoney(amount);
        cout << name << " balance " << c->balance << endl;
    }

    void buy(string name, string productName)
    {
        Customer *c = getCustomer(name);
        Product *p = getProduct(productName);

        if (p == nullptr || !p->isAvailable())
        {
            cout << productName << " unavailable" << endl;
            return;
        }

        if (!c->canAfford(p->price))
        {
            cout << name << " insufficient funds" << endl;
            return;
        }

        c->deduct(p->price);
        p->decreaseStock();
        cout << name << " bought " << productName << endl;
    }

    void refund(string name)
    {
        Customer *c = getCustomer(name);
        cout << name << " refund " << c->refund() << endl;
    }

    void status()
    {
        int count = 0;
        for (int i = 0; i < productCount; i++)
        {
            if (products[i]->stock > 0)
                count++;
        }
        cout << "Items with stock: " << count << endl;
    }
};

int main()
{
    int P, Q;
    VendingMachine vm;
    cin >> P >> Q;
    while (P--)
    {
        string name;
        int price, stock;
        cin >> name >> price >> stock;
        vm.addProduct(name, price, stock);
    }

    while (Q--)
    {
        string input;
        cin >> input;
        if (input == "INSERT")
        {
            string name;
            int amount;
            cin >> name >> amount;
            vm.insert(name, amount);
        }
        else if (input == "BUY")
        {
            string name, prod;
            cin >> name >> prod;
            vm.buy(name, prod);
        }
        else if (input == "REFUND")
        {
            string name;
            cin >> name;
            vm.refund(name);
        }
        else
        {
            vm.status();
        }
    }

    return 0;
}
```
