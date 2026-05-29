# PR114-2-41: Question 41: The Bounded Vector Access

## 題目敘述
給定一個整數序列與一個索引 k，請模擬使用 vector::at(k) 來存取元素。若索引合法，輸出該元素；若索引超出範圍，輸出 out_of_range。本題要求你用 try-catch 接住標準函式庫的例外，而不是自己先用 if 檢查後直接輸出。
Given an integer sequence and an index k, simulate accessing the element with vector::at(k). If the index is valid, output that element. If the index is out of range, output out_of_range. You are required to use try-catch to catch the standard library exception instead of only checking the range manually.

## 輸入說明
第一行輸入 n。第二行輸入 n 個整數。第三行輸入索引 k。
The first line contains n. The second line contains n integers. The third line contains the index k.

## 輸出說明
若成功存取，輸出該元素；否則輸出 out_of_range。
If the access succeeds, output the element; otherwise output out_of_range.

---

## 範例測試
### 範例輸入 1
```text
5
10 20 30 40 50
2
```
### 範例輸出 1
```text
30
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, k;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    cin >> k;
    try
    {
        cout << v.at(k) << endl;
    }
    catch (out_of_range &e)
    {
        cout << "out_of_range" << endl;
    }
    return 0;
}
```
