# no link

def knapsack(values, weights, W):
	dp = [[0 for i in range(W+1)] for i in range(len(values)+1)]
	# print(dp)
	values =[0]+values
	weights = [0]+weights
	for i in range(len(values)):
		for j in range(W+1):
			# print(i,j)
			if i ==0 or j ==0:
				dp[i][j]=0
			elif j<weights[i]:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
	return dp[len(values)-1][W]


if __name__ == '__main__':
	weights  = [1,3,4,5]
	values = [1,4,5,7]
	W = 7
	print(knapsack(values, weights, W))