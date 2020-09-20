import pandas as pd
class LinkedListNode:
    def __init__(self,name,price=None,review=None,takingSaftyMeasure=None,pic=None,features=None):
        self.name=name
        self.pic=pic
        self.price=price
        self.review=review
        self.features=features
        self.takingSaftyMeasure=takingSaftyMeasure
        self.next=None
from selenium import webdriver
driver = webdriver.Chrome("/Users/manshusharma/Downloads/chromedriver")
driver.get("https://www.tripadvisor.in/Hotels-g304551-New_Delhi_National_Capital_Territory_of_Delhi-Hotels.html")


def LinkedList():
    hotelName = driver.find_elements_by_class_name("property_title")
    price = driver.find_elements_by_class_name("price,__resizeWatch")
    review=driver.find_elements_by_class_name("review_count")
    takingSaftyMeasure = driver.find_elements_by_class_name("_1shPZD63")
    pic = driver.find_elements_by_class_name("_1a4WY7aS")

    head=None
    tail=None
    #Here i use diffrent variables because it is easy for me to identify
    # i hotelName
    # j price
    # k review
    # l takingSaftyMeasure
    # m pic
    # n features

    for i,j,k,l,m in zip(hotelName,price,review,takingSaftyMeasure,pic):
        NewNode=LinkedListNode(i.get_attribute("innerHTML")[5:],j.get_attribute("innerHTML")[7:],k.get_attribute("innerHTML")[0:-7],l.get_attribute("innerHTML"),m.get_attribute('src'))
        if head is None:
            head=NewNode
            tail=NewNode
        else:
            tail.next=NewNode
            tail=NewNode
    return head

hotel=[]
price=[]
review=[]
takingSaftyMeasure=[]
pic=[]

#Optionally creted to see our output on cli
def printLL(head):
    while head is not None:
        hotel.append(head.name)
        price.append(head.price)
        review.append(head.review)
        takingSaftyMeasure.append(head.takingSaftyMeasure)
        pic.append(head.pic)


        print(head.name,head.price,head.review,head.takingSaftyMeasure,head.pic)
        head=head.next
    print()

#features=driver.find_elements_by_class_name("text")
printLL(LinkedList())

dict = {'hotel': hotel, 'price': price, 'review': review,'takingSaftyMeasure': takingSaftyMeasure, 'pic': pic}
df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('file1.csv')

driver.close()