import xlrd as excel
import numpy as numpy
import matplotlib.pyplot as pl
import math as math


my_book = excel.open_workbook('B://Softwares//ML_course_dataset//university data.xlsx');
university_data = my_book.sheet_by_index(0)
print("UBitName: ", 'ronakhem')
print('personNumber: ', '50205775')


number_of_rows = university_data.nrows - 2
cs_score = []
research_overhead = []
base_pay = []
tuition = []
sum1 = 0
mu1 = 0

for rownum in range(1, university_data.nrows - 1):
    sum1 += university_data.cell(rownum, 2).value
    cs_score.append(university_data.cell(rownum, 2).value)
# print('The total of column 1 is ', sum)
mu1 = sum1 / (university_data.nrows - 2)
print('mu1 = ', round(mu1, 3))


sum2 = 0
mu2 = 0
for rownum in range(1, university_data.nrows - 1):
    sum2 += university_data.cell(rownum, 3).value
    research_overhead.append(university_data.cell(rownum, 3).value)
mu2 = sum2 / (university_data.nrows - 2)
print('mu2 = ', round(mu2, 3))

sum3 = 0
mu3 = 0
for rownum in range(1, university_data.nrows - 1):
    sum3 += university_data.cell(rownum, 4).value
    base_pay.append(university_data.cell(rownum, 4).value)
mu3 = sum3 / (university_data.nrows - 2)
print('mu3 = ', round(mu3, 3))

sum4 = 0
mu4 = 0
for rownum in range(1, university_data.nrows - 1):
    sum4 += university_data.cell(rownum, 5).value
    tuition.append(university_data.cell(rownum, 5).value)
mu4 = sum4 / (university_data.nrows - 2)
print('mu4 = ', round(mu4, 3))

print('var1 = ', round(numpy.var(cs_score), 3))
print('var2 = ', round(numpy.var(research_overhead), 3))
print('var3 = ', round(numpy.var(base_pay), 3))
print('var4 = ', round(numpy.var(tuition), 3))
print('sigma1 = ', round(numpy.std(cs_score), 3))
print('sigma2 = ', round(numpy.std(research_overhead), 3))
print('sigma3 = ', round(numpy.std(base_pay), 3))
print('sigma4 = ', round(numpy.std(tuition), 3))


a = numpy.array(cs_score)
b = numpy.array(research_overhead)
c = numpy.array(base_pay)
d = numpy.array(tuition)
x = numpy.vstack((a, b, c, d))
print('----------------4x4 covariance matrix-------------')
print(numpy.around(numpy.cov(x), 3))
print('----------------4x4 correlation matrix-------------')
print(numpy.around(numpy.corrcoef(x), 3))
print('The most correlated variables are cs_score and research_overhead with value ', 0.456)
print('The least correlated variables are base_pay and tuition with value ', -0.245)


def get_probability_value(mean, variance, value):
    var1 = 1/numpy.sqrt(2 * variance * math.pi)
    var2 = math.pow(value - mean, 2)
    var3 = 2 * variance
    var4 = -(var2 / var3)
    return normpdf(value,mean,variance);


def normpdf(x, mean, var):
    # var = float(sd)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for rownum in range(1, university_data.nrows-1):
    cellValue = university_data.cell(rownum, 2).value
    probability = get_probability_value(mu1, round(numpy.var(cs_score), 3), cellValue)
    sum1 += numpy.log(probability)
print('CS MLE', ' : ', round(sum1, 3))

for rownum in range(1, university_data.nrows-1):
    cellValue = university_data.cell(rownum, 3).value
    probability = get_probability_value(mu2, round(numpy.var(research_overhead), 3), cellValue)
    sum2 += numpy.log(probability)
print('research overhead MLE', ' : ',round(sum2, 3))

for rownum in range(1, university_data.nrows-1):
    cellValue = university_data.cell(rownum, 4).value
    probability = get_probability_value(mu3, round(numpy.var(base_pay), 3), cellValue)
    sum3 += numpy.log(probability)
print('base pay MLE', ' : ',  round(sum3, 3))

for rownum in range(1, university_data.nrows-1):
    cellValue = university_data.cell(rownum, 5).value
    probability = get_probability_value(mu4, round(numpy.var(tuition), 3), cellValue)
    sum4 += numpy.log(probability)
print('tuition', ' : ', round(sum4, 3))

print('logLikelihood:', round(sum1+sum2+sum3+sum4, 3))

f, axarr = pl.subplots(4, 4)
axarr[0, 0].scatter(cs_score, cs_score)
axarr[0, 0].set_xlabel('CS score')
axarr[0, 0].xaxis.set_label_position('top')
axarr[0, 0].set_ylabel('CS score')
axarr[0, 0].yaxis.set_label_position('left')
axarr[0, 1].scatter(cs_score, base_pay)
axarr[0, 1].set_xlabel('base_pay')
axarr[0, 1].xaxis.set_label_position('top')
axarr[0, 2].scatter(cs_score, research_overhead)
axarr[0, 2].set_xlabel('research_overhead')
axarr[0, 2].xaxis.set_label_position('top')
axarr[0, 3].scatter(cs_score, tuition)
axarr[0, 3].set_xlabel('tuition')
axarr[0, 3].xaxis.set_label_position('top')

axarr[1, 0].scatter(base_pay, cs_score)
axarr[1, 0].set_ylabel('base_pay')
axarr[1, 0].yaxis.set_label_position('left')
axarr[1, 1].scatter(base_pay, base_pay)
axarr[1, 2].scatter(base_pay, research_overhead)
axarr[1, 3].scatter(base_pay, tuition)

