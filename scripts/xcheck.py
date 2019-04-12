import xlrd


def main():
    files = ["MLG F18EFG ABL_c.xlsx", "NLG F18EFG ABL_c.xlsx"]
    for f in files:
        wb = xlrd.open_workbook("../data/" + f)
        print("Check file", f)
        for sheet_name in wb.sheet_names():
            print("  Check sheet", sheet_name)
            sheet = wb.sheet_by_name(sheet_name)

            stack = []
            for r in range(1, sheet.nrows):
                part_number = _cell_str(sheet, r, 1)
                if part_number == "":
                    break

                level = int(sheet.cell_value(r, 0))
                while len(stack) > level:
                    stack.pop()

                if level > 0:
                    parent = _cell_str(sheet, r, 5)
                    if stack[level - 1] != parent:
                        print("    err: row %i next=%s but parent=%s" % (
                            r, parent, stack[level - 1]))
                stack.append(part_number)


def _cell_str(sheet, row, col) -> str:
    cell = sheet.cell(row, col)
    if cell is None:
        return ""
    if cell.value is None:
        return ""
    return str(cell.value).strip()


if __name__ == "__main__":
    main()