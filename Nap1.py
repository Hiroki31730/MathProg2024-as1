import time

#ナップサック問題を総当たりで解く関数
def knapsack(values, weights, capacity):
    n = len(values)
    best_value = 0
    best_combination_w = None
    best_combination_v = None
    
    #それぞれの荷物を入れるかどうかを0,1で表すと2**nのパターンがある
    for i in range(2**n):
        combination_w = []
        combination_v = []
        total_weight = 0
        total_value = 0
        
        for j in range(n):
            #荷物を入れるかどうかを確認する
            if (i >> j) & 1:
                combination_w.append(weights[j])
                combination_v.append(values[j])
                total_weight += weights[j]
                total_value += values[j]
        
        # ナップサックの容量を超えないかつ価値が最大かどうかをチェック
        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_combination_w = combination_w
            best_combination_v = combination_v
    
    return best_value, best_combination_w, best_combination_v


#荷物の価値、重さ、限界容量の設定
values = [7, 12, 9, 7, 13, 8, 4, 5]
weights = [3, 6, 5, 4, 8, 5, 3, 4]
capacity = 25

#計測開始
start = time.time()

best_value, best_combination_w, best_combination_v = knapsack(values, weights, capacity)
print("組み合わせ(重さ):", best_combination_w)
print("組み合わせ(価値)", best_combination_v)
print("最も高い価値:", best_value)

#計測終了
end = time.time()

result_time = end - start
print(result_time) #時間表示
