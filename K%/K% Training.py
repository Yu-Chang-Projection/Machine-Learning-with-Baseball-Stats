import itertools
from function import training_function

# parameters
selected_stats = ["O-Swing%","O-Contact%","Z-Swing%","Z-Contact%","Zone%","F-Strike%","SwStr%","CSW%","M-Swing%","Meat%","Edge%","Fair/Foul ratio"]
target_stat = "K%"

# run function
for i in range(10):
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