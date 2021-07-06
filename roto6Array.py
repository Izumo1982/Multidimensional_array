import pandas as pd

#単純な出目
win_num = [0 for i in range(43)]

#2数字コンビネーション
win_num_2 = [[0 for i in range(43)]for j in range(43)]

#3数字コンビネーション
win_num_3 = [[[0 for i in range(43)]for j in range(43)]for k in range(43)]

print("配列3終了")
#4数字コンビネーション
win_num_4 = [[[[0 for i in range(43)]for j in range(43)]for k in range(43)]for l in range(43)]
print("配列4終了")

#5数字コンビネーション
win_num_5 = [[[[[0 for i in range(43)]for j in range(43)]for k in range(43)]for l in range(43)]for m in range(43)]
print("配列5終了")

#6数字コンビネーション
#win_num_6 = [[[[[[0 for i in range(43)]for j in range(43)]for k in range(43)]for l in range(43)]for m in range(43)]for n in range(43)]
#print("6終了")


df = pd.read_csv('loto6.csv').values.tolist()
for dat in df:
     for i in range(2,8):
         print(dat[0])
         #単純な出目
         win_num[dat[i] - 1] += 1
         for j in range(2,8):
             if dat[i] != dat[j]:
                 #2数字コンビネーション
                 win_num_2[dat[i] - 1][dat[j] - 1] += 1
                 for k in range(2,8):
                     if dat[i] != dat[k] and dat[j] != dat[k]:
                         #3数字コンビネーション
                         win_num_3[dat[i] - 1][dat[j] - 1][dat[k] - 1] += 1
                         for l in range(2,8):
                             if dat[i] != dat[l] and dat[j] != dat[l] and dat[k] != dat[l]:
                                 #4数字コンビネーション
                                 win_num_4[dat[i] - 1][dat[j] - 1][dat[k] - 1][dat[l] - 1] += 1
                                 for m in range(2,8):
                                     if dat[i] != dat[m] and dat[j] != dat[m] and dat[k] != dat[m] and dat[l] != dat[m]:
                                         #5数字コンビネーション
                                         win_num_5[dat[i] - 1][dat[j] - 1][dat[k] - 1][dat[l] - 1][dat[m] - 1] += 1
                                         #for n in range(2,8):
                                            #if dat[i] != dat[n] and dat[j] != dat[n] and dat[k] != dat[n] and dat[l] != dat[n] and dat[m] != dat[n]:
                                                 #6数字コンビネーション
                                                 #win_num_6[dat[i] - 1][dat[j] - 1][dat[k] - 1][dat[l] - 1][dat[m] - 1][dat[n] - 1] += 1
																								 #6はコメント化を解除すると処理にすごく時間が掛かります。ご注意下さい。

f2 = open('win_num_2.json', 'w')
f2.write(str(win_num_2))

f3 = open('win_num_3.json', 'w')
f3.write(str(win_num_3))

f4 = open('win_num_4.json', 'w')
f4.write(str(win_num_4))

print("ファイル出力4終了")
f5 = open('win_num_5.json', 'w')
f5.write(str(win_num_5))

print("ファイル出力5終了")
#f6 = open('win_num_6.json', 'w')
#f6.write(str(win_num_6))
#print("ファイル出力6終了")