axarr[2, 0].scatter(research_overhead, cs_score)
axarr[2, 0].set_ylabel('research_overhead')
axarr[2, 0].yaxis.set_label_position('left')
axarr[2, 1].scatter(research_overhead, base_pay)
axarr[2, 2].scatter(research_overhead, research_overhead)
axarr[2, 3].scatter(research_overhead, tuition)


axarr[3, 0].scatter(tuition, cs_score)
axarr[3, 0].set_ylabel('tuition')
axarr[3, 0].yaxis.set_label_position('left')
axarr[3, 1].scatter(tuition, base_pay)
axarr[3, 2].scatter(tuition, research_overhead)
axarr[3, 3].scatter(tuition, tuition)

# f.tight_layout()
f.subplots_adjust(hspace=.18)
f.subplots_adjust(wspace=.41)
f.subplots_adjust(top=.95)
f.subplots_adjust(right=.98)
f.subplots_adjust(left=.05)
f.subplots_adjust(bottom=.03)

x0 = numpy.ones(shape=(1, 49))
a00 = x0*x0
a01 = base_pay*x0
a02 = tuition*x0
a03 = research_overhead*x0

a10 = base_pay*x0
a11 = numpy.array(base_pay)*numpy.array(base_pay)
a12 = numpy.array(tuition)*numpy.array(base_pay)
a13 = numpy.array(research_overhead)*numpy.array(base_pay)

a20 = tuition*x0
a21 = numpy.array(base_pay)*numpy.array(tuition)
a22 = numpy.array(tuition)*numpy.array(tuition)
a23 = numpy.array(research_overhead)*numpy.array(tuition)

a30 = numpy.array(research_overhead)*x0
a31 = numpy.array(base_pay)*numpy.array(research_overhead)
a32 = numpy.array(tuition)*numpy.array(research_overhead)
a33 = numpy.array(research_overhead)*numpy.array(research_overhead)

sum_a00 = 0
sum_a01 = 0
sum_a02 = 0
sum_a03 = 0

sum_a10 = 0
sum_a11 = 0
sum_a12 = 0
sum_a13 = 0

sum_a20 = 0
sum_a21 = 0
sum_a22 = 0
sum_a23 = 0

sum_a30 = 0
sum_a31 = 0
sum_a32 = 0
sum_a33 = 0

# ------------------------------

for i in range(0, a00.size-1):
    sum_a00 += a00[0][i]

for i in range(0, a01.size-1):
    sum_a01 += a01[0][i]

for i in range(0, a02.size-1):
    sum_a02 += a02[0][i]

for i in range(0, a03.size-1):
    sum_a03 += a03[0][i]

# ------------------------------
for i in range(0, a10.size-1):
    sum_a10 += a10[0][i]

for i in range(0, a11.size-1):
    sum_a11 += a11[i]

for i in range(0, a12.size-1):
    sum_a12 += a12[i]

for i in range(0, a13.size-1):
    sum_a13 += a13[i]

# ------------------------------
for i in range(0, a20.size-1):
    sum_a20 += a20[0][i]

for i in range(0, a21.size-1):
    sum_a21 += a21[i]

for i in range(0, a22.size-1):
    sum_a22 += a22[i]

for i in range(0, a23.size-1):
    sum_a23 += a23[i]

# ------------------------------
for i in range(0, a30.size-1):
    sum_a30 += a30[0][i]

for i in range(0, a31.size-1):
    sum_a31 += a31[i]

for i in range(0, a32.size-1):
    sum_a32 += a32[i]

for i in range(0, a33.size-1):
    sum_a33 += a33[i]

A = numpy.zeros((4, 4))

A[0][0] = sum_a00
A[0][1] = sum_a01
A[0][2] = sum_a02
A[0][3] = sum_a03

A[1][0] = sum_a10
A[1][1] = sum_a11
A[1][2] = sum_a12
A[1][3] = sum_a13

A[2][0] = sum_a20
A[2][1] = sum_a21
A[2][2] = sum_a22
A[2][3] = sum_a23

A[3][0] = sum_a30
A[3][1] = sum_a31
A[3][2] = sum_a32
A[3][3] = sum_a33

y = numpy.zeros((4, 1))

y00 = x0*cs_score
y01 = numpy.array(base_pay)*numpy.array(cs_score)
y02 = numpy.array(tuition)*numpy.array(cs_score)
y03 = numpy.array(research_overhead)*numpy.array(cs_score)

y[0][0] = numpy.sum(y00)
y[1][0] = numpy.sum(y01)
y[2][0] = numpy.sum(y02)
y[3][0] = numpy.sum(y03)

matrix_A = numpy.matrix(A)
beta = matrix_A.I*y
sigma_squared = 0

for i in range(0, 49):
    term = beta[0][0]+(beta[1][0]*base_pay[i])+(beta[2][0]*tuition[i])+(beta[3][0]*research_overhead[i])-cs_score[i]
    sigma_squared += math.pow(term, 2)
sigma_squared /= (university_data.nrows-2)
l = 0
k = (-0.5)*numpy.log(2*math.pi*sigma_squared)
for i in range(0, 49):
    term = beta[0][0]+(beta[1][0]*base_pay[i])+(beta[2][0]*tuition[i])+(beta[3][0]*research_overhead[i])-cs_score[i]
    l += k-(0.5*(1/sigma_squared))*math.pow(term, 2)

bngraph = numpy.zeros((4, 4))
bngraph[1][0] = 1
bngraph[2][0] = 1
bngraph[3][0] = 1
print("BNgraph:")
print(bngraph)
print("BNlogLikelihood:", round(l+sum2+sum3+sum4, 3))
pl.show()
