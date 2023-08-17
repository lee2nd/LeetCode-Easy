class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # the timespan 1950-2050 covers 101 years
        delta = [0] * 101

		    # to make explicit the conversion from the year (1950 + i) to the ith index
        conversionDiff = 1950 
		
        for l in logs:
			  # the log's first entry, birth, increases the population by 1
            delta[l[0] - conversionDiff] += 1 
			
			  # the log's second entry, death, decreases the population by 1
            delta[l[1] - conversionDiff] -= 1

        runningSum = 0
        maxPop = 0
        year = 1950
		
		    # find the year with the greatest population
        for i, d in enumerate(delta):
            runningSum += d
			
			  # since we want the first year this population was reached, only update if strictly greater than the previous maximum population
            if runningSum > maxPop:
                maxPop = runningSum
                year = conversionDiff + i
				
        return year
# test case : logs = [[1950,1961],[1960,1971],[1970,1981]]
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
