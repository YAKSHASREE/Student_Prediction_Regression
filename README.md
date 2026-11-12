# Student Performance Prediction Using Machine Learning

## Project Overview

Student Performance Prediction is a Machine Learning web application developed using Python, Flask, and Multiple Linear Regression. The application predicts a student's Performance Index based on academic performance and lifestyle factors.

The system takes five input features from the user and uses a trained Machine Learning model to generate a predicted Performance Index through a web-based interface.

## Dataset Information

The project uses the Student Performance Dataset containing **10,000 records and 6 columns**.

### Features Description

| Feature                          | Description                                          |
| -------------------------------- | ---------------------------------------------------- |
| Hours Studied                    | Number of hours spent studying                       |
| Previous Scores                  | Student's previous academic scores                   |
| Extracurricular Activities       | Participation in extracurricular activities (Yes/No) |
| Sleep Hours                      | Number of hours spent sleeping                       |
| Sample Question Papers Practiced | Number of sample question papers practiced           |
| Performance Index                | Target variable to be predicted                      |

### Dataset Summary

* Total Records: 10,000
* Total Columns: 6
* Independent Features: 5
* Target Variable: Performance Index
* Missing Values: 0
* Training Data: 80% (8,000 records)
* Testing Data: 20% (2,000 records)

## Technologies Used

* **Programming Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib
* **Machine Learning:** Scikit-learn
* **Algorithm:** Multiple Linear Regression
* **Backend:** Flask
* **Frontend:** HTML, CSS
* **Model Serialization:** Pickle
* **Deployment:** Render, Gunicorn

## Project Structure

```text
Student_Performance_Regression/
│
├── main.py
├── SPR.py
├── SPR.pkl
├── Student_Performance.csv
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

### File Description

| File                      | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| `SPR.py`                  | Data preprocessing, model training, evaluation and model saving |
| `main.py`                 | Flask application for handling user inputs and predictions      |
| `SPR.pkl`                 | Saved trained Machine Learning model                            |
| `Student_Performance.csv` | Dataset used for training                                       |
| `index.html`              | Web interface developed using HTML and CSS                      |
| `requirements.txt`        | Required Python dependencies                                    |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```powershell
cd Student_Performance_Regression
```

### 3. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 4. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```powershell
pip install -r requirements.txt
```

## Requirements

Create a `requirements.txt` file:

```text
numpy
pandas
matplotlib
scikit-learn>=1.4
flask
gunicorn
```

## Model Development and Training

The Machine Learning workflow is implemented in `SPR.py`.

### 1. Data Loading

The dataset is loaded using Pandas.

```python
self.df = pd.read_csv(path)
```

### 2. Data Preprocessing

Categorical data is converted into numerical values.

```python
self.df['Extracurricular Activities'] = self.df[
    'Extracurricular Activities'
].map({'Yes': 1, 'No': 0}).astype(int)
```

### 3. Feature Selection

The independent variables and target variable are separated.

```python
self.X = self.df.iloc[:, :-1]
self.y = self.df.iloc[:, -1]
```

### 4. Train-Test Split

The dataset is divided into 80% training data and 20% testing data.

```python
self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
    self.X,
    self.y,
    test_size=0.2,
    random_state=42
)
```

### 5. Model Building

Multiple Linear Regression is used to train the model.

```python
self.reg = LinearRegression()
self.reg.fit(self.X_train, self.y_train)
```

### 6. Model Evaluation

The trained model is evaluated using:

* R² Score
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

### 7. Model Saving

The trained model is saved using Pickle.

```python
with open("SPR.pkl", "wb") as f:
    pickle.dump(self.reg, f)
```

### Run the Training File

```powershell
python SPR.py
```

This command performs data preprocessing, trains the model, evaluates its performance, and saves the trained model as `SPR.pkl`.

## Model Evaluation Results

The model was evaluated using 8,000 training records and 2,000 testing records.

### Training Performance

| Evaluation Metric       |  Result |
| ----------------------- | ------: |
| R² Score                | 0.98869 |
| Mean Squared Error      |  4.1697 |
| Root Mean Squared Error |  2.0420 |

### Testing Performance

| Evaluation Metric       |  Result |
| ----------------------- | ------: |
| R² Score                | 0.98898 |
| Mean Squared Error      |  4.0826 |
| Root Mean Squared Error |  2.0206 |

### Performance Summary

* Training R² Score: 98.87%
* Testing R² Score: 98.90%
* Testing RMSE: 2.02
* Testing MSE: 4.08

The testing R² score indicates that the model explains approximately 98.90% of the variance in the target variable on the test dataset.

## Running the Flask Application

After training the model and generating `SPR.pkl`, execute:

```powershell
python main.py
```

The Flask application will run at:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser to access the application.

## Application Screenshots

### Home Page

The home page provides an interface to enter student details.

![Home Page](screenshots/home.png)

### Student Input Form

Users can enter the following details:

* Hours Studied
* Previous Scores
* Extracurricular Activities
* Sleep Hours
* Sample Question Papers Practiced

![Input Form](screenshots/input.png)

### Prediction Result

The application displays the predicted Performance Index after submitting the input details.

![Prediction Result](screenshots/result.png)



## Sample Prediction

The model was tested with the following sample input:

| Feature                          | Input Value |
| -------------------------------- | ----------: |
| Hours Studied                    |           4 |
| Previous Scores                  |          90 |
| Extracurricular Activities       |     Yes (1) |
| Sleep Hours                      |           8 |
| Sample Question Papers Practiced |           4 |

**Predicted Performance Index: 74.21**

## Deployment Using Render

The Flask application can be deployed on Render using Gunicorn.

### Step 1: Push the Project to GitHub

```powershell
git init
git add .
git commit -m "Student Performance Prediction"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

### Step 2: Create a Web Service

1. Visit [Render](https://render.com/).
2. Log in to your account.
3. Select **New + → Web Service**.
4. Connect your GitHub repository.
5. Select your project repository.

### Step 3: Configure Deployment

Use the following configuration:

| Setting       | Value                             |
| ------------- | --------------------------------- |
| Environment   | Python 3                          |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn main:app`               |

### Step 4: Deploy

Click **Deploy Web Service** and wait for the deployment to complete.

Once deployed, Render provides a public URL to access the application.

**Deployment Note:** Ensure that `SPR.pkl` is included in your repository or generated during deployment before the Flask application starts.

## Future Enhancements

* Improve the user interface and responsiveness.
* Add interactive data visualizations.
* Experiment with additional Machine Learning algorithms.
* Implement prediction history.
* Include additional student-related features for performance analysis.

## Author

Developed as a Machine Learning project using Python and Flask.

**Project Domain:** Machine Learning
**Algorithm:** Multiple Linear Regression

---

If you find this project useful, consider giving the repository a star!
