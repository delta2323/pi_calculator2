import math
import maflib.plot
@maflib.plot.plot_by
def simple_plot(figure, data, parameter):
  estimates = sorted(data.get_data_1d('estimate', key='sampling_num').items())
  axes = figure.add_subplot(111)
  xs = map(lambda (x, _) : math.log10(x), estimates)
  ys = map(lambda (_, y): y[0], estimates)
  axes.plot(xs, ys)

