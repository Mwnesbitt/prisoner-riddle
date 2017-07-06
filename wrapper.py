import prisonerriddle
import sys
import csv
import statistics

prisoners, logging = int(sys.argv[1]), bool(int(sys.argv[2])) #prisoners not used, keep same sysargs structure as prisonerriddle.py?
iterations = int(sys.argv[3])
lowBound = int(sys.argv[4])
highBound = int(sys.argv[5])

means=[]
stdDevs=[]
for i in range(lowBound, highBound):
  counter = []
  for k in range(iterations):
    tempGame = prisonerriddle.Game(i,logging)
    tempGame.runGame()
    counter.append(tempGame.visits)
    #might be interesting to track standard deviation too instead of just mean
  avgVisits = statistics.mean(counter)
  stdDevVisits = statistics.stdev(counter)  
  if logging:
    print(avgVisits)
    print(i)
  means.append(avgVisits)
  stdDevs.append(stdDevVisits)

squares = [x**2 for x in range(lowBound,highBound)]
devMean = []
difference = []
diffMean = []
for j in range(lowBound, highBound):
  difference.append(abs(squares[j-1]-means[j-1]))
  diffMean.append(difference[j-1]/means[j-1])
  devMean.append(stdDevs[j-1]/means[j-1])
  
rows = zip(range(lowBound,highBound),squares,means,difference, diffMean, stdDevs,devMean)
  
with open('output.csv', 'w',encoding='utf8',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)    
    header=['Prisoner Riddle']
    writer.writerow(header)
    header=['Iterations of Algorithm for each Prisoner Number: '+str(iterations)]
    writer.writerow(header)
    header=["Prisoner Number Low Bound: "+str(lowBound)]
    writer.writerow(header)
    header=["Prisoner Number High Bound: "+str(highBound)]
    writer.writerow(header)
    header=['Prisoners', 'Prisoners^2','Mean Guesses', 'Difference', 'Difference/Mean', 'Standard Deviation', 'Deviation/Mean'] #Avg runtime no need to implement as it would be linear with # visits
    writer.writerow(header)
    for item in rows:
        writer.writerow(item)
    csvfile.close()