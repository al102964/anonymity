#import jnius_config
from cn.protect import Protect
from cn.protect.privacy import KAnonymity
from cn.protect.quality import Loss
from cn.protect.hierarchy import DataHierarchy, OrderHierarchy, IntervalHierarchy
import pandas as pd

pd.set_option('display.max_rows', 50)

dataset = pd.read_csv("data/data.csv")
print(dataset.head())

prot = Protect(dataset,KAnonymity(2))
prot.quality_model = Loss()

prot.supression = .1

for col in dataset.columns:
    print(col)    
    prot.itypes[col] = 'quasi'
#prot.itypes.PassengerId = 'identifying'
#prot.itypes.Name = 'identifying'
#prot.itypes.Ticket = 'identifying'
prot.itypes.ZipCode = 'identifying'

prot.hierarchies.Age = OrderHierarchy('interval',2,2,2,2,2,2)
prot.hierarchies.Nationality = DataHierarchy(pd.read_csv("data/Nationality.csv"))
prot.hierarchies.Condition = DataHierarchy(pd.read_csv("data/Condition.csv"))
#prot.hierarchies.ZipCode = IntervalHierarchy(pd.read_csv("data/ZipCode.csv"))

prot.hierarchies.ZipCode = IntervalHierarchy(intervals=[[12000,19999]],fanouts=[[1]])
#prot.hierarchies.Fare = OrderHierarchy('interval',10,2,2,2,2)
priv = prot.protect()
print(priv)
print(type(priv))
#print(priv[["Age"]])
priv.to_csv("salida.csv")
print(prot.stats)