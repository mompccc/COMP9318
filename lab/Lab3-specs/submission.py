################# Question 1 #################
def count_func(dic, sum_all):
	count = 0
	for key in dic:
		count += dic[key]
	for key in dic:
		dic[key] = (dic[key]+1)/(count+sum_all)
	return dic, count

def multinomial_nb(training_data, sms):# do not change the heading of the function
	ham = {}
	spam = {}
	ham_num = 0
	spam_num = 0
	ham_sms = 1
	spam_sms = 1
	temp = {}

	for data_set in training_data:
		if data_set[1] == 'ham':
			ham_num += 1
			for key in data_set[0]:
				if key not in ham:
					ham[key] = data_set[0][key]
				else:
					ham[key] += data_set[0][key]
		else:
			spam_num += 1
			for key in data_set[0]:
				if key not in spam:
					spam[key] = data_set[0][key]
				else:
					spam[key] += data_set[0][key]

	for key in ham:
		if key not in temp:
			temp[key] = ham[key]
	for key in spam:
		if key not in temp:
			temp[key] = spam[key]

	sum_all = len(temp)
	ham_p, ham_count = count_func(ham, sum_all)
	spam_p, spam_count = count_func(spam, sum_all)
	
	new =[]
	for key in sms:
		if key in temp:
			new.append(key)

	for i in new:
		if i not in ham:
			ham_sms = ham_sms * 1/(ham_count+sum_all)
		else:
			ham_sms = ham_sms * ham_p[i]

		if i not in spam:
			spam_sms = spam_sms * 1/(spam_count+sum_all)
		else:
			spam_sms = spam_sms * spam_p[i]

	spam_sms = spam_sms * spam_num
	ham_sms = ham_sms * ham_num
	return spam_sms/ham_sms