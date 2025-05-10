import requests

def get_top_10( url, number):
    top_stories = requests.get(url)
    # Get the stories list, 
    stories_list = eval(top_stories.content.decode())
    top_10 = stories_list[: number]
    return top_10



def get_link(id, title=False):
    end_point = f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
    req_object = requests.get(end_point)
    id_dict = eval(req_object.content.decode())
    id_url = id_dict['url']

    if title == True:
        description = id_dict['title']
        
        return id_url, description
    
    
    return id_url




url = ' https://hacker-news.firebaseio.com/v0/topstories.json'
no_of_items_to_fetch = int(input("No of top news stories to fetch: "))
stories_id = get_top_10(url, no_of_items_to_fetch)



print(stories_id)

for i in stories_id:
    try:
        
        link = get_link(i, title=False)
        print(link)
        # print("Description: " ,link[1])
        # print()e
    except:
        # print()
#     except: # Need some Error Handling and what to do when such things creep on the top page of Hackernews.
        print("id = ", i)



