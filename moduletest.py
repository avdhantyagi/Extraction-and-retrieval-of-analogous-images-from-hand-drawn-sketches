import algoPred as ap
import pandas as pd


inp = "/Users/avdhantyagi/Desktop/Bottle.JPEG"
algo = input("Algo :")
ui_class = input("Class :s")

index_for_classes = pd.read_csv("./index_for_classes.csv")

start = 0
end = 0
for i in range(len(index_for_classes['class'])):
    if(ui_class == index_for_classes['class'][i]):
        start = index_for_classes['id'][i]
        end = index_for_classes['id'][i+1]


data = pd.read_csv("./dataset.csv")

if algo == "Jaccard":
    arr = ap.pred_jaccard(inp, data, start, end)