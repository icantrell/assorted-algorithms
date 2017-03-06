formulas = file('formulas.txt').readlines()

while 1:
    P = raw_input('p:')
    Q = raw_input('q:')

    P = P.replace(" ","")
    Q = Q.replace(" ","")
    
    if len(formulas) is 0:
        formulas.append(P + '->' + Q)                             
        thefile = open('formulas.txt','a')
        thefile.write(P + '->' + Q)
        thefile.close()
        
    else:
    
        for formula in formulas:
            print 'using ' + formula
            formula = formula.replace(" ","")
            
            form = formula.rpartition('->')
            formula = form[0]
            
            print 'matching '+  formula
            table = {}
            n = 0
            for i in xrange(len(P)):
                for p in P[i:]:
                   
                    if P + '->' + Q not in formulas:
                        
                        if n >= len(formula):
                            print 'writing formula.'
                            original = P[i:i+len(formula)]
                            P = P[:i] + P[i:].replace(original,form[2])

                            if P == Q:
                                formulas.append(P + '->' + Q)
                                
                                thefile = open('formulas.txt','a')

                                thefile.write('\n'+P + '->' + Q)
                                thefile.close()
                                break
                        else:
                            if p in table:
                                print table
                                if not formula[n] == table[p]:
                                    print 'cleared ' +str(n)
                                    table.clear()
                                    n = 0
                                else:
                                    n += 1
                            else:
                                if formula[n] == '+':
                                    if not formula[n] == p:
                                        table.clear()
                                        n = 0
                                    else:
                                        n+=1
                                elif formula[n] == '-':
                                    if not formula[n] == p:
                                        table.clear()
                                        n = 0
                                    else:
                                        n+=1
                                elif formula[n] == '(':
                                    if not formula[n] == p:
                                        table.clear()
                                        n = 0
                                    else:
                                        n+=1
                                elif formula[n] == ')':
                                    if not formula[n] == p:
                                        table.clear()
                                        n = 0
                                    else:
                                        n+=1
                                else:
                                    table[p] = formula[n]
                                    n+=1

                    
                
                    
        
        
