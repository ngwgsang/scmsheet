from scmsheet import GoogleSheet


tool = GoogleSheet(
    secret_key_path="secret_key.json",
    sheet_key="1jwyagmLBOKaAYrrWiZr6sMp9C0VZMEXXXXXXXXXX"
)


# tool.insert_data(tab="YOUR_TAB", new_row= ["Hi there", "Bobs!"])
tool.get_all_data(tab="YOUR_TAB")