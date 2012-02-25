default: average

average: 0original_data
	mkdir 1average_label
	paste 0original_data/*1.label > 1average_label/combine_label1.txt
	paste 0original_data/*2.label > 1average_label/combine_label2.txt
	cat 0original_data/1.txt 0original_data/2.txt | cut -f2 > 1average_label/1-2x.txt
	cat 1average_label/combine_label1.txt 1average_label/combine_label2.txt | awk '{print ($$1+$$2+$$3+$$4+$$5)/5}' > 1average_label/1-2y.txt
	paste 1average_label/1-2y.txt 1average_label/1-2x.txt > 1average_label/1-2yx.txt

clean:
	rm -rf 1average_label

graph:average
	R CMD BATCH code/visualize.r
