from sklearn.linear_model import LogisticRegression
x=[1],[2],[3],[4]
y=[0,0,1,1]
model=LogisticRegression()
model.fit(x,y)
# Enter the hour value 
hours=float(input("enter your number"))
result =model.predict([[hours]])[0]


if result==1:
    print(f"based on hours{hours},you likely pass")
else:
    print(f"based on your result{hours}, you likey fail ")
