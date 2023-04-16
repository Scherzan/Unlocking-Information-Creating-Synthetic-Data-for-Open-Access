Unlocking Information - 
Creating Synthetic Data for Open Access
===

![PyConDE](./images/pyconde_official.png)

This repo provides the slides and the materials
for [my talk at PyConDE/PyDataBerlin 2023](https://2023.pycon.de/program/J9KRKZ/), on Wednesday April 20th.

# To watch the slides on localy follow these steps:

### Installation

```bash
pip install -r requirements.txt
```
I used python version 3.10.10.

### Pull and prepare the data

Download the data from:
https://zenodo.org/record/7669442#.ZDv6uI5ByEI
The File is named app_data.xlsx

run data_gen.py with the downloaded file once in order to create the subsample used as demo data in the talk


### Start the presentation

Just run:

```bash
streamlit run Unlocking_Information_with_Synthetic_Data.py
```

You should see the first slide with the title:
Unlocking Information - 
Creating Synthetic Data for Open Access

### Additional material

Find accompanying notebooks in the demo_notebook folder
Check out the mindmap on synthetic data in the ressources folder
Some content not covered in the talk:
- tuning ctgan with ray
- conditional sampling tutorial
- Gaussian Copula and Copula GAN demo

### Collaboration
