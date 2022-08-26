import itertools
from function import training_function

# parameters
selected_stats = ["FB%","GB%","LD%","SweetSpot%","Barrel%","HardHit%","LDFB_EV","Pull%","Cent%","Oppo%"]
target_stat = "ISO"

# run function
for i in range(1):
    for stat_combo in itertools.combinations(selected_stats,10):
        stat_combo = list(stat_combo)
        print (stat_combo)
        training_function(
            selected_stats = stat_combo,
            target_stat = target_stat,
            test_size = 0.12,
            loops = 100,
            type = "Linear"
        )