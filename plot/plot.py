import math
import maflib.plot
@maflib.plot.plot_by
def simple_plot(figure, data, parameter):
  estimates = data.get_data_1d('estimate', key='sampling_num')
  axes = figure.add_subplot(111)
  xs = map(lambda x: math.log10(x), estimates.keys())
  ys = map(lambda y: y[0], estimates.values())
  axes.plot(xs, ys)

