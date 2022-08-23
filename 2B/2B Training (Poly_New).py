from runc import training_function
import itertools


# parameters
selected_stats = ["FB%","LD%","HR/FB","Pull%","Barrel%","HardHit%","LDFB_EV"]
target_stat = "HR%"

# run function
for stat_combo in itertools.combinations(selected_stats,7):
    stat_combo = list(stat_combo)
    print(stat_combo)
    for t in range(1):
        training_function(
            selected_stats = stat_combo,
            target_stat = target_stat,
            loops = 50,
            type = "P"
        )