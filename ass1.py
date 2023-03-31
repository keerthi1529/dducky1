import pandas as pd
#data1={'S.No':pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21] ,index=[])}
data1=pd.read_excel("dcass1in.xlsx")
df1=pd.DataFrame(data1)
df1
data2=pd.read_excel("dataassin2.xlsx")
df2=pd.DataFrame(data2)
df5=df2
df2
df2['Thinking_Team Leaderboard']=df1["Team Name"]
df3=pd.DataFrame()
df2['Averagestatements']=df2.groupby('Thinking_Team Leaderboard')['total_statements'].transform(lambda x: x.mean())
df2['Averagereasons']=df2.groupby('Thinking_Team Leaderboard')['total_reasons'].transform(lambda x: x.mean())
df2['Averagestatements']=df2['Averagestatements'].round(2)
df2['Averagereasons']=df2['Averagereasons'].round(2)
df3=df2
df3=df3.drop_duplicates(subset='Thinking_Team Leaderboard')
df3.reindex()
df3['sum']=df2['Averagereasons']+df2['Averagestatements']
df3['Rank']=df3['sum'].rank(ascending=False)
df3['Rank']=df3['Rank'].astype('int')
df3=df3.sort_values(by='Rank',ascending=True)
df4=df3[['Rank','Thinking_Team Leaderboard','Averagestatements','Averagereasons']]
df4=df4.rename(index={0:0,7:1,3:2,9:3,16:4,8:5,19:6,4:7})
#output1 (df4)
df4 
df5['sums']=df5['total_statements']+df5['total_reasons']
df5['Rank']=df5['sums'].rank(ascending=False,method='first')
df5['Rank']=df5['Rank'].astype('int')
df5=df5.sort_values(by=['Rank','name'],ascending=[True,True])
df5
df6=df5[['Rank','name','uid','total_statements','total_reasons']]
df6=df6.rename(index={10:0,0:1,1:2,3:3,2:4,15:5,7:6,9:7,8:8,12:9,20:10,16:11,17:12,5:13,18:14,6:15,11:16,13:17,4:18,14:19,19:20})
#output2 (df6)
df6
