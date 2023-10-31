
![GitHub repo size](https://img.shields.io/github/repo-size/sangcamap/scmsheet?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/sangcamap/scmsheet?style=for-the-badge)

## Install
```
pip install git+https://github.com/sangcamap/scmsheet.git
```

## 🙌 Goals!

### Init

```python
from scmsheet import GoogleSheet

tool = GoogleSheet(
    secret_key_path="secret_key.json",
    sheet_key="1jwyagmLBOKaAYrrWiZr6sMp9C0VZMEXXXXXXXXXX"
)
```

### Read all data
```python
tool.get_all_data(tab="YOUR_TAB")
```
### Insert new row 
```python
tool.insert_data(tab="YOUR_TAB", new_row= ["Hi there", "Bobs!"])
```