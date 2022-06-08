def filterFun(message, spam, ham):
	num_spam_messages = len(spam)
	num_ham_messages = len(ham)
	num_messages = num_spam_messages + num_ham_messages
	
	pSpam = num_spam_messages / num_messages
	pHam = num_ham_messages / num_messages
#	print(pHam)
#	print(pSpam)
	
	runningSpamProb = pSpam
	runningHamProb = pHam

	for each in message:
#		print("The word: %d" % (each))
		num_in_spam = 0
		num_in_ham = 0
		for each1 in spam:
			if each in each1:
				num_in_spam += 1
		pSpamGivenWord = num_in_spam / num_spam_messages
#		print(pSpamGivenWord)
		runningSpamProb *= pSpamGivenWord
		for each2 in ham:
			if each in each2:
				num_in_ham += 1
		pHamGivenWord = num_in_ham / num_ham_messages
		runningHamProb *= pHamGivenWord
#	print(runningSpamProb)
#	print(runningHamProb)
	if runningHamProb <= runningSpamProb:
		return True
	else: 
		return False
		
	
message1 = [0,1]
spam1 = [[0,1,2], [1,3,0], [2,3,4]]
ham1 = [[2,3,5], [6,1,0]]

filterFun(message1, spam1, ham1)

message2 = [1,2]
spam2 = [[0,1], [3,0], [2,0]]
ham2 = [[1], [1,2], [0,2]]

filterFun(message2, spam2, ham2)
