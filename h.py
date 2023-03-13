import pandas as pd

df=pd.read_csv('play_tennis.csv',header=0)
df=df.set_index('day')

df.head()
f=open('Hunts.txt','w')
data_sets=[]
data_sets.append((df.copy(),'main'))
g1=""

while(len(data_sets)>0):
  temp_df,parent_feature=data_sets.pop(0) 
  
  if(len(temp_df)==0):
    continue
  best_column=(temp_df.columns)[0]

  if parent_feature!='main':
    g1=g3+"=>"
    g1=g1+parent_feature+"=>"+best_column+"=>"
  else:
    g3=best_column
    g1=g1+best_column+"=>"

  grouped_data=temp_df.groupby(best_column)
  for g,data in grouped_data:
    new_df=data.copy()
    new_df.drop([best_column],axis=1,inplace=True)
    
    pi1=list(new_df['play'].value_counts())
    if(len(pi1)==1):
      v1=new_df['play'].value_counts().index.tolist()[0]
      g2=g1+g
      print(f'{g2}=>{v1}')
      f.write("%s=>%s\n" %(g2,str(v1)))
    else:
      if parent_feature!='main':
        data_sets.append((new_df,parent_feature+'=>'+g))
      else:
        data_sets.append((new_df,g))

f.close()
