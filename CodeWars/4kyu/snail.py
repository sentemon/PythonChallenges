def snail(array):
    result: list[int] = []; exec("while array:\n\tresult += array.pop(0)\n\tif array and array[0]:\n\t\tfor row in array: result.append(row.pop(-1))\n\tif array:\n\t\tresult += array.pop(-1)[::-1]\n\tif array and array[0]:\n\t\tfor row in array[::-1]: result.append(row.pop(0))"); return result