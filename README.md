Unlocking Information - 
Creating Synthetic Data for Open Access  
===
<div align="center">
<img src="./images/PyConDE_PyDataBer_circle_trans_500.png" data-canonical-src="./images/PyConDE_PyDataBer_circle_trans_500.png" width="100" />
</div>

This repo provides the slides and the materials
for [my talk at PyConDE/PyDataBerlin 2023]([https://www.youtube.com/watch?v=N1i_Z-WKaRs&list=PLGVZCDnMOq0peDguAzds7kVmBr8avp46K&index=14]), on Wednesday April 20th.

## To watch the slides you can follow these steps. 
You need to have Python 3.10 and uv installed.

### Clone the repository and navigate to the directory

Use git clone or your preferred method to download/clone the repo.


### Installation with uv

Navigate to your project directory and do:

```bash
uv venv --python 3.10
```
```bash
source .venv/bin/activate
```
```bash
uv pip install -r requirements.txt
```

### Start the presentation

Just run:

```bash
streamlit run 🔓_Synthetic_Data.py
```

You should see the first slide with the title:
Unlocking Information - 
Creating Synthetic Data for Open Access

### Additional material

Find accompanying notebooks in the demo_notebook folder

## GitHub Copilot Agent Documentation

If you're using GitHub Copilot with this repository, check out our comprehensive guide on how to use SKILL files, instruction files, prompt files, and agent files:

📖 **[GitHub Copilot Agents Guide](GITHUB_COPILOT_AGENTS.md)**

This guide covers:
- Understanding SKILL files, instruction files, prompt files, and agent files
- Where these files are located and how to organize them
- Typical use cases and examples
- How specs relate to the agent workflow
- Best practices for creating custom agents

