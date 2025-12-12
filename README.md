## NxLog Assessment Submission

---


### Libraries and Framework

---

- [ ] [pyest-playwright](https://pypi.org/project/pytest-playwright/)
- [ ] [pyest-html](https://pypi.org/project/pytest-html/)
---

### Virtual Environment

---

It is a good practise to create a virtual environment. It allows the ability to configure dependencies exclusively for each project. There are several ways to create a virtual environment and one of them is through `virtualenv`.

- Check if you already have virtualenv with `virtualenv --version`. 
- To create this first install virtual environment with `pip install virtualenv`

---
### Setup 

---

- Clone repository into your local machine using `git clone https://github.com/bhadmus/nxlog-assessment.git`
- Navigate to the cloned folder and open a terminal within the root directory.
- Create a virtual environment with `virtualenv <name-of-env>` (common names include venv, .venv, env)
- Activate the virtual environment by;
  - MacOS =: `source <name-of-env>/bin/activate` 
  - Windows with CMD =: `.\<name-of-env>\Scripts\activate.bat`
  - Windows with powershell =: `.\<name-of-env>\Scripts\activate.ps1`
- Now that the virtual environment is activated, execute the command `pip install -r requirements.txt` to install all dependencies for the project.
---
### Execution

---

To execute the project you can do the following;
- Run headless =: `pytest`
- Run headless and generate report =: `pytest --html=<report-folder-destination>/<html-file-name>.html`. Common names used include; `test-results/reports.html`, `reports/result.html`. You decide to just collect the html file only as well by removing the directory part
- Run with browser =: `pytest --headed`
- Run with browser and generate report =: `pytest --headed --html=<report-folder-destination>/<html-file-name>.html`.
---
### Contact

---
All issues can be sent to me via [email](mailto:bhadmusademola.1@gmail.com) or connect with me on
[LinkedIn](https://www.linkedin.com/in/ademola-bhadmus)