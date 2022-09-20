import itertools
from function import training_function

# parameters
selected_stats = ["FB%","GB%","LD%","SweetSpot%","Pull%","Cent%","Oppo%","Barrel%","HardHit%","LDFB_EV","Spd","UBR"]
target_stat = "2B%"

# run function
for i in range(5):
    for stat_combo in itertools.combinations(selected_stats,12):
        stat_combo = list(stat_combo)
        print (stat_combo)
        training_function(
            selected_stats = stat_combo,
            target_stat = target_stat,
            test_size = 0.13,
            loops = 100,
            type = "Poly"
        )