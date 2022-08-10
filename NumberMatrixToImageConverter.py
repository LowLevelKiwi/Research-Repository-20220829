def Convert(image):
    """
  Converts a Matrix of numbers into an ascii Image

  0 = "  " \n
  1 = "--" \n
  2 = "||" \n
  3 = "\\\\" \n
  4 = "//" \n
  5 = "\\|" \n
  6 = "|/" \n
  7 = "|\\" \n
  8 = "/|" \n
  9 = "==" \n
  """
    pic = ''

    for row in image:
        data = ''
        for pixel in row:
            data += '>>' if pixel == 13 else '<<' if pixel == 12 else '\\/' if pixel == 11 else '/\\' if pixel == 10 else '==' if pixel == 9 else '/|' if pixel == 8 else '|\\' if pixel == 7 else '|/' if pixel == 6 else '\\|' if pixel == 5 else '//' if pixel == 4 else '\\\\' if pixel == 3 else "||" if pixel == 2 else '--' if pixel == 1 else '  '
            # if pixel == 2:
            #   data += "||"
            # elif pixel == 3:
            #   data += '\\\\'
            # elif pixel == 4:
            #   data += '//'
            # elif pixel == 5:
            #   data += '\\|'
            # elif pixel == 6:
            #   data += '|/'
            # elif pixel == 7:
            #   data += '|\\'
            # elif pixel == 8:
            #   data += '/|'
            # elif pixel == 9:
            #   data += '=='
            # elif pixel == 10:
            #   data += '/\\'
            # elif pixel == 11:
            #   data += '\\/'
            # elif pixel == 12:
            #   data += '<<'
            # elif pixel == 13:
            #   data += '>>'
            # elif pixel:
            #   data += '--'
            # else:
            #   data += '  '

        pic += data + '\n'  #adds a new line for every row

    print(pic)
