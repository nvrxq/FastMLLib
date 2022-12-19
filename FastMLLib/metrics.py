from utils import (
    argmax
)


def accuracy(output, y):
    '''
    Accuracy is output data / true data
    '''
    hit = 0
    output = output.argmax()
    y = y.argmax()
    for a in zip(output, y):
        if (a[0] == a[1]):
            hit += 1

    p = (hit*100)/output._paramR
    return p


def compute_tp_tn_fn_fp(y_act, y_pred):
    '''
    True positive - actual = 1, predicted = 1
    False positive - actual = 1, predicted = 0
    False negative - actual = 0, predicted = 1
    True negative - actual = 0, predicted = 0
    '''
    tp = sum((y_act == 1) & (y_pred == 1))
    tn = sum((y_act == 0) & (y_pred == 0))
    fn = sum((y_act == 1) & (y_pred == 0))
    fp = sum((y_act == 0) & (y_pred == 1))
    return tp, tn, fp, fn


def compute_accuracy(tp, tn, fn, fp):
    '''
    Accuracy = TP + TN / FP + FN + TP + TN

    '''
    return ((tp + tn) * 100) / float(tp + tn + fn + fp)


def compute_precision(tp, fp):
    '''
    Precision = TP  / FP + TP 

    '''
    return (tp * 100) / float(tp + fp)


def compute_recall(tp, fn):
    '''
    Recall = TP /FN + TP 

    '''
    return (tp * 100) / float(tp + fn)


def compute_f1_score(y_true, y_pred):
    '''
        F1 score
        '''
    tp, tn, fp, fn = compute_tp_tn_fn_fp(y_true, y_pred)
    precision = compute_precision(tp, fp)/100
    recall = compute_recall(tp, fn)/100
    f1_score = (2*precision*recall) / (precision + recall)

    return f1_score


def compute_sens_spec(tp, tn, fp, fn):
    '''
        Sensitivity = Recall = TP/(TP+FN)
    Specificity = True Negative Rate =  TN/(TN+FP)
        '''
    return (tp * 100) / float(tp + fn), (tn * 100) / float(tn + fp)


def MSE(y_true, y_pred):
    '''
    “Mean squared error” is perhaps the most popular metric used for regression problems. 
    It essentially finds the average squared error between the predicted and actual values.
    '''
    result = 0
    for a in zip(y_true, y_pred):
        result += (a[0] - a[1])**2

    return result


def MAE(y_true, y_pred):
    '''
    Mean absolute error (or mean absolute deviation) is another metric 
    which finds the average absolute distance between the predicted and target values. 
    '''
    result = 0
    for a in zip(y_true, y_pred):
        result += abs(a[0] - a[1])

    return result
