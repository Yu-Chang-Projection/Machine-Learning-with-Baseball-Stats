import itertools
from function import training_function

# parameters
selected_stats = ["LA","FB%","LD%","HR/FB","Pull%","Barrel%","HardHit%","LDFB_EV"]
target_stat = "HR%"

# run function
for i in range(2):
    for stat_combo in itertools.combinations(selected_stats,8):
        stat_combo = list(stat_combo)
        print (stat_combo)
        training_function(
            selected_stats = stat_combo,
            target_stat = target_stat,
            test_size = 0.12,
            loops = 100,
            type = "Poly"
        )