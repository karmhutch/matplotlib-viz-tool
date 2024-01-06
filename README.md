This [visualization tool](https://github.com/karmhutch/matplotlib-viz-tool) 
was developed using Python v3.12.1 and Matplotlib v3.8.2. Its purpose is 
to automate the styling of single- and multi-axes figures. 


### **Files and Directories**

- changelog.md
- pyproject.toml
- LICENSE
- src/**vizkarmhutch**
  - style.py
  - functions.py


### **Installation Instructions**

The package *vizkarmhutch* has been uploaded to TestPyPI, which is an instance 
of PyPI (Python Package Index) used for testing. You can view the latest version
[here](https://test.pypi.org/project/vizkarmhutch/0.1.7/). You can see how to use 
the package in this [example](https://github.com/karmhutch/matplotlib-viz-tool/tree/main/examples). 
**Note that this package requires Python v3.10 or greater**. 

To install the package and its 
dependencies, execute the following in the command line:
```bash
pip install --upgrade pip matplotlib numpy pandas

pip install --upgrade -i https://test.pypi.org/simple/ vizkarmhutch
```