from math import *
from decimal import *
d = Decimal
getcontext().prec = 512

d9 = d('286386577668298411128469151667598498812366')
d8 = d('56130437228687557907788')
d7 = d('2414682040998')
d6 = d('7828354') #((5**d(10))-(5**d(9)))+((((5+168)*2)+7581)*2) just for funs
d5 = d('7581')
d4 = d('168')
d3 = d('20')
d2 = d('6')
d1 = d('3')
d0 = d('2')

'''
It is trivial to show the following...

>>> (log(d1, pi) / log(d0, d3))
4.147811090177013
>>> (log(d2, pi) / log(d1, d3))
4.268106353358759
>>>
>>> (log(d3, pi) / log(d2, d3))
4.375455454718115
>>> (log(d3, pi) / log(d2, d4))
7.483871753620199
>>> (log(d3, pi) / log(d2, d3))
4.375455454718115
>>> (log(d4, pi) / log(d3, d3))
4.4761336650184775
>>> (log(d5, pi) / log(d4, d3))
4.562582269225801
>>> (log(d6, pi) / log(d5, d3))
4.649961795684958
>>> (log(d7, pi) / log(d6, d3))
4.700785337247993
>>> (log(d8, pi) / log(d7, d3))
4.8077858456397955
>>> (log(d9, pi) / log(d8, d3))
4.769043170541039

The ratio of the logs of d8 and d7 are higher than the subsequent quotient of the log of d9 to d8, but the quotient of d9 to d8 is, critically, not lower than the previous quotient. The values in the series generally increase, so this demonstrates a soft bound.

Based on this if we output the results...
'''

print(d(e)**((d(log(d9, d3))*d('4.769043170541039'))*d(log(pi))))

'''
We see that this generally agrees with the estimate given on John Cook's blog.
And is well within the bounds given in other posts.

If we assign these values to a variable, and look at the ratio of each subsequent pair, as a sliding window, like so..
'''

r = [4.147811090177013, 4.268106353358759, 4.375455454718115, 4.4761336650184775, 4.562582269225801, 4.649961795684958, 4.700785337247993, 4.8077858456397955, 4.769043170541039]

r.reverse()

'''

A couple samples shows us that
>>> r[0]/r[1]
0.991941680361264
>>> r[1]/r[2]
1.0227622621998826
>>> r[2]/r[3]
1.0109298836842482
>>> r[3]/r[4]
1.019151331702778

And following from that..
>>> 1/0.991941680361264
1.0081237836843404
>>> 1.0109298836842482/(1/0.991941680361264)
1.0027834875491703

Seems like a big jump, but except for that aberration, previous pairs had a ratio of
>>> 1.019151331702778/1.0109298836842482
1.00813256008277

Which is actually in line with the expected rate.

So if we multiply r[0] by 1.0081237836843404, we should get the quotient for the logarithms of D(10) to D(9)

'''

d10log = r[0]*1.0081237836843404
print(d10log)
'''

should give you 4.8077858456397955

with that in hand we do a little math to find an estimate of the next dedekind, D(10)
'''

d10est = (d(e)**((d(log(d9, d3))*d('4.8077858456397955'))*d(log(pi)))) / (10**d(76))
print(d10est)

'''

which should give you a number roughly equal to 1.454560726301921*(10**(76))

Given John Cook's estimate, and the fact the logarithmic series here demonstrates a general upward trend, and his lowest bound is 10**75 by heuristic, and the established hard upperbound is 10**83~, and my lowest lower bound is in the range of 10**50-ish, 
and we know, based on the series value, that the value can't generally be lower than about 1.454560726301921*(10**(76)),
that means this estimate is very likely *very* close to D(10)
'''