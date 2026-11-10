piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

#i am slicing thru the indexes the last one IS INCLUDED
print(piano_keys[2:5]) #here i get hold of the indexes from 1 to 5 but NOT INCLUDING THE ELEMENT OF 5 just from 2 to 4
#answer "c", "d", "e"

#if i want eveything up to position 5
print(piano_keys[:5]) #I get rid of the first value on the slicing

#WE CAN ADD ANOTHER NUMBER TO HAVE AN INCREMENT AS HAPPENS ON OTHERS methods
print(piano_keys[2:5:2]) #the last numbers tells us is slicing every 2 or every second one

#specify this negative one as the increment and that wa could go backwards or reverse this list for us
#manipulating lists and tuples
print(piano_keys[::-1]) #this list starting from the end all the way back to the beginning INSTEAD OF USING .reverse()

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:5])