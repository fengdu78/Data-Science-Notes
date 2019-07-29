pipe = make_pipeline(StandardScaler(), SGDClassifier(max_iter=1000))
param_grid = {'sgdclassifier__loss': ['hinge', 'log'],
              'sgdclassifier__penalty': ['l2', 'l1']}
grid = GridSearchCV(pipe, param_grid=param_grid, cv=3, n_jobs=-1)
scores = cross_validate(grid, X_breast, y_breast, scoring='balanced_accuracy', cv=3, return_train_score=True)
df_scores = pd.DataFrame(scores)
df_scores[['train_score', 'test_score']].boxplot()

grid.fit(X_breast_train, y_breast_train)
print(grid.best_params_)
