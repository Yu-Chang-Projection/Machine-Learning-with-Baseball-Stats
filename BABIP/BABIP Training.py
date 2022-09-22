import itertools
from function import training_function

# parameters
selected_stats = ["LD%","GB%","FB%","SweetSpot%","Barrel%","HardHit%","Cent%","Oppo%","Spd","LDFB_EV"]
target_stat = "BABIP"

# run function
for i in range(2):
    for stat_combo in itertools.combinations(selected_stats,10):
        stat_combo = list(stat_combo)
        print (stat_combo)
        training_function(
            selected_stats = stat_combo,
            target_stat = target_stat,
            test_size = 0.13,
            loops = 100,
            type = "Linear"
        )