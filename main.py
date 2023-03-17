from algorithm import Exercise28ProbesCangur
#import time


def main():
    banana = [
        ['b', 'a', 'n'],
        ['a', 'n', 'a'],
        ['n', 'a', 'n']
    ]   
    
    #startTime = time.time()
    print(Exercise28ProbesCangur(banana, 'banana').calculate())

    #print(time.time() - startTime)

if __name__ == '__main__':
    main()