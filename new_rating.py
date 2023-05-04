def new_rating(original,result,user):
  ratings=[]
  for i in range(original.shape[1]):
    r=original[user,i]
    if r==0:
      if result[user,i] > 5:
        ratings.append((i, 5))
      elif result[user, i] < 0:
        ratings.append((i, 0))
      else:
        ratings.append((i,result[user,i]))
  return sorted(ratings,key=lambda x:x[1],reverse=True)