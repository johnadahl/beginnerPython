#This comes from the recomendation found here: https://github.com/karan/Projects
#This is the description. Create an application which manages an inventory of products. 
#Create a product class which has a price, id, and quantity on hand. 
#Then create an inventory class which keeps track of various products and can sum up the inventory value.
#We're going to do a gpu shop. It should be easy because there is never any stock. Ha Ha.

#So we have watched the first video from cory schafer and have made this. 
#It should be good learning because it's not blindly copying cory schafer, but rather chaning it.

class gpu:

    totalCards = 0

    def __init__(self, name, price, company):
        self.name = name
        self.price = price
        self.realprice = price * 3
        self.company = company

        gpu.totalCards += 1
        #I can increase the totalCards class variable here because every time a new card is added, it will instance it.



#    def canYouGetIt(self):
#        This works when we pass in self because self already has all the arguments from above.
#        It has self.memory, self.cores, etc.
#        print('There are exactly ' + str(self.stock) + ' of this gpu avaliable and one costs ' + str(self.price))
#        if self.stock < 10 or self.price > 500:
#            print('You cannot get one.')
#        else:
#            print('You should probably not get one.')



#So the self is just another way of saying the instance being created.
#In short, if we make a card that is named gtx1060, when self.memory = memory what it means is the 
#memory argument we pass in when we create the gtx1060 is read as gtx1060.memory.
#I feel like a genius.

gpu1 = gpu(gtx1060, 300, nvidia)
print(gpu1)
gpu_1.canYouGetIt()
