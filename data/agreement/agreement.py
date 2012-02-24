"""
Compute the inter-annotator agreement
"""

import nltk
from nltk.metrics.agreement import AnnotationTask

t1 = AnnotationTask(data=[x.split() for x in open("1.txt")])
print t1.kappa()
t2 = AnnotationTask(data=[x.split() for x in open("2.txt")])
print t2.kappa()
