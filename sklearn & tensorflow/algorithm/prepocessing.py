import os

''' Data prepocessing '''
if os.path.exists('input/') is True and os.path.exists('output/') is False:
    print('Begin data preporcessing, transfer data_batch_1/5 --> data_batch_1/10 ')
    os.system('mkdir output')
    os.system('split -n 2 -d --additional-suffix=.bin input/data_batch_1.bin output/data_batch_1-')
    os.system('split -n 2 -d --additional-suffix=.bin input/data_batch_2.bin output/data_batch_2-')
    os.system('split -n 2 -d --additional-suffix=.bin input/data_batch_3.bin output/data_batch_3-')
    os.system('split -n 2 -d --additional-suffix=.bin input/data_batch_4.bin output/data_batch_4-')
    os.system('split -n 2 -d --additional-suffix=.bin input/data_batch_5.bin output/data_batch_5-')

    os.system('mv output/data_batch_1-00.bin output/data_batch_1.bin')
    os.system('mv output/data_batch_1-01.bin output/data_batch_2.bin')
    os.system('mv output/data_batch_2-00.bin output/data_batch_3.bin')
    os.system('mv output/data_batch_2-01.bin output/data_batch_4.bin')
    os.system('mv output/data_batch_3-00.bin output/data_batch_5.bin')
    os.system('mv output/data_batch_3-01.bin output/data_batch_6.bin')
    os.system('mv output/data_batch_4-00.bin output/data_batch_7.bin')
    os.system('mv output/data_batch_4-01.bin output/data_batch_8.bin')
    os.system('mv output/data_batch_5-00.bin output/data_batch_9.bin')
    os.system('mv output/data_batch_5-01.bin output/data_batch_10.bin')
else:
    print('No input file, or have already finished data prepocessing. Begin to Training...')