### Configure Local Environment

- Clone the project

  ```
  >> git clone _____
  ```

- Download the data

  - Downloaded from https://www.kaggle.com/datasets/kwentar/blur-dataset

  - Created the following directory structure under the project root:

    ```
    - datasets
    	- sharp
    	- blurry
    	- test
    ```

    - Sharp holds sharp images, blurry holds blurry images, and test holds a mix of both

  - Moved 350 sharp images from the downloaded sharp images directory to *blur-detection/datasets/sharp*

  - Moved 175 blurry images from each of the the two blurry image directories to *blur-detection/datasets/blurry*

  - Moved 70 sharp images from *blur-detection/datasets/sharp* to *blur-detection/datasets/test*

  - Moved 70 blurry images from *blur-detection/datasets/blurry* to *blur-detection/datasets/test* 

- Activate the virtual environment and import all required libraries

  ```
  >> python -m venv env
  
  >> source env/Scripts/activate
  
  >> python -m pip install -U jupyter numpy matplotlib pandas scipy scikit-learn scikit-image imutils opencv-python
  ```



### Train the Model

- Open a Jupyter notebook session from the project root

  ```
  >> jupyter notebook
  ```

- Open the *train.ipynb* file and run all of the scripts



### Test the Application

- Execute the script from the project root directory

  ```
  >> python controller.py
  ```