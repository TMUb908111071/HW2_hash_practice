# HW2_hash_practice
## 程式碼報告
![image](https://github.com/TMUb908111071/HW2_hash_practice/assets/161851654/e1ed33f0-b4bb-495a-abc2-9540d7b7af88)
## 執行結果
![image](https://github.com/TMUb908111071/HW2_hash_practice/assets/161851654/f2ac39e6-6aea-4c4e-b04a-fa18dfdb2f00)
***
## 程式碼解釋
### 打開檔案並讀取檔案，讀取英文字串
```
f = open('hw2_data.txt', 'r')
lines = f.readlines()
```

### 統計每個英文字出現次數，去除換行符號，計算總共有多少個不重複的英文字
```
letter_count = {}
for line in lines:
    letter = line.strip()
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
unique_letters = len(letter_count)
```
### 關閉檔案
```
f.close()
```
### 輸出結果並編排輸出結果的位置
```
print("總共有", unique_letters, "個不重複的英文字：")
for letter, count in letter_count.items():
    print("%6s %5s %3s"%(letter, "出現次數：", count))
```
