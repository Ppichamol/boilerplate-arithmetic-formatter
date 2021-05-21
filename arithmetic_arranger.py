def arithmetic_arranger(problems, ex = False):
  if len(problems)<=5 :
    arranged_problems = check(problems,ex)
  else : return ("Error: Too many problems.")
  return arranged_problems


def check(problems,ex):
  b=list()
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  sign =['+','-']
  for i in problems :
    a = i.split()
    first = a[0]
    sec = a[2]
    if a[1] not in sign :
      return ("Error: Operator must be '+' or '-'.")
    elif len(first)<=4 and len(sec)<=4:
      if first.isdigit() and sec.isdigit():
        x = max(len(first),len(sec))
        line1 += first.rjust(x+2)+'    '
        line2 += a[1] + sec.rjust(x+1) + '    '
        line3 += ('-'*(x+2)) + '    '
        if a[1] == sign[0] :
          line4 += (str(int(first)+int(sec))).rjust(x+2) + '    '
        else : line4 += (str(int(first)-int(sec))).rjust(x+2) + '    '
          
      else: return ("Error: Numbers must only contain digits.")
    else : return ("Error: Numbers cannot be more than four digits.")
  if ex == True:
    n = line1.rstrip() +"\n" + line2.rstrip() +"\n" +line3.rstrip() +"\n" +line4.rstrip()
  else : n = line1.rstrip() +"\n" + line2.rstrip() +"\n" +line3.rstrip()
  
  return(n)
  
    


  