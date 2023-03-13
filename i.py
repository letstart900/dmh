import pandas as pd
import math

df=pd.read_csv('play_tennis.csv',header=0)
df=df.set_index('day')

df.head()

def entropy(df):
  pi=list(df['play'].value_counts())
  s=0
  su=sum(pi)
  for i in pi:
    val=i/su
    s+=val*math.log(val,2)
  return -s

def information_gain(df,column_name):
  ie=entropy(df)
  group_data=df.groupby(column_name)
  h=0
  for g, data in group_data:
    sub_e=entropy(data)
    h+=len(data)/len(df)*sub_e

  return ie-h

def ig_arr(df):
  ig={}
  for col in df.columns:
    if(col!='play'):
      ig[col]=information_gain(df.copy(),col)
  return ig

#ID3 Algorithm
#Writing into a file for ID3 Algorithm
f=open('ID3.txt','w')
data_sets=[]
data_sets.append((df.copy(),'main'))
g1=""

while(len(data_sets)>0):
  temp_df,parent_feature=data_sets.pop(0) 

  ig=ig_arr(temp_df)
  if(len(temp_df)==0 or len(ig)==0):
    continue
  best_column=max(ig,key=lambda x:ig[x])
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

    if(entropy(new_df)==0):
      v1=new_df['play'].value_counts().index.tolist()[0]
      g2=g1+g
      print(f'{g2}=>{v1}')
      f.write("%s=>%s\n" %(g2,str(v1)))
     
    else:
      data_sets.append((new_df,g))
  
f.close()
