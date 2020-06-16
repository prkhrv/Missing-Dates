import datetime
import statistics

# dict_1 = {'2019-01-01':100,'2019-01-04':115}
# dict_2 = {'2019-01-10':10,'2019-01-11':20,'2019-01-13':10}




def getAvg(date, D, gap):
    if str(date) in D.keys():
        return D[str(date)]
    else:
        conv_date = datetime.datetime.strptime(date,'%Y-%m-%d')
        prev_date = datetime.datetime.strftime(conv_date-datetime.timedelta(days=1),'%Y-%m-%d')
        next_date = datetime.datetime.strftime(conv_date+datetime.timedelta(days=1),'%Y-%m-%d')
        

        if all(key in D for key in (prev_date, next_date)):
            avg = (D[prev_date] + D[next_date]) // 2
            # Updating Orginal Dict
            D[date] = avg

            return avg
        elif prev_date in D.keys():
            l_value = 2 * D[prev_date]
            r_value = D[list(D)[-1]]
            avg = (l_value + r_value) // (3 * (2 ** (gap-3)))

            D[date] = avg
            return avg

        else:
            return 0


def solution(D):
    last_key = list(D)[-1]
    first_key = list(D)[0]

    startDate = datetime.datetime.strptime(first_key, '%Y-%m-%d')
    endDate = datetime.datetime.strptime(last_key, '%Y-%m-%d')

    days = (endDate - startDate).days
    allDates = {datetime.datetime.strftime(startDate+datetime.timedelta(days=k), 
                                       "%Y-%m-%d"):getAvg(datetime.datetime.strftime(startDate+datetime.timedelta(days=k), 
                                       "%Y-%m-%d"),D,days) for k in range(days+1)}

    return allDates