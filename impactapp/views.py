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
        acbser1 = fin_df['ID']
        acbser_1 = acbser1.tolist()
        acbser2 = []
        for i in range(len(acbser_1)):
            vg = acbser_1[i]
            vg_new = vg.strip("INC")
            acbser2.append(vg_new)
        fin_df['ID'] = acbser2                           
        fin_df['ID'] = fin_df['ID'].astype(int)

        def abcser(m):
            for col in m:
                updatser1=[]
                updatser=fin_df[col]
                for i in range(len(fin_df[col])):
                    j = updatser[i]
                    l = j.split()
                    r = l[1]
                    updatser1.append(r)
                fin_df[col]=updatser1
        m=['ID_caller','location','category_ID','user_symptom','Support_group','support_incharge']
        abcser(m)
        def abser(n):
            for col in n:
                updatser1=[]
                updatser=fin_df[col]
                for i in range(len(fin_df[col])):
                    j = updatser[i]
                    l = j.split()
                    r = l[2]
                    updatser1.append(r)
                fin_df[col]=updatser1
        n=['opened_by','Created_by','updated_by']
        abser(n)
        idstaser=fin_df['ID_status'].unique()
        idstaser1={}
        for i in range(9):
            idstaser1[i]=idstaser[i]
        idstaser2=fin_df['ID_status']
        for i in range(len(idstaser2)): 
            for j in range(9):
                if idstaser2[i]==idstaser1[j]:
                    idstaser2[i]=j
        fin_df['ID_status'] = fin_df['ID_status'].astype(int)
        fin_df['count_reassign'] = fin_df['count_reassign'].astype(int)
        fin_df['count_updated'] = fin_df['count_updated'].astype(int)
        fin_df['ID_caller'] = fin_df['ID_caller'].astype(int)
        fin_df['opened_by'] = fin_df['opened_by'].astype(int)
        fin_df['Created_by'] = fin_df['Created_by'].astype(int)
        fin_df['updated_by'] = fin_df['updated_by'].astype(int)
        fin_df['location'] = fin_df['location'].astype(int)
        fin_df['category_ID'] = fin_df['category_ID'].astype(int) 
        fin_df['user_symptom'] = fin_df['user_symptom'].astype(int)
        fin_df['Support_group'] = fin_df['Support_group'].astype(int)
        fin_df['support_incharge'] = fin_df['support_incharge'].astype(int)
        pred_val = np.array(classifier.predict(fin_df))
        Id_val = np.array(fin_df['ID'])
        fin_series = pd.Series(pred_val, index = Id_val)
        dict_impact = {1 : "Low", 2 : "Medium", 3 : "High"}
        fin_series = fin_series.map(dict_impact)
        pred_dict = fin_series.to_dict()
        context = {"pred_dict" : pred_dict}
        return render(request, "result.html", context = context)
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