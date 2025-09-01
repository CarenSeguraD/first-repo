print("")

LOL_dict = {"name": "Caren", "Position": "Support",
            "Main Champion": "Seraphine"}

LOL_times_playeded_champs = {"Seraphine": 24,
                             "Janna": 4, "Lulu": 27, "Nami": 44}
print(LOL_times_playeded_champs)
LOL_dict.update({"name": "Caren Segura"})
print("")

average = sum(LOL_times_playeded_champs.values()) / \
    len(LOL_times_playeded_champs)

print("Average times played:", average)
print("")
print(f"Main role: {LOL_dict["Position"]}")
