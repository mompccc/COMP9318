import helper
import numpy


def fool_classifier(test_data):  ## Please do not change the function defination...
    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...
    with open(test_data) as file:
        data = [line.strip().split(" ") for line in file]
    num_data = len(data)


    strategy_instance = helper.strategy()
    parameters = {}
    all_words = []
    x_train = []

    parameters['gamma'] = 3
    parameters['C'] = 0.8
    parameters['kernel'] = 'linear'
    parameters['degree'] = 2
    parameters['coef0'] = 0.8

    x_data = strategy_instance.class0
    y_data = strategy_instance.class1

    # create a list <all_world> containing all distinct feature words
    for lines in x_data:
        for words in lines:
            if words not in all_words:
                all_words.append(words)
    for lines in y_data:
        for words in lines:
            if words not in all_words:
                all_words.append(words)

    # biuld a matrix which x axis is <all_world> and y axis is every lines in both class 0 and 1
    # the matrix is build with 0 and 1
    for lines in x_data:
        x_list = [0 for i in range(len(all_words))]
        for words in lines:
            x_list[all_words.index(words)] = 1
        x_train.append(x_list)
    for lines in y_data:
        x_list = [0 for i in range(len(all_words))]
        for words in lines:
            x_list[all_words.index(words)] = 1
        x_train.append(x_list)
    x_train = numpy.array(x_train)

    # build a set y with classification for training data
    y_train = [0 for i in range(len(x_data))]
    for j in range(len(y_data)):
        y_train.append(1)
    y_train = numpy.array(y_train)

    # transform test_data into a suitable matrix in form of 0 and 1
    to_test = []
    for lines in data:
        data_list = [0 for i in range(len(all_words))]
        for words in lines:
            if words not in all_words:
                continue
            else:
                data_list[all_words.index(words)] = 1
        to_test.append(data_list)
    to_test = numpy.array(to_test)

    # run the SVM training function
    clf = strategy_instance.train_svm(parameters, x_train, y_train)
    print("gama:{}, C:{}, kernel:{}, degree:{}, coef0:{}".format(parameters['gamma'],
                                                                 parameters['C'], parameters['kernel'],
                                                                 parameters['degree'], parameters['coef0']))
    print("result: ", sum(clf.predict(to_test)) / num_data)
    print(clf.predict(to_test))
    weight = clf.coef_[0]  # get the weights for each features

    print("Modifying file...")

    # delete top 20 words that weight to class 1
    for i in range(len(data)):
        a = 0
        temp = list(weight)
        while a < 20:
            max_weight = max(temp)
            ind = temp.index(max_weight)
            temp[ind] = -100
            while all_words[ind] in data[i]:
                data[i].remove(all_words[ind])
                if all_words[ind] not in data[i]:
                    a += 1

    to_test = []
    for lines in data:
        data_list = [0 for i in range(len(all_words))]
        for words in lines:
            if words not in all_words:
                continue
            else:
                data_list[all_words.index(words)] = 1
        to_test.append(data_list)
    to_test = numpy.array(to_test)

    # run the SVM training function
    clf = strategy_instance.train_svm(parameters, x_train, y_train)
    print("gama:{}, C:{}, kernel:{}, degree:{}, coef0:{}".format(parameters['gamma'],
                                                                 parameters['C'], parameters['kernel'],
                                                                 parameters['degree'], parameters['coef0']))
    print("result: ", sum(clf.predict(to_test)) / num_data)
    print(clf.predict(to_test))

    modified_data = './modified_data.txt'
    with open(modified_data, 'w') as file:
        for d in data:
            file.writelines(' '.join(d) + '\n')
    assert strategy_instance.check_data(test_data, modified_data)
    return strategy_instance  ## NOTE: You are required to return the instance of this class.

