from bs4 import BeautifulSoup
import lxml

with open("/Users/Tshifhiwa/Downloads/wetransfer_python_stuffs_2024-04-27_1325/Website_dev/html/3.4+Birthday+Invite+Project/3.4 Birthday Invite Project/index.html") as file:
    content = file.read()
#beutiful soup first add the file you are using, then specify the type of file ypu are using(html or lxml)
#(if using lxml you must import it first)
soup = BeautifulSoup(content, "html.parser")

#to start accessing info in the file use: soup.<tag>
content_title = soup.title
# print(content_title)

#to get first tag: soup.<tag>.name
content_title_tag = soup.title.name
#print(content_title_tag)

#to get the actual string in first tag: soup.<tag>.string
content_title_string = soup.title.string
#print(content_title_string)

#to print out the whole objet: soup
#to indent the content: soup.prettify()
#print(soup.prettify())

#to get all the <tags> e.g. all the <li> or all the <p>: soup.find_all()
#can search by name: soup.find_all(name=<tag>) will be in a list
all_li_tags = soup.find_all(name="li")
# print(content_all_li)

#get string in all <tags>: user a for loop then getText()
#for tag in all_li_tags:
    #li_text = tag.getText()
#     print(li_text)

#get link in all the <tags>: use a for loop then get()
all_a_tags = soup.find_all(name="a")
for link in all_a_tags:
    links = link.get("href")
    #print(links)

#you can also use the "find_all" using attribute
#you can use "find" in the same way to get a single <tag> with the same attribute
#this can be done using the class attribute(needs to be "typed class_")
#to get text add ".getText()"
#to get tag name add ".name"
# to get the id or class ect: use ".get(insert attribute you need)"

first_heading_with_id = soup.find_all(name="h1", id="first_heading")
#print(first_heading_with_id) #.getText()
first_heading_with_class = soup.find(name="h3", class_="first_h3")
#print(first_heading_with_class) #.name

#to get a tag that's within a tag: soup.select_one(selector=)
#the "selector=" is based on css(you can also use it to find attributes[keep in mind css uses symbols #=id .=class])
#select_one will give us the first matching one
#"selector=" can also be used in select not just select_one

googleMaps_url = soup.select_one(selector="h4 a")
#print(googleMaps_url)
h1 = soup.select_one(selector="#first_heading")
#print(h1)
h3 = soup.select(selector=".first_h3")
#print(h3)






