# cognilearn
A set of some ML utils frequently used by me while working as Data Scientist in Cognizant

## Getting Started
These instructions will get you a copy of the library up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
You need Python 3.x.x for sure, and following libraries
1. scikit-learn
2. pandas
3. matplotlib
4. seaborn

### Installing
Follwoing step by step commands will tell you how to get a library running

1. Firstly install the prerequisites
```
pip install -r requirements.txt
```

2. Now build the wheel package
```
python setup.py sdist bdist_wheel
```

3. This command should output a lot of text and once completed should generate two files in the dist directory:
```
dist/
  cognilearn_adityajain-0.0.3-py3-none-any.whl
  cognilearn_adityajain-0.0.3.tar.gz
```

4. Go to dist directory and install package using following command
```
pip install cognilearn_adityajain-0.0.3-py3-none-any.whl
```


## Package Discription/Tree
Currently package contains following features. More will be added soon

1. In cognilearn.metrics
	* sensitivity
	* specificity
	* accuracy
	* roc_curves
	* specificity_vs_sensitivity
	* confusion_matrix_modified

2. In cognilearn.feature_selection
	* backward_selection
	* forward_selection

3. In cognilearn.analysis
	* decile_analysis
	* information_value
	* prepareDeciles

4. In cognilearn.preprocessing
	* correlation_graph

5. In cognilearn.ensemble
	* Stacker


## Contributing

Please feel free to contribute to the library. If you have something which can ease the work of data scientist around the world, just fork repository and give a pull request or directly contact me and provide code snippet. I would love to put your name in contributors.

## Versioning

Current version is 0.0.3. We will release new version every month.

## Authors

* **Aditya Jain** - [Portfolio](https://adityajn105.github.io)

See also the list of [contributors](https://github.com/adityajn105/cognilearn/graphs/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](https://github.com/adityajn105/cognilearn/blob/master/LICENSE) file for details

## Acknowledgments

* Keshav Kumar
* Cognizant Data Science Team