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
try:
    no_of_items_to_fetch = int(input("No of top news stories to fetch: "))
except:
    raise Exception("Enter a proper number")
get_title = input("Get Title y/n ")
stories_id = get_top_10(url, no_of_items_to_fetch)



print(stories_id)

if get_title == 'y':
    for i in stories_id:
        the_link, title_stuff = get_link(i, title=True)
        print("Description: ", title_stuff, "\n","url: ", the_link)

elif get_title == 'n':
    for i in stories_id:
        print(get_link(i, title=False))

else:
    print("Invalid Choice Please run again. ")
