# MCQ Generator Application

This project is an MCQ (Multiple Choice Question) Generator Application built with Langchain and Streamlit. It uses the Google Generative AI API to create and evaluate multiple-choice questions from uploaded text or PDF files.

## Features

- Generate MCQs from PDF or TXT files
- Customize the number of questions, subject, and complexity level
- Evaluate and review generated questions
- Display results in a user-friendly table format

## Installation

1. Clone the repository:
git clone https://github.com/NishDananjaya/MCQ_Generator.git
cd MCQ_Generator

2. Install the required packages:
pip install -r requirements.txt

3. Set up your environment variables:
Create a `.env` file in the root directory and add your Google API key:
GOOGLE_API_KEY=your_api_key_here

## Usage

Run the Streamlit app:
streamlit run streamlitapp.py

Follow the on-screen instructions to:
1. Upload a PDF or TXT file
2. Specify the number of MCQs to generate
3. Enter the subject and complexity level
4. Click "Create MCQs" to generate and evaluate questions

## Project Structure

- `setup.py`: Package configuration file
- `streamlitapp.py`: Main Streamlit application
- `src/mcqgenerator/MCQGenerater.py`: Core logic for MCQ generation and evaluation
- `src/mcqgenerator/utils.py`: Utility functions for file reading and data processing

## Dependencies

- openai
- langchain
- streamlit
- python-dotenv
- PyPDF2

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/NishDananjaya/MCQ_Generator/issues) if you want to contribute.

## Author

- Nishan Dananjaya
- Email: dananjayanishanpro@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.