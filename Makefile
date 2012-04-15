default: 0extract_text_and_label

0extract_text_and_label:
	#python code_svm_regression/0extract_text_and_label.py
	for f in data_svm_regression/1testset/*.txt; do cut -f1 $$f > $${f%.*}.time; done
	for f in data_svm_regression/1testset/*.txt; do cut -f2 $$f > $${f%.*}.text; done

1normalization: data_svm_regression/1testset data_svm_regression/1trainset

2segmentation: data_svm_regression/2trainset_normalization data_svm_regression/2testset_normalization
	for x in ~/weibo/data_svm_regression/2testset_normalization/*.text; do ./segment.sh pku $x UTF-8 0 > ~/weibo/data_svm_regression/3testset_segmentation/$$(basename $$x); done

3postprocess: data_svm_regression/3trainset_segmenation data_svm_regression/3testset_segmentation
	cat ~/weibo/data_svm_regression/3trainset_segmenation/text1.txt | python code_svm_regression/3postprocess.py > ~/weibo/data_svm_regression/4trainset_postprocess/text1.txt
	cat ~/weibo/data_svm_regression/3trainset_segmenation/text2.txt | python code_svm_regression/3postprocess.py > ~/weibo/data_svm_regression/4trainset_postprocess/text2.txt
	for x in ~/weibo/data_svm_regression/3testset_segmentation/*.text; do cat $$x | python code_svm_regression/3postprocess.py > ~/weibo/data_svm_regression/4testset_postprocess/$$(basename $$x); done

4text_to_libsvm: data_svm_regression/4trainset_postprocess/ data_svm_regression/4testset_postprocess/
	#rm -rf data_svm_regression/5trainset_libsvm/vocab.bin
	#python code_svm_regression/text_to_libsvm.py data_svm_regression/5trainset_libsvm/train.txt data_svm_regression/5trainset_libsvm/vocab < data_svm_regression/4trainset_postprocess/text_all.txt
	#cat data_svm_regression/1trainset/label1.txt data_svm_regression/1trainset/label2.txt | python code_svm_regression/labelizer.py  > data_svm_regression/5trainset_libsvm/train.label
	for x in ~/weibo/data_svm_regression/4testset_postprocess/*.text; do cat $$x | python code_svm_regression/text_to_libsvm.py  ~/weibo/data_svm_regression/5testset_libsvm/$$(basename $$x) ~/weibo/data_svm_regression/5trainset_libsvm/vocab; done

5predict: data_svm_regression/5testset_libsvm/ data_svm_regression/5trainset_libsvm/
	#python code_svm_regression/svm_regression.py train data_svm_regression/5trainset_libsvm/train.libsvm data_svm_regression/5trainset_libsvm/train.label data_svm_regression/5trainset_libsvm/SVR.pickle
	#for x in data_svm_regression/5testset_libsvm/*.text; do python code_svm_regression/svm_regression.py predict $$x data_svm_regression/5trainset_libsvm/SVR.pickle > data_svm_regression/6testset_libsvm/$$(basename $$x); done
	for x in data_svm_regression/6testset_libsvm/*.text; do paste data_svm_regression/1testset/$$(basename $${x%.*}).time $$x > $${x%.*}.all; done
