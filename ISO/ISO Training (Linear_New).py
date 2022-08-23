import itertools
from function import training_function


# parameters
selected_stats = ["FB%","GB%","LD%","SweetSpot%","Barrel%","HardHit%","LDFB_EV","Pull%","Cent%","Oppo%","Spd"]
target_stat = "ISO"

# run function
for i in range(10,30):
    for stat_combo in itertools.combinations(selected_stats,11):
        stat_combo = list(stat_combo)
        print(i/100)
        training_function(
            selected_stats = stat_combo,
            target_stat = target_stat,
            test_size = i/100,
            loops = 100,
            type = "L"
        )