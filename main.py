from encodings.base64_codec import base64_decode

import xlrd as excel
import numpy as numpy
import pylab as pl
import math as math

my_book = excel.open_workbook('B://Softwares//ML_course_dataset//university data.xlsx');
# print('This workbook has ', my_book.nsheets, 'sheets')
# print(my_book.sheet_names())
university_data = my_book.sheet_by_index(0)
# print('The number of rows in current sheet is ', university_data.nrows)
# print('The number of columns in current sheet is ', university_data.ncols)
print("UBitName: ", 'ronakhem')
print('personNumber: ', '50205775')
# --------------------------------------
# routines for calculating mean of a variable
# ---------------------------------------
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
# --------------------------------------
# ---------------------------------------

sum2 = 0
mu2 = 0
for rownum in range(1, university_data.nrows - 1):
    sum2 += university_data.cell(rownum, 3).value
    research_overhead.append(university_data.cell(rownum, 3).value)
mu2 = sum2 / (university_data.nrows - 2)
print('mu2 = ', round(mu2, 3))

# --------------------------------------
# ---------------------------------------

sum3 = 0
mu3 = 0
for rownum in range(1, university_data.nrows - 1):
    sum3 += university_data.cell(rownum, 4).value
    base_pay.append(university_data.cell(rownum, 4).value)
mu3 = sum3 / (university_data.nrows - 2)
print('mu3 = ', round(mu3, 3))

# --------------------------------------
# ---------------------------------------

sum4 = 0
mu4 = 0
for rownum in range(1, university_data.nrows - 1):
    sum4 += university_data.cell(rownum, 5).value
    tuition.append(university_data.cell(rownum, 5).value)
mu4 = sum4 / (university_data.nrows - 2)
print('mu4 = ', round(mu4, 3))

# routines for calculating variance for each variable
# print('cs score ', cs_score)
# print('research overhead ', research_overhead)
# print('base pay ', base_pay)
# print('Tuition ', tuition)

# print('-------------variance ---------------------------')
print('var 1 = ', round(numpy.var(cs_score), 3))
print('var 2 = ', round(numpy.var(research_overhead), 3))
print('var 3 = ', round(numpy.var(base_pay), 3))
print('var 4 = ', round(numpy.var(tuition), 3))
print('std 1 = ', round(numpy.std(cs_score), 3))
print('std 2 = ', round(numpy.std(research_overhead), 3))
print('std 3 = ', round(numpy.std(base_pay), 3))
print('std 4 = ', round(numpy.std(tuition), 3))

# print('-------------covariance  matrix -----------------------')
# print(numpy.cov(cs_score, research_overhead))
# print(numpy.cov(cs_score, base_pay))
# print(numpy.cov(cs_score, tuition))
# print(numpy.cov(research_overhead, base_pay))
# print(numpy.cov(research_overhead, tuition))
# print(numpy.cov(base_pay, tuition))

# print('---------------correlation coefficients--------------------')
# print(numpy.corrcoef(cs_score, research_overhead))
# print(numpy.corrcoef(cs_score, base_pay))
# print(numpy.corrcoef(cs_score, tuition))
# print(numpy.corrcoef(research_overhead, base_pay))
# print(numpy.corrcoef(research_overhead, tuition))
# print(numpy.corrcoef(research_overhead, tuition))

a = numpy.array(cs_score)
b = numpy.array(research_overhead)
c = numpy.array(base_pay)
d = numpy.array(tuition)
x = numpy.vstack((a, b, c, d))
print('----------------4x4 covariance matrix-------------')
print(numpy.cov(x))
print('----------------4x4 correlation matrix-------------')
print(numpy.corrcoef(x))


def get_probability_value(mean, variance, value):
    var1 = 1/numpy.sqrt(2 * variance * math.pi)
    var2 = math.pow(value - mean, 2)
    var3 = 2 * variance
    var4 = -var2 / var3
    return var1 * math.exp(var4)
print('----values for cs score -------')
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for rownum in range(1, university_data.nrows-1):
    cellValue = university_data.cell(rownum, 2).value
    probability = get_probability_value(mu1, round(numpy.var(cs_score), 3), cellValue)
    sum1 += probability
    print(cellValue, ' : ', probability)

print('----values for research overhead -------')
for rownum in range(1, university_data.nrows-1):
    cellValue = university_data.cell(rownum, 3).value
    probability = get_probability_value(mu2, round(numpy.var(research_overhead), 3), cellValue)
    sum2 += probability
    print(cellValue, ' : ', probability)

print('----base pay  -------')
for rownum in range(1, university_data.nrows-1):
    cellValue = university_data.cell(rownum, 4).value
    probability = get_probability_value(mu3, round(numpy.var(base_pay), 3), cellValue)
    sum3 += probability
    print(cellValue, ' : ', probability)

print('----tuition -------')
for rownum in range(1, university_data.nrows-1):
    cellValue = university_data.cell(rownum, 5).value
    probability = get_probability_value(mu4, round(numpy.var(tuition), 3), cellValue)
    sum4 += probability
    print(cellValue, ' : ',probability)

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

pl.show()
