from matplotlib import *
import matplotlib.pyplot as plt
import pickle

tvk=[]
admk=[]
dmk=[]
ntk=[]
none=[]

voted_ids=[]

village_people=[
    {"name":"arun","vote_id":"101"},
    {"name":"bala","vote_id":"102"},
    {"name":"kumar","vote_id":"103"},
    {"name":"raja","vote_id":"104"},
    {"name":"vicky","vote_id":"105"},
    {"name":"surya","vote_id":"106"},
    {"name":"mani","vote_id":"107"},
    {"name":"ajay","vote_id":"108"},
    {"name":"dinesh","vote_id":"109"},
    {"name":"gokul","vote_id":"110"},
    {"name":"hari","vote_id":"111"},
    {"name":"jegan","vote_id":"112"},
    {"name":"karthi","vote_id":"113"},
    {"name":"lokesh","vote_id":"114"},
    {"name":"madhan","vote_id":"115"},
    {"name":"naveen","vote_id":"116"},
    {"name":"praveen","vote_id":"117"},
    {"name":"ramesh","vote_id":"118"},
    {"name":"sakthi","vote_id":"119"},
    {"name":"vijay","vote_id":"120"}
]

f=open("village_people.bin","wb")
pickle.dump(village_people,f)
f.close()

f=open("village_people.bin","rb")
data=pickle.load(f)
f.close()

for x in range(3):

    a=str(input("1.tvk \n2.admk \n3.dmk \n4.ntk \n5.none \nenter a choice: "))

    name=input("enter a name: ")
    vote_id=input("enter a vote id: ")

    if vote_id in voted_ids:
        print("already voted")
        continue

    found=False

    for i in data:
        if i["vote_id"]==vote_id:
            found=True

    if found==False:
        print("vote id not found")
        continue

    age=int(input("enter a age: "))

    if age<18:
        print("not eligible")
        continue

    voted_ids.append(vote_id)

    c={
        "name":name,
        "vote_id":vote_id,
        "age":age
    }

    if(a=='1'):
        tvk.append(c)

    elif(a=='2'):
        admk.append(c)

    elif(a=='3'):
        dmk.append(c)

    elif(a=='4'):
        ntk.append(c)

    elif(a=='5'):
        none.append(c)

    else:
        print("invalid choice")

f=open("tvk_votelist.bin","wb")
for x in tvk:
    x=str(x)+'\n'
    x=x.encode()
    f.write(x)
f.close()

f=open("admk_votelist.bin","wb")
for x in admk:
    x=str(x)
    x=x.encode()
    f.write(x)
f.close()

f=open("dmk_votelist.bin","wb")
for x in dmk:
    x=str(x)+'\n'
    x=x.encode()
    f.write(x)
f.close()

f=open("ntk_votelist.bin","wb")
for x in ntk:
    x=str(x)+'\n'
    x=x.encode()
    f.write(x)
f.close()

f=open("none_votelist.bin","wb")
for x in none:
    x=str(x)+'\n'
    x=x.encode()
    f.write(x)
f.close()

print("\npeople who not voted\n")

for x in data:

    if x["vote_id"] not in voted_ids:
        print(x["name"],x["vote_id"])

tvk=len(tvk)
admk=len(admk)
dmk=len(dmk)
ntk=len(ntk)
none=len(none)

print("\n------result------\n")

print("tvk votes :",tvk)
print("admk votes :",admk)
print("dmk votes :",dmk)
print("ntk votes :",ntk)
print("none votes :",none)

result={
    "tvk":tvk,
    "admk":admk,
    "dmk":dmk,
    "ntk":ntk,
    "none":none
}

winner=max(result,key=result.get)

print("\nwinner is :",winner)

total=tvk+admk+dmk+ntk+none

if total>0:

    print("\nvote percentage\n")

    print("tvk :",(tvk/total)*100)
    print("admk :",(admk/total)*100)
    print("dmk :",(dmk/total)*100)
    print("ntk :",(ntk/total)*100)
    print("none :",(none/total)*100)

plt.pie(
    [tvk,admk,dmk,ntk,none],
    labels=["tvk","admk","dmk","ntk","none"],
    autopct="%1.1f%%"
)

plt.title("election result")

plt.show()