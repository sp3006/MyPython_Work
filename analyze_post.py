import csv

f = open('hacker_news.csv')
hn = list(csv.reader(f))
hn[:5]
headers = hn[0]
hn = hn[1:]
print(headers)
print(hn[:5])
ask_posts = []
show_posts =[]
other_posts = []

for post in hn:
    title = post[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(post)
    elif title.lower().startswith("show hn"):
        show_posts.append(post)
    else:
        other_posts.append(post)

for i in ask_posts:
    print(ask_posts)
    
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))
