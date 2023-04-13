def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args,**kwargs)
        g.send(None)
        return g
    return inner

def subgenerator():
    x = 'Ready to except message'
    message = yield x
    print('Subgenerator received:', message)


class BlaBlaException(Exception):
    pass


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('All done (except StopIteration).')
            break
        except BlaBlaException:
            print('-------- (except BlaBlaException)')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
            print('average =', average)
    return average



if __name__ == '__main__':
    g = average()
    
    g.send(5)
    print(g)

    g.send(3)

    g.throw(BlaBlaException)

    try:
        g.throw(StopIteration)
    except StopIteration as e:
        print('Average =', e.value)
