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

  simulator, result, log = 'app/simulator.py', 'result', 'log'
  simulation_num = 4
  exp(source = simulator,
      target = [result, log],
      parameters = [{'sampling_num' : int(math.pow(10, i)) for i in xrange(simulation_num)}],
      rule = 'python ${SRC} ${sampling_num} ${seed} ${TGT[0].abspath()} > ${TGT[1].abspath()}'
  )

  plot = 'plot.png'
  exp(source = result,
      target = plot,
      aggregate_by = ['sampling_num'],
      rule = p.simple_plot
  )
