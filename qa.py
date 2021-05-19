import os
import pandas as pd
from ast import literal_eval


from cdqa.utils.converters import pdf_converter
from cdqa.pipeline import QAPipeline



df = pdf_converter(directory_path='./docs/')
pd.set_option('display.max_colwidth', -1)
cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)
cdqa_pipeline.fit_retriever(df=df)
import joblib
joblib.dump(cdqa_pipeline, './models/bert_qa_custom.joblib')




