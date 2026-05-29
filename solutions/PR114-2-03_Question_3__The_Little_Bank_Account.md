# PR114-2-03: Question 3: The Little Bank Account

## 題目敘述
請想像建立一個**BankAccount**類別，帳戶一開始有一筆初始金額。
接著會有若干次操作，每次操作可能是存款或提款：
**deposit x**：存入 x 元**withdraw x**：提出 x 元請在所有操作結束後，輸出帳戶餘額。
你可以把餘額設計成 private，並透過 public method 進行修改。
Imagine creating a**BankAccount**class. The account starts with an initial balance.
Then there are several operations:
**deposit x**: deposit x dollars**withdraw x**: withdraw x dollarsAfter all operations, output the final balance.
You may store the balance as a private member and modify it through public methods.

## 輸入說明
第一行有兩個整數**balance n**，代表初始金額與操作次數。
接下來**n**行，每行為一個操作，格式為：
**deposit x**或**withdraw x**
The first line contains two integers**balance n**, the initial balance and the number of operations.
The next**n**lines each contain an operation in one of the following forms:
**deposit x**or**withdraw x**

## 輸出說明
輸出一行：**Balance: X**，其中**X**為最後餘額。
Output one line:**Balance: X**, where**X**is the final balance.

---

## 範例測試
### 範例輸入 1
```text
100 3
deposit 50
withdraw 20
deposit 10
```
### 範例輸出 1
```text
Balance: 140
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

class BankAccount
{
private:
    int balance;

public:
    BankAccount(int initialBalance) : balance(initialBalance) {}
    int getBalance()
    {
        return balance;
    }
    void setBalance(int b)
    {
        balance = b;
    }
};

int main()
{
    int balance, n;
    std::cin >> balance >> n;
    BankAccount account(balance);
    std::string motion;
    int money;
    for (int i = 0; i < n; i++)
    {
        std::cin >> motion >> money;
        if (motion == "deposit")
        {
            account.setBalance(account.getBalance() + money);
        }
        else if (motion == "withdraw")
        {
            account.setBalance(account.getBalance() - money);
        }
    }
    std::cout << "Balance: " << account.getBalance() << std::endl;
    return 0;
}
```
