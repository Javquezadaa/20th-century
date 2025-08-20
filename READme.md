# Cloning Repository and virtual environements.

We cloned the 20th-Century repository and transferred the files requirements_1.4.txt and 1.4 Accessing Web Data without API-final.ipynb from the Desktop to the repository, then deleted the originals from the Desktop.

A new virtual environment, venv_1.4, was created for Task Achievement 1.4. Python was downgraded to 3.9 to ensure compatibility with the project requirements, resolving prior errors. We installed NumPy 1.23 to meet library version requirements and then activated the virtual environment.



# Reproductible Set Up

## 1. Cloning the Repository
```bash
git clone git@github.com:Javquezadaa/20th-century.git

```

 Going to the folder : 
   ```bash 
   cd 20th-century
 
   ```

## 2. Moving Jupyter Notebook and files into the new repository
   
   Example: move Task 1.4 notebook into the repo folder: 
 ```bash    
 mv ~/Desktop/Task\ 1.4.ipynb
 
   ```


## 3. Creating a Virtual environement with Python 3.9

```bash
 conda create-n venv_1.4 python=3.9
```

## 4. Activate Environement.
```bash
 conda activate venv_1.4
 ```
Cloning Repository: 
```bash
git clone git@github.com:Javquezadaa/20th-century.git
```
 Going to the folder :
 
 ```bash
  cd 20th-century
  ```

## 5. Moving Jupyter Notebook and files into the new repository
 Example: move Task 1.4 notebook into the repo folder:
 
 ```bash
  mv ~/Desktop/Task\ 1.4.ipynb
```

## 6. Creating a Virtual environement with Python 3.9
 ```bash
conda create-n venv_1.4 python=3.9
   ```

## 7. Activate Environement.
```bash 
conda activate venv_1.4
```

## 8. Instaling Required Packages.
For example installing Numpy 1.23 : 

```bash 
pip install  numpy==1.23
pip install pandas matplotlib jupyter
```

## 9. Starting Jupyter: Opening a script or creating a new one.

a. Adding the Notebook to Git : 
```bash
git add " Task 1.4"
```

b. Commiting the changes :
```bash
 git commit -m "Add Task 1.4 notebook" 
 ```
c. Pulling  any remote changes before pushing:  
```bash
 git pull origin main --rebase
 ```
d. Pushing to GitHub: 
```bash
git push origin main 
```