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

## Model Details
- The model is trained using a dataset of SMS messages (`spam.csv`).
- Text preprocessing includes tokenization and vectorization (stored in `vectorizer.pkl`).
- The trained model is saved as `model.pkl` for future predictions.

## Requirements
- Python
- Streamlit
- Nltk
- Scikit-learn

## Contributions
Feel free to fork, improve, and submit pull requests.

## License
This project is open-source. Modify and use it as needed.

## 🧑‍💻 Try the app.
[![image](https://github.com/user-attachments/assets/083fac81-15b5-46ad-a694-d94d9c23f68d)](https://sms-spam-classifier-by-mz.streamlit.app/)

