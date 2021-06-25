import numpy as np
from numpy import inf
import time

#girdilerimiz
start = time.time()
d = np.array(    [[0, 82, 34, 127, 118, 46, 110, 127, 52, 44],
                  [82, 0, 76, 83, 99, 89, 106, 83, 84, 33],
                  [34, 76, 0, 127, 74, 44, 56, 106, 94, 86],
                  [127, 83, 127, 0, 37, 51, 118, 106, 124, 99],
                 [118, 99, 74, 37, 0, 91, 37, 132 ,49, 37],
                 [46, 89, 44, 51, 91, 0, 112, 131, 66, 85],
                  [110, 106, 56, 118, 37, 112, 0, 64, 121, 71],
            [127, 83, 106, 106, 132, 131, 64, 0, 43, 107],
            [52, 84, 94, 124, 49, 66, 121, 43, 0, 89],
            [44, 33, 86, 99, 37, 85, 71, 107, 89, 0]]
            )

iteration = 1000
n_ants = 10
n_citys = 10
# alpha ve betayı 1 olarak veriyoruz
m = n_ants
n = n_citys
e = .5  # evaporation rate
alpha = 1  # pheromone factor
beta = 1  # visibility factor
#  sonraki sehir  gorunurlulugunu hesaplama kısmı (i, j) = 1 / d (i, j)
visibility = 1 / d
visibility[visibility == inf] = 0
# sehirlere giden yollarda mevcut olan feromonu başlatmak
pheromne = .1 * np.ones((m, n))
rute = np.ones((m, n + 1))

for ite in range(iteration):

    rute[:, 0] = 1

    for i in range(m):

        temp_visibility = np.array(visibility)

        for j in range(n - 1):
            # print(rute)
            combine_feature = np.zeros(5)
            cum_prob = np.zeros(5)
            cur_loc = int(rute[i, j] - 1)  #karincanın suanki sehri
            temp_visibility[:, cur_loc] = 0  #simdiki sehrin gorunurlulugunu sifir yapiyoruz
            p_feature = np.power(pheromne[cur_loc, :], beta)  # feremonu hesaplama
            v_feature = np.power(temp_visibility[cur_loc, :], alpha)
            p_feature = p_feature[:, np.newaxis]
            v_feature = v_feature[:, np.newaxis]
            combine_feature = np.multiply(p_feature, v_feature)
            total = np.sum(combine_feature)
            probs = combine_feature / total
            cum_prob = np.cumsum(probs)
            # print(cum_prob)
            r = np.random.random_sample()
            # print(r)
            city = np.nonzero(cum_prob > r)[0][0] + 1
            # print(city)
            rute[i, j + 1] = city  # rotaya sehri eklemek

        left = list(set([i for i in range(1, n + 1)]) - set(rute[i, :-2]))[
            0]
        rute[i, -2] = left
    rute_opt = np.array(rute)
    dist_cost = np.zeros((m, 1))

    for i in range(m):

        s = 0
        for j in range(n - 1):
            s = s + d[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1]
        dist_cost[i] = s

    dist_min_loc = np.argmin(dist_cost)
    dist_min_cost = dist_cost[dist_min_loc]
    best_route = rute[dist_min_loc, :]
    pheromne = (1 - e) * pheromne

    for i in range(m):
        for j in range(n - 1):
            dt = 1 / dist_cost[i]
            pheromne[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1] = pheromne[int(rute_opt[i, j]) - 1, int(
                rute_opt[i, j + 1]) - 1] + dt



print('route of all the ants at the end :')
print(rute_opt)
print()
print('best path :', best_route)
print('cost of the best path', int(dist_min_cost[0]) + d[int(best_route[-2]) - 1, 0])
end = time.time()
print("time" ,end - start)