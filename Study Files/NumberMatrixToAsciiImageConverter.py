# This function converts a matrix of numbers 0 - 13 into an image using symbols 
#
#

def Convert(image):
    pic = '' # creates an empty string to hold the Converted picture

    for row in image: # loops over evry row in the number matrix
        data = '' # creates an empty string to hold the current row of text
        for pixel in row: # loops over every entry in the current row and add their assigned text to the data string 
             if pixel == 2:
               data += "||"
             elif pixel == 3:
               data += '\\\\'
             elif pixel == 4:
               data += '//'
             elif pixel == 5:
               data += '\\|'
             elif pixel == 6:
               data += '|/'
             elif pixel == 7:
               data += '|\\'
             elif pixel == 8:
               data += '/|'
             elif pixel == 9:
               data += '=='
             elif pixel == 10:
               data += '/\\'
             elif pixel == 11:
               data += '\\/'
             elif pixel == 12:
               data += '<<'
             elif pixel == 13:
               data += '>>'
             elif pixel:
               data += '--'
             else:
               data += '  '
            
        pic += data + '\n'  # adds the row to the picture and adds a new line
        
    return pic # returns the image so that i can be used else where

# example = [
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
#[0,4,9,3,0,4,9,3,0,4,9,9,9,9,9,3,0,4,9,3,0,0,0,0,0,4,9,3,0,0,0,0,0,4,9,9,9,9,9,3,0,],
#[0,2,1,2,0,2,1,2,0,2,1,1,1,1,1,2,0,2,1,2,0,0,0,0,0,2,1,2,0,0,0,0,0,2,1,1,1,1,1,2,0,],
#[0,2,1,4,9,3,1,2,0,2,1,4,9,9,9,4,0,2,1,2,0,0,0,0,0,2,1,2,0,0,0,0,0,2,1,4,9,3,1,2,0,],
#[0,2,1,1,1,1,1,2,0,2,1,9,9,9,0,0,0,2,1,2,0,0,0,0,0,2,1,2,0,0,0,0,0,2,1,2,0,2,1,2,0,],
#[0,2,1,3,9,4,1,2,0,2,1,3,9,9,9,3,0,2,1,3,9,9,9,3,0,2,1,3,9,9,9,3,0,2,1,3,9,4,1,2,0,],
#[0,2,1,2,0,2,1,2,0,2,1,1,1,1,1,2,0,2,1,1,1,1,1,2,0,2,1,1,1,1,1,2,0,2,1,1,1,1,1,2,0,],
#[0,3,9,4,0,3,9,4,0,3,9,9,9,9,9,4,0,3,9,9,9,9,9,4,0,3,9,9,9,9,9,4,0,3,9,9,9,9,9,4,0,],
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
#] 
# Will convert to
#
#  //==\\  //==\\  //==========\\  //==\\          //==\\          //==========\\
#  ||--||  ||--||  ||----------||  ||--||          ||--||          ||----------||
#  ||--\\==//--||  ||--//======//  ||--||          ||--||          ||--//==\\--||
#  ||----------||  ||--======      ||--||          ||--||          ||--||  ||--||
#  ||--//==\\--||  ||--\\======\\  ||--\\======\\  ||--\\======\\  ||--\\==//--||
#  ||--||  ||--||  ||----------||  ||----------||  ||----------||  ||----------||
#  \\==//  \\--//  \\==========//  \\==========//  \\==========//  \\==========//
#
