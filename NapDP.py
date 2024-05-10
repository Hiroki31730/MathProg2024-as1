import time 

#動的計画を用いた関数作成
def knapsackDP(values, weights, capacity):
    N = len(values)
    dp = [[0]*(capacity+1) for i in range(N+1)] #配列作成
    
    #i番目以下で最大になるように配列に配置していく
    for i in range(N):
        for j in range(capacity+1):
            if j < weights[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-weights[i]]+values[i])
            
    
    max_number = dp[N][capacity]
    combination_list = []
    combination_list_w = []
    combination_list_v = []
    
    #価値が最大の時、20個の荷物について選択されているかをYes,Noで表し、リストに追加
    for x in range(N, 0, -1):
        if dp[x][capacity] != dp[x-1][capacity]:
            combination_list.append("Yes")
            capacity -= weights[x - 1]
            
        else:
            combination_list.append("No")
            
    #20番目から処理を始めているので、リストを逆転させて降順にする
    combination_list.reverse()
    
    #選択された荷物の重さ、価値を表示できるようにリストに追加
    for y in range(len(combination_list)):
        if combination_list[y] == "Yes":
            combination_list_w.append(weights[y])
            combination_list_v.append(values[y])
        else:
            continue
            
        
    
    
    return max_number, combination_list_w, combination_list_v
    
    
#荷物の価値、重さ、限界容量の設定
values =  [7,12,9,7,13,8,4,5,3,10,7,5,6,14, 5,9, 6,12,5,9]
weights = [3, 6,5,4, 8,5,3,4,3, 5,6,4,8, 7,11,8,14,6,12,4]
capacity = 55

#計測開始
start = time.time()

best_value2, best_combination_w2, best_combination_v2 = knapsackDP(values, weights, capacity)
print("組み合わせ(重さ):", best_combination_w2)
print("組み合わせ(価値)", best_combination_v2)
print("最も高い価値:", best_value2)

#計測終了
end = time.time()

result_time = end - start
print(result_time) #時間表示