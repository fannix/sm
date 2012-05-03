default: 0extract_text_and_label

0extract_text_and_label:
	python code_svm_regression/0extract_text_and_label.py
	for f in data_svm_regression/1testset/*.txt; do cut -f1 $$f > $${f%.*}.time; done
	for f in data_svm_regression/1testset/*.txt; do cut -f2 $$f > $${f%.*}.text; done

1normalization: data_svm_regression/1testset data_svm_regression/1trainset
	#cat ~/weibo/data_svm_regression/1trainset/text1.txt | python code_svm_regression/1normalize_text.py > ~/weibo/data_svm_regression/2trainset_normalization/text1.txt
	#cat ~/weibo/data_svm_regression/1trainset/text2.txt | python code_svm_regression/1normalize_text.py > ~/weibo/data_svm_regression/2trainset_normalization/text2.txt
	for x in ~/weibo/data_svm_regression/1testset/*.text; do cat $$x | python code_svm_regression/1normalize_text.py > ~/weibo/data_svm_regression/2testset_normalization/$$(basename $$x); done

2segmentation: data_svm_regression/2trainset_normalization data_svm_regression/2testset_normalization
	#segment.sh -k pku ~/weibo/data_svm_regression/2trainset_normalization/text1.txt UTF-8 0 > ~/weibo/data_svm_regression/3trainset_segmenation/text1.txt
	#segment.sh -k pku ~/weibo/data_svm_regression/2trainset_normalization/text2.txt UTF-8 0 > ~/weibo/data_svm_regression/3trainset_segmenation/text2.txt
	for x in ~/weibo/data_svm_regression/2testset_normalization/*.text; do segment.sh -k pku $$x UTF-8 0 > ~/weibo/data_svm_regression/3testset_segmentation/$$(basename $$x); done

3postprocess: data_svm_regression/3trainset_segmenation data_svm_regression/3testset_segmentation
	#cat ~/weibo/data_svm_regression/3trainset_segmenation/text1.txt | python code_svm_regression/3postprocess.py > ~/weibo/data_svm_regression/4trainset_postprocess/text1.txt
	#cat ~/weibo/data_svm_regression/3trainset_segmenation/text2.txt | python code_svm_regression/3postprocess.py > ~/weibo/data_svm_regression/4trainset_postprocess/text2.txt
	#cat ~/weibo/data_svm_regression/4trainset_postprocess/text1.txt ~/weibo/data_svm_regression/4trainset_postprocess/text2.txt > ~/weibo/data_svm_regression/4trainset_postprocess/text_all.txt
	for x in ~/weibo/data_svm_regression/3testset_segmentation/*.text; do cat $$x | python code_svm_regression/3postprocess.py > ~/weibo/data_svm_regression/4testset_postprocess/$$(basename $$x); done

4text_to_libsvm: data_svm_regression/4trainset_postprocess/ data_svm_regression/4testset_postprocess/
	#rm -rf data_svm_regression/5trainset_libsvm/vocab.bin
	#rm -rf data_svm_regression/5trainset_libsvm/vocab.txt
	#python code_svm_regression/text_to_libsvm.py data_svm_regression/5trainset_libsvm/train.txt data_svm_regression/5trainset_libsvm/vocab < data_svm_regression/4trainset_postprocess/text_all.txt
	#cat data_svm_regression/1trainset/label1.txt data_svm_regression/1trainset/label2.txt | python code_svm_regression/labelizer.py  > data_svm_regression/5trainset_libsvm/train.label
	for x in ~/weibo/data_svm_regression/4testset_postprocess/*.text; do cat $$x | python code_svm_regression/text_to_libsvm.py  ~/weibo/data_svm_regression/5testset_libsvm/$$(basename $$x) ~/weibo/data_svm_regression/5trainset_libsvm/vocab; done

5predict: data_svm_regression/5testset_libsvm/ data_svm_regression/5trainset_libsvm/
	python code_svm_regression/regression.py train data_svm_regression/5trainset_libsvm/train.txt data_svm_regression/5trainset_libsvm/train.label data_svm_regression/5trainset_libsvm/regression.pickle
	for x in data_svm_regression/5testset_libsvm/*.text; do python code_svm_regression/regression.py predict data_svm_regression/5trainset_libsvm/vocab.txt $$x data_svm_regression/5trainset_libsvm/regression.pickle > data_svm_regression/6testset_libsvm/$$(basename $$x); done
	for x in data_svm_regression/6testset_libsvm/*.text; do paste data_svm_regression/1testset/$$(basename $${x%.*}).time $$x > $${x%.*}.all; done
