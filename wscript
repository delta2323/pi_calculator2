import math
def options(opt):
  opt.load('maf')

def configure(conf):
  conf.load('maf')

def build(bld):
  pass

def experiment(exp):
  import random
  import plot.plot as p
  import maflib.util
  random.seed(0)

  simulator, result, log = 'app/simulator.py', 'result', 'log'
  simulation_num = 4
  exp(source = simulator,
      target = [result, log],
      parameters = maflib.util.product({'seed' : [random.randint(0, 1000) for i in xrange(4)],
                                        'sampling_num' : [int(math.pow(10, i)) for i in xrange(4)]
                                      }),
      rule = 'python ${SRC} ${sampling_num} ${seed} ${TGT[0].abspath()} > ${TGT[1].abspath()}'
  )

  average = 'average'
  exp(source = result,
      target = average,
      aggregate_by = ['seed'],
      rule = maflib.rules.average
  )

  plot = 'plot.png'
  exp(source = average,
      target = plot,
      aggregate_by = ['sampling_num'],
      rule = p.simple_plot
  )
