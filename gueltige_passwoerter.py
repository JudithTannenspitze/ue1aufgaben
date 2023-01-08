def gueltiges_passwort(*values):
   zaehlvariable = 0
   for word in values:
      low = int(word[0])
      high = int(word[2])
      slicing_word = word.split(" ")
      character = (slicing_word[1])[0:1]
      password = slicing_word[2]
      zaehlvariableInSchleife = 0
      for value in password:
        wert = value
        if wert == character:
         zaehlvariableInSchleife +=1
      if (zaehlvariableInSchleife >=low and zaehlvariableInSchleife<=high):
         zaehlvariable+=1
   return zaehlvariable   


print ("Es entsprechen " +  str(gueltiges_passwort("1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc")) + " Wörter den Vorgaben")

