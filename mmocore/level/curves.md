# 📈 Experience Curves

**This is a very technical feature, you will not learn anything by reading this page on its own (out of context). It should only be read if other wiki pages redirect you to this page.**

Experience curves allow you to define how much experience a player needs in order to level up either a profession or a class. All exp curves can be found under the `/MMOCore/expcurves` folder. You can setup an exp curve by creating a **.txt** file with the following format:
```
200
400
600
800
1000
1200
1400
1600
1800
2000
2200
2400
2600
...
```
The first line says how much exp a player needs in order to reach level 2, second line for level 3 and so on. Exp curves are not cumulative, which means that a player reaching a 200-exp level will lose these 200 exp points and will have to "start all over".

## Generating an EXP curve using Excel
Using Excel (you can use it for free online on the Microsoft website) you can easily generate a MMOCore exp curve **if you have a formula of needed exp as a function of the player level**.

![x3lXKwi](uploads/477b8c9c17ef4e24f3f3ca7bc0fd3da2/x3lXKwi.png)
On Excel, you can use the `ROW(CELL_NAME)` function to retrieve the cell line number. You can therefore, for instance, use this formula: `= 100 + ROW(A1) * 30` and duplicate the cell all the way down to generate a list of numbers which correspond to the amount of experience needed to reach the n-th level.

Once you have this setup, save your file **as a .txt** file using the **Text (tab separator)** file type. Make sure there is only one column so that there is no tab separator. Using this file format has the effect of losing all the cell formulas and directly saving the calculated values.
![3TIdlsd](uploads/9046a25b1df2b06516d936fed4674a12/3TIdlsd.png)

You should have generated a text file which has the same format as the MMOCore exp curves.