import numpy

a = numpy.array([['sfsdf','s']])
a = numpy.append(a, [['ssss','dd']], axis = 0)
print(a)
numpy.savetxt("countries.csv", a, delimiter=',', header="A,B", comments="", fmt = '%s')