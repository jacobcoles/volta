#!/bin/bash

TASK=7
MODEL=vilbert
MODEL_CONFIG=vilbert_base
TASKS_CONFIG=vilbert_test_tasks
PRETRAINED=/home/guscoleja@GU.GU.SE/volta/checkpoints/mscoco/${MODEL}/RetrievalFlickr30k_${MODEL_CONFIG}/pytorch_model_18.bin
OUTPUT_DIR=results/mscoco/${MODEL}


cd ../../..
python3.6 eval_retrieval.py \
	--config_file config/${MODEL_CONFIG}.json --from_pretrained ${PRETRAINED} \
	--tasks_config_file config_tasks/${TASKS_CONFIG}.yml --task $TASK --split test --batch_size 1 \
	--output_dir ${OUTPUT_DIR}


