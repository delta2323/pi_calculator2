import random

def dist2(x, y):
    return x*x+y*y

class Simulator:
    def simulate(self, sampling_num):
        inside_circle = 0
        for i in xrange(sampling_num):
            x, y = random.random(), random.random()
            if dist2(x, y) < 1 : inside_circle += 1
        return float(4*inside_circle) / sampling_num

def main(sampling_num, output):
    s = Simulator()
    estimate = s.simulate(sampling_num)
    with open(output, 'w') as f:
        import json
        f.write(json.dumps({'estimate' : estimate}))

if __name__ == "__main__":
    import sys
    print 'Arguments:'
    print sys.argv
    main(int(sys.argv[1]), sys.argv[2])

