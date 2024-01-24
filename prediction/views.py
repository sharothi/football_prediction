from django.shortcuts import render
from django.http import HttpResponse
from .make_data import read_csv, get_features_for_team, difference_betwen_two_team
from .models import CsvUpload


# Create your views here.
import pandas as pd
# file_path='matches.csv'
# matches = pd.read_csv(file_path)
# matches.head()
# matches["date"] = pd.to_datetime(matches["date"])
# matches["vanue_code"] = matches["venue"].astype("category").cat.codes
# matches["opp_code"] = matches["opponent"].astype("category").cat.codes
# matches["hour"] = matches["time"].str.replace(":.+","",regex=True).astype("int")
# matches["day_code"] = matches["date"].dt.dayofweek
# matches["target"] = (matches["result"] == "W").astype("int")




# def rolling_averages(group, cols, new_cols):
#     group =  group.sort_values("date")
#     rolling_stats = group[cols].rolling(3, closed='left').mean()
#     group[new_cols] = rolling_stats
#     group = group.dropna(subset = new_cols)
#     return group


# cols = ["gf", "ga", "sh", "sot", "dist", "fk", "pk", "pkatt"]
# new_cols = [f"{c}_rolling" for c in cols]


# team1 = rolling_averages(group_1, cols, new_cols)
# group_2 = grouped_matches.get_group("Arsenal")  
# team2 = rolling_averages(group_2, cols, new_cols)



# def get_features_for_team(historical_data):
#     goals_scored = historical_data["gf"].mean()
#     goals_conceded = historical_data["ga"].mean()
#     win_percentage = historical_data["result"].value_counts()["W"]/len(historical_data)
#     return[goals_scored,goals_conceded,win_percentage]


# res1 = get_features_for_team(team1)

# res2 = get_features_for_team(team2)

# def difference_betwen_two(historical_data):
#     # print(type(oponent));
#     data = historical_data[historical_data["opponent"] == "Brentford"]
#     print(data["result"].value_counts()["W"])
#     print(len(data))
#     win_percentage = data["result"].value_counts()["W"]/len(data)
#     return win_percentage

# difference_betwen_two(team1)


# matches_rolling = matches.groupby("team").apply(lambda x:rolling_averages(x, cols, new_cols))





    


from django.shortcuts import render, redirect
from .forms import CsvUploadForm, TeamStatusForm, CompersionForm

def upload_csv(request):
    if request.method == 'POST':
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Create a success template or redirect to another page
    else:
        form = CsvUploadForm()

    return render(request, 'upload_csv.html', {'form': form})



def upload_success(request):
    return HttpResponse('File uploaded successfully!')



def read_data(request):
    file_path = CsvUpload.objects.last().csv_file
    read_csv(file_path)
    return redirect('upload_success')


def team_status(request):
    data = 0
    # team_name = "Manchester City"
    # data = get_features_for_team(team_name, file_path)
    # print(data)
    if request.method == 'POST':
        form = TeamStatusForm(request.POST)
        if form.is_valid():
            # Handle form submission here
            # form.cleaned_data['your_model_field'] will contain the selected instance
            file_path = CsvUpload.objects.last().csv_file
            team_name = form.cleaned_data['team_name'].team
            # import pdb; pdb.set_trace()
            data = get_features_for_team(team_name, file_path)
    # print(data)
    else:
        form = TeamStatusForm()

    if data:
        return render(request, 'team_status.html', {'form': form, 'data':data})
    else:
        return render(request, 'team_status.html', {'form': form})



def compersion(request):
    data = 0
    if request.method == 'POST':
        form = CompersionForm(request.POST)
        
        if form.is_valid():
            # Handle form submission here
            # form.cleaned_data['your_model_field'] will contain the selected instance
            print(form.cleaned_data)
            file_path = CsvUpload.objects.last().csv_file
            team_name = form.cleaned_data['team_name'].team
            opponent = form.cleaned_data['oponent_name'].team
            data = difference_betwen_two_team(team_name,opponent,file_path)
    # print(data)
    else:
        form = CompersionForm()

    if data:
        return render(request, 'compersion.html', {'form': form, 'data':data})
    else:
        return render(request, 'compersion.html', {'form': form})
