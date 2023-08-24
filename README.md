1. 先分析再寫，別邊寫邊改</br>
2. 背時間複雜度有哪些算法，不是背算法的時間複雜度</br>
3. 要練習邊說出來邊 coding</br>
4. 從 easy 開始慢慢把難度增加</br>
5. 可以用 print 在 Stdout 看結果</br>
6. 別宣告太多變數，讓單一變數覆蓋</br>
7. [sliding window](https://www.geeksforgeeks.org/window-sliding-technique/)</br>
8. [Time Complexity of the Built-in Python Functions](https://medium.com/@nedspnt/how-to-make-your-code-run-faster-time-complexity-of-the-built-in-python-functions-38a415008fa2)</br>
9. The easiest way to reduce the time complexity is to avoid a for loop whenever possible.</br>
10. code 太長換行用 \
11. [multiple OR in if statement?](https://stackoverflow.com/questions/17615020/what-is-the-best-approach-in-python-multiple-or-or-in-in-if-statement) : if cond in {'1','2','3','4'}:
12. [Putting a simple if-then-else statement on one line](https://stackoverflow.com/questions/2802726/putting-a-simple-if-then-else-statement-on-one-line) : 'Yes' if fruit == 'Apple' else 'No'</br>
13. [ValueError: Exceeds the limit (4300) for integer string conversion](https://stackoverflow.com/questions/73693104/valueerror-exceeds-the-limit-4300-for-integer-string-conversion) :</br>
   import sys</br>
   sys.set_int_max_str_digits(0)</br>
14. [caret (^) operator](https://stackoverflow.com/questions/2451386/what-does-the-caret-operator-do) : bitwise XOR (exclusive OR)</br>
15. list 用 l = sorted(l) 會比 l.sort() 還快</br>
16. 兩兩相乘的題目，迴圈的終點，可以思考用 int(num**0.5)+1 ex: #492 #507</br>
17. #557 用 list 去處理 for loop 的東西，會比用 string 的處理快</br>
18. 變數後面加底線 : 避免與 python 關鍵字衝突, ex: sum_, class_</br>
19. [How to Break out of multiple loops](https://www.geeksforgeeks.org/how-to-break-out-of-multiple-loops-in-python/?fbclid=IwAR3pOpp323cET1hE3HCNsOWO6sEwOpzrfwQzFpXx4lnzq4L6IN_V9v2OLMQ)
      * 若有多層 loops, break 只會跳出最內層
      * 若要一次跳出整個 loops
         * return
         * else: continue
         * use a flag variable
20. [difference between find and index](https://stackoverflow.com/questions/22190064/difference-between-find-and-index) : index 會比 find 更快
21. [What is the difference between dict and collections.defaultdict?](https://www.google.com/search?q=difference+between+defaultdict+and+dict&rlz=1C1CHBF_zh-TWTW1031TW1031&oq=&gs_lcrp=EgZjaHJvbWUqDAgBECMYJxjqAhiMBDIMCAAQIxgnGOoCGIwEMgwIARAjGCcY6gIYjAQyDAgCECMYJxjqAhiMBDIMCAMQIxgnGOoCGIwEMgwIBBAjGCcY6gIYjAQyDAgFECMYJxjqAhiMBDIMCAYQIxgnGOoCGIwEMgwIBxAjGCcY6gIYjATSAQgzNjAzajBqOagCCLACAQ&sourceid=chrome&ie=UTF-8): defaultdict will "default" a value if that key has not been set yet</br>
22. 從一串 list 中要找出某個 index 的題目, 可用 enumerate 發想</br>
23. 別用 one liner solution (要考慮到 readability)</br>
24. [Dynamic programming](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E6%BC%94%E7%AE%97%E6%B3%95%E7%AD%86%E8%A8%98%E7%B3%BB%E5%88%97-dynamic-programming-%E5%8B%95%E6%85%8B%E8%A6%8F%E5%8A%83-de980ca4a2d3): 將問題分解成數個小問題，找到其中的規律，每次將小問題的答案記錄下來，當下一回來用到前一回合答案時就直接查表
25. [a tuple can be used as a dictionary key](https://stackoverflow.com/questions/1938614/in-what-case-would-i-use-a-tuple-as-a-dictionary-key)
26. 取得 n 個東西中共有幾對 pairs: n*(n-1)//2 (不是用 c n 取 k，在 n=2 時會有問題)
27. [call a function twice or more times consecutively](https://stackoverflow.com/questions/9047985/how-do-i-call-a-function-twice-or-more-times-consecutively)
28. 判斷奇數或偶數，用 n & 1 == 1 會比用 n % 2 == 1 來得快
29. defaultdict 字典裡面不需要 key 值就能直接 assign key & value
30. [inverse function to XOR](https://stackoverflow.com/questions/14279866/what-is-inverse-function-to-xor) : a XOR b = c, we know the values of a and c. we use the formula to find b -> a XOR c = b
31. 什麼都不管，單純跑四次一樣的東西 for _ in range(4): print(1)
32. 用 a*a 會比用 a**2 還快
33. [check if a float value is a whole number](https://stackoverflow.com/questions/21583758/how-to-check-if-a-float-value-is-a-whole-number) : 
   (1.0).is_integer()
   True
   (1.555).is_integer()
   False
34. [Python ord()](https://www.programiz.com/python-programming/methods/built-in/ord) : ord('A') # 65  ord('B') # 66
35. split() 可以無視空白的長度
36. char.isalpha() 確認是不是字母
    
