
# coding: utf-8

# In[1]:


users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def search_id(user):
    for u in users:
        if u["name"] == user:
            return u["id"]
        
def num_friends(user):
    id = search_id(user)
    count = 0
    for i in friendship:
        temp = i.count(id)
        count = count + temp
    return count
    
#print(num_friends("Hero"))


def sort_by_num_friends():
    list = []
    for user in users:
        dict = {}
        dict["name"] = user["name"]
        dict["num_friends"] = num_friends(user["name"])
        list.append(dict)
    list = sorted(list, key=lambda k:k['num_friends'], reverse=True)
    return list
    


# In[2]:


sort_by_num_friends()


# In[8]:


print(search_id("Hero"))


# In[9]:


num_friends("Hero")

