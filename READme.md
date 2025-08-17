# Cloning Repository and virtual environements.

First we cloned the 20th-century repository.
We transfered the documents : requierements_1.4.txt and 1.4 Accesing web data without API-final.ipynb from the old file in Desktop to the new cloned one
called 20th-Century. After we proceded to delete the file on the Desktop.
We created a new virtual environement for the task Achievement 1.4 named venv_1.4 and we downloaded Python 3.9 to downgrade Python 3.12  because the projects
requierements were not fully compatible with the newer Python versions. Downgrading Python fixed the errors we were encountering.
We Installed Numpy 1.23 because they are certain  libraries  on the project just would work with that version. Then we activated the environement.

# Reproductible Set Up

## Cloning the Repository
1. Go to Desktop : cd ~/Desktop
2. Cloning Repository: git clone git@github.com:Javquezadaa/20th-century.git
3. Going to the folder : cd 20th-century

## Moving Jupyter Notebook and files into the new repository
1. Example: move Task 1.4 notebook into the repo folder: mv ~/Desktop/Task\ 1.4.ipynb

## Creating a Virtual environement with Python 3.9
1. conda create-n venv_1.4 python=3.9

## Activate Environement.
1. conda activate venv_1.4


2. Cloning Repository: git clone git@github.com:Javquezadaa/20th-century.git
3. Going to the folder : cd 20th-century

## Moving Jupyter Notebook and files into the new repository
1. Example: move Task 1.4 notebook into the repo folder: mv ~/Desktop/Task\ 1.4.ipynb

## Creating a Virtual environement with Python 3.9
1. conda create-n venv_1.4 python=3.9

## Activate Environement.
1. conda activate venv_1.4

## Instaling Required Packages.
1. For example installing Numpy 1.23 : pip install  numpy==1.23
                                     : pip install pandas matplotlib jupyter

## Starting Jupyter: Opening a script or creating a new one.
1. Adding the Notebook to Git : git add " Task 1.4"
2. Commiting the changes : git commit -m "Add Task 1.4 notebook"
3. Pulling  any remote changes before pushing:  git pull origin main --rebase
4. Pushing to GitHub: git push origin main 
