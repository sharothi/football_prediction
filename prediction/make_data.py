import pandas as pd
from .models import TeamName


file_path='matches.csv'



def read_csv(file_path):
    # print(file_path)
    matches = pd.read_csv(file_path)
    name_of_teams = matches["team"]
    # print(name_of_teams)
    for team in name_of_teams:
        try:
            TeamName.objects.create(
                team = team
            )
        except:
            continue
    return None




def organize_data(file_path):
    matches = pd.read_csv(file_path)
    matches.head()
    matches["date"] = pd.to_datetime(matches["date"])
    matches["vanue_code"] = matches["venue"].astype("category").cat.codes
    matches["opp_code"] = matches["opponent"].astype("category").cat.codes
    matches["hour"] = matches["time"].str.replace(":.+","",regex=True).astype("int")
    matches["day_code"] = matches["date"].dt.dayofweek
    matches["target"] = (matches["result"] == "W").astype("int")
    grouped_matches = matches.groupby("team")
    return grouped_matches



# def rolling_averages(group, cols, new_cols):
#     group =  group.sort_values("date")
#     rolling_stats = group[cols].rolling(3, closed='left').mean()
#     group[new_cols] = rolling_stats
#     group = group.dropna(subset = new_cols)
#     return group


# cols = ["gf", "ga", "sh", "sot", "dist", "fk", "pk", "pkatt"]
# new_cols = [f"{c}_rolling" for c in cols]


# team1 = rolling_averages(group_1, cols, new_cols)
# team_name = "Manchester City"
# group_1 = grouped_matches.get_group(team_name)
# group_1 = grouped_matches.get_group(team_name)
# group_2 = grouped_matches.get_group("Arsenal")  
# team2 = rolling_averages(group_2, cols, new_cols)



def get_features_for_team(team_name,file_path):
    grouped_matches = organize_data(file_path)
    historical_data = grouped_matches.get_group(team_name)
    goals_scored = historical_data["gf"].mean()
    goals_conceded = historical_data["ga"].mean()
    win_percentage = historical_data["result"].value_counts()["W"]/len(historical_data)
    return [goals_scored,goals_conceded,win_percentage]


# res1 = get_features_for_team(team1)

# res2 = get_features_for_team(team2)

def difference_betwen_two_team(team_name,oponent,file_path):
    grouped_matches = organize_data(file_path)
    historical_data = grouped_matches.get_group(team_name)
    data = historical_data[historical_data["opponent"] == oponent]
    total_matches = len(data)
    win_percentage = 0
    win_matches = 0
    draw_matchs = 0
    loss_matchs = 0
    if total_matches:
        try:
            win_matches = data["result"].value_counts()["W"]
            win_percentage = win_matches/total_matches
        except:
            win_matches = 0
        try: 
            draw_matchs = data["result"].value_counts()["D"]
        except:
            draw_matchs = 0
        try: 
            loss_matchs = data["result"].value_counts()["L"]
        except:
            loss_matchs = 0

    return [total_matches,win_matches, draw_matchs, loss_matchs, win_percentage]

# difference_betwen_two(team1)


# matches_rolling = matches.groupby("team").apply(lambda x:rolling_averages(x, cols, new_cols))
