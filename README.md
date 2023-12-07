# llm-pdf-extractor
This project demonstrates the use of llm for extracting and analyzing data from PDFs.
[![My text](./BillExtractor.png)


Setup new python environment.
python3 -m venv pdfenv
cd pdfenv
source bin/activate

## Features

- Upload the bill files from data directory in this Github. (or upload similiar files of your own)
- Click on the `Extractr Bill Data` button.
- See the power of LangChain with OpenAI LLM work.
- The summary of Bill Data will be displayed after LLM processing.
- Export summary as csv.

## Installation

This project requires requires [python](https://python.org/) v3+ to run. I have used [streamlit] (http://streamlit.io) for UI.

Install the dependencies and start the server.

```sh
pip install langchain openai python_dotenv
```
If you get Error like 
`` pydantic.errors.PydanticUserError: If you use `@root_validator` with pre=False (the default) you MUST specify `skip_on_failure=True`. Note that `@root_validator` is deprecated and should be replaced with `@model_validator`.		``

Install a specific vesion of pydantic
```sh
pip install pydantic==1.10.9
```
Install other dependencies for PDF Reader and UI display. 
```sh
pip install streamlit
pip install pandas, regex, pypdf
```
If you get an error starting streamlit that says, (on MacOS)
`` INTEL MKL ERROR: dlopen(/Users/jay/opt/anaconda3/lib/libmkl_core.1.dylib, 9): image not found. ``
 run the following command.
```sh
conda install -c anaconda mkl
```
#### Start the server.
Type 
```sh
streamlit run app.py
```


