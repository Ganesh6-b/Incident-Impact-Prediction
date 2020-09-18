from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import pickle

classifier = pickle.load(open("impactpredictor.pkl", "rb"))
# Create your views here.
 
def home(request):
    return render(request, "home.html")

def ImpactPrediction(request):
    if request.method == 'POST':
        try:
            df = pd.read_csv(request.FILES['files'])
        except:
            df = pd.read_excel(request.FILES['files'], sheet_name=1)
        fin_df = df[['ID', 'ID_status', 'count_reassign', 'count_updated', 'ID_caller','opened_by', 'Created_by', 'updated_by', 'location', 'category_ID','user_symptom', 'Support_group', 'support_incharge']]
        fin_df['ID'] = fin_df['ID'].astype(str).str[3:].astype(int)
        #Remove the extra part the attributes like "Opened by 8" to "8" for more understanding. do it for all attributes which have like this
        fin_df['ID_caller'] = fin_df['ID_caller'].astype(str).str[7:].astype(int)
        fin_df['opened_by'] = fin_df['opened_by'].astype(str).str[10:].astype(int)
        fin_df['Created_by'] = fin_df['Created_by'].astype(str).str[11:].astype(int)
        fin_df['updated_by'] = fin_df['updated_by'].astype(str).str[11:].astype(int)
        fin_df['location'] = fin_df['location'].astype(str).str[9:].astype(int)
        fin_df['category_ID'] = fin_df['category_ID'].astype(str).str[9:].astype(int)
        fin_df['user_symptom'] = fin_df['user_symptom'].astype(str).str[8:].astype(int)
        fin_df['Support_group'] = fin_df['Support_group'].astype(str).str[6:].astype(int)
        fin_df['support_incharge'] = fin_df['support_incharge'].astype(str).str[9:].astype(int)

        ID_status_dict = {'New' : 0 , 'Resolved' : 1, 'Closed' : 2, 'Active': 3, 'Awaiting User Info': 4, 'Awaiting Problem' : 5, 'Awaiting Vendor' : 6, 'Awaiting Evidence' : 7, '-100' : 8}
        fin_df['ID_status'] = fin_df['ID_status'].map(ID_status_dict)

        fin_df['ID_status'] = fin_df['ID_status'].astype(int)
        fin_df['count_reassign'] = fin_df['count_reassign'].astype(int)
        fin_df['count_updated'] = fin_df['count_updated'].astype(int)
        pred_val = np.array(classifier.predict(fin_df))
        Id_val = np.array(fin_df['ID'])
        fin_series = pd.Series(pred_val, index = Id_val)
        dict_impact = {1 : "Low", 2 : "Medium", 3 : "High"}
        fin_series = fin_series.map(dict_impact)
        pred_dict = fin_series.to_dict()
        context = {"pred_dict" : pred_dict}
        return render(request, "result.html", context = context)
    else:
        return render(request, "home.html")
def ImpactPredictionValue(request):  
    if request.method == 'POST':
        ID = int(request.POST['ID'])
        ID_status = request.POST['ID_status']
        count_reassign = int(request.POST['count_reassign'])
        count_updated = int(request.POST['count_updated'])
        ID_caller = int(request.POST['ID_caller'])
        if ID_status == "New":
            ID_status = 0
        elif ID_status == "Resolved":
            ID_status = 1
        elif ID_status == "Closed":
            ID_status = 2
        elif ID_status == "Active":
            ID_status = 3
        elif ID_status == "Awaiting User Info":
            ID_status = 4
        elif ID_status == "Awaiting Problem":
            ID_status = 5
        elif ID_status == "Awaiting Vendor":
            ID_status = 6
        elif ID_status == "Awaiting Evidence":
            ID_status = 7
        elif ID_status == "-100":
            ID_status = 8
        opened_by = int(request.POST['opened_by'])
        Created_by = int(request.POST['Created_by'])
        updated_by = int(request.POST['updated_by'])
        location = int(request.POST['location'])
        category_ID = int(request.POST['category_ID'])
        user_symptom = int(request.POST['user_symptom'])
        Support_group = int(request.POST['Support_group'])
        support_incharge = int(request.POST['support_incharge'])
        arr = np.array([[ID, ID_status, count_reassign, count_updated, ID_caller,opened_by, Created_by, updated_by, location, category_ID,user_symptom, Support_group, support_incharge]])
        pred_val = int(classifier.predict(arr))
        if pred_val == 1:
            impact = "Low"
        elif pred_val == 2:
            impact == 'Medium'
        elif pred_val == 3:
            impact == 'High'
        context = {"impact" : impact}
        return render(request, 'home.html', context = context)
    else:
        return render(request, "home.html")