def faulty():
    raise Exception('Something is wrong!')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print 'Exception handled!'

handle_exception()

ignore_exception()
