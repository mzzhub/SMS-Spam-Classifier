# SMS Spam Classifier

This project is an SMS Spam Classifier that uses machine learning to distinguish between spam and ham (legitimate) messages.

## Project Structure

```
├── model.pkl            # Trained model exported from Jupyter Notebook
├── README.md            # Project documentation
├── requirements.txt     # Dependencies
├── sms.ipynb            # Jupyter Notebook for training and exporting the model
├── spam.csv             # Dataset used for training
├── streamlit_app.py     # Streamlit app for user interface
├── vectorizer.pkl       # Exported function for text vectorization
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Jupyter Notebook
To retrain the model, open and run `sms.ipynb`:
   ```sh
   jupyter notebook sms.ipynb
   ```

### Running the Streamlit App
To use the SMS spam classifier via a web interface:
   ```sh
   streamlit run streamlit_app.py
   ```

## Model Details
- The model is trained using a dataset of SMS messages (`spam.csv`).
- Text preprocessing includes tokenization and vectorization (stored in `vectorizer.pkl`).
- The trained model is saved as `model.pkl` for future predictions.

## Contributions
Feel free to fork, improve, and submit pull requests.

## License
This project is open-source. Modify and use it as needed.

