f = open('hw2_data.txt', 'r')                           # 打開檔案
lines = f.readlines()                                   # 讀取檔案，逐行讀取英文字串

letter_count = {}                                       # 初始化計數器

for line in lines:                                      # 統計每個英文字出現次數
    letter = line.strip()                               # 去除換行符號
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

unique_letters = len(letter_count)                      # 計算總共有多少個不重複的英文字

f.close()                                               # 關閉檔案


print("總共有", unique_letters, "個不重複的英文字：")   # 輸出結果
for letter, count in letter_count.items():
    print("%6s %5s %3s"%(letter, "出現次數：", count))  # 輸出結果並編排輸出結果的位置