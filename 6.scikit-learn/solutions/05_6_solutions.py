from sklearn.compose import make_column_transformer
preprocessor = make_column_transformer((col_cat, pipe_cat, ), (col_num, pipe_num))
