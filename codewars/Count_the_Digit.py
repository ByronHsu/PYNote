def nb_dig(n, d):
   # your code
   l = list()
   count = 0
   for i in range(n+1):
      l.append(str(i**2))
   for e in l:
      for c in e:
         if(c == str(d)):
            count += 1
   return count

# def nb_dig(n, d):
#     return sum(str(i*i).count(str(d)) for i in range(n+1))
          
