def QuestionsMarks(strParam):

  # code goes here
  for count, value in enumerate(strParam):

    if strParam[count] == "?" and strParam[count+1] == "?" and strParam[count+2] == "?":
      case = True
      break
    elif count >= len(strParam)-2:
      case = False
      break
    else:
      continue
    






  return case

# keep this function call here 
print(QuestionsMarks(input()))